# AI Information Gathering

Personal AI-powered knowledge management tool that collects YouTube content, generates summaries, and organizes everything in an Obsidian wiki.

Based on [Andrej Karpathy's LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Problem

Too much AI content on YouTube. Impossible to watch everything. Important trends get missed. Found information gets lost without structure or connections.

## Solution

A three-layer system following Karpathy's pattern:

```
Raw Sources (immutable)  →  Wiki (LLM-maintained)  →  Schema (conventions)
vault/sources/              vault/wiki/                vault/schema.md
```

Four ways content enters the vault:

1. **Web Clipper** (primary) — clip a YouTube video in the browser, it lands in `vault/inbox/`
2. **CLI process** — post-processes inbox files: pulls transcript, generates summary, creates wiki pages
3. **RSS feeds** — discover new videos from tracked channels
4. **Manual** — drop any file into `vault/sources/`

## Setup

```bash
# Clone with submodule
git clone --recurse-submodules https://github.com/StefanFVogel/ai-information-geathering.git
cd ai-information-geathering

# Create virtual environment
python -m venv .venv

# Install dev-standards toolchain
.venv/Scripts/python.exe standards/scripts/maintain_tools.py --setup   # Windows
# .venv/bin/python standards/scripts/maintain_tools.py --setup          # Linux/Mac

# Install project dependencies
pip install youtube-transcript-api yt-dlp feedparser python-frontmatter click pyyaml anthropic

# Initialize vault
python -m src.cli init
```

### Obsidian Setup

1. Open `vault/` as an Obsidian vault
2. Install plugins: **Dataview**, **Web Clipper**, **Local REST API**
3. Import `web-clipper-template.json` into Web Clipper settings
4. Set `ANTHROPIC_API_KEY` environment variable for summaries

## Usage

### Clip a YouTube Video

1. Watch a video in the browser
2. Click the Obsidian Web Clipper extension
3. Select the "YouTube Video" template
4. Video metadata lands in `vault/inbox/`

### Process Inbox

```bash
# Process all clipped videos: pull transcripts, generate summaries, update wiki
aig process
```

This will:
- Extract the full transcript with timestamps
- Generate a ~300 word summary via Claude
- Extract mentioned people, concepts, and tools as `[[Wikilinks]]`
- Create or update wiki pages for each entity
- Move the file from `inbox/` to `sources/youtube/`
- Update `index.md` and `log.md`

### Track YouTube Channels

```bash
# Add a channel
aig channel add "https://youtube.com/@karpathy"

# List tracked channels
aig channel list

# Check for new videos
aig feed
```

### Daily Briefing

```bash
# Generate today's briefing
aig briefing
```

Creates `vault/daily/YYYY-MM-DD.md` with:
- New videos from tracked channels (top 10)
- Trending topics (appearing in 2+ channels)
- Newly mentioned people

### Wiki Maintenance

```bash
# Rebuild the wiki index
aig wiki rebuild-index

# Check wiki health (orphans, broken links)
aig wiki lint
```

## Vault Structure

```
vault/
├── schema.md              Conventions and frontmatter format
├── index.md               Catalog of all wiki pages
├── log.md                 Chronological activity log
├── inbox/                 New, unprocessed entries
├── sources/
│   ├── youtube/           Processed transcripts
│   ├── articles/          Web Clipper articles
│   ├── papers/            PDFs, papers
│   └── other/             Other sources
├── wiki/
│   ├── people/            Researchers, creators
│   ├── concepts/          RAG, Fine-Tuning, Agents...
│   ├── tools/             Frameworks, libraries
│   └── syntheses/         Comparisons, analyses
├── channels/              YouTube channel profiles
├── daily/                 Daily briefings
└── assets/                Images, attachments
```

## Configuration

Edit `config.yaml`:

```yaml
vault_path: "./vault"          # Path to Obsidian vault
summary_length: 300            # Target summary word count
last_feed_check: null          # Auto-updated by feed command
channels: []                   # Managed by channel add/remove
```

## Quality

This project uses the [dev-standards](https://github.com/StefanFVogel/dev-standards) submodule:

- Architekten-Ampel quality gate (Ruff, Pyright, Radon, Vulture, Bandit, jscpd)
- 36 unit tests, all passing
- Superpowers workflow: Brainstorming → Requirements → Architecture → Backend → QA

## Project Documentation

- [Superpowers Brainstorming Spec](docs/superpowers/spec/2026-04-07-ai-information-gathering-spec.md)
- [PRD](docs/PRD.md)
- [Feature Index](features/INDEX.md)
- [AIG-1: YouTube Ingest Pipeline](docs/features/AIG-1-youtube-ingest.md)
- [AIG-2: Wiki Maintenance](docs/features/AIG-2-wiki-maintenance.md)
- [AIG-3: Daily Briefing](docs/features/AIG-3-daily-briefing.md)

## License

Private project.
