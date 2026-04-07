"""Tests for feed module."""

from src.feed import build_rss_url


def test_build_rss_url() -> None:
    """Build correct RSS URL from channel ID."""
    url = build_rss_url("UCxxxxxx")
    assert url == "https://www.youtube.com/feeds/videos.xml?channel_id=UCxxxxxx"
