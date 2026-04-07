# [AIG-2] Wiki-Pflege durch Claude

## Status
- [x] Requirements
- [ ] Architecture
- [ ] Implementation
- [ ] QA
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
*Wird von /architecture ausgefüllt*

## QA Results
*Wird von /qa ausgefüllt*

## Changelog
- 2026-04-07: Erstellt via Superpowers Brainstorming
