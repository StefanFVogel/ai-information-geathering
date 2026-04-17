---
category: concepts
last_updated: '2026-04-17'
related_sources:
- 2026-04-16-Claude Opus 4.7 Just Dropped... Or Did It Really.md
title: Adaptive Thinking
type: wiki
---

# Adaptive Thinking

Mechanismus, bei dem das Modell selbst entscheidet, wieviel Reasoning-Budget es pro Turn investiert — inklusive der Option, gar nicht zu denken (0 Reasoning-Tokens).

## Einführung und Fallout

Eingeführt in [[Opus 4.6]] am 9. Februar 2026 ohne prominente User-Kommunikation. Unmittelbare Folgen laut einer AMD-Analyse über ~7.000 [[Claude Code]]-Sessions:

- Thinking-Depth fiel um 73% (2.200 → 600 Zeichen im Schnitt)
- File-Reads-Before-Edit fielen von 94% auf ~66%
- User-Interrupts stiegen um Faktor 12
- Halluzinierte Git-Hashes, fabrizierte Package-Namen, "simplest" 3x häufiger im Output
- [[Boris Cherny]] (Creator of Claude Code) bestätigte: Zero-Reasoning-Turns produzierten Halluzinationen, Deep-Reasoning-Turns waren korrekt

## Kombinierte Drosselung

Zur gleichen Zeit wurde der Effort-Default für Pro- und Max-User still auf "medium" gedrosselt — erst am 15. April (über einen Monat später) noch immer so. Die Kombination aus Adaptive Thinking + niedrigem Effort-Default erklärt den wahrgenommenen Qualitäts-Kollaps.

## In Opus 4.7

Adaptive Thinking ist in [[Opus 4.7]] weiterhin Standard, aber zusätzlich steht das [[X-High Effort]]-Level zur Verfügung, und laut Anthropic soll das Modell logische Fehler in der Planning-Phase selbst erkennen.

## Sources

- [[2026-04-16-Claude Opus 4.7 Just Dropped... Or Did It Really.md]]
