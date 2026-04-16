---
author: '[[AICodeKing]]'
channel_id: UC0m81bQuthaQZmFbXEY9QSw
date: '2026-04-12'
duration: 481
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- karpathy skills repo
- agent instructions
- andrej karpathy skills
- claude code
- claude code plugin
- '[ai]'
- github repo for ai coding
- andrej karpathy
- ai coding agents
- claude md
- ai coding workflow
title: 'Karpathy-Skill + Claude Code,OpenCode: This SIMPLE ONE-FILE SKILL Makes YOUR
  AI CODER WAY BETTER!'
type: inbox
url: https://www.youtube.com/watch?v=PzhTLHQfdRE&t=7s
---

## Summary

**Kernaussage:** Das Andrej Karpathy Skills Repo ist kein Feature-Bundle, sondern eine leichtgewichtige Instruktions-Schicht, die AI Coding Agents disziplinierter und zuverlässiger macht — basierend auf vier Kernprinzipien.

**Inhalt:**
- Vorstellung des GitHub-Repos "Andrej Karpathy Skills" — eine einzelne claude.md Datei als Plugin
- Typische Probleme von AI Coding Agents: zu schnelle Annahmen, Over-Engineering, unkontrollierte Edits, falsche Zuversicht
- **Vier Kernprinzipien:**
  1. **Think before coding** — Ambiguitäten aufdecken, Rückfragen stellen statt raten
  2. **Simplicity first** — minimaler Code, keine spekulativen Abstraktionen
  3. **Surgical changes** — nur das Nötige ändern, kein zufälliges Refactoring
  4. **Goal-driven execution** — verifizierbare Erfolgskriterien statt "trust me"
- Installation: Als Claude Code Plugin oder direkt als claude.md in ein Projekt
- Erkennungszeichen dass es wirkt: bessere Rückfragen, kleinere Diffs, kein ungewolltes Refactoring
- Prinzipien sind portabel — funktionieren in jedem Tool das Regeln/Instructions unterstützt

**Erwähnte Tools/Konzepte:**
- [[Andrej Karpathy Skills]] — GitHub-Repo mit Agent-Verhaltensprinzipien
- [[Claude Code]] — Ziel-Plattform für das Plugin
- [[Verdant]] — Alternatives AI Coding Tool

**Erwähnte Personen:**
- [[Andrej Karpathy]] — Namensgeber, Prinzipien basieren auf seinen Beobachtungen

**Bewertung:** Gutes Erklärvideo für Einsteiger, die verstehen wollen warum Agent-Disziplin wichtiger ist als Agent-Features. Die vier Prinzipien sind universell anwendbar und decken sich mit Best Practices für jedes AI-gestützte Coding-Setup.


In this video, I'll be talking about Andrej Karpathy Skills, a lightweight GitHub repo that helps AI coding agents behave more like careful engineers by improving how they think, simplify tasks, limit

---

## Transcript

[00:00:02] [music]
[00:00:05] >> Hi. Welcome to another video.
[00:00:07] So, today I want to talk about a GitHub
[00:00:10] repo that looks extremely simple on the
[00:00:13] surface.
[00:00:14] But I think it is actually one of the
[00:00:15] more useful things you can add to your
[00:00:17] AI coding workflow right now.
[00:00:19] It is called Andrej Karpathy skills.
[00:00:22] Now, despite the name, this is not
[00:00:24] really about some giant bundle of flashy
[00:00:26] skills or crazy automation.
[00:00:29] The main idea is actually much simpler
[00:00:30] than that.
[00:00:32] It is basically a lightweight
[00:00:33] instruction layer derived from Andrej
[00:00:35] Karpathy's observations about how coding
[00:00:37] agents usually fail.
[00:00:39] And if you have used AI coding tools for
[00:00:41] any real work, you already know exactly
[00:00:43] what he means.
[00:00:44] These agents often make assumptions too
[00:00:45] quickly. They over-engineer simple
[00:00:47] tasks. They edit files they were never
[00:00:49] asked to touch. They sound confident
[00:00:51] even when they are confused. And
[00:00:53] sometimes they will happily create 500
[00:00:55] lines of architecture when 50 lines
[00:00:57] would have solved the problem. So, let's
[00:00:59] get right into it. What this repo tries
[00:01:01] to do is fix that behavior at the
[00:01:03] instruction level. According to the
[00:01:05] readme, the whole thing is centered
[00:01:07] around four principles. The first one is
[00:01:08] think before coding. This basically
[00:01:10] means the agent should not silently
[00:01:12] guess what you meant. If something is
[00:01:14] ambiguous, it should surface the
[00:01:15] ambiguity, ask the right clarifying
[00:01:17] question, or at least show the
[00:01:19] trade-offs instead of just charging
[00:01:20] ahead. The second one is simplicity
[00:01:23] first. This is one of my favorite parts
[00:01:25] because a lot of AI coding tools still
[00:01:27] have this weird urge to overbuild
[00:01:29] everything. This repo pushes the agent
[00:01:31] to write the minimum code needed to
[00:01:33] solve the problem. No speculative
[00:01:35] abstractions, no giant framework for a
[00:01:37] one function task, no trying to be
[00:01:38] clever for no reason. The third
[00:01:40] principle is surgical changes, and
[00:01:42] this one is super important. The agent
[00:01:44] should only touch what is necessary for
[00:01:46] the task. It should not randomly clean
[00:01:48] up unrelated code, rewrite comments,
[00:01:50] refactor adjacent functions, or improve
[00:01:52] stuff that was not part of the request.
[00:01:55] And then the fourth principle is
[00:01:56] goal-driven execution. This is basically
[00:01:59] about turning vague requests into
[00:02:01] verifiable outcomes. So, instead of just
[00:02:02] saying fix the bug and hoping for the
[00:02:04] best, the agent should think in terms of
[00:02:06] success criteria.
[00:02:08] Reproduce the bug, make the fix, verify
[00:02:10] that it works, and then stop. So, this
[00:02:12] is kind of great because what you're
[00:02:14] really installing here is not a feature.
[00:02:16] You're installing discipline. That is
[00:02:18] why I think this repo matters. It is not
[00:02:20] trying to make the model sound smarter.
[00:02:22] It is trying to make the workflow more
[00:02:23] reliable. And to be honest, that is what
[00:02:26] most people actually need.
[00:02:28] Now, let me explain what this thing
[00:02:29] actually is in practice. The repo is
[00:02:31] basically centered around a single
[00:02:33] Claude.md file, plus a plugin install
[00:02:36] path for Claude code. So, this is not
[00:02:39] some giant complicated setup. It is
[00:02:41] intentionally lightweight.
[00:02:43] You can use it in two main ways. The
[00:02:45] first way is the Claude code plugin
[00:02:47] path, which is the recommended option in
[00:02:49] the repo. The readme says you first add
[00:02:52] the marketplace with plugin marketplace
[00:02:54] add forest chang andrej karpathy skills,
[00:02:57] and then install it with plugin install
[00:02:59] andrej karpathy skills at karpathy
[00:03:01] skills. That makes it available as a
[00:03:03] Claude code plugin. So, the guidelines
[00:03:05] can be used across your projects. The
[00:03:07] second way is the simpler per project
[00:03:10] route. If you want it only inside one
[00:03:12] repo, you can just download the
[00:03:14] Claude.md file directly into your
[00:03:16] project. For new project, the readme
[00:03:19] shows this. And if you already have a
[00:03:21] Claude.md,
[00:03:22] you can append it instead of replacing
[00:03:24] your existing project instructions. So,
[00:03:27] the setup itself is actually very easy.
[00:03:30] But now the more important question is,
[00:03:32] how do you use it?
[00:03:34] And this is the part that I think people
[00:03:35] misunderstand.
[00:03:37] You do not really use this like some
[00:03:39] separate feature where you type a fancy
[00:03:41] {slash} command every time.
[00:03:43] You install it once, and then it changes
[00:03:45] how your agent behaves during normal
[00:03:47] work. So, for example, let us say I ask
[00:03:50] my coding agent to add a billing
[00:03:51] dashboard.
[00:03:53] Without these kinds of guidelines, a lot
[00:03:55] of agents will just start coding
[00:03:56] immediately. They create tables, API
[00:03:58] routes, webhooks, UI components,
[00:04:01] validation, maybe even some settings
[00:04:03] pages, all in one go.
[00:04:05] And then you have to inspect a giant
[00:04:06] diff and figure out what on earth it
[00:04:08] just did. With these Karpathy-inspired
[00:04:10] guidelines in place, the ideal behavior
[00:04:12] is very different. The agent should
[00:04:14] first clarify the scope. Are we talking
[00:04:17] one-time payments or subscriptions? What
[00:04:19] provider are we using? Do we need a full
[00:04:21] dashboard or just a read-only billing
[00:04:23] summary? What is the minimal version
[00:04:25] needed right now?
[00:04:26] Then it should keep the solution simple.
[00:04:28] Then it should make only the necessary
[00:04:30] edits. Then it should verify the result
[00:04:32] with a concrete check, a test, or some
[00:04:35] kind of success criteria.
[00:04:37] That is the real usage pattern. You are
[00:04:39] basically giving the agent a better
[00:04:41] default operating system for engineering
[00:04:43] work. Now, there's also a nice practical
[00:04:45] way to know if it is actually working.
[00:04:47] If you install this and your agent
[00:04:49] starts asking better clarification
[00:04:50] questions before writing code, that is a
[00:04:52] good sign. If your diffs get smaller and
[00:04:55] more focused, that is a good sign. If it
[00:04:58] stops randomly refactoring neighboring
[00:04:59] files that had nothing to do with the
[00:05:01] task, that is a very good sign. And if
[00:05:04] it starts thinking in terms of
[00:05:05] verification instead of just I
[00:05:07] implemented it, trust me, that is also
[00:05:09] exactly what you want. So,
[00:05:12] this is not really about adding power in
[00:05:14] the usual sense. It is about removing
[00:05:16] failure modes.
[00:05:18] And that is why I like it. Now, briefly,
[00:05:20] I want to mention how I think about this
[00:05:22] with Verdant because I do use Verdant,
[00:05:24] and that is why I would configure it
[00:05:26] there, too.
[00:05:27] I would not frame it as installing it
[00:05:29] exactly the same way inside Verdant. I
[00:05:32] would frame it more as porting the
[00:05:33] philosophy.
[00:05:35] Since Verdant already lets you define
[00:05:36] project context, rules, and agent
[00:05:39] behavior, I would just take these same
[00:05:41] four principles and place them into my
[00:05:43] Verdant instruction setup, so the agents
[00:05:45] follow the same discipline there, as
[00:05:47] well.
[00:05:48] So, the point is not really Verdant
[00:05:50] itself. The point is that these
[00:05:52] guidelines are portable. If your tool
[00:05:54] gives you a place for rules, agent
[00:05:56] memory, or system level instructions,
[00:05:58] you can usually carry the same ideas
[00:06:00] over.
[00:06:01] And that is one of the biggest strengths
[00:06:03] of this repo. It is not tied to some
[00:06:05] magical proprietary feature. It is a
[00:06:08] reusable way of making AI coding agents
[00:06:10] behave more like careful engineers.
[00:06:13] Now, one more thing I want to say here
[00:06:15] is that this repo is valuable even if
[00:06:17] you never install it exactly as is
[00:06:20] because the four principles are just
[00:06:22] solid advice for prompting coding agents
[00:06:24] in general. Think before coding. Keep it
[00:06:26] simple. Change only what is necessary.
[00:06:29] And define success clearly.
[00:06:32] If you start prompting your agents with
[00:06:33] that mindset, you will already get
[00:06:35] better results. But if you actually
[00:06:37] install the repo and bake those
[00:06:38] principles into the tool itself, then
[00:06:40] you do not have to remember to restate
[00:06:42] them every single time. The discipline
[00:06:44] is already there by default, which is
[00:06:46] pretty good, for sure. So, my overall
[00:06:48] take is this.
[00:06:49] Andrej Karpathy skills is not a hype
[00:06:51] repo. It is not trying to wow you with
[00:06:54] some giant dashboard or some fancy
[00:06:56] benchmark claim. It is solving a very
[00:06:58] real problem, which is that coding
[00:07:00] agents are often capable but badly
[00:07:02] behaved. This gives them a better
[00:07:05] behavioral framework. It helps reduce
[00:07:07] wrong assumptions. It helps reduce
[00:07:09] over-engineering. It helps reduce messy
[00:07:12] diffs. And it pushes the agent toward
[00:07:14] verifiable goal-driven execution. That
[00:07:17] is useful in Claude code. That is useful
[00:07:19] in any tool where you can inject rules.
[00:07:21] And in my case, because I use Verdant,
[00:07:23] too, I would absolutely carry the same
[00:07:25] principles over there as part of my
[00:07:27] configuration. So, yes, I think this is
[00:07:29] worth trying. Overall, it's pretty cool.
[00:07:32] Anyway, let me know your thoughts in the
[00:07:33] comments. If you like this video,
[00:07:35] consider donating through the super
[00:07:36] thanks option or becoming a member
[00:07:38] [music] by clicking the join button.
[00:07:40] Also, give this video a thumbs up and
[00:07:42] subscribe to my channel. I'll see you in
[00:07:43] the next one. Until then, bye.
[00:07:56] >> [music]