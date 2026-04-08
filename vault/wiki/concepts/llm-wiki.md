---
category: concepts
last_updated: '2026-04-07'
related_sources:
- Andrej Karpathy Just 10x'd Everyone's Claude Code.md
title: LLM Wiki
type: wiki
---

# LLM Wiki

A pattern by [[Andrej Karpathy]] where LLMs build and maintain a persistent wiki -- structured, interlinked markdown files -- instead of traditional [[RAG]].

## How It Works

1. **Raw Sources** -- articles, transcripts, PDFs into raw folder
2. **LLM Processing** -- reads sources, creates entity/concept pages, builds cross-references
3. **Wiki Output** -- organized markdown with wikilinks, index.md, log.md
4. **Query** -- ask questions, LLM searches wiki and synthesizes answers
5. **[[Linting]]** -- periodic health checks for inconsistencies and gaps

## Why It Matters

- No infrastructure needed -- just markdown files
- Knowledge compounds -- each source enriches existing pages
- 95% token reduction reported vs traditional approaches
- Deep relationships via wikilinks vs shallow similarity search

## Sources

- [[Andrej Karpathy Just 10x'd Everyone's Claude Code.md]]
- [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)