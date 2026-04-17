---
category: concepts
last_updated: '2026-04-17'
related_sources:
- 2026-04-16-Claude Code + Graphify = Instant Knowledge Graph (Free).md
title: Knowledge Graph
type: wiki
---

# Knowledge Graph

Strukturierte Darstellung von Konzepten (Nodes) und Beziehungen (Edges). Im [[LLM Wiki]]-Kontext: Alternative zu reinem [[RAG]], bei der Verbindungen expliziert werden statt über Vektor-Ähnlichkeit implizit bleiben.

## Graphify-Beispiel

[[Graphify]] baut einen Knowledge Graph über Code + Docs + Media:
- **Nodes** = Klassen, Funktionen, Konzepte, Dokumente
- **Edges** = calls, imports, references, semantic relations
- **Neighborhoods** = Communities verwandter Konzepte (farblich gruppiert)

In einem Test-Projekt: 4.041 Nodes, 20.900 Edges, 185 Communities.

## Vorteile gegenüber Raw-File-Scanning

- [[Claude Code]] liest vor File-Reads zuerst den Graph-Summary → 2-3 gezielte Reads statt 15
- Quality-Boost: Antworten enthalten mehr strukturelle Details (Phase-Erklärungen statt bloße Funktionsnamen)
- Kosten-Einsparung: gering (~7-8% in typischen Sessions), wächst mit Session-Länge und Projekt-Größe

## Verwandt

- [[LLM Wiki]] — menschen-kuratierter Wissensspeicher in Markdown
- [[RAG]] — Retrieval via Embeddings, keine expliziten Edges
- [[Progressive Disclosure]] — gezieltes On-Demand-Laden von Kontext

## Sources

- [[2026-04-16-Claude Code + Graphify = Instant Knowledge Graph (Free).md]]
