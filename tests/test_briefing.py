"""Tests for briefing module."""

from datetime import date, datetime
from pathlib import Path

import frontmatter  # type: ignore[import-untyped]

from src.briefing import _build_briefing_content, _detect_trends, generate_briefing
from src.config import Channel, Config
from src.feed import FeedEntry
from src.vault import ensure_vault_structure, write_note


def _make_config(tmp_path: Path, channels: list[Channel] | None = None) -> Config:
    """Create a test config."""
    return Config(
        vault_path=tmp_path,
        summary_length=300,
        last_feed_check=None,
        channels=channels or [],
    )


def test_generate_briefing_no_channels(tmp_path: Path) -> None:
    """Return None when no channels configured."""
    ensure_vault_structure(tmp_path)
    config = _make_config(tmp_path)

    result = generate_briefing(config)
    assert result is None


def test_build_briefing_content_no_entries() -> None:
    """Build briefing with no entries shows 'no new videos'."""
    content = _build_briefing_content([], [], [])
    assert "No new videos" in content


def test_build_briefing_content_with_entries() -> None:
    """Build briefing includes video entries."""
    entries = [
        FeedEntry(
            title="Test Video",
            url="https://youtube.com/watch?v=abc",
            channel_name="TestChannel",
            published=datetime(2026, 4, 7),
        ),
    ]

    content = _build_briefing_content(entries, [], [])

    assert "Test Video" in content
    assert "TestChannel" in content
    assert "1 new video" in content


def test_build_briefing_content_caps_at_10() -> None:
    """Build briefing shows max 10 entries."""
    entries = [
        FeedEntry(
            title=f"Video {i}",
            url=f"https://youtube.com/watch?v={i}",
            channel_name="Ch",
            published=datetime(2026, 4, 7),
        )
        for i in range(15)
    ]

    content = _build_briefing_content(entries, [], [])
    assert "...and 5 more" in content


def test_build_briefing_content_with_trends() -> None:
    """Build briefing includes trend section."""
    topics = [("RAG", 3), ("Agents", 2)]
    content = _build_briefing_content([], topics, [])

    assert "## Trends" in content
    assert "[[RAG]]" in content
    assert "3 mentions" in content


def test_build_briefing_content_with_new_people() -> None:
    """Build briefing includes new people section."""
    content = _build_briefing_content([], [], ["Andrej Karpathy"])

    assert "## New People" in content
    assert "[[Andrej Karpathy]]" in content


def test_detect_trends_empty(tmp_path: Path) -> None:
    """No trends when no sources exist."""
    ensure_vault_structure(tmp_path)
    result = _detect_trends(tmp_path)
    assert result == []


def test_detect_trends_with_sources(tmp_path: Path) -> None:
    """Detect topics appearing in multiple sources."""
    ensure_vault_structure(tmp_path)
    sources_path = tmp_path / "sources" / "youtube"

    for i in range(3):
        post = frontmatter.Post(
            f"Content {i}",
            type="source",
            date=date.today().isoformat(),
            topics=["[[RAG]]", "[[Agents]]"],
        )
        file_path = sources_path / f"video-{i}.md"
        write_note(file_path, post)

    result = _detect_trends(tmp_path)
    topic_names = [t for t, _ in result]

    assert "RAG" in topic_names
    assert "Agents" in topic_names
