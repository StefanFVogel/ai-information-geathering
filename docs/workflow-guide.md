# Workflow Guide: Working with AI Information Gathering

This guide explains the day-to-day workflow for using the tool to build your personal AI knowledge wiki.

## The Big Picture

```
You browse YouTube          Claude processes          You browse in Obsidian
        │                         │                         │
  See something interesting       │                   Graph View shows
        │                         │                   connections
  Click Web Clipper               │                         │
        │                   Pulls transcript          Click through
  Lands in inbox/                 │                   wiki pages
        │                   Generates summary               │
  Run: aig process                │                   Ask Claude
        │                   Creates wiki pages        questions
        ▼                         ▼                         ▼
   vault/inbox/  ──────►  vault/sources/  ◄──────  vault/wiki/
```

## Daily Workflow

### Morning: Check What's New

```bash
# See new videos from your tracked channels
aig feed

# Generate today's briefing
aig briefing
```

Open `vault/daily/` in Obsidian to see the briefing. It shows:
- New videos ranked by relevance
- Trending topics (what are multiple channels talking about?)
- New people you haven't seen before

### During the Day: Clip Interesting Content

When you find a video worth keeping:

1. Click the **Obsidian Web Clipper** browser extension
2. Select **"YouTube Video"** template
3. Done — it's in your inbox

You can also clip articles, blog posts, or any web page (use Obsidian's default template for non-YouTube content).

### Evening: Process & Explore

```bash
# Process everything you clipped today
aig process
```

Then open Obsidian:
- **Graph View** shows the growing network of people, concepts, and tools
- **Dataview queries** let you filter by tags, date, relevance
- Click any `[[Wikilink]]` to jump to the entity page
- Entity pages list all sources where they were mentioned

### Weekly: Maintenance

```bash
# Check wiki health
aig wiki lint

# Rebuild index if needed
aig wiki rebuild-index
```

## Working with Claude

Claude is your thinking partner, not just a processor. Use it for:

### Questions
> "What do the sources say about RAG vs. Fine-Tuning?"

Claude searches your wiki pages and synthesizes an answer with citations.

### Planning
> "Based on what I've collected, what should I learn next about AI agents?"

Claude analyzes your wiki and suggests a learning path.

### Analysis
> "Compare what Karpathy and Hinton say about AI safety."

Claude finds relevant sources and creates a synthesis page.

## Managing Channels

```bash
# Track a new channel
aig channel add "https://youtube.com/@karpathy"
aig channel add "https://youtube.com/@lexfridman"
aig channel add "https://youtube.com/@yanaborisov"

# See all tracked channels
aig channel list

# Remove a channel
aig channel remove "ChannelName"
```

YouTube RSS feeds update automatically — no API key needed.

## Frontmatter & Dataview

Every file in the vault has YAML frontmatter. This powers Obsidian's Dataview plugin.

### Example Dataview Queries

**All unprocessed inbox items:**
```dataview
TABLE title, author, date
FROM "inbox"
WHERE status = "inbox"
SORT date DESC
```

**Recent YouTube sources:**
```dataview
TABLE title, author, tags
FROM "sources/youtube"
SORT date DESC
LIMIT 20
```

**People with most source references:**
```dataview
TABLE title, length(related_sources) as "Sources"
FROM "wiki/people"
SORT length(related_sources) DESC
```

**This week's topics:**
```dataview
TABLE title, date
FROM "sources/youtube"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

## Tips

- **Start small**: Add 3-5 channels you actually watch, not 50 you might watch
- **Clip selectively**: Only clip what you found valuable — the system works because you curate
- **Use Graph View**: The visual connections between entities reveal patterns you won't see in a list
- **Ask Claude**: Don't just collect — synthesize. Ask questions across your sources
- **Weekly lint**: Run `aig wiki lint` to keep the wiki clean

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| YouTube source | `YYYY-MM-DD-video-slug.md` | `2026-04-07-karpathy-llm-wiki.md` |
| Daily briefing | `YYYY-MM-DD.md` | `2026-04-07.md` |
| Person page | `firstname-lastname.md` | `andrej-karpathy.md` |
| Concept page | `concept-name.md` | `retrieval-augmented-generation.md` |
| Tool page | `tool-name.md` | `obsidian.md` |
