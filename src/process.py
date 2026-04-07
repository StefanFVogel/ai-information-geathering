"""Post-process inbox files: add transcripts, summaries, and move to sources."""

from pathlib import Path

import click
import frontmatter

from src.config import Config
from src.metadata import extract_video_id, fetch_metadata
from src.summarize import Err as SumErr
from src.summarize import generate_summary
from src.transcript import Err as TrErr
from src.transcript import extract_transcript
from src.vault import append_to_log, list_inbox, move_to_sources, write_note


def process_inbox(config: Config) -> None:
    """Process all unprocessed files in the vault inbox.

    Args:
        config: Application configuration.
    """
    vault_path = config.vault_path
    inbox_files = list_inbox(vault_path)

    if not inbox_files:
        click.echo("No files in inbox.")
        return

    for file_path in inbox_files:
        _process_single_file(file_path, config)


def _process_single_file(file_path: Path, config: Config) -> None:
    """Process a single inbox file.

    Args:
        file_path: Path to the inbox file.
        config: Application configuration.
    """
    post = frontmatter.load(file_path)

    if post.get("status") == "processed":
        click.echo(f"Skipping (already processed): {file_path.name}")
        return

    url = post.get("url", "")
    if not url or "youtube.com" not in url and "youtu.be" not in url:
        click.echo(f"Skipping (no YouTube URL): {file_path.name}")
        return

    video_id = extract_video_id(url)
    if not video_id:
        click.echo(f"Skipping (could not extract video ID): {file_path.name}")
        return

    click.echo(f"Processing: {file_path.name}")
    _enrich_with_metadata(post, url)
    _enrich_with_transcript(post, video_id, config)

    post["status"] = "processed"
    write_note(file_path, post)

    dest = move_to_sources(file_path, config.vault_path, "youtube")
    append_to_log(config.vault_path, "ingest", f"Processed {dest.name}")
    click.echo(f"  → Moved to {dest}")


def _enrich_with_metadata(post: frontmatter.Post, url: str) -> None:
    """Add video metadata to the post frontmatter.

    Args:
        post: The frontmatter post to enrich.
        url: The YouTube video URL.
    """
    result = fetch_metadata(url)
    if isinstance(result, type) or hasattr(result, "message"):
        return

    meta = result.value
    post["title"] = post.get("title") or meta.title
    post["author"] = f"[[{meta.channel_name}]]"
    post["channel_id"] = meta.channel_id

    if meta.upload_date:
        post["date"] = meta.upload_date.isoformat()

    if meta.tags:
        existing_tags = post.get("tags", []) or []
        post["tags"] = list(set(existing_tags + meta.tags[:10]))

    post["duration"] = meta.duration


def _enrich_with_transcript(post: frontmatter.Post, video_id: str, config: Config) -> None:
    """Add transcript and summary to the post content.

    Args:
        post: The frontmatter post to enrich.
        video_id: The YouTube video ID.
        config: Application configuration.
    """
    tr_result = extract_transcript(video_id)

    if isinstance(tr_result, TrErr):
        click.echo(f"  Warning: {tr_result.message}")
        post.content = f"> **Note**: Transcript not available.\n\n{post.content}"
        return

    transcript = tr_result.value
    post["language"] = transcript.language

    title = post.get("title", "Untitled")
    summary_result = generate_summary(transcript.full_text, str(title), config.summary_length)

    summary_section = _build_summary_section(summary_result)
    transcript_section = f"\n\n---\n\n## Transcript\n\n{transcript.timestamped_text}"

    post.content = f"{summary_section}\n\n{post.content}{transcript_section}"


def _build_summary_section(summary_result: object) -> str:
    """Build the summary markdown section.

    Args:
        summary_result: Result from generate_summary.

    Returns:
        Formatted summary section string.
    """
    if isinstance(summary_result, SumErr):
        return f"> **Note**: Summary generation failed: {summary_result.message}"

    return f"## Summary\n\n{summary_result.value.text}"
