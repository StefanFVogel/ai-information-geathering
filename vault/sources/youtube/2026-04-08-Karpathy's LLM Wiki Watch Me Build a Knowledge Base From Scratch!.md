---
author: '[[Onchain AI Garage]]'
channel_id: UCqB1bhMwGsW-yefBxYwFCCg
date: '2026-04-06'
duration: 1014
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- agent
- ai
- claudecode
- claude
- llm wiki
- karpathy
- '[ai]'
title: 'Karpathy''s LLM Wiki: Watch Me Build a Knowledge Base From Scratch!'
type: inbox
url: https://www.youtube.com/watch?v=zVEb19AwkqM
---

## Summary

*Ask Claude to summarize this transcript.*


Curious how to evolve beyond basic RAG? Andrej Karpathy's viral tweet unveiled a new paradigm for AI research: LLM-powered knowledge bases!🐦 Follow Tonbi on...

---

## Transcript

[00:00:00] So, I'm sure many of you saw this tweet
[00:00:02] from Andre Karpathy last week talking
[00:00:05] about LLM knowledge bases. It caught a
[00:00:07] lot of interest as kind of a new way to
[00:00:09] use AI as a research tool. And the core
[00:00:12] concept was to use LLMs to build
[00:00:14] personal knowledge bases for various
[00:00:15] topics of your research interest.
[00:00:18] He breaks down how he did it here. And
[00:00:21] there were a couple other follow-up
[00:00:22] tweets as well as other uh researchers
[00:00:25] and AI enthusiasts talking about the way
[00:00:28] that they've done this kind of tooling.
[00:00:30] So in today's video, we're going to
[00:00:32] build this for ourselves. First, I'm
[00:00:34] going to kind of break down what the
[00:00:35] concept is and why it's useful uh
[00:00:39] compared to other alternatives.
[00:00:41] And then we're going to actually build
[00:00:43] this out together in Claude Code. So
[00:00:44] you'll see a good example of how you
[00:00:47] would actually build this out. So wait,
[00:00:48] wait till the end for that. So let's
[00:00:51] start with the problem. Right now uh
[00:00:53] most people's experience with LLMs and
[00:00:55] documents look like rag ra retrieval
[00:00:58] automated generation. You upload some
[00:01:00] files to chat GBT or notebook LM or
[00:01:03] whatever tool and when you ask a
[00:01:05] question it retrieves some chunks and
[00:01:07] generates an answer.
[00:01:11] And that works fine for simple
[00:01:12] questions. But here's the issue. Nothing
[00:01:15] accumulates. Every time you ask a
[00:01:17] question, the LM is red rediscovering
[00:01:20] knowledge from scratch. It's reiecing
[00:01:22] together fragments every single time. So
[00:01:24] if you ask something subtle that
[00:01:26] requires synthesizing five different
[00:01:27] documents, it has to find and connect
[00:01:29] all those pieces on every query. There's
[00:01:31] no memory, no cross references, no
[00:01:33] accumulated understanding. But this LLM
[00:01:36] powered wiki pattern flips this. Instead
[00:01:39] of retrieving at query time, the LLM
[00:01:41] builds a persistent interlink wiki up
[00:01:44] front. The cross references are already
[00:01:46] there. Contradictions are already
[00:01:49] flagged. The synthesist already reflects
[00:01:51] everything you've already fed it.
[00:01:52] Knowledge compounds instead of being
[00:01:54] thrown away after each conversation.
[00:01:58] And this is the key quote from Karpathy
[00:02:01] when discussing this. The LM
[00:02:03] incrementally builds and maintains a
[00:02:04] persistent wiki structured interlin
[00:02:07] markdown files sitting between you and
[00:02:09] your raw sources. And the critical thing
[00:02:11] is you never write the wiki yourself.
[00:02:13] The LLM writes and maintains all of it.
[00:02:16] You're in charge of the important stuff,
[00:02:17] finding the good sources, exploring,
[00:02:20] asking the right questions. The LLM
[00:02:21] handles all the grunt work, the
[00:02:23] summarizing, the cross referencing, the
[00:02:24] filing, the bookkeeping, all the stuff
[00:02:26] that makes knowledge bases useful, but
[00:02:28] that no one actually wants to do.
[00:02:32] So there are many ways we can do this,
[00:02:34] but the basic architecture has three
[00:02:36] different layers uh based on what
[00:02:37] Carpathy was describing, and it's fairly
[00:02:40] clean. On the left you have raw sources.
[00:02:42] So articles, papers, images, data sets,
[00:02:44] whatever you're collecting. You know,
[00:02:45] I'm sure most of us who are in this
[00:02:47] field find interesting articles, find
[00:02:49] interesting tweets, uh interesting
[00:02:51] GitHubs, and these are your raw sources
[00:02:55] and these are immutable. The LM reads
[00:02:58] them but never touches them. They're
[00:02:59] your source of truth. In the middle
[00:03:01] here, uh is the wiki itself, directory
[00:03:04] of markdown files that the LM owns
[00:03:06] entirely, summaries, entity pages,
[00:03:08] concept pages, comparisons. The LM
[00:03:10] creates these, updates them when new
[00:03:13] sources come in and maintains all the
[00:03:15] cross references, keeps everything
[00:03:16] consistent.
[00:03:18] And on the right is the schema and this
[00:03:20] is the configuration file basically like
[00:03:22] a clawed MD. Uh, and this tells your
[00:03:25] tells the LLM how the wiki is
[00:03:26] structured, what the conventions are,
[00:03:29] what workflows to follow. So you and the
[00:03:31] LLM co-evolve this over time as you
[00:03:34] figure out what works for your domain.
[00:03:35] Think of it like this. The wiki is a
[00:03:37] codebase and then obsidian is the IDE
[00:03:41] and the LLM is the programmer and the
[00:03:43] schema is the style guide.
[00:03:50] So there are three core operations.
[00:03:52] First is to ingest. You drop a new
[00:03:54] source into a raw folder and tell the
[00:03:56] LLM to process it. It reads the source,
[00:03:58] writes a summary page, updates the index
[00:04:00] and cross-links it across all relevant
[00:04:02] existing pages. A single source might
[00:04:04] touch 10 to 15 wiki pages. The second is
[00:04:07] query. You ask questions against the
[00:04:09] wiki. The LM searches the index, reads
[00:04:12] the relevant pages, and synthesizes an
[00:04:14] answer. And here's kind of the clever
[00:04:16] part. Good answers can be filed back
[00:04:19] into the wiki as new pages. So your
[00:04:21] explorations compound in the knowledge
[00:04:22] base just like ingested sources do.
[00:04:26] And the third is lint. So this is the
[00:04:28] maintenance pass. You ask the LM to
[00:04:30] health check the wiki, find
[00:04:32] contradictions, stale claims, orphan
[00:04:34] pages with no links, missing cross
[00:04:36] references, gaps that could be filled
[00:04:37] with a web search. So the LM is good at
[00:04:40] suggesting new questions to investigate
[00:04:42] and this keeps the wiki healthy as it
[00:04:43] grows.
[00:04:46] So what happens when you ingest a
[00:04:48] source, right? Um because this is where
[00:04:51] the real power in this is. So step one,
[00:04:53] the LM reads the raw source. Step two,
[00:04:56] it extracts key information, concepts,
[00:04:58] entities, claims, data points. Step
[00:05:00] three, it writes a summary page in the
[00:05:02] wiki with metadata and tags. Step four,
[00:05:05] it updates all the existing entity and
[00:05:07] concept pages, integrating the new
[00:05:09] information into what's already known.
[00:05:11] Step five, it flags any contradictions
[00:05:14] when new data conflicts with existing
[00:05:15] claims. Step six, it updates the index,
[00:05:18] the master catalog of everything in the
[00:05:20] wiki. And step seven, it appends to the
[00:05:23] log. Uh a timestamped record of what's
[00:05:27] changed and when.
[00:05:30] And seven,
[00:05:32] uh so one source drops in and the entire
[00:05:35] wiki gets a little bit smarter. So
[00:05:37] that's the compounding effect. So here's
[00:05:40] the division of later labor. Um and it's
[00:05:43] pretty clean. The human curates
[00:05:44] questions and thinks. You pick the
[00:05:48] sources, you direct the analysis, you
[00:05:49] ask the good questions, you decide what
[00:05:51] actually matters. The LM agent uh just
[00:05:54] summarizes cross references and
[00:05:56] maintains. It writes all of the wiki
[00:05:59] pages. It keeps cross cross references
[00:06:01] up to date. It maintains summaries,
[00:06:02] flags contradictions. And here's this
[00:06:05] and here is why this works. Carpathy
[00:06:07] puts it well. Humans abandon wiks
[00:06:09] because the maintenance burden grows
[00:06:11] faster than the value, right? it becomes
[00:06:14] a huge labor just to maintain once these
[00:06:16] become a certain size. But nicely the uh
[00:06:19] LLMs don't get bored. They don't forget
[00:06:21] to update a cross reference. They can
[00:06:22] touch 15 files in a single pass. The
[00:06:25] cost of maintenance drops to near zero.
[00:06:27] So the wiki actually stays maintained
[00:06:29] properly.
[00:06:33] So this is why this approach wins and
[00:06:34] there are four principles behind it that
[00:06:37] make it really compelling. First, it's
[00:06:39] explicit. The knowledge is all visible
[00:06:40] in a navigable wiki which most of us are
[00:06:43] familiar with. You can exact you can see
[00:06:45] exactly what the AI knows and what it
[00:06:47] doesn't know. There's no hidden embing
[00:06:49] embeddings. There's no opaque memory
[00:06:51] system. Second, it's yours. You can
[00:06:53] customize it yourself. These are all
[00:06:55] local files on your computer. You're not
[00:06:57] locked into any provider's system and uh
[00:07:01] you keep everything yourself. Third,
[00:07:05] it's file over app. Everything is in
[00:07:07] universal formats marked down in images.
[00:07:09] This means it's interoperable with any
[00:07:11] tool, any CLI, any viewer. The entire
[00:07:14] Unix toolkit works with on your data.
[00:07:16] And fourth, you can bring your own a AI.
[00:07:19] You can plug in claw, GBT, codecs, open
[00:07:22] source models, whatever you want. You
[00:07:24] can even fine-tune a model on your wiki
[00:07:26] so it knows your data in its weights,
[00:07:28] not just in its context. And I think
[00:07:30] that's probably the next step.
[00:07:37] So what can you build with this? Right?
[00:07:39] This pattern applies to a lot of
[00:07:40] different domains. Research obviously
[00:07:42] going deep on the topic over weeks and
[00:07:44] months, reading papers, building up a
[00:07:45] comprehensive wiki with an evolving
[00:07:47] thesis. Personal, you can track your
[00:07:49] goals, health, self-improvement. Uh you
[00:07:52] can build a structured picture of
[00:07:53] yourself over time. Business certainly
[00:07:56] um an internal wiki fed by Slack,
[00:07:58] meetings, customer calls, always current
[00:08:01] because the LM handles maintenance.
[00:08:02] reading
[00:08:05] um filling each chapter of a book,
[00:08:08] building out character and theme pages
[00:08:10] and due diligence obviously. Uh today
[00:08:13] we're going to build one with trading
[00:08:14] strategy strategies which is part of a
[00:08:16] larger project that I've been working on
[00:08:19] and you'll probably see a video in the
[00:08:21] coming weeks uh me breaking down this
[00:08:23] project. But I've been doing a lot of
[00:08:25] research on advanced trading strategies
[00:08:28] and that's the wiki we're going to build
[00:08:29] today.
[00:08:33] So this is kind of the breakdown of what
[00:08:35] it's going to look like the directory
[00:08:37] structure and it's the same thing that
[00:08:40] we've said the raw sources the wiki
[00:08:41] itself and then the schema and workflows
[00:08:43] in the clawed file claude because I'm
[00:08:46] going to be using this in claude code
[00:08:47] with uh opus 4.6. So what the LLM will
[00:08:51] build it will be the strategy pages, the
[00:08:55] concept pages, the entity pages, cross
[00:08:58] referencing, links to everything, and
[00:09:00] then synthesis pages, comparisons,
[00:09:02] trade-offs. Uh so it's time to build it.
[00:09:07] I know you're all probably sick of sick
[00:09:08] of my slides. So now we're actually
[00:09:10] going to go in Claude Code and build
[00:09:12] this. Before we really get into it, if
[00:09:14] you enjoy this video or find it useful,
[00:09:15] please leave a like, please subscribe,
[00:09:17] or share it with your friends. It helps
[00:09:20] a lot to grow the channel. And if you're
[00:09:21] feeling generous, please leave a tip as
[00:09:23] a thanks. It helps me keep making these.
[00:09:26] And of course, leave a comment. I read
[00:09:28] and try to answer all the comments to
[00:09:30] the best of my ability. I really
[00:09:31] appreciate all the kind words everyone
[00:09:33] said, and there are always a ton of
[00:09:34] really smart, insightful comments and
[00:09:36] questions that dig deeper into the
[00:09:38] content of the video. Now, let's get
[00:09:40] back to it. I have given Claude a bunch
[00:09:44] of the tweets. Uh like I said this is
[00:09:46] the Karpathy tweet I've given
[00:09:49] some others uh some of the other users
[00:09:51] who have done really well. Farza was one
[00:09:53] of them. Euchen here as well. Euchen Jin
[00:09:57] um had this really nice uh diagram that
[00:10:00] broke it down. So I fed this to Claude
[00:10:03] along with a couple other tweets people
[00:10:05] talking about how they did this. Okay.
[00:10:08] So it's going to start out in plan mode.
[00:10:09] Obviously, um, we were talking about
[00:10:12] this concept earlier, but I said, "Okay,
[00:10:14] design the plan to build this." So, it
[00:10:16] entered plan mode. It's exploring the
[00:10:19] documents I just showed you, and then
[00:10:21] it's going to plan the architecture. So,
[00:10:24] it finished up its plan here. You can
[00:10:26] see it's building this LM wiki pattern.
[00:10:29] Um, we're going to be doing it
[00:10:30] initially. I have eight transcript
[00:10:32] files, longish videos um on trading
[00:10:35] concepts and then we can start from here
[00:10:38] and then build it out. Um it has some
[00:10:41] concepts you could see here.
[00:10:44] So it's going to create the directory
[00:10:46] structure, copy the transcript files as
[00:10:49] the raw sources. Um it's going to write
[00:10:51] the claw MD which is going to be the
[00:10:53] schema here that it's going to use. Uh
[00:10:55] we're going to be using Obsidian style
[00:10:57] wiki links for everything.
[00:11:00] create the wiki logs, seed the concept
[00:11:03] pages,
[00:11:05] you can see what uh we're working with
[00:11:06] right now, how granular it's going to
[00:11:08] get, market structure and liquidity,
[00:11:10] strategy and execution, psychology. Uh
[00:11:13] so it goes into like every general
[00:11:15] concept.
[00:11:16] Um and you can decide how granular you
[00:11:19] want to get with this.
[00:11:21] And then it's going to create the wiki
[00:11:22] index page.
[00:11:25] Ingest all the raw. Okay, so it's got
[00:11:27] everything here. Yep, it looks like a
[00:11:28] good plan.
[00:11:31] So it's going to start building for us.
[00:11:33] Okay, it's building out the directories
[00:11:35] and the transcripts were copied. Now
[00:11:36] it's writing the schema file
[00:11:42] seeding the concept pages.
[00:11:45] Okay, the scaffolding is complete. You
[00:11:47] can see the all the directories. The
[00:11:48] next step is to ingest the eight raw
[00:11:51] transcripts.
[00:11:52] Go ahead.
[00:11:56] So it's running two agents right now to
[00:11:58] ingest the raw sources, create the
[00:12:01] summaries and then update the concept
[00:12:02] pages.
[00:12:05] Okay, the initial ingest is done and now
[00:12:08] it's pretty much set up the original
[00:12:10] structure that we need. Just to
[00:12:12] visualize it, Carpathy talks about using
[00:12:14] Obsidian as well as an ID. Uh but you
[00:12:17] can download this or just ask your agent
[00:12:19] to download it. It's a very light file.
[00:12:21] Uh but this is what we get.
[00:12:25] It's probably easier to see. Uh it's
[00:12:27] basic
[00:12:29] file uh structure. You can see all the
[00:12:31] file here. This is the wiki
[00:12:33] has all of the
[00:12:37] knowledge that you were trying to b
[00:12:38] build up based on it.
[00:12:41] You could see what we do here. Identity
[00:12:44] shift protected stops. It has all the
[00:12:47] links. You can see the links to other
[00:12:49] files.
[00:12:51] So you have a link to draw on liquidity
[00:12:54] here if you want to see this. So this is
[00:12:55] just a really nice clean visualization
[00:12:57] of this and you could build out a proper
[00:12:59] front end like this. I know people have
[00:13:01] done that but for my purposes this is uh
[00:13:05] all I need just to kind of see the
[00:13:07] information.
[00:13:08] Okay. So lastly let's try asking it some
[00:13:10] questions. Right. I asked can you
[00:13:12] explain drawn liquidity to me? and it
[00:13:14] read the files based on it and gave me
[00:13:16] an answer without having to go do web
[00:13:19] searches and check everything else. Uh
[00:13:22] it goes into the core idea of draw and
[00:13:24] liquidity, types of draws, qualifying
[00:13:27] and disqualifying draws, concrete
[00:13:29] examples, how it connects to everything
[00:13:31] else.
[00:13:33] So let me ask um how do draws on
[00:13:37] liquidity
[00:13:41] actually appear?
[00:13:44] So it read as well. This is how it
[00:13:46] appears on the chart. Failure swings
[00:13:50] and unfilled fair value gaps.
[00:13:56] And then if I ask a question is there
[00:13:57] any other ways to identify them? Check
[00:13:59] outside the wiki. If I ask any question
[00:14:02] based on this wiki information that it
[00:14:03] doesn't have on hand, it can then do a
[00:14:06] web search and then it will go and
[00:14:08] automatically backfill the wiki with the
[00:14:10] new information that it found. So it
[00:14:12] found several other drawing liquidity
[00:14:14] identification methods. Uh four of them,
[00:14:17] five actually. Uh so using these
[00:14:20] resources now it's going to continue to
[00:14:22] build out the wiki again.
[00:14:25] And this is really how you develop the
[00:14:26] knowledge base. it kind of gets smarter
[00:14:29] on its own as you ask it questions and
[00:14:32] if there's information it can't find
[00:14:34] from the the wiki itself. It can do
[00:14:37] quick searches and then back fill it so
[00:14:38] that it has all the answers later on.
[00:14:40] And instead of just answering questions,
[00:14:42] you can also set it up to create
[00:14:44] markdown files, slideshows,
[00:14:46] uh which is a really useful presentation
[00:14:49] or mapplot lib images and then you can
[00:14:51] all view them in Obsidian like that. So
[00:14:54] there's a lot of ways you can customize
[00:14:56] it visually. So you can see based on the
[00:14:58] answer it's writing new concepts order
[00:15:00] blocks breaker blocks equal high lows so
[00:15:03] that once these concepts and information
[00:15:05] is inside the wiki you don't have to go
[00:15:08] and fetch it every single time you ask
[00:15:10] about this these concepts again and I'm
[00:15:13] doing this with claude with opus 4.6
[00:15:14] six. But like I said before, you can use
[00:15:16] any LLM to that does basic research and
[00:15:20] writing functions or any agent. You can
[00:15:21] use open claw to do this or Hermes
[00:15:24] agent. So as Claude says here, this is
[00:15:27] exactly how the wiki is meant to grow.
[00:15:29] You ask a question, I researched beyond
[00:15:31] the wiki and the new knowledge got filed
[00:15:34] back as permanent pages. So every future
[00:15:36] query count now reference order blocks,
[00:15:38] breaker blocks, equal high lows um along
[00:15:41] with the original stuff. So this is how
[00:15:43] you really build it up and eventually
[00:15:45] over time you'd have a really massive
[00:15:46] knowledge base to work on. And now you
[00:15:49] can see in Obsidian it has breaker
[00:15:51] blocks as a concept everything linked
[00:15:54] together very easy to understand
[00:16:00] related concepts and links to everything
[00:16:03] that you need. Right? So that was the
[00:16:06] core concept from Karpathy. He talked
[00:16:08] about this last week and you just saw us
[00:16:09] build this together. There's a lot of
[00:16:11] and the great thing is there's a lot of
[00:16:12] ways to customize this to exactly what
[00:16:14] you need
[00:16:17] and by doing that you can create a
[00:16:18] really powerful knowledge base. So I
[00:16:21] hope I hope you found this video
[00:16:23] helpful. We got to break down the
[00:16:25] concept and then you got to see me build
[00:16:27] one and what didn't take that long. You
[00:16:30] could probably do like this basic
[00:16:31] version in an hour or so and call it
[00:16:33] code and then customize it however you'd
[00:16:36] like from there. But that's going to be
[00:16:37] it for today's video.
[00:16:39] Please leave a like, subscribe, leave a
[00:16:42] comment. Let me know how you're building
[00:16:43] your own knowledge bases or if you have
[00:16:46] any hints to do it better than I did
[00:16:47] here. We have a lot of great videos
[00:16:49] lined up for this week, so please look
[00:16:50] forward to that. Thank you for watching.