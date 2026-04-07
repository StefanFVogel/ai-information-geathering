"""Generate daily briefings from RSS feeds and processed sources."""

from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import frontmatter  # type: ignore[import-untyped]

from src.config import Config
from src.feed import FeedEntry, get_new_videos
from src.vault import write_note


def generate_briefing(config: Config) -> Path | None:
    """Generate a daily briefing markdown file.

    Args:
        config: Application configuration.

    Returns:
        Path to the created briefing file, or None if no channels configured.
    """
    vault_path = config.vault_path

    if not config.channels:
        return None

    all_entries = _collect_feed_entries(config)
    topics = _detect_trends(vault_path, days=7)
    new_people = _find_new_people(vault_path, all_entries)

    briefing_path = vault_path / "daily" / f"{date.today().isoformat()}.md"
    content = _build_briefing_content(all_entries, topics, new_people)

    top_topics = [t for t, _ in topics[:5]]
    post = frontmatter.Post(
        content,
        type="daily",
        date=date.today().isoformat(),
        video_count=len(all_entries),
        top_topics=top_topics,
    )

    briefing_path.parent.mkdir(parents=True, exist_ok=True)
    write_note(briefing_path, post)
    return briefing_path


def _collect_feed_entries(config: Config) -> list[FeedEntry]:
    """Collect new videos from all tracked channels.

    Args:
        config: Application configuration.

    Returns:
        List of feed entries from all channels, newest first.
    """
    all_entries: list[FeedEntry] = []
    for ch in config.channels:
        entries = get_new_videos(ch.rss_url, config.last_feed_check)
        all_entries.extend(entries)

    all_entries.sort(key=lambda e: e.published or datetime.min, reverse=True)
    return all_entries


def _build_briefing_content(
    entries: list[FeedEntry],
    topics: list[tuple[str, int]],
    new_people: list[str],
) -> str:
    """Build the briefing markdown content.

    Args:
        entries: Feed entries to include.
        topics: Trending topics with counts.
        new_people: Newly mentioned people.

    Returns:
        Formatted markdown string.
    """
    today = date.today().isoformat()
    lines = [f"# Daily Briefing — {today}\n"]

    if not entries:
        lines.append("\nNo new videos since last check.\n")
    else:
        lines.append(f"\n**{len(entries)} new video(s)**\n")
        lines.append("\n## Videos\n")

        display_entries = entries[:10]
        for entry in display_entries:
            pub = entry.published.strftime("%Y-%m-%d") if entry.published else "unknown"
            lines.append(f"- **[{entry.title}]({entry.url})** — {entry.channel_name} ({pub})")

        if len(entries) > 10:
            lines.append(f"\n*...and {len(entries) - 10} more.*\n")

    if topics:
        lines.append("\n## Trends\n")
        lines.append("*Topics appearing across multiple channels in the last 7 days:*\n")
        for topic, count in topics[:5]:
            lines.append(f"- [[{topic}]] — {count} mentions")

    if new_people:
        lines.append("\n## New People\n")
        lines.append("*First-time mentions:*\n")
        for person in new_people[:10]:
            lines.append(f"- [[{person}]]")

    return "\n".join(lines) + "\n"


def _detect_trends(vault_path: Path, days: int = 7) -> list[tuple[str, int]]:
    """Detect trending topics from recently processed sources.

    Args:
        vault_path: Root path of the Obsidian vault.
        days: Number of days to look back.

    Returns:
        List of (topic, count) tuples sorted by count descending.
    """
    sources_path = vault_path / "sources" / "youtube"
    if not sources_path.exists():
        return []

    cutoff = date.today() - timedelta(days=days)
    topic_counter: Counter[str] = Counter()

    for md_file in sources_path.glob("*.md"):
        post = frontmatter.load(str(md_file))
        file_date = _extract_date(post)

        if file_date and file_date < cutoff:
            continue

        topics: list[str] = list(post.get("topics") or [])
        for topic in topics:
            clean = topic.strip("[]")
            if clean:
                topic_counter[clean] += 1

    return [(topic, count) for topic, count in topic_counter.most_common() if count >= 2]


def _find_new_people(vault_path: Path, entries: list[FeedEntry]) -> list[str]:
    """Find people mentioned in entries that don't have wiki pages yet.

    Args:
        vault_path: Root path of the Obsidian vault.
        entries: Current feed entries.

    Returns:
        List of new people names.
    """
    people_dir = vault_path / "wiki" / "people"
    existing_people: set[str] = set()

    if people_dir.exists():
        for md_file in people_dir.glob("*.md"):
            post = frontmatter.load(str(md_file))
            existing_people.add(str(post.get("title", md_file.stem)).lower())

    new_people: list[str] = []
    for entry in entries:
        if entry.channel_name.lower() not in existing_people:
            name = entry.channel_name
            if name not in new_people:
                new_people.append(name)

    return new_people


def _extract_date(post: Any) -> date | None:
    """Extract date from a frontmatter post.

    Args:
        post: Frontmatter post object.

    Returns:
        Parsed date or None.
    """
    raw = post.get("date")
    if isinstance(raw, date):
        return raw
    if isinstance(raw, str):
        try:
            return date.fromisoformat(raw)
        except ValueError:
            return None
    return None
