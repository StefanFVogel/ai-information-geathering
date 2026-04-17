---
category: concepts
last_updated: '2026-04-17'
related_sources:
- 2026-04-17-I Gave OpenClaw $10,000 to Trade Stocks.md
- 2026-04-17-I Turned Claude Opus 4.7 Into a 247 Trader.md
title: AI Trading
type: wiki
---

# AI Trading

Autonome Trading-Agenten, die Research, Entscheidung und Order-Placement ohne direkten Menscheneingriff vollziehen. Typisch: LLM-gesteuert (z.B. [[Opus 4.6]], [[Opus 4.7]]), zeitgesteuerter Loop (Cron oder [[Claude Code Routines]]), API-Brokerage wie [[Alpaca]].

## Beobachtete Muster

**30-Tage-Challenge ([[Nate Herk]] vs. [[Samin Yasar]], April 2026):**
Beide Bots schlugen den S&P in einem Monat mit -8,46% Markt-Performance. Bots mit sehr unterschiedlichen Strategien (Nate: freie Wealth-Advisor-Agents, Samin: Pareto/VC-Risk + [[Capitol Trades]]-Copy-Trading) outperformten gleichermaßen — das wirft die Frage auf, ob der Markt schlechter ist als die Strategien gut sind.

**Empirische Erkenntnisse aus den Bots:**
- 10% Trailing-Stops statt 2% (vermeidet verfrühtes Ausstoppen)
- Short-dated Options sind Bot-Killer — einzelne Trades kosten mehrere hundert Dollar
- All-in auf thematische Sektoren (z.B. Energy) performte besser als Streuung
- Bots können selbst Strategie-Anpassungen erkennen ("scalping bei -2%", "take profit bei +5%")
- Alpaca blockt Trades über Account-Level-Frequenz — Bot muss Strategie anpassen

## Verwandte Strategien

- [[Wheel Strategy]] — Option-basiertes "Nie-richtig-verkaufen"
- [[Copy Trading]] — Signale von erfolgreichen Tradern nachahmen
- [[Trailing Stop Strategy]] — dynamische Stop-Losses
- [[Algorithmic Trading]] — regelbasiertes Trading allgemein
- [[Options Trading]]

## Technologie-Stack

**Klassisch ([[OpenClaw]]-basiert):**
Agent-Framework + [[Opus 4.6]] + [[Alpaca]] + Telegram

**Modern ([[Claude Code Routines]]-basiert):**
Reine [[Claude Code]]-Lösung + [[Opus 4.7]] + [[Alpaca]] + [[Perplexity]] + [[ClickUp]]

## Sources

- [[2026-04-17-I Gave OpenClaw $10,000 to Trade Stocks.md]]
- [[2026-04-17-I Turned Claude Opus 4.7 Into a 247 Trader.md]]
