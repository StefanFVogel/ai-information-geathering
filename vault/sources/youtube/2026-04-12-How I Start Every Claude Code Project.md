---
author: '[[AI LABS]]'
channel_id: UCelfWQr9sXVMTvBzviPGlFw
date: '2026-04-10'
duration: 792
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- claude code
- how to set up claude code
- how to setup claude code
- '[ai]'
- vscode claude code
- claude code coder
- claude code vscode
- claude code setup
- claude code setup guide
- claude code cloud
- claude code tips
title: How I Start Every Claude Code Project
type: inbox
url: https://www.youtube.com/watch?v=ywIhw15za9Y&t=614s
---

## Summary

**Kernaussage:** Bevor man mit Claude Code baut, muss man die Agent-Umgebung korrekt einrichten — PRD, claude.md, Skills, Agents, MCPs, Tests und Issue-Tracking sind essentiell für produktive Ergebnisse.

**Inhalt:**
- **Planung zuerst:** Eigenen Planner-Agent statt Claude's Planning Mode nutzen, der produktfokussiert statt technisch plant und ein PRD erstellt
- **claude.md richtig schreiben:** Nur Dinge reinschreiben, die der Agent nicht selbst herausfinden kann; Best Practices, Coding Conventions, Schreibstil — keine Projektstruktur
- **Skills vs. Agents:** Skills für wiederholbare Workflows mit Guidelines/Referenzen; Agents für Tasks die eigenes Context Window brauchen
- **Path-specific Rules:** Dedizierte Regeln für bestimmte Bereiche der App, verlinkt in claude.md
- **Negative Constraints:** Explizit definieren was der Agent NICHT tun soll — positive Specs lassen Lücken
- **Progress & Learnings Files:** Agent trackt Fortschritt und Fehler in dedizierten Dateien während des Builds
- **Tests vor Implementation:** Tests aus PRD ableiten (nicht aus Implementation), um Spec-Abweichungen zu erkennen
- **Issue Tracking:** GitHub für technische User, Notion/Trello via MCP für nicht-technische Teammitglieder
- **Load Testing:** Stress-Tests mit erwarteter Nutzerzahl planen (z.B. mit [[K6]])

**Erwähnte Tools/Konzepte:**
- [[Claude Code]] — Agent-Umgebung und Skills/Agents
- [[Supabase]] — Backend via MCP
- [[shadcn UI]] — UI-Komponenten
- [[Playwright]] — Browser-Testing
- [[K6]] — Load Testing
- [[GitHub]] — Issue Tracking und Versionierung
- [[Notion]] / [[Trello]] — Projekt-Management via MCP
- [[Git Worktree]] — Isolierte experimentelle Branches

**Erwähnte Personen:**
- Keine spezifischen Personen erwähnt

**Bewertung:** Sehr guter Überblick über eine strukturierte Claude Code Projekteinrichtung. Besonders wertvoll sind die Punkte zu negativen Constraints, Test-First aus PRD, und die Unterscheidung Skills vs. Agents. Richtet sich an Entwickler, die über das Hobby-Level hinaus mit Claude Code arbeiten wollen.


The complete claude code setup that you need before writing a single prompt. Most people jump straight into building, but the real difference between apps that work and apps that break comes down to h

---

## Transcript

[00:00:00] The truth is that AI will never
[00:00:01] revolutionize the software building
[00:00:03] process, at least not in the way that
[00:00:05] you think. It sure makes everything
[00:00:07] faster, and it also makes it easier to
[00:00:09] recover when things go wrong. But the
[00:00:10] processes that have been set over 60
[00:00:12] years of product building are still as
[00:00:14] important today, just for different
[00:00:16] reasons. Before they were implemented to
[00:00:18] make sure that humans had a structured
[00:00:20] way to develop these products, but now
[00:00:21] that has shifted to enabling AI agents
[00:00:24] to work the way humans did. So in order
[00:00:26] to make AI agents work properly, you
[00:00:28] need to set up their environment the
[00:00:30] right way so that they actually follow
[00:00:31] the process. And we are going to go
[00:00:33] through all of the steps you need to
[00:00:35] take before you even start building.
[00:00:36] Planning your requirements properly is
[00:00:38] the most important thing you do before
[00:00:40] writing a single prompt. This is the
[00:00:41] part where no matter how good models
[00:00:43] get, you would need to spend time. Now
[00:00:45] there are multiple ways of planning. You
[00:00:47] can plan your app using claude code in
[00:00:48] planning mode, but its planning is very
[00:00:50] technical focused, not product focused.
[00:00:52] As we mentioned in the previous video
[00:00:54] that with the way agents are
[00:00:55] progressing, the planning mode doesn't
[00:00:57] need to be as detailed or technical and
[00:00:59] should instead focus heavily on the
[00:01:00] product aspect because the new models
[00:01:02] are powerful and planning has to be
[00:01:04] different than as it used to be with the
[00:01:05] early models being not much capable. So
[00:01:07] instead of Claude's planning mode, you
[00:01:09] can create another agent to help plan
[00:01:11] out your app. It contains the
[00:01:12] instructions for helping build a proper
[00:01:14] PRD with a template as well to guide
[00:01:16] Claude on what exactly the requirements
[00:01:18] are. Once you have set up the agent, you
[00:01:20] can give Claude a prompt to use it and
[00:01:22] plan out the app you want to build. It
[00:01:23] actually loads the planner agent and
[00:01:25] keeps asking questions until it
[00:01:27] understands all of the requirements. It
[00:01:29] keeps on asking questions until you're
[00:01:30] satisfied with the planning. Now, to
[00:01:32] understand the MVP, the agent is
[00:01:34] designed to ask many questions and at
[00:01:36] the end it will ask you if there is
[00:01:38] anything else that you need in your app.
[00:01:40] If you do, you can add the things that
[00:01:41] you want the agent to implement. If you
[00:01:43] are satisfied with all of the questions
[00:01:45] and think that the agent has understood
[00:01:47] the plan, you can just tell it that's
[00:01:48] it. After the questioning and answering
[00:01:50] session, it creates a PRD document and
[00:01:52] saves it to the project folder. This
[00:01:54] document contains details on all the
[00:01:56] requirements you discussed. The
[00:01:58] implementation is divided into phases
[00:02:00] and it contains all the key design
[00:02:01] decisions and everything that is needed
[00:02:03] for the app. Now that you have refined
[00:02:05] what app you want to build, the next
[00:02:07] step is to properly define a claude.md
[00:02:10] file. This file is important because it
[00:02:12] contains all of the instructions that
[00:02:13] you want your agent to follow. You link
[00:02:15] the PRD document so that it can access
[00:02:17] all of the app requirements directly
[00:02:19] from there and you don't have to repeat
[00:02:21] anything here. This file should contain
[00:02:23] only the things that the agent does not
[00:02:24] know instead of mentioning the things
[00:02:26] that it already knows. It references the
[00:02:28] rules that you want the project to
[00:02:30] follow. You can add in your project
[00:02:32] conventions and all of the instructions
[00:02:34] that you want Claude to specifically
[00:02:35] follow while implementing the app. The
[00:02:37] ideal approach is that you do not create
[00:02:39] the claude.md file from the init command
[00:02:42] and instead create it on your own
[00:02:43] because this command just generates the
[00:02:45] file based on what the existing codebase
[00:02:47] is like, not what it actually needs to
[00:02:49] know. But this file is not a write once
[00:02:51] file that you set and forget. You have
[00:02:53] to keep adding things to it so that it
[00:02:55] can incrementally improve the process of
[00:02:57] building apps while you work. Now, as we
[00:02:59] talked about in our previous video, this
[00:03:00] file is loaded once and stays in the
[00:03:02] context forever, acting as a guideline
[00:03:04] while it's working. So make sure that
[00:03:06] this file does not contain things that
[00:03:08] are actually not needed or are specific
[00:03:10] to one area of implementation. The
[00:03:12] things that you need to add to this file
[00:03:14] are the best practices your project will
[00:03:16] follow your coding conventions, your
[00:03:18] writing style and conventions and other
[00:03:20] similar things but not the things that
[00:03:21] it can figure out on its own like how
[00:03:23] the project is structured. For that it
[00:03:25] can read the file structure and
[00:03:27] understand it by itself. So take your
[00:03:28] time when you're writing this file and
[00:03:30] ensure that it is properly tailored to
[00:03:32] your needs and your project before
[00:03:34] actually implementing the app. The next
[00:03:36] thing you set up is your skills, agents,
[00:03:38] and any MCP you want to use in your
[00:03:40] project all prior to actually building
[00:03:42] it. MCPs are easier to connect. You can
[00:03:44] just connect whichever external service
[00:03:46] you want the agent to access and have
[00:03:48] them installed by running their
[00:03:50] installation commands. For example, we
[00:03:51] wanted our backend built on Superbase.
[00:03:53] So we connected the Superbase MCP to our
[00:03:56] agent in the project. If you are using
[00:03:57] shad CN UI for UI components and
[00:04:00] playright for browser testing, you need
[00:04:02] to have them all connected prior to
[00:04:04] building the app so that agents can
[00:04:06] access these tools while building. But
[00:04:07] those were just for connecting to
[00:04:09] external services and you also need to
[00:04:11] configure agents. You can configure as
[00:04:13] many agents as needed. You already have
[00:04:15] a dedicated planner agent for planning.
[00:04:17] You can also create a commit agent which
[00:04:19] is responsible for committing, running
[00:04:21] pre-checks, and following conventional
[00:04:22] commit messages. You can have a
[00:04:24] refactoring agent that refactors the
[00:04:26] code and improves performance overall.
[00:04:28] And you can have a verification agent
[00:04:30] that uses the tools of the playright MCP
[00:04:32] so that it can verify if the UI and user
[00:04:35] flow are working as intended and it
[00:04:37] contains all the instructions on how to
[00:04:38] do that. Now, aside from the agents, you
[00:04:40] also need to configure skills. You can
[00:04:42] create as many skills as you need and
[00:04:44] you can easily create them using the
[00:04:46] skill creator which is available on the
[00:04:47] open-source GitHub repo. You can add as
[00:04:50] many references as you want and also
[00:04:51] include scripts so that it can run the
[00:04:53] script directly and use its output. For
[00:04:55] the distinction between when to use
[00:04:57] agents and when to use skills, implement
[00:04:59] all those workflows that are repeatable
[00:05:01] and need guidance and references as
[00:05:03] skills. For example, you can create a
[00:05:05] front-end skill because it's a
[00:05:07] repeatable workflow and needs to follow
[00:05:08] dedicated guidelines consistently
[00:05:10] throughout the app. Implement agents for
[00:05:12] tasks that need a dedicated context
[00:05:14] window. You can also use the front-end
[00:05:16] skill that's open source and is actively
[00:05:18] used by the Claude codes creator
[00:05:19] himself. You also need to add path
[00:05:21] specific rules for particular aspects of
[00:05:23] your app. These rules define the path to
[00:05:25] which they apply and include all the
[00:05:26] instructions needed for implementing
[00:05:28] that specific part. You can configure as
[00:05:30] many of these as you like and also link
[00:05:32] them in your cloud.md so that the agent
[00:05:34] knows it has to follow these
[00:05:36] instructions. As we mentioned earlier,
[00:05:37] claude.md is for broad principles. So
[00:05:40] that's why you have path specific rules
[00:05:42] tailored to specific parts so the agent
[00:05:44] knows what it needs to do for specific
[00:05:46] implementation. We cover all of these
[00:05:47] setups and more on building products
[00:05:49] with AI on this channel. So if you want
[00:05:51] to see more of this, subscribe and keep
[00:05:53] an eye out for future videos. But even
[00:05:55] with all of these positive instructions,
[00:05:57] there is still a gap. Agents are biased
[00:05:59] toward action and may implement things
[00:06:00] beyond what your positive constraints
[00:06:02] specify. Therefore, you need to
[00:06:04] explicitly tell the agent what it should
[00:06:05] not do. You can create this file in your
[00:06:07] docs folder and link it in claude.md so
[00:06:10] the agent knows these constraints exist.
[00:06:12] It should contain all instructions
[00:06:14] tailored to the project specifying each
[00:06:16] and everything you don't want the agent
[00:06:18] to create. Negative constraints are
[00:06:20] important because positive specs leave
[00:06:22] an implied gap and negative constraints
[00:06:24] close that gap removing ambiguity and
[00:06:26] preventing the agent from experimenting
[00:06:28] where it shouldn't. They give a clearer
[00:06:30] goal for what the output shouldn't look
[00:06:31] like. For example, if you don't want the
[00:06:33] AI to follow the default purple or blue
[00:06:35] and white combination it usually uses,
[00:06:37] explicitly state that you don't want
[00:06:39] that instead of just implying it. But
[00:06:41] before we move forwards, let's have a
[00:06:43] word by our sponsor, Weigh-In Video. If
[00:06:45] you work with long videos, you know the
[00:06:46] struggle. Hours of scrubbing through
[00:06:48] footage just to find one good moment,
[00:06:50] then even more time editing it down.
[00:06:52] Weighin Video fixes all of that. It's an
[00:06:54] AI video platform that actually
[00:06:55] understands your video. Their AI
[00:06:57] clipping skill on OpenClaw takes any
[00:06:59] long video, finds the most viral
[00:07:01] moments, auto refframes them to
[00:07:02] vertical, and adds captions. No coding,
[00:07:04] no setup. Just run the skill and your
[00:07:06] clips are ready to post. Just like that.
[00:07:08] If you want something specific, you can
[00:07:10] search inside any video using plain
[00:07:11] English. Just type funny reaction or
[00:07:14] best quote, and it jumps right to it. It
[00:07:16] also handles video summaries and
[00:07:18] transcriptions with speaker labels.
[00:07:19] Perfect for podcasts, lectures, and
[00:07:21] streams. Whether you're repurposing
[00:07:23] content or automating your workflow,
[00:07:25] weigh-in video saves you hours every
[00:07:27] single week. Stop wasting time on manual
[00:07:29] editing. Click the link in the pinned
[00:07:31] comment to get started. Now, this is one
[00:07:33] thing that most AI frameworks use in one
[00:07:35] form or another, which is using multiple
[00:07:37] documents for different purposes. But
[00:07:39] the core behind all of those documents
[00:07:41] is the progress and learning document.
[00:07:42] The progress file is critical because
[00:07:44] when you are working on a large-scale
[00:07:46] app with multiple features, the agent
[00:07:48] loses track of which features it has
[00:07:50] already implemented and which it has yet
[00:07:52] to work on. Without this file, the agent
[00:07:54] has to go back, read the implementation,
[00:07:56] and compare it against the docs to
[00:07:57] figure out what's been done. That
[00:07:59] creates overhead and wastes both time
[00:08:01] and tokens. So, create a progress file
[00:08:03] where the agent can just look at one
[00:08:05] place and know exactly where things
[00:08:06] stand. But tracking progress alone is
[00:08:08] not enough because the agent also needs
[00:08:10] to know what went wrong. Therefore, you
[00:08:12] also need a learnings file where the
[00:08:14] agent records its errors, what caused
[00:08:16] them, and how it fixed them. This way,
[00:08:17] when it encounters a similar situation
[00:08:19] later, it doesn't make the same mistake
[00:08:21] twice. Now, since both of these files
[00:08:23] are meant to be actively updated while
[00:08:25] the agent is implementing the app, you
[00:08:27] need to explicitly instruct the agent in
[00:08:29] the claw.md so that it keeps adding to
[00:08:31] these files, improving its knowledge
[00:08:33] base during the build. Now, these two
[00:08:35] files are the most essential ones that
[00:08:37] every setup needs. You can use these
[00:08:38] when you're building the coding setup
[00:08:40] for your own. We have also previously
[00:08:42] made a video that talks about how you
[00:08:44] can build the frameworks on your own
[00:08:45] which you can watch on the channel. But
[00:08:47] if you don't want to go through the
[00:08:48] hassle of setting up your own, you can
[00:08:50] just rely on the coding frameworks
[00:08:52] because they use different mechanisms
[00:08:53] for doing exactly that which you can
[00:08:55] implement directly. Another common
[00:08:57] mistake is implementing tests only at
[00:08:59] the end of development. This is
[00:09:01] problematic because if you ask an agent
[00:09:03] to write and implement tests after the
[00:09:05] features are built, the tests won't be
[00:09:06] as effective as they would be if written
[00:09:08] beforehand. When writing tests, you
[00:09:10] should have the agent refer to the PRD
[00:09:12] you created and based on that deduce how
[00:09:15] the functionality should work. The agent
[00:09:16] should then write tests from these
[00:09:18] deduced requirements. Essentially
[00:09:20] reverse engineering the functionality
[00:09:22] and things where the app might go wrong
[00:09:23] from the PRD. Once the tests are ready,
[00:09:25] you can run them at the end to
[00:09:27] crossverify if the implementation meets
[00:09:29] the requirements. The reason for writing
[00:09:30] tests first is that if you implement
[00:09:32] them afterward, the agent only knows
[00:09:34] what was actually implemented. It will
[00:09:36] optimize tests for the features as they
[00:09:38] exist, not for the functionality as
[00:09:40] required in the specifications. This can
[00:09:42] cause you to miss testing features that
[00:09:43] were specified but not implemented
[00:09:45] correctly. Because the agent optimizes
[00:09:47] toward the implemented approach, it may
[00:09:49] slack on thorough testing, missing edge
[00:09:51] cases that could have been caught if the
[00:09:53] tests were derived directly from the
[00:09:55] specs. You shouldn't give the agent
[00:09:56] open-ended instructions like test the
[00:09:58] application because this way Claude just
[00:10:00] optimizes for the implementation.
[00:10:02] Instead, implement proper tests guided
[00:10:04] by the specs so the agent knows exactly
[00:10:06] what to optimize for. Also, if you are
[00:10:08] enjoying our content, consider pressing
[00:10:09] the hype button because it helps us
[00:10:11] create more content like this and reach
[00:10:13] out to more people. Another problem many
[00:10:15] people encounter during app development
[00:10:17] is the lack of upfront issue tracking.
[00:10:19] Without it, issues pile up with no
[00:10:21] record of what caused them or when they
[00:10:23] started. And as the app scales up, it
[00:10:25] gets harder to track. Therefore,
[00:10:27] maintaining proper logs during testing
[00:10:29] is crucial. Many people use GitHub for
[00:10:31] this and GitHub is an excellent platform
[00:10:33] for tracking and managing issues.
[00:10:34] Combining it with well ststructured Git
[00:10:36] commit messages provides guidance to
[00:10:38] Claude on what was done in each commit
[00:10:40] and allows it to track its progress. One
[00:10:42] of the best features of Git is that if a
[00:10:44] change breaks the codebase, you can
[00:10:46] revert commits. And if you want to test
[00:10:48] something experimental, you can use the
[00:10:50] work tree to do it in isolation. You can
[00:10:52] configure your setup so that the agent
[00:10:54] commits after every implementation using
[00:10:56] detailed messages to maintain clarity.
[00:10:58] But GitHub works well for technical
[00:11:00] users and non-technical team members may
[00:11:02] struggle to submit issues. Therefore,
[00:11:04] for them, connecting the agent to a
[00:11:06] project management tool like Trello or
[00:11:07] Notion is ideal. This allows logging
[00:11:09] issues, tracking progress, and
[00:11:11] collaborating on fixes. You should
[00:11:13] connect the MCP of the respective tool
[00:11:15] so the agent can access it, track
[00:11:16] issues, move them across boards, and
[00:11:18] manage reporting efficiently. You also
[00:11:20] need to add an instruction in claude.md
[00:11:22] specifying that the agent should use the
[00:11:24] notion MCP for tracking bugs and issues
[00:11:27] properly. Setting this up at the start
[00:11:29] is invaluable as the project scales and
[00:11:31] multiple people start developing
[00:11:33] together, ensuring that everything can
[00:11:35] be logged and tracked efficiently. But
[00:11:37] even if your app works perfectly in
[00:11:38] testing, AI generated code is not
[00:11:40] inherently built to handle multiple
[00:11:42] users simultaneously. This is why many
[00:11:44] people find AI implementations
[00:11:46] underperforming in production.
[00:11:47] Therefore, you need to prepare for that
[00:11:49] as well. If you have an estimate, you
[00:11:50] can tell your agent the expected number
[00:11:52] of users and that multiple users will be
[00:11:54] using the app at the same time. The
[00:11:56] agent should then write the test cases
[00:11:58] for stress testing the load based on
[00:12:00] this information. There are multiple
[00:12:01] testing tools you can use and you can
[00:12:03] choose whichever matches your
[00:12:04] requirements. We used K6 for a next.js
[00:12:07] app because it's easy to implement and
[00:12:09] matched our requirements. You can also
[00:12:11] use Claude's plan mode here to map out
[00:12:13] multiple approaches for the app because
[00:12:15] here we need a detailed technical plan.
[00:12:17] Claude plans based on the PRD and the
[00:12:19] approximate number of users you expect
[00:12:21] to be using it simultaneously. Claude
[00:12:23] asks multiple questions from different
[00:12:25] perspectives and clarifies potential
[00:12:27] issues that could arise in production.
[00:12:29] This helps the app fail gracefully even
[00:12:31] if problems occur and ensures the user
[00:12:33] experience is optimized. Using this
[00:12:35] mode, you can clarify your intent and
[00:12:37] have the agents plan for scalability as
[00:12:39] well. This plan becomes the final piece
[00:12:41] in taking your app from an idea to
[00:12:42] production ready. Now, all these agents
[00:12:44] and skills mentioned here are available
[00:12:46] in AIAS Pro for this video and for all
[00:12:49] our previous videos from where you can
[00:12:51] download and use it for your own
[00:12:52] projects. If you found value in what we
[00:12:54] do and want to support the channel, this
[00:12:56] is the best way to do it. The links in
[00:12:58] the description. That brings us to the
[00:13:00] end of this video. If you'd like to
[00:13:01] support the channel and help us keep
[00:13:03] making videos like this, you can do so
[00:13:05] by using the super thanks button below.
[00:13:07] As always, thank you for watching and
[00:13:09] I'll see you in the next one.