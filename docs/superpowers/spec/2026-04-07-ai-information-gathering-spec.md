# Superpowers Brainstorming: AI Information Gathering

**Datum**: 2026-04-07
**Methode**: Superpowers Brainstorming
**Grundlagen**: [Karpathy LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), dev-standards Workflow

---

## 1. Vision

Ein persönliches AI-gestütztes Wissensmanagement-Tool, das YouTube-Content und andere Quellen automatisch sammelt, zusammenfasst und in einem Obsidian Wiki organisiert — damit der User AI-Trends verfolgen kann ohne alles schauen zu müssen.

**Setup**: Claude auf einer Seite, Obsidian auf der anderen. Claude macht die Arbeit, der User browst die Ergebnisse in Echtzeit.

---

## 2. Problem

| # | Problem | Auswirkung |
|---|---------|------------|
| 1 | **Information Overload** | Zu viel AI-Content auf YouTube und im Web. Unmöglich alles zu konsumieren. |
| 2 | **Fehlende Struktur** | Gefundene Informationen gehen verloren. Kein zentraler Ort, keine Verknüpfungen. |
| 3 | **Verpasste Trends** | Wichtige Entwicklungen werden übersehen weil man nicht alle Kanäle verfolgen kann. |
| 4 | **Quellen-Verlust** | Von Zusammenfassungen kommt man nicht zurück zu Originalquellen (Papers, Tools, Repos). |

---

## 3. Zielgruppe

Eine Person (der User) — AI-Praktiker der auf dem Laufenden bleiben will ohne den ganzen Tag Content zu konsumieren. Muttersprache Deutsch, Fokus auf englischsprachige Quellen.

---

## 4. Superpowers-Analyse

Die Projektidee entstand aus der Frage: *"Was würde dieses Tool tun, wenn es Superkräfte hätte?"*

| Superkraft | Fähigkeit | Abgeleitetes Feature |
|------------|-----------|---------------------|
| **Allwissenheit** | Jede Quelle gleichzeitig durchsuchen | Multi-Source Gathering (YouTube, Web, Papers) |
| **Telepathie** | Versteht was der User wirklich wissen will | Intelligente Zusammenfassungen + Relevanz-Bewertung |
| **Röntgenblick** | Sieht durch Lärm hindurch, erkennt Bias | Quellenbewertung + Trend-Erkennung |
| **Superspeed** | Sammelt und strukturiert in Sekunden | Automatische Verarbeitung + tägliches Briefing |
| **Formwandlung** | Liefert in jedem Format | Obsidian-kompatibles Markdown mit Wikilinks |
| **Zeitreise** | Verfolgt Entwicklungen über Zeit | Chronologisches Log + Verlaufsanalyse |

---

## 5. Architektur-Konzept: Karpathy LLM Wiki Pattern

Drei Schichten nach Karpathy:

```
┌─────────────────────────────────────────────┐
│  Schema Layer                               │
│  schema.md — Konventionen, Workflows        │
├─────────────────────────────────────────────┤
│  Wiki Layer (LLM-generiert & gepflegt)      │
│  wiki/people/, wiki/concepts/, wiki/tools/  │
│  index.md, log.md                           │
├─────────────────────────────────────────────┤
│  Raw Sources Layer (unveränderlich)          │
│  sources/youtube/, sources/articles/, ...    │
└─────────────────────────────────────────────┘
```

**Kernoperationen:**
- **Ingest** — Neue Quelle rein → LLM liest, fasst zusammen, verknüpft, aktualisiert Index
- **Query** — Frage stellen → LLM durchsucht Wiki, synthetisiert Antwort mit Zitaten
- **Lint** — Gesundheitscheck → Widersprüche, verwaiste Seiten, fehlende Verknüpfungen

**Arbeitsteilung:**
- *Mensch*: Quellen kuratieren, Analyse steuern, gute Fragen stellen, denken
- *LLM*: Alles andere (Bookkeeping, Verknüpfungen, Zusammenfassungen, Index-Pflege)

---

## 6. Vier Eingangswege

```
Weg 1: Automatisch (Python)        Weg 3: Web Clipper (Browser)
  YouTube RSS → neue Videos           Webseite → Clip → Vault
  → Transkript ziehen                 → Template formatiert
  → Zusammenfassung                   → landet in sources/
  → in Inbox                          

Weg 2: On-Demand (Claude)          Weg 4: Manuell (Dateien)
  "Fasse dieses Video zusammen"       PDF, Markdown, Notizen
  → Transkript + Analyse              → in sources/ ablegen
  → Wiki-Seiten updaten               → Claude verarbeitet
```

---

## 7. Kern-Features (v1)

### [AIG-1] YouTube Ingest Pipeline

**User Stories:**
1. Als User möchte ich eine YouTube-URL eingeben und automatisch Transkript + Zusammenfassung als Markdown im Vault erhalten, damit ich ein Video nicht schauen muss um den Inhalt zu kennen.
2. Als User möchte ich YouTube-Kanäle registrieren und automatisch über neue Videos informiert werden, damit ich nichts Wichtiges verpasse.
3. Als User möchte ich die Metadaten eines Videos (Titel, Kanal, Datum, Beschreibung, Tags) automatisch als Frontmatter im Markdown haben, damit Dataview-Queries funktionieren.

**Acceptance Criteria:**
- [ ] `cli ingest <youtube-url>` erstellt eine Markdown-Datei in `vault/sources/youtube/` mit korrektem Frontmatter
- [ ] Frontmatter enthält: type, source_type, title, url, author, date, tags, status, channel_id
- [ ] Transkript wird vollständig extrahiert (mit Timestamps)
- [ ] Zusammenfassung (ca. 300 Wörter) wird am Anfang der Datei eingefügt
- [ ] Erwähnte Personen, Papers und Tools werden als `[[Wikilinks]]` formatiert
- [ ] `cli channel add <channel-url>` registriert einen YouTube-Kanal in `config.yaml`
- [ ] `cli feed check` listet neue Videos aller registrierten Kanäle seit dem letzten Check
- [ ] Neue Videos erscheinen in `vault/inbox/` mit Status `inbox` und Relevanz-Schätzung (1-5)
- [ ] Bei Netzwerkfehlern oder fehlenden Transkripten: klare Fehlermeldung
- [ ] Vault-Pfad ist über `config.yaml` konfigurierbar

**Edge Cases:**
- Video hat kein Transkript → Fallback auf Beschreibung + Metadaten, Warnung
- Video ist privat/gelöscht → klare Fehlermeldung
- Kanal-URL in verschiedenen Formaten (@handle, /channel/ID, /c/name) → alle unterstützen
- Transkript in Nicht-Englisch → Sprache im Frontmatter, bevorzugt englisches Transkript
- Sehr langes Video (>2h) → Zusammenfassung in Abschnitte gliedern
- Video bereits verarbeitet → Warnung, Option zum Überschreiben

**Dependencies:** youtube-transcript-api, yt-dlp, feedparser, python-frontmatter

---

### [AIG-2] Wiki-Pflege durch Claude

**User Stories:**
1. Als User möchte ich dass Claude eine neue Quelle liest und automatisch Personen-, Konzept- und Tool-Seiten erstellt oder aktualisiert, damit mein Wissen vernetzt wächst.
2. Als User möchte ich dass Index und Log automatisch aktuell gehalten werden, damit ich den Überblick behalte.
3. Als User möchte ich Claude Fragen über mein Wissen stellen können ("Was sagen die Experten zu RAG?"), damit ich Synthesen über mehrere Quellen bekomme.
4. Als User möchte ich dass Claude Widersprüche zwischen Quellen erkennt und kennzeichnet.

**Acceptance Criteria:**
- [ ] `vault/schema.md` definiert Konventionen: Ordnerstruktur, Frontmatter-Format, Wikilink-Regeln
- [ ] Ingest-Workflow: Claude liest Source → erstellt/aktualisiert Wiki-Seiten in `wiki/people/`, `wiki/concepts/`, `wiki/tools/`
- [ ] Jede Wiki-Seite hat standardisiertes Frontmatter (type: wiki, related_sources, last_updated)
- [ ] Personen-Seiten: Kurzbiographie, Zugehörigkeit, Hauptthemen, Quellenliste
- [ ] Konzept-Seiten: Definition, verwandte Konzepte als Wikilinks, Pro/Contra, Quellen
- [ ] `index.md` wird bei jedem Ingest aktualisiert
- [ ] `log.md` wird bei jeder Aktion erweitert (Datum, Aktion, betroffene Seiten)
- [ ] Query-Workflow: Claude beantwortet Fragen und zitiert Wiki-Seiten
- [ ] Lint-Workflow: Verwaiste Seiten, fehlende Verknüpfungen, Widersprüche identifizieren
- [ ] MCP Server ermöglicht Claude den Vault-Zugriff

**Edge Cases:**
- Person hat schon eine Seite → aktualisieren statt duplizieren
- Widersprüchliche Infos → beide festhalten mit Quellenangabe
- Wiki wächst über ~100 Seiten → Hinweis auf Skalierungsbedarf
- Quelle in anderer Sprache → Wiki bleibt einheitlich auf Englisch

**Dependencies:** AIG-1, MCP Server (mcp-obsidian oder Local REST API)

---

### [AIG-3] Tägliches Briefing

**User Stories:**
1. Als User möchte ich täglich eine Übersicht neuer Videos auf meinen Kanälen bekommen.
2. Als User möchte ich Trends erkennen (Thema X bei mehreren Kanälen gleichzeitig).
3. Als User möchte ich eine Relevanz-Einschätzung pro Video (1-5).
4. Als User möchte ich das Briefing als Obsidian-Seite in `vault/daily/`.

**Acceptance Criteria:**
- [ ] `cli briefing` erstellt `vault/daily/YYYY-MM-DD.md`
- [ ] Enthält: Datum, Anzahl neue Videos, Top-Videos nach Relevanz
- [ ] Pro Video: Titel (Link), Kanal, Relevanz (1-5), 1-Satz-Zusammenfassung
- [ ] Trend-Sektion: Themen bei 2+ Kanälen in den letzten 7 Tagen
- [ ] "Neue Köpfe"-Sektion: Erstmals erwähnte Personen
- [ ] Wikilinks zu bestehenden Wiki-Seiten
- [ ] Frontmatter: type: daily, date, video_count, top_topics
- [ ] Ohne neue Videos: "Nichts Neues"-Meldung
- [ ] Generierung < 60 Sekunden

**Edge Cases:**
- Erster Tag → alle Videos als "neu", Hinweis
- 50+ Videos an einem Tag → Top 10, Rest als "X weitere"
- Keine Kanäle → hilfreiche Meldung
- Wenige Kanäle (<3) → Trend-Sektion weglassen

**Dependencies:** AIG-1, AIG-2, config.yaml

---

## 8. Out of Scope (v1)

- Web UI / Dashboard (Obsidian ist das Interface)
- Echtzeit-Streaming / Live-Monitoring
- Mobile App
- Automatische Video-Downloads (nur Transkripte + Metadaten)

---

## 9. Tech Stack

### Python Libraries
| Library | Zweck |
|---------|-------|
| `youtube-transcript-api` | Transkripte ziehen (kein API Key) |
| `yt-dlp` | Metadaten (Titel, Kanal, Datum) |
| `feedparser` | YouTube RSS Feed Monitoring |
| `markdownify` | HTML → Markdown |
| `python-frontmatter` | YAML Frontmatter |

### Obsidian Plugins
| Plugin | Zweck |
|--------|-------|
| **Web Clipper** (offiziell) | Webseiten direkt in Vault clippen |
| **Dataview** | Dynamische Queries über Frontmatter |
| **Local REST API** | Claude/Python Zugriff auf Vault |
| **YTranscript** | YouTube Transkripte direkt in Obsidian |

### Qualität
- dev-standards Submodule (Architekten-Ampel, Hooks, Skills)
- Python 3.12, Ruff, Pyright, Bandit

---

## 10. Vault-Schema

### Ordnerstruktur
```
vault/
├── schema.md          ← Konventionen
├── index.md           ← Katalog aller Wiki-Seiten
├── log.md             ← Chronologisches Aktivitätslog
├── inbox/             ← Neue, unverarbeitete Einträge
├── sources/
│   ├── youtube/       ← Transkripte + Metadaten
│   ├── articles/      ← Web Clipper Output
│   ├── papers/        ← PDFs, Papers
│   └── other/         ← Sonstige Quellen
├── wiki/
│   ├── people/        ← Personen
│   ├── concepts/      ← Konzepte
│   ├── tools/         ← Tools & Frameworks
│   └── syntheses/     ← Vergleiche, Analysen
├── channels/          ← YouTube-Kanal-Profile
├── daily/             ← Tägliche Briefings
└── assets/            ← Bilder, Attachments
```

### Frontmatter-Standard
```yaml
---
type: source | wiki | inbox | channel | daily
source_type: youtube | article | paper | other
title: "Titel"
url: "https://..."
author: "[[Person]]"
date: 2026-04-07
tags: [ai, llm, agents]
status: inbox | curated | processed
relevance: 3
topics: ["[[RAG]]", "[[Agents]]"]
related_sources: ["[[source-datei]]"]
last_updated: 2026-04-07
---
```

### Namenskonventionen
- Dateinamen: `kebab-case.md` (z.B. `andrej-karpathy.md`)
- Wikilinks: `[[Andrej Karpathy]]` (Display Name)
- YouTube Sources: `YYYY-MM-DD-video-slug.md`
- Daily Briefings: `YYYY-MM-DD.md`

### Wikilink-Regeln
- Personen: `[[Vorname Nachname]]`
- Konzepte: `[[Konzeptname]]` (englisch)
- Tools: `[[Tool Name]]`
- Quellen-Referenz: `> Quelle: [[source-datei]]`

---

## 11. Nächste Schritte

1. **Setup**: venv + `maintain_tools.py --setup` + CLAUDE.md
2. **PRD erstellen**: `docs/PRD.md` basierend auf dieser Spec
3. **Feature-Specs**: `docs/features/AIG-{1,2,3}-*.md`
4. **`/architecture`** für AIG-1 als erstes Feature
5. **`/backend`** für Implementierung
6. **`/qa`** für Tests

---

## Quellen

- [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [dev-standards Submodule](https://github.com/StefanFVogel/dev-standards)
- Obsidian Web Clipper, Dataview, Local REST API, YTranscript Plugins
- youtube-transcript-api, yt-dlp, feedparser (Python)
