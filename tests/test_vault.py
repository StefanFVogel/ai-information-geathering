"""Tests for vault module."""

from pathlib import Path

import frontmatter  # type: ignore[import-untyped]

from src.vault import (
    append_to_log,
    ensure_vault_structure,
    list_inbox,
    move_to_sources,
    read_note,
    write_note,
)


def test_ensure_vault_structure(tmp_path: Path) -> None:
    """Create vault directories."""
    ensure_vault_structure(tmp_path)

    assert (tmp_path / "inbox").is_dir()
    assert (tmp_path / "sources" / "youtube").is_dir()
    assert (tmp_path / "wiki" / "people").is_dir()
    assert (tmp_path / "daily").is_dir()


def test_list_inbox_empty(tmp_path: Path) -> None:
    """Empty inbox returns empty list."""
    ensure_vault_structure(tmp_path)
    assert list_inbox(tmp_path) == []


def test_list_inbox_with_files(tmp_path: Path) -> None:
    """Inbox with files returns sorted paths."""
    ensure_vault_structure(tmp_path)
    (tmp_path / "inbox" / "b.md").write_text("test")
    (tmp_path / "inbox" / "a.md").write_text("test")

    result = list_inbox(tmp_path)

    assert len(result) == 2
    assert result[0].name == "a.md"
    assert result[1].name == "b.md"


def test_write_and_read_note(tmp_path: Path) -> None:
    """Write a note and read it back."""
    file_path = tmp_path / "test.md"
    post = frontmatter.Post("Hello world", title="Test", tags=["ai"])

    write_note(file_path, post)
    loaded = read_note(file_path)

    assert loaded["title"] == "Test"
    assert loaded["tags"] == ["ai"]
    assert "Hello world" in loaded.content


def test_move_to_sources(tmp_path: Path) -> None:
    """Move file from inbox to sources."""
    ensure_vault_structure(tmp_path)
    src = tmp_path / "inbox" / "video.md"
    src.write_text("content")

    dest = move_to_sources(src, tmp_path, "youtube")

    assert dest == tmp_path / "sources" / "youtube" / "video.md"
    assert dest.exists()
    assert not src.exists()


def test_append_to_log(tmp_path: Path) -> None:
    """Append entry to log file."""
    log_path = tmp_path / "log.md"
    log_path.write_text("# Log\n")

    append_to_log(tmp_path, "ingest", "Processed video.md")

    content = log_path.read_text()
    assert "**ingest**" in content
    assert "Processed video.md" in content
