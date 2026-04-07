"""Obsidian vault operations: read, write, and move markdown files."""

from datetime import datetime
from pathlib import Path

import frontmatter  # type: ignore[import-untyped]


def ensure_vault_structure(vault_path: Path) -> None:
    """Create the vault directory structure if it does not exist.

    Args:
        vault_path: Root path of the Obsidian vault.
    """
    directories = [
        "inbox",
        "sources/youtube",
        "sources/articles",
        "sources/papers",
        "sources/other",
        "wiki/people",
        "wiki/concepts",
        "wiki/tools",
        "wiki/syntheses",
        "channels",
        "daily",
        "assets",
    ]
    for d in directories:
        (vault_path / d).mkdir(parents=True, exist_ok=True)


def list_inbox(vault_path: Path) -> list[Path]:
    """List all markdown files in the inbox directory.

    Args:
        vault_path: Root path of the Obsidian vault.

    Returns:
        List of paths to inbox markdown files.
    """
    inbox_dir = vault_path / "inbox"
    if not inbox_dir.exists():
        return []
    return sorted(inbox_dir.glob("*.md"))


def read_note(file_path: Path) -> frontmatter.Post:
    """Read a markdown file with frontmatter.

    Args:
        file_path: Path to the markdown file.

    Returns:
        Parsed frontmatter Post object with metadata and content.
    """
    return frontmatter.load(str(file_path))


def write_note(file_path: Path, post: frontmatter.Post) -> None:
    """Write a markdown file with frontmatter.

    Args:
        file_path: Path to write the file to.
        post: Frontmatter Post object with metadata and content.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))


def move_to_sources(file_path: Path, vault_path: Path, source_type: str = "youtube") -> Path:
    """Move a processed file from inbox to sources.

    Args:
        file_path: Path to the file in inbox.
        vault_path: Root path of the Obsidian vault.
        source_type: Subdirectory in sources (youtube, articles, papers, other).

    Returns:
        New path of the moved file.
    """
    dest = vault_path / "sources" / source_type / file_path.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    file_path.rename(dest)
    return dest


def append_to_log(vault_path: Path, action: str, details: str) -> None:
    """Append an entry to the activity log.

    Args:
        vault_path: Root path of the Obsidian vault.
        action: Type of action (ingest, query, lint).
        details: Description of what was done.
    """
    log_path = vault_path / "log.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"- [{timestamp}] **{action}**: {details}\n"

    with log_path.open("a", encoding="utf-8") as f:
        f.write(entry)
