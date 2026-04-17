---
category: tools
last_updated: '2026-04-17'
related_sources:
- 2026-04-17-I Gave OpenClaw $10,000 to Trade Stocks.md
title: OpenClaw
type: wiki
---

# OpenClaw

Agent-Framework mit Claude-Backend, das für autonomes Trading verwendet wird. [[Nate Herk]] und [[Samin Yasar]] setzten damit ihre 30-Tage-Trading-Challenge um — jeweils 10.000 USD Echtgeld, Steuerung via [[Opus 4.6]], Brokerage [[Alpaca]], Benachrichtigungen via Telegram.

## Architektur

- **Cron-Scheduler** — trading-times alle 30 Minuten
- **Sub-Agents** — z.B. "team of wealth advisors" für Research
- **Memory** — Journaling aus vorherigen Trades
- **Inter-Agent-Messaging** — Bots mailten einander täglich (Trash-Talk, Prompt-Injection-Versuche)

## Ergebnisse der Challenge

| Agent | Strategie | End-Value | vs. S&P (-8,46%) |
|---|---|---|---|
| Bull ([[Nate Herk]]) | Wealth-Advisor-Team, freie Hand | $9.980 | +8% |
| Salmon ([[Samin Yasar]]) | Pareto/VC-Risk, [[Capitol Trades]] | $9.624 | +4,7% |

## Entwicklung

Im Folge-Video stellt [[Nate Herk]] auf eine reine [[Claude Code]]-Lösung mit [[Claude Code Routines]] + [[Opus 4.7]] um — ohne OpenClaw-Framework.

## Sources

- [[2026-04-17-I Gave OpenClaw $10,000 to Trade Stocks.md]]
