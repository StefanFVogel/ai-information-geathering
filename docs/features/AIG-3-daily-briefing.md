# [AIG-3] Tägliches Briefing

## Status
- [x] Requirements
- [ ] Architecture
- [ ] Implementation
- [ ] QA
- [ ] Deployed

## User Stories
1. Als User möchte ich jeden Tag eine kurze Übersicht bekommen welche neuen Videos auf meinen Kanälen erschienen sind, damit ich nichts verpasse.
2. Als User möchte ich dass Trends erkannt werden (Thema X wird von mehreren Kanälen gleichzeitig behandelt), damit ich weiß was gerade wichtig ist.
3. Als User möchte ich eine Relevanz-Einschätzung pro Video (1-5 Sterne), damit ich weiß was ich priorisieren soll.
4. Als User möchte ich das Briefing als Obsidian-Seite in `vault/daily/` haben, damit ich es durchblättern und auf Links klicken kann.

## Acceptance Criteria
- [ ] `cli briefing` erstellt eine Markdown-Datei in `vault/daily/YYYY-MM-DD.md`
- [ ] Briefing enthält: Datum, Anzahl neue Videos, Top-Videos nach Relevanz
- [ ] Jedes Video im Briefing hat: Titel (als Link zur Source), Kanal, Relevanz (1-5), 1-Satz-Zusammenfassung
- [ ] Trend-Sektion: Themen die bei 2+ Kanälen in den letzten 7 Tagen aufgetaucht sind
- [ ] "Neue Köpfe"-Sektion: Personen die zum ersten Mal erwähnt werden
- [ ] Briefing verlinkt auf bestehende Wiki-Seiten via Wikilinks
- [ ] Frontmatter: type: daily, date, video_count, top_topics
- [ ] Ohne neue Videos seit letztem Briefing: kurze "Nichts Neues"-Meldung statt leerer Seite
- [ ] Briefing-Generierung dauert < 60 Sekunden

## Edge Cases
- Erster Tag (kein vorheriges Briefing) → alle bekannten Videos als "neu" behandeln, Hinweis geben
- Kanal hat 50+ Videos in einem Tag (z.B. Playlist-Import) → Top 10 zeigen, Rest als "X weitere" zusammenfassen
- Keine Kanäle registriert → hilfreiche Meldung: "Füge erst Kanäle hinzu mit `cli channel add`"
- Trend-Erkennung bei wenigen Kanälen (<3) → Sektion weglassen, Hinweis dass mehr Kanäle nötig

## Dependencies
- [AIG-1] YouTube Ingest Pipeline (Kanäle, Feed-Daten)
- [AIG-2] Wiki-Pflege (Wikilinks zu bestehenden Seiten)
- config.yaml (Kanalliste)

## Tech Design
*Wird von /architecture ausgefüllt*

## QA Results
*Wird von /qa ausgefüllt*

## Changelog
- 2026-04-07: Erstellt via Superpowers Brainstorming
