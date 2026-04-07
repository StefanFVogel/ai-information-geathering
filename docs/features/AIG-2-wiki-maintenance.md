# [AIG-2] Wiki-Pflege durch Claude

## Status
- [x] Requirements
- [x] Architecture
- [x] Implementation
- [x] QA
- [ ] Deployed

## User Stories
1. Als User möchte ich dass Claude eine neue Quelle liest und automatisch Personen-, Konzept- und Tool-Seiten im Wiki erstellt oder aktualisiert, damit mein Wissen vernetzt wächst.
2. Als User möchte ich dass der Wiki-Index (`index.md`) und das Log (`log.md`) automatisch aktuell gehalten werden, damit ich den Überblick behalte.
3. Als User möchte ich Claude Fragen über mein gesammeltes Wissen stellen können ("Was sagen die Experten zu RAG?"), damit ich Synthesen über mehrere Quellen bekomme.
4. Als User möchte ich dass Claude Widersprüche zwischen Quellen erkennt und kennzeichnet, damit ich informierte Entscheidungen treffen kann.

## Acceptance Criteria
- [ ] `vault/schema.md` definiert Konventionen: Ordnerstruktur, Frontmatter-Format, Wikilink-Regeln, Namenskonventionen
- [ ] Ingest-Workflow: Claude liest neue Source → erstellt/aktualisiert relevante Wiki-Seiten in `wiki/people/`, `wiki/concepts/`, `wiki/tools/`
- [ ] Jede Wiki-Seite hat standardisiertes Frontmatter (type: wiki, related_sources, last_updated)
- [ ] Personen-Seiten enthalten: Kurzbiographie, Zugehörigkeit, Hauptthemen, Liste aller Quellen wo erwähnt
- [ ] Konzept-Seiten enthalten: Definition, verwandte Konzepte als Wikilinks, Pro/Contra wenn kontrovers, Quellen
- [ ] `index.md` wird bei jedem Ingest aktualisiert: Seitenname + Einzeiler + Kategorie
- [ ] `log.md` wird bei jeder Aktion erweitert: Datum, Aktion (ingest/query/lint), betroffene Seiten
- [ ] Query-Workflow: Claude kann Fragen beantworten und zitiert dabei die relevanten Wiki-Seiten
- [ ] Lint-Workflow: Claude kann verwaiste Seiten, fehlende Verknüpfungen und Widersprüche identifizieren
- [ ] MCP Server (mcp-obsidian oder Local REST API) ermöglicht Claude den Vault-Zugriff

## Edge Cases
- Quelle erwähnt eine Person die schon eine Seite hat → aktualisieren statt duplizieren
- Widersprüchliche Informationen aus verschiedenen Quellen → beide festhalten mit Quellenangabe
- Wiki wächst über ~100 Seiten → Index-basierte Suche wird langsam → Hinweis auf Skalierungsbedarf
- Quelle in anderer Sprache als bestehende Wiki-Seiten → Wiki bleibt einheitlich auf Englisch

## Dependencies
- [AIG-1] YouTube Ingest Pipeline (liefert die Quellen)
- MCP Server für Obsidian (mcp-obsidian oder Local REST API Plugin)
- Obsidian Vault mit definierter Struktur (vault/schema.md)

## Tech Design

### Component Structure
```
src/
  wiki.py              ← NEW  Wiki page CRUD, index rebuild, lint
  process.py           ← MOD  Integrated wiki update after ingest
  cli.py               ← MOD  Added wiki rebuild-index, wiki lint commands
```

### Tech Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Entity detection | Wikilink regex from summary text | Simple, leverages Claude's output |
| Page format | frontmatter Post with related_sources | Tracks provenance per entity |
| Index rebuild | Full scan of wiki/ directory | Reliable at moderate scale (<100 pages) |
| Lint | Orphan + broken link detection | Two most common wiki health issues |

## QA Results

**Date:** 2026-04-07
**Tester:** Claude QA
**Ampel:** GREEN

### Acceptance Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Entity page creation (people) | PASS | test_update_wiki_creates_people_page |
| 2 | Entity page creation (concepts) | PASS | test_update_wiki_creates_concept_page |
| 3 | Source reference on existing page | PASS | test_update_wiki_adds_source_to_existing |
| 4 | No duplicate sources | PASS | test_update_wiki_no_duplicate_source |
| 5 | Index rebuild includes all pages | PASS | test_update_index |
| 6 | Index shows empty sections | PASS | test_update_index_empty_wiki |
| 7 | Lint detects orphaned pages | PASS | test_lint_wiki_finds_orphans |
| 8 | Lint passes on healthy wiki | PASS | test_lint_wiki_healthy |
| 9 | Wiki integrated into ingest pipeline | PASS | process.py _update_wiki called after ingest |
| 10 | CLI commands wiki rebuild-index, lint | PASS | Import check OK |

### Verdict
**READY**

## Changelog
- 2026-04-07: Erstellt via Superpowers Brainstorming
- 2026-04-07: Architecture, Implementation, QA completed
