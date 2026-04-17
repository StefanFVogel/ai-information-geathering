---
category: tools
last_updated: '2026-04-17'
related_sources:
- 2026-04-16-Claude Opus 4.7 Just Dropped... Or Did It Really.md
- 2026-04-17-I Turned Claude Opus 4.7 Into a 247 Trader.md
title: Opus 4.7
type: wiki
---

# Opus 4.7

[[Anthropic]]s aktuelles Top-Modell, Release Mitte April 2026. Marketing-Fokus: "full-throttle agentic work, judgment over ambiguity, self-verifying outputs." Direkter Upgrade-Pfad von [[Opus 4.6]] — aber Token-Verbrauch steigt um 1-1.3x durch neuen Tokenizer und tieferes Thinking auf höheren Effort-Leveln.

## Neue Features

- **Adaptive Thinking** — Modell entscheidet selbst, wieviel Reasoning pro Turn nötig ist
- **X-High Effort Level** — exklusiv für 4.7, über "max" hinaus
- **1M-Token-Context-Window** (geteilt mit 4.6)
- **Substantially better vision** — strukturelle Modell-Änderung
- **Document reasoning**, **biomolecular reasoning** (>2x), **long-term coherence**
- Neuer Slash-Command [[Ultra Review]] (`/ultra-review`) — dedizierte Review-Session, liest Änderungen und flaggt Probleme

## Benchmarks

- SWBench Pro: deutlicher Sprung
- 3x Production-Task-Resolution auf Rakuten-Third-Party-Benchmark
- Agentic Financial Analysis: +4% vs. 4.6
- Misaligned Behavior Benchmark: zwischen 4.6 und Mythus-Preview

## Kontext zum Release

Opus 4.6 war wegen silenter Drossel ([[Adaptive Thinking]], Effort-Default auf "medium") in Verruf geraten — jeder 4.6-Fix findet sich 1:1 in 4.7-Marketing wieder. Nates Verdikt: real neue Features (X-high, Vision) + Fixes, aber Marketing-Optik fragwürdig.

## Einsatz

- [[Nate Herk]] baut auf Opus 4.7 + [[Claude Code Routines]] einen 24/7-[[AI Trading]]-Agent
- Model ist verfügbar im Web, Claude Desktop App, Claude Code (`claude update`), VS Code Extension

## Sources

- [[2026-04-16-Claude Opus 4.7 Just Dropped... Or Did It Really.md]]
- [[2026-04-17-I Turned Claude Opus 4.7 Into a 247 Trader.md]]
