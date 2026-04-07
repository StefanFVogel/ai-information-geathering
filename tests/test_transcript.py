"""Tests for transcript module."""

from src.transcript import Transcript, TranscriptSegment


def test_transcript_full_text() -> None:
    """Full text joins all segments."""
    transcript = Transcript(
        segments=[
            TranscriptSegment(text="Hello", start=0.0, duration=1.0),
            TranscriptSegment(text="world", start=1.0, duration=1.0),
        ],
        language="en",
    )

    assert transcript.full_text == "Hello world"


def test_transcript_timestamped_text() -> None:
    """Timestamped text includes HH:MM:SS format."""
    transcript = Transcript(
        segments=[
            TranscriptSegment(text="First", start=0.0, duration=1.0),
            TranscriptSegment(text="Second", start=65.0, duration=1.0),
            TranscriptSegment(text="Third", start=3661.0, duration=1.0),
        ],
        language="en",
    )

    result = transcript.timestamped_text
    assert "[00:00:00] First" in result
    assert "[00:01:05] Second" in result
    assert "[01:01:01] Third" in result
