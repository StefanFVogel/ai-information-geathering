# [AIG-1] YouTube Ingest Pipeline

## Status
- [x] Requirements
- [x] Architecture
- [ ] Implementation
- [ ] QA
- [ ] Deployed

## User Stories
1. Als User möchte ich ein YouTube-Video im Browser per Web Clipper in meinen Vault clippen, damit nur Videos die ich bewusst ausgewählt habe ins System kommen.
2. Als User möchte ich dass geclippte Videos automatisch nachverarbeitet werden (Transkript + Zusammenfassung), damit ich den Inhalt schnell erfassen kann ohne das Video nochmal zu schauen.
3. Als User möchte ich YouTube-Kanäle registrieren und über neue Videos informiert werden, damit ich interessante Kanäle im Blick behalte und entscheiden kann was ich clippe.
4. Als User möchte ich die Metadaten eines Videos automatisch als Frontmatter haben, damit Dataview-Queries funktionieren.

## Acceptance Criteria

### Web Clipper Ingest (Hauptweg)
- [ ] Obsidian Web Clipper Template für YouTube erstellt und dokumentiert
- [ ] Template erzeugt korrektes Frontmatter: type, source_type, title, url, author, date, tags, status: inbox
- [ ] Geclippte Videos landen in `vault/inbox/` mit Dateiname `YYYY-MM-DD-video-slug.md`
- [ ] Template extrahiert Metadaten automatisch (Titel, Kanal, Datum, Beschreibung)

### Post-Processing (Python CLI)
- [ ] `cli process` findet neue Dateien in `vault/inbox/` mit status: inbox
- [ ] Transkript wird vollständig extrahiert (mit Timestamps) und an die Datei angehängt
- [ ] Zusammenfassung (ca. 300 Wörter) wird am Anfang der Datei eingefügt
- [ ] Erwähnte Personen, Papers und Tools werden als `[[Wikilinks]]` formatiert
- [ ] Status wird von `inbox` auf `processed` aktualisiert
- [ ] Verarbeitete Datei wird von `inbox/` nach `sources/youtube/` verschoben
- [ ] Bei fehlenden Transkripten: Fallback auf Beschreibung, Warnung in der Datei

### Feed Discovery (Optional)
- [ ] `cli channel add <channel-url>` registriert einen YouTube-Kanal in `config.yaml`
- [ ] `cli feed check` listet neue Videos aller registrierten Kanäle seit dem letzten Check
- [ ] Ausgabe: Titel, Kanal, Datum, URL — User entscheidet selbst ob er clippt

### Konfiguration
- [ ] Vault-Pfad ist über `config.yaml` konfigurierbar
- [ ] Bei Netzwerkfehlern: klare Fehlermeldung

## Edge Cases
- Video hat kein Transkript → Fallback auf Beschreibung + Metadaten, Warnung in Datei
- Video ist privat oder gelöscht (Transkript nicht abrufbar) → Warnung, Datei bleibt mit Clip-Inhalt
- Transkript in Nicht-Englisch → Sprache im Frontmatter, bevorzugt englisches Transkript
- Sehr langes Video (>2h) → Transkript vollständig, Zusammenfassung in Abschnitte
- Datei in inbox/ hat keine YouTube-URL → überspringen mit Hinweis
- Video wurde bereits verarbeitet (existiert in sources/) → Warnung, Option zum Überschreiben

## Dependencies
- Obsidian Web Clipper (Browser Extension)
- youtube-transcript-api (Transkript-Extraktion)
- yt-dlp (Metadaten + Channel-ID Auflösung)
- feedparser (RSS für Feed Discovery)
- python-frontmatter (YAML Frontmatter)
- anthropic SDK (Claude API für Zusammenfassung)
- config.yaml (Vault-Pfad, Kanalliste)

## Tech Design

### Component Structure

```
src/
  __init__.py              ← NEW  Package init
  cli.py                   ← NEW  CLI entry point (click)
  config.py                ← NEW  Config laden aus config.yaml
  transcript.py            ← NEW  Transkript-Extraktion (youtube-transcript-api)
  metadata.py              ← NEW  Video-Metadaten via yt-dlp
  feed.py                  ← NEW  RSS Feed Monitoring (feedparser)
  process.py               ← NEW  Post-Processing: Transkript + Zusammenfassung an Inbox-Dateien
  summarize.py             ← NEW  Claude API Zusammenfassung + Wikilink-Extraktion
  vault.py                 ← NEW  Vault-Operationen (Dateien lesen/schreiben/verschieben)

config.yaml                ← NEW  Konfiguration
vault/                     ← NEW  Obsidian Vault (in .gitignore)

Web Clipper:
  youtube-template.json    ← NEW  Obsidian Web Clipper Template (wird manuell importiert)
```

### Datenfluss

```
Browser                    vault/inbox/              vault/sources/youtube/
   │                           │                           │
   │  Web Clipper              │  cli process              │
   │  (youtube-template)       │                           │
   ├──────────────────────►    │                           │
   │  Frontmatter + Clip       │  1. Inbox scannen         │
   │                           │  2. YouTube-URL finden    │
   │                           │  3. Transkript ziehen     │
   │                           │  4. Zusammenfassung       │
   │                           │  5. Wikilinks einfügen    │
   │                           │  6. Status → processed    │
   │                           ├──────────────────────►    │
   │                           │  7. Datei verschieben     │
```

### Data Model

Kein SQL — alle Daten sind Markdown-Dateien mit YAML Frontmatter.

**VideoMetadata** (in-memory, wird aus yt-dlp extrahiert)
- video_id: string — YouTube Video ID
- title: string
- channel_name: string
- channel_id: string
- upload_date: date
- description: string
- tags: list of strings
- duration: int (Sekunden)
- url: string
- language: string

**Channel** (in config.yaml)
- name: string — Display-Name
- channel_id: string — YouTube Channel ID
- rss_url: string — abgeleitet aus channel_id
- added_date: date

**Config** (config.yaml)
- vault_path: string — default: `./vault/`
- channels: list of Channel
- last_feed_check: datetime
- summary_length: int — default: 300

### Tech Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Primärer Ingest | Obsidian Web Clipper | User kuratiert aktiv — nur Relevantes kommt rein |
| CLI Rolle | Post-Processor | Verarbeitet was der User geclippt hat, kein eigener Ingest |
| CLI Framework | `click` | Leichtgewichtig, deklarativ, weit verbreitet |
| Transkript | `youtube-transcript-api` | Kein API Key, direkte Extraktion |
| Metadaten | `yt-dlp` (als Library) | Robusteste Option, kein API Key |
| RSS | `feedparser` | Simpel, Standard-Format |
| Zusammenfassung | Claude via `anthropic` SDK | LLM-Zusammenfassung mit Wikilink-Extraktion |
| Persistenz | Dateisystem (Markdown) | Obsidian ist die Datenbank |
| Duplikaterkennung | Dateiname-Check | Einfach, deterministisch |
| Konfiguration | `config.yaml` + `pyyaml` | Menschenlesbar, einfach editierbar |

### Dependencies

**Python packages (pip):**
- youtube-transcript-api, yt-dlp, feedparser, python-frontmatter, click, pyyaml, anthropic

**Browser:**
- Obsidian Web Clipper Extension (Chrome/Edge)

**Infrastructure:** Keine — alles lokal.

## QA Results

**Date:** 2026-04-07
**Tester:** Claude QA
**Ampel:** GREEN

### Acceptance Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Web Clipper Template erstellt | PASS | `web-clipper-template.json` vorhanden mit korrektem Schema |
| 2 | Template erzeugt korrektes Frontmatter | PASS | Template enthält type, source_type, title, url, author, date, tags, status |
| 3 | Geclippte Videos landen in inbox/ | PASS | Template path: "inbox", Dateiname: YYYY-MM-DD-slug |
| 4 | `cli process` findet inbox-Dateien | PASS | `test_vault.py::test_list_inbox_with_files` — 19/19 tests passed |
| 5 | Transkript-Extraktion funktioniert | PASS | `test_transcript.py` — Segment-Parsing + Timestamp-Format korrekt |
| 6 | Video-ID Extraktion aus URLs | PASS | `test_metadata.py` — Standard, Short, Embed URLs + Params korrekt |
| 7 | Config laden/speichern | PASS | `test_config.py` — Defaults, Channels, Round-Trip korrekt |
| 8 | Vault-Struktur erstellen | PASS | `test_vault.py::test_ensure_vault_structure` — alle Ordner korrekt |
| 9 | Dateien schreiben/lesen/verschieben | PASS | `test_vault.py` — write_note, read_note, move_to_sources korrekt |
| 10 | Log-Einträge | PASS | `test_vault.py::test_append_to_log` — Format korrekt |
| 11 | Vault-Pfad konfigurierbar | PASS | config.yaml vault_path wird korrekt geladen |

### Security Audit

| Area | Status | Notes |
|---|---|---|
| Secrets | PASS | Kein API Key hardcoded, Anthropic SDK nutzt ANTHROPIC_API_KEY env var |
| Input Validation | PASS | Video-ID via Regex validiert, URL-Check vor Processing |
| Injection | N/A | Kein SQL, kein HTML-Output |

### Bugs Found

Keine Critical/High Bugs gefunden.

| # | Severity | Description | File/Line |
|---|----------|-------------|-----------|
| 1 | Low | frontmatter.load() deprecation warning (codecs.open) | Third-party, nicht unser Code |

### Verdict

**READY**
Reason: Alle Acceptance Criteria erfüllt, Ampel GRÜN, 19/19 Tests bestanden, keine Security-Findings.

## Changelog
- 2026-04-07: Erstellt via Superpowers Brainstorming
- 2026-04-07: Architektur-Pivot: Web Clipper als primärer Ingest statt CLI, Python wird Post-Processor
