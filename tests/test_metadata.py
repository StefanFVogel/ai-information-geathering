"""Tests for metadata module."""

from datetime import date

from src.metadata import _parse_date, extract_video_id


def test_extract_video_id_standard_url() -> None:
    """Extract ID from standard YouTube URL."""
    assert extract_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_extract_video_id_short_url() -> None:
    """Extract ID from youtu.be short URL."""
    assert extract_video_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_extract_video_id_embed_url() -> None:
    """Extract ID from embed URL."""
    assert extract_video_id("https://www.youtube.com/embed/dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_extract_video_id_with_params() -> None:
    """Extract ID from URL with extra parameters."""
    assert extract_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=120") == "dQw4w9WgXcQ"


def test_extract_video_id_invalid() -> None:
    """Return None for non-YouTube URL."""
    assert extract_video_id("https://example.com") is None


def test_parse_date_valid() -> None:
    """Parse valid YYYYMMDD date."""
    assert _parse_date("20260407") == date(2026, 4, 7)


def test_parse_date_invalid() -> None:
    """Return None for invalid date string."""
    assert _parse_date("") is None
    assert _parse_date("abc") is None
    assert _parse_date("2026") is None
