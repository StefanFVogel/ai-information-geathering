---
type: schema
title: "Vault Schema"
---

# Vault Schema

## Ordnerstruktur

- `inbox/` — Neue, unverarbeitete Einträge (Web Clipper Output)
- `sources/youtube/` — Verarbeitete YouTube-Transkripte
- `sources/articles/` — Web-Artikel
- `sources/papers/` — Papers, PDFs
- `sources/other/` — Sonstige Quellen
- `wiki/people/` — Personen (Forscher, Creator)
- `wiki/concepts/` — Konzepte (RAG, Fine-Tuning, Agents)
- `wiki/tools/` — Tools & Frameworks
- `wiki/syntheses/` — Vergleiche, Trend-Analysen
- `channels/` — YouTube-Kanal-Profile
- `daily/` — Tägliche Briefings
- `assets/` — Bilder, Attachments

## Frontmatter-Standard

```yaml
type: source | wiki | inbox | channel | daily
source_type: youtube | article | paper | other
title: "Titel"
url: "https://..."
author: "[[Person]]"
date: 2026-04-07
tags: [ai, llm]
status: inbox | curated | processed
relevance: 3
topics: ["[[Konzept]]"]
```

## Namenskonventionen

- Dateinamen: `kebab-case.md`
- YouTube Sources: `YYYY-MM-DD-video-slug.md`
- Daily Briefings: `YYYY-MM-DD.md`
- Wikilinks: `[[Vorname Nachname]]`, `[[Konzeptname]]`, `[[Tool Name]]`
