"""Extract video metadata from YouTube using yt-dlp."""

import re
from dataclasses import dataclass
from datetime import date

import yt_dlp


@dataclass
class VideoMetadata:
    """Metadata for a YouTube video."""

    video_id: str
    title: str
    channel_name: str
    channel_id: str
    upload_date: date | None
    description: str
    tags: list[str]
    duration: int
    url: str


@dataclass
class Ok:
    """Successful result."""

    value: VideoMetadata


@dataclass
class Err:
    """Error result."""

    message: str


MetadataResult = Ok | Err


def extract_video_id(url: str) -> str | None:
    """Extract the video ID from a YouTube URL.

    Args:
        url: A YouTube URL in any format.

    Returns:
        The video ID string, or None if not found.
    """
    patterns = [
        r"(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"(?:embed/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def fetch_metadata(url: str) -> MetadataResult:
    """Fetch metadata for a YouTube video.

    Args:
        url: The YouTube video URL.

    Returns:
        Ok with VideoMetadata on success, Err with message on failure.
    """
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": False,
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return Err(f"Failed to fetch metadata for {url}: {e}")

    if info is None:
        return Err(f"No metadata returned for {url}")

    return Ok(value=_parse_info(info, url))


def _parse_info(info: dict[str, object], url: str) -> VideoMetadata:
    """Parse yt-dlp info dict into VideoMetadata.

    Args:
        info: The yt-dlp info dictionary.
        url: The original URL.

    Returns:
        Parsed VideoMetadata object.
    """
    upload_date_str = str(info.get("upload_date", ""))
    upload_date = _parse_date(upload_date_str)

    return VideoMetadata(
        video_id=str(info.get("id", "")),
        title=str(info.get("title", "Untitled")),
        channel_name=str(info.get("channel", info.get("uploader", "Unknown"))),
        channel_id=str(info.get("channel_id", "")),
        upload_date=upload_date,
        description=str(info.get("description", "")),
        tags=list(info.get("tags", []) or []),
        duration=int(info.get("duration", 0) or 0),
        url=url,
    )


def _parse_date(date_str: str) -> date | None:
    """Parse a YYYYMMDD date string.

    Args:
        date_str: Date string in YYYYMMDD format.

    Returns:
        Parsed date or None if invalid.
    """
    if len(date_str) == 8 and date_str.isdigit():
        return date(int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8]))
    return None


def resolve_channel_id(channel_url: str) -> MetadataResult:
    """Resolve a YouTube channel URL to get channel metadata.

    Args:
        channel_url: YouTube channel URL (@handle, /channel/ID, /c/name).

    Returns:
        Ok with a VideoMetadata-like object containing channel info, Err on failure.
    """
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": True,
        "playlist_items": "1",
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(channel_url, download=False)
    except Exception as e:
        return Err(f"Failed to resolve channel {channel_url}: {e}")

    if info is None:
        return Err(f"No info returned for {channel_url}")

    channel_id = str(info.get("channel_id", info.get("id", "")))
    channel_name = str(info.get("channel", info.get("uploader", "Unknown")))

    return Ok(
        value=VideoMetadata(
            video_id="",
            title=channel_name,
            channel_name=channel_name,
            channel_id=channel_id,
            upload_date=None,
            description="",
            tags=[],
            duration=0,
            url=channel_url,
        )
    )
