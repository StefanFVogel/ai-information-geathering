# Product Requirements Document

## Vision
Ein persönliches AI-gestütztes Wissensmanagement-Tool, das YouTube-Content und andere Quellen automatisch sammelt, zusammenfasst und in einem Obsidian Wiki organisiert — damit ein AI-Praktiker Trends verfolgen kann ohne alles schauen zu müssen.

## Problem
1. **Information Overload**: Zu viel AI-Content auf YouTube und im Web. Unmöglich alles zu konsumieren.
2. **Fehlende Struktur**: Gefundene Informationen gehen verloren. Kein zentraler Ort, keine Verknüpfungen zwischen Personen, Konzepten und Quellen.
3. **Verpasste Trends**: Wichtige Entwicklungen werden übersehen weil man nicht alle Kanäle verfolgen kann.
4. **Quellen-Verlust**: Von Zusammenfassungen kommt man nicht zurück zu den Originalquellen (Papers, Tools, Repos).

## Zielgruppe
Eine Person — AI-Praktiker der auf dem Laufenden bleiben will ohne den ganzen Tag Content zu konsumieren. Muttersprache Deutsch, Fokus auf englischsprachige Quellen.

## Kern-Features
1. **[AIG-1] YouTube Ingest Pipeline** — Videos per Web Clipper im Browser clippen, Python post-processed (Transkript + Zusammenfassung), RSS Feed Discovery für neue Videos
2. **[AIG-2] Wiki-Pflege durch Claude** — Neue Quellen verarbeiten, Personen-/Konzept-/Tool-Seiten erstellen und verknüpfen, Index pflegen, Widersprüche erkennen
3. **[AIG-3] Tägliches Briefing** — Zusammenfassung neuer Inhalte, Trend-Erkennung über mehrere Kanäle, Relevanz-Bewertung

## Nicht-Ziele (Out of Scope)
- Web UI / Dashboard (Obsidian ist das Interface)
- Echtzeit-Streaming / Live-Monitoring
- Mobile App
- Automatische Video-Downloads (nur Transkripte + Metadaten)

## Technische Rahmenbedingungen
- **Sprache**: Python 3.12
- **Interface**: CLI + Obsidian (kein Web UI)
- **AI**: Claude via MCP Server für Wiki-Pflege
- **Vault**: Obsidian Vault mit konfigurierbarem Pfad (MVP: `./vault/`, später Cloud-Sync). Vault NICHT in Git.
- **Dependencies**: youtube-transcript-api, yt-dlp, feedparser, markdownify, python-frontmatter
- **Obsidian Plugins**: Web Clipper, Dataview, Local REST API, YTranscript
- **Qualität**: dev-standards Submodule (Architekten-Ampel, Hooks, Skills)
- **Grundlage**: Karpathy's LLM Wiki Pattern (Sources → Wiki → Schema)
