"""Generate summaries and extract wikilinks using Claude API."""

from dataclasses import dataclass

import anthropic

SUMMARY_SYSTEM_PROMPT = """You are a knowledge curator for a personal Obsidian wiki.
Your job is to summarize video transcripts and extract key entities.

Rules:
- Write the summary in English
- Use [[Wikilinks]] for people, concepts, tools, and papers mentioned
- People: [[Firstname Lastname]]
- Concepts: [[Concept Name]]
- Tools: [[Tool Name]]
- Keep the summary concise but comprehensive
- Structure with bullet points for key takeaways
- End with a "Mentioned" section listing all entities"""


@dataclass
class Summary:
    """A generated summary with extracted entities."""

    text: str
    people: list[str]
    concepts: list[str]
    tools: list[str]


@dataclass
class Ok:
    """Successful result."""

    value: Summary


@dataclass
class Err:
    """Error result."""

    message: str


SummaryResult = Ok | Err


def generate_summary(transcript_text: str, title: str, summary_length: int = 300) -> SummaryResult:
    """Generate a summary of a video transcript using Claude.

    Args:
        transcript_text: The full transcript text.
        title: The video title for context.
        summary_length: Target word count for the summary.

    Returns:
        Ok with Summary on success, Err with message on failure.
    """
    prompt = (
        f"Summarize this video transcript in approximately {summary_length} words.\n"
        f"Video title: {title}\n\n"
        f"Transcript:\n{transcript_text[:50000]}"
    )

    try:
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            system=SUMMARY_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
    except Exception as e:
        return Err(f"Claude API error: {e}")

    response_text = message.content[0].text
    entities = _extract_entities(response_text)

    return Ok(
        value=Summary(
            text=response_text,
            people=entities["people"],
            concepts=entities["concepts"],
            tools=entities["tools"],
        )
    )


def _extract_entities(text: str) -> dict[str, list[str]]:
    """Extract wikilinked entities from summary text.

    Args:
        text: Summary text containing [[Wikilinks]].

    Returns:
        Dict with people, concepts, tools lists.
    """
    import re

    wikilinks = re.findall(r"\[\[([^\]]+)\]\]", text)

    # Simple heuristic: names with spaces are people, rest are concepts/tools
    people: list[str] = []
    concepts: list[str] = []
    tools: list[str] = []

    for link in wikilinks:
        parts = link.split()
        if len(parts) == 2 and parts[0][0].isupper() and parts[1][0].isupper():
            people.append(link)
        else:
            concepts.append(link)

    return {"people": list(set(people)), "concepts": list(set(concepts)), "tools": tools}
