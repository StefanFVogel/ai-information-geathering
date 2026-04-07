"""Extract transcripts from YouTube videos."""

from dataclasses import dataclass
from typing import Any

from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore[import-untyped]


@dataclass
class TranscriptSegment:
    """A single segment of a transcript with timing."""

    text: str
    start: float
    duration: float


@dataclass
class Transcript:
    """A complete video transcript."""

    segments: list[TranscriptSegment]
    language: str

    @property
    def full_text(self) -> str:
        """Return the full transcript as plain text."""
        return " ".join(seg.text for seg in self.segments)

    @property
    def timestamped_text(self) -> str:
        """Return the transcript with timestamps in HH:MM:SS format."""
        lines: list[str] = []
        for seg in self.segments:
            hours, remainder = divmod(int(seg.start), 3600)
            minutes, seconds = divmod(remainder, 60)
            timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            lines.append(f"[{timestamp}] {seg.text}")
        return "\n".join(lines)


@dataclass
class Ok:
    """Successful result."""

    value: Transcript


@dataclass
class Err:
    """Error result."""

    message: str


TranscriptResult = Ok | Err


def extract_transcript(video_id: str, preferred_language: str = "en") -> TranscriptResult:
    """Extract the transcript for a YouTube video.

    Args:
        video_id: The YouTube video ID.
        preferred_language: Preferred transcript language code.

    Returns:
        Ok with Transcript on success, Err with message on failure.
    """
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)  # type: ignore[attr-defined]
    except Exception as e:
        return Err(f"Could not access transcripts for video {video_id}: {e}")

    return _find_best_transcript(transcript_list, preferred_language)


def _find_best_transcript(transcript_list: Any, preferred_language: str) -> TranscriptResult:
    """Find the best available transcript from the transcript list.

    Args:
        transcript_list: YouTube transcript list object.
        preferred_language: Preferred language code.

    Returns:
        Ok with Transcript on success, Err with message on failure.
    """
    try:
        transcript = transcript_list.find_transcript([preferred_language])
    except Exception:
        try:
            transcript = transcript_list.find_generated_transcript([preferred_language])
        except Exception:
            try:
                available = list(transcript_list)
                if not available:
                    return Err("No transcripts available for this video.")
                transcript = available[0]
            except Exception as e:
                return Err(f"Failed to find any transcript: {e}")

    return _fetch_and_parse(transcript)


def _fetch_and_parse(transcript: Any) -> TranscriptResult:
    """Fetch transcript data and parse into segments.

    Args:
        transcript: A YouTube transcript object.

    Returns:
        Ok with Transcript on success, Err with message on failure.
    """
    try:
        data = transcript.fetch()
        segments = [
            TranscriptSegment(
                text=entry["text"],
                start=entry["start"],
                duration=entry["duration"],
            )
            for entry in data
        ]
        language: str = getattr(transcript, "language_code", "unknown")
        return Ok(value=Transcript(segments=segments, language=language))
    except Exception as e:
        return Err(f"Failed to fetch transcript: {e}")
