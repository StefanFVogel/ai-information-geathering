---
category: tools
last_updated: '2026-04-17'
related_sources:
- 2026-04-16-Claude Code + Graphify = Instant Knowledge Graph (Free).md
title: Graphify
type: wiki
---

# Graphify

Tool, das über ein Projekt einmalig einen [[Knowledge Graph]] baut, den [[Claude Code]] bei jedem Session-Start via Hook automatisch liest. Ziel: Claude soll nicht jede Session dieselben Dateien neu lesen ("new hire every day" → "senior colleague with a map"). Shipped 48 Stunden nach [[Andrej Karpathy]]s Beschreibung der Idee, ~25.000 GitHub-Stars.

## Drei-Pass-Pipeline

1. **Code-Struktur** — lokaler Parser (Python, TypeScript, Go, Rust). Klassen, Funktionen, Imports, Calls. Keine API-Kosten.
2. **Audio/Video** — lokale Transkription via [[Faster-Whisper]]. Keine API-Kosten.
3. **Rest** (Markdown, PDFs, Images) — Claude-Sub-Agents extrahieren Konzepte und Beziehungen. Einziger Schritt mit API-Kosten, läuft nur einmal.

Ein Algorithmus gruppiert verwandte Konzepte in "Neighborhoods" (Communities). Output: `graphify-out/` mit `GRAPH_REPORT.md` und interaktivem `graph.html`.

## Setup

```
pip install graphifyy
graphify install
graphify claude install    # wires Hook
graphify update            # inkrementelles Update
graphify hook install      # Git-Hook für Auto-Rebuild
```

## Benchmark-Realität

Claim: 71,5x Token-Reduktion — aber Vergleich gegen "alle Files direkt in Context laden", ein Workflow den niemand nutzt. Reale Einsparung in typischen Sessions: ~7-8%, aber deutlich bessere Antwortqualität. Großer Nutzen bei Mixed-Content-Vaults (Research, Meeting-Recordings, PDFs).

## Links

- GitHub: https://github.com/safishamsi/graphify

## Sources

- [[2026-04-16-Claude Code + Graphify = Instant Knowledge Graph (Free).md]]
