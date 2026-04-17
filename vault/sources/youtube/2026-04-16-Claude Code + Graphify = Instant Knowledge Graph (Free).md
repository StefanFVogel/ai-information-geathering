---
author: '[[FuturMinds]]'
channel_id: UCzsmpPhpoweC6itJd_oAt3w
date: '2026-04-15'
duration: 634
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- claude code tutorial
- '[ai]'
- FuturMinds
- claude graphify
- graphify claude code
- claude code agents
- how to install graphify
- how to use claude code
- claude code setup
- claude code graphify
- graphify
title: Claude Code + Graphify = Instant Knowledge Graph (Free)
type: inbox
url: https://www.youtube.com/watch?v=BkHps04qGgc
---

## Summary

[[FuturMinds]] stellt [[Graphify]] vor — ein Tool, das einen [[Knowledge Graph]] über den Codebase baut, damit [[Claude Code]] nicht in jeder neuen Session dieselben Dateien neu liest. Das Tool erschien 48 Stunden nach [[Andrej Karpathy]]s Beschreibung der Idee und hat inzwischen ~25.000 GitHub-Stars.

**Drei-Pass-Pipeline:**
1. **Code-Struktur** — lokaler Parser (Python, TypeScript, Go, Rust) extrahiert Klassen, Funktionen, Imports, Calls. Keine API-Kosten.
2. **Audio/Video** — [[Faster-Whisper]] transkribiert lokal (kostenlos).
3. **Rest** (Markdown, PDFs, Images) — Claude-Sub-Agents extrahieren Konzepte und Beziehungen. Einziger Teil mit API-Kosten, läuft nur einmal.

Ein Hook liest vor jeder Claude-Session den Graph-Report automatisch. **Real-World-Einsparung:** 7-8% Token-Reduktion (nicht die beworbenen 71,5x — der Benchmark vergleicht gegen "alle 52 Files ins Context-Fenster laden", was niemand tatsächlich tut). Qualitative Antworten werden jedoch deutlich besser. Funktioniert auch für Research-Vaults, Meeting-Recordings, gemischte Content-Ordner — dort ist der Nutzen am größten.

**Setup:** `pip install graphifyy` → `graphify install` → `graphify claude install` (installiert Hook). Update via `graphify update` oder Git-Hooks (`graphify hook install`).

**Kernaussage:** Wenn Claude in Deinen Sessions wiederholt dieselben Dateien liest, lohnt sich Graphify. Besonders wertvoll bei langen Sessions, großen Projekten und Mixed-Content-Repositories.


Claude Code + Graphify = Instant Knowledge Graph
https://github.com/safishamsi/graphify

For business enquiries: ai@futurminds.com

🔗 My Resources:

Use the below link and coupon code 'FUTURMINDS ' t

---

## Transcript

[00:00:00] Let's say you're working on a project in Claude Code. You have
[00:00:03] just opened a new session and you want to understand the codebase before building
[00:00:07] something new. So you ask a question. What does browser-use
[00:00:11] do? Give me a one-line summary of each major component. It's a very simple
[00:00:15] question. And now watch what happens. Before it answers
[00:00:18] a single word, it reads the project readme to figure out what kind of project
[00:00:22] this even is. It goes through multiple files. It builds a mental model from
[00:00:26] scratch. Reading through your codebase file by file, and every one of those
[00:00:30] reads costs money. And the answer you get is only as good as what Claude
[00:00:35] managed to find in those reads. Now, here's the issue. If you close
[00:00:38] that session and open a new one tomorrow, Claude starts from zero
[00:00:42] again. No memory of what it read, no map of how the files are connected.
[00:00:46] Every session, it rebuilds the same understanding from scratch. It burns
[00:00:50] the same tokens, makes the same searches, re-reads the same files
[00:00:54] every time. There's a tool that fixes this. It's called Graphify.
[00:00:58] It reads your project once, builds a knowledge graph of how everything connects,
[00:01:02] and Claude reads that graph at the start of every session.
[00:01:06] Instead of re-reading your files. Let me show you how it works — and then I'll
[00:01:10] show you the actual numbers from running ten questions in two identical sessions.
[00:01:14] Here's the simplest way to understand what just happened. So you can think of
[00:01:18] a Claude session as a new hire that shows up on their first day.
[00:01:21] They have never seen the project, and they have to read through everything before
[00:01:25] answering a single question. And every new session means a new hire.
[00:01:29] Graphify builds the senior colleague — someone who already has the
[00:01:33] map, who already knows where the decision logic lives,
[00:01:36] which components talk to each other, and which five components are the hub that
[00:01:40] everything routes through. You build that map once, and Claude reads it at
[00:01:44] the start of every session automatically. And that's the whole idea.
[00:01:47] And it's not just for code. It also works for research papers,
[00:01:51] meeting recordings, strategy documents, or any kind of mixed content.
[00:01:55] I'll come back to that, but first let me show you exactly how it works
[00:01:59] under the hood. This tool shipped 48 hours after Andrej Karpathy, co-founder
[00:02:04] of OpenAI, described exactly what it should do. Currently, it has almost
[00:02:08] 25,000 stars. There are three passes, and that's the
[00:02:12] whole system. First pass analyzes the code structure. If your folder
[00:02:16] has Python, TypeScript, Go, Rust, or anything with real syntax,
[00:02:20] Graphify runs a code parser across every file. It reads
[00:02:24] every class, every function, every import, every call.
[00:02:27] This runs entirely on your machine. No external API calls
[00:02:31] are made, no tokens are used. It extracts hard facts — this
[00:02:35] function calls that one, this class imports this module. Facts, not guesses.
[00:02:39] Second pass analyzes the audio and video.
[00:02:43] If you've got meeting recordings, tutorials, or YouTube URLs,
[00:02:47] Graphify transcribes them locally using Faster-Whisper, which is
[00:02:51] also free. Third pass: it scans everything else — markdown,
[00:02:55] PDFs, images, readme files,
[00:02:58] docs, et cetera. Claude sub-agents run in parallel,
[00:03:02] extract concepts and relationships and figure out what things mean and
[00:03:06] how they connect with each other. Pass three is the only part that touches Claude's
[00:03:10] API and it only runs once. After that, every session reads the
[00:03:14] cached graph for free. Everything merges into one graph.
[00:03:17] An algorithm groups related concepts into neighborhoods.
[00:03:21] You can think of them as departments. Every time you open a new conversation
[00:03:25] or session, before Claude reads a single file, that hook fires
[00:03:29] and Claude reads a summary of the entire graph. Then it makes two or three
[00:03:33] targeted reads instead of fifteen. And that's where the savings come from.
[00:03:37] Now, does this actually save tokens? I ran ten questions
[00:03:41] in two identical sessions to find out. Same project, same ten questions,
[00:03:45] asked in the same order. The session on the left is not using
[00:03:49] Graphify, the one on the right is using Graphify. Let me run
[00:03:53] all ten questions.
[00:03:59] Now, if we check the context usage in both of these
[00:04:03] sessions, the session without Graphify is using 120,000
[00:04:07] tokens and the one using Graphify is using 113,000
[00:04:11] tokens. So it's not a big difference, probably less than 8%.
[00:04:16] However, if you look at the questions and their replies,
[00:04:19] I think the quality of responses in the session using Graphify is
[00:04:23] better than the one which is not. So if you look at this question,
[00:04:26] both of these found that there are three phases. But on the left
[00:04:30] it simply mentions these three functions as phases.
[00:04:34] But on the right it has explained phase one in detail,
[00:04:38] and similarly phase two and phase three it
[00:04:43] has also added details about loop detection and replanning, et cetera.
[00:04:46] If we look at Graphify's GitHub repository, you will see these
[00:04:50] worked examples where they're claiming that they achieved 71.5x
[00:04:54] reduction. So why did our sessions look more like 7 to 8%
[00:04:58] reduction? I'll explain exactly what that benchmark actually measures
[00:05:02] and when the big savings are. But first, let's see how to set it up.
[00:05:06] You can scroll down to the install section, then copy this command,
[00:05:10] go to your project, open a terminal, paste and run.
[00:05:14] If you are on Windows you will see this error. It's because double ampersand
[00:05:18] is not recognized. So you can simply run each of these commands separately.
[00:05:23] First, let's run pip install graphifyy — double y. It's complete.
[00:05:26] Now let's run graphify install. And
[00:05:31] this is now ready. By the way, if you are using other platforms like
[00:05:34] Codex, Opencode, et cetera — you can copy the corresponding command from here
[00:05:38] and replace the graphify install with it. Once that is done,
[00:05:42] we want our Claude Code to use Graphify in every session without
[00:05:45] us asking to do it. And to set it up we need to run this
[00:05:49] command: graphify claude install. And
[00:05:54] it is done. Now we can start a new Claude session and run Graphify.
[00:05:59] So this is a new session. Now let's run slash graphify.
[00:06:02] Alright, so it has found a corpus of
[00:06:06] 357 code files, 53 docs and seven images.
[00:06:11] There is a threshold of 200 files in one go, so it's
[00:06:15] asking us to select subdirectories for which we want to create the graph.
[00:06:18] Let's select browser-use and examples.
[00:06:24] Okay, so it took around 12 minutes to complete and here's
[00:06:28] what we get. There's a new directory called graphify-out.
[00:06:32] It contains GRAPH_REPORT.md. It has identified
[00:06:35] 4,041 nodes, 20,900 edges
[00:06:39] and 185 communities. We also get this graph
[00:06:43] dot HTML and if you open it in a browser, this is what you're going to see.
[00:06:46] On the right hand side we have the list of communities that it has identified
[00:06:50] and by default all of these are selected. So you can deselect any
[00:06:54] of these by clicking on that community. Each dot in this graph is a
[00:06:59] concept, a class, a function, a documented idea — and each line
[00:07:03] is a relationship between two dots or two concepts. The colors
[00:07:07] are neighborhoods, and the bigger the dot, the more things connect to
[00:07:11] it. Now, building this entire graph was really cheap and we just
[00:07:15] need to build it once and then Claude has access to this entire graph.
[00:07:18] It can easily understand how things are connected so that it can selectively
[00:07:22] read those relevant docs instead of blindly going through a large number
[00:07:26] of docs. Now, when you're working on your project, you're of course making changes,
[00:07:30] adding new files, making code changes, et cetera. And you want to keep that
[00:07:34] graph in sync. To do that there are a couple of options. One is
[00:07:38] you can simply run graphify update. And
[00:07:42] it will automatically identify what changed from the previous run and update your graph.
[00:07:46] Or you can run graphify hook install, and this will wire
[00:07:51] up git hooks. The graph rebuilds automatically if there is a new
[00:07:55] commit or when you switch your branch, and it has been set up successfully.
[00:07:59] Now here's what this actually means for your day to day. Every
[00:08:03] time you open a new Claude session on any project where you have run Graphify,
[00:08:07] that graph report gets read first automatically.
[00:08:10] You don't type anything special, you don't run a command — you just
[00:08:14] ask a question and Claude already has the map. The seventy-one times claim.
[00:08:18] Here's what it actually measures. The benchmark took a 52-file corpus —
[00:08:22] three repos, five papers and four images. The naive approach: loading
[00:08:27] all 52 files directly into Claude's context at once — that costs around
[00:08:31] 123,000 tokens. Whereas Graphify's
[00:08:35] approach is to first read that graph file and only go through
[00:08:39] the relevant neighborhoods in the graph, and it consumed only 1,700
[00:08:43] tokens per query. And that ratio is 71.5 times.
[00:08:47] But here's the thing: nobody works by pasting 52 files into a Claude
[00:08:52] conversation. In real Claude Code sessions, you will probably tag
[00:08:56] your folder and start asking questions. You will never tag a large number of
[00:09:00] files because you wouldn't know where to look. So that 71
[00:09:04] times benchmark is comparing against a workflow most people don't actually use.
[00:09:08] So this number doesn't really make sense. Your savings will be considerable if
[00:09:12] you're working on mixed projects that contain code plus docs,
[00:09:16] or if you are working on long sessions, or if you have large
[00:09:20] projects. If your project has more files, Claude would otherwise search through more files,
[00:09:24] but with the graph it can reduce that search. So what
[00:09:28] Graphify actually gives you in Claude Code is fewer wrong-direction file reads,
[00:09:32] better answers from the first message, and savings that
[00:09:36] grow with session length. This isn't only for code projects.
[00:09:40] I ran Graphify on a folder of YouTube scripts, transcripts and research notes.
[00:09:44] There was no Python or JavaScript, just Markdown and text files.
[00:09:48] And I asked questions like what topics I have covered most and
[00:09:52] what's missing in my content on this subject, et cetera. And it answered using the graph,
[00:09:56] not by reading every file. And it's the same idea for research folders.
[00:10:00] You can point it to a stack of PDFs or papers and
[00:10:04] Claude can start making connections across all of them. You can have just one connected
[00:10:08] map for all of your meeting recordings, strategy docs and client files.
[00:10:12] And the short version is: if Claude keeps reading the same things over
[00:10:16] and over in your sessions, Graphify is worth running. So if you're
[00:10:20] using this for a research vault or business planning folder, it's definitely worth it.
[00:10:24] I hope you found the video useful, and I would love to know your thoughts
[00:10:28] and experience on this. Don't forget to like the video and subscribe to the channel
[00:10:32] and I'll see you in the next one.