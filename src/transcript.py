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
    api = YouTubeTranscriptApi()

    try:
        transcript_list = api.list(video_id)
    except Exception as e:
        return Err(f"Could not access transcripts for video {video_id}: {e}")

    return _find_best_transcript(transcript_list, preferred_language, api, video_id)


def _find_best_transcript(
    transcript_list: Any, preferred_language: str, api: Any, video_id: str
) -> TranscriptResult:
    """Find the best available transcript from the transcript list.

    Args:
        transcript_list: YouTube transcript list object.
        preferred_language: Preferred language code.
        api: YouTubeTranscriptApi instance.
        video_id: The video ID for fetching.

    Returns:
        Ok with Transcript on success, Err with message on failure.
    """
    best_transcript = None
    language = "unknown"

    try:
        available = list(transcript_list)
        if not available:
            return Err("No transcripts available for this video.")

        # Prefer manual transcript in preferred language
        for t in available:
            if t.language_code == preferred_language and not t.is_generated:
                best_transcript = t
                break

        # Fallback: auto-generated in preferred language
        if best_transcript is None:
            for t in available:
                if t.language_code == preferred_language:
                    best_transcript = t
                    break

        # Fallback: any available transcript
        if best_transcript is None:
            best_transcript = available[0]

        language = best_transcript.language_code
    except Exception as e:
        return Err(f"Failed to find any transcript: {e}")

    return _fetch_and_parse(api, video_id, language)


def _fetch_and_parse(api: Any, video_id: str, language: str) -> TranscriptResult:
    """Fetch transcript data and parse into segments.

    Args:
        api: YouTubeTranscriptApi instance.
        video_id: The video ID.
        language: Language code to fetch.

    Returns:
        Ok with Transcript on success, Err with message on failure.
    """
    try:
        fetched = api.fetch(video_id, languages=[language])
        segments = [
            TranscriptSegment(
                text=snippet.text,
                start=snippet.start,
                duration=snippet.duration,
            )
            for snippet in fetched.snippets
        ]
        return Ok(value=Transcript(segments=segments, language=language))
    except Exception as e:
        return Err(f"Failed to fetch transcript: {e}")
