"""Monitor YouTube channel RSS feeds for new videos."""

from dataclasses import dataclass
from datetime import datetime

import feedparser

YOUTUBE_RSS_BASE = "https://www.youtube.com/feeds/videos.xml?channel_id="


@dataclass
class FeedEntry:
    """A single video entry from an RSS feed."""

    title: str
    url: str
    channel_name: str
    published: datetime | None


def build_rss_url(channel_id: str) -> str:
    """Build the YouTube RSS feed URL for a channel.

    Args:
        channel_id: The YouTube channel ID.

    Returns:
        The RSS feed URL.
    """
    return f"{YOUTUBE_RSS_BASE}{channel_id}"


def fetch_feed(rss_url: str) -> list[FeedEntry]:
    """Fetch and parse a YouTube channel RSS feed.

    Args:
        rss_url: The RSS feed URL.

    Returns:
        List of FeedEntry objects, newest first.
    """
    feed = feedparser.parse(rss_url)
    entries: list[FeedEntry] = []

    for entry in feed.entries:
        published = _parse_published(entry)
        entries.append(
            FeedEntry(
                title=entry.get("title", "Untitled"),
                url=entry.get("link", ""),
                channel_name=feed.feed.get("title", "Unknown"),
                published=published,
            )
        )

    return entries


def get_new_videos(rss_url: str, since: datetime | None) -> list[FeedEntry]:
    """Get videos published after a given datetime.

    Args:
        rss_url: The RSS feed URL.
        since: Only return videos published after this time. If None, return all.

    Returns:
        List of new FeedEntry objects, newest first.
    """
    entries = fetch_feed(rss_url)
    if since is None:
        return entries
    return [e for e in entries if e.published is not None and e.published > since]


def _parse_published(entry: object) -> datetime | None:
    """Parse the published date from a feed entry.

    Args:
        entry: A feedparser entry object.

    Returns:
        Parsed datetime or None.
    """
    published_parsed = getattr(entry, "published_parsed", None)
    if published_parsed is not None:
        try:
            return datetime(*published_parsed[:6])
        except (TypeError, ValueError):
            return None
    return None
