# CLAUDE.md

@standards/docs/claude_coding_rules.md

## Project: AI Information Gathering

Personal knowledge management tool that collects AI content (primarily YouTube), generates summaries, and organizes everything in an Obsidian wiki. Based on Karpathy's LLM Wiki Pattern.

### Architecture

Three-layer system:
- **Raw Sources** (`vault/sources/`) — immutable, clipped or scraped content
- **Wiki** (`vault/wiki/`) — LLM-generated entity pages (people, concepts, tools)
- **Schema** (`vault/schema.md`) — conventions, frontmatter format

Primary ingest: Obsidian Web Clipper → `vault/inbox/` → `aig process` → sources + wiki pages.

### Key Files

| File | Purpose |
|------|---------|
| `config.yaml` | Vault path, channels, settings |
| `pyproject.toml` | Dependencies, tool config |
| `web-clipper-template.json` | Obsidian Web Clipper template for YouTube |
| `docs/PRD.md` | Product Requirements Document |
| `docs/features/AIG-*.md` | Feature specs with acceptance criteria + QA results |
| `docs/superpowers/spec/` | Brainstorming spec |
| `docs/workflow-guide.md` | User-facing workflow documentation |
| `features/INDEX.md` | Feature index with status |

### Source Modules

| Module | Responsibility |
|--------|---------------|
| `src/cli.py` | CLI entry point (click) — init, process, channel, feed, briefing, wiki |
| `src/config.py` | Load/save config.yaml |
| `src/transcript.py` | YouTube transcript extraction (youtube-transcript-api) |
| `src/metadata.py` | Video metadata via yt-dlp |
| `src/feed.py` | YouTube RSS feed monitoring (feedparser) |
| `src/process.py` | Post-processing pipeline: transcript → summary → wiki update |
| `src/summarize.py` | Claude API summary generation + wikilink extraction |
| `src/vault.py` | Obsidian vault file operations (read/write/move/log) |
| `src/wiki.py` | Wiki page CRUD, index rebuild, lint |
| `src/briefing.py` | Daily briefing generation, trend detection |

### Test Files

Tests in `tests/` mirror source modules: `test_config.py`, `test_vault.py`, `test_metadata.py`, `test_transcript.py`, `test_feed.py`, `test_wiki.py`, `test_briefing.py`.

Run: `.venv/Scripts/python.exe -m pytest tests/ -v`

### Conventions

- **Vault is NOT in git** — configured in `.gitignore`, path in `config.yaml`
- **Frontmatter standard** — see `vault/schema.md` for type/source_type/status/tags/topics
- **Wikilinks** — People: `[[Firstname Lastname]]`, Concepts: `[[Concept Name]]`, Tools: `[[Tool Name]]`
- **Result pattern** — Ok/Err dataclasses for expected errors (no exceptions)
- **Third-party types** — yt-dlp, feedparser, frontmatter lack stubs; use `# type: ignore[import-untyped]` and `Any` for their return types
- **ANTHROPIC_API_KEY** env var required for summary generation
