---
category: concepts
last_updated: '2026-04-17'
related_sources:
- 2026-04-17-I Turned Claude Opus 4.7 Into a 247 Trader.md
title: Claude Code Routines
type: wiki
---

# Claude Code Routines

Scheduler-Feature in [[Claude Code]], mit dem [[Claude Code]]-Sessions auf Cron-Basis automatisch laufen. Macht echte 24/7-Agenten möglich, ohne externen Orchestrator.

## Anwendungsmuster

[[Nate Herk]] nutzt Routines für einen 24/7-Trading-Agent mit vier Cron-Slots:

1. **Pre-Market** — Übersicht holen, Overnight-News scannen
2. **Market Open** — erste Trades
3. **Midday** — Rebalancing basierend auf Intraday-Entwicklung
4. **Close** — End-of-Day-Journaling + Summary an [[ClickUp]]

## Kombination mit Opus 4.7

Besonders effektiv mit [[Opus 4.7]], dessen "judgment over ambiguity" und "self-verifying outputs" für autonome Mehrstufen-Workflows ausgelegt sind.

## Abgrenzung

- Kein externes Framework wie [[OpenClaw]] oder Hermes nötig
- Läuft rein in Claude Code mit Skills + Cron
- Modular: Tools (Broker, Research, Notifications) sind austauschbar

## Sources

- [[2026-04-17-I Turned Claude Opus 4.7 Into a 247 Trader.md]]
