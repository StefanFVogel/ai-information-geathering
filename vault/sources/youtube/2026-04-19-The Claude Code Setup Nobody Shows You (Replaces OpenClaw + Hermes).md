---
author: '[[Simon Scrapes]]'
channel_id: UCdCR4-uYOg5ju-IUuDnfnQA
date: '2026-04-18'
duration: 1186
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- '[ai]'
title: The Claude Code Setup Nobody Shows You (Replaces OpenClaw + Hermes)
type: inbox
url: https://www.youtube.com/watch?v=c2kJ7j3CgUs
---

## Summary

*Ask Claude to summarize this transcript.*


🚀 Build agentic systems that run your business: https://skool.com/scrapes
Don't miss the next build - https://www.youtube.com/@simonscrapes?sub_confirmation=1

Agentic frameworks like Hermes and Open

---

## Transcript

[00:00:00] So take a look at this for a second.
[00:00:01] Install a skill, set a schedule for an
[00:00:03] automated job, and then get the result
[00:00:06] delivered to you on your phone. That's
[00:00:08] it. That is the pitch for Hermes and the
[00:00:09] pitch for Open Claw pretty much, too.
[00:00:11] And honestly, when I first saw this, I
[00:00:13] was completely sold. Because in reality,
[00:00:15] this is exactly what every business
[00:00:16] owner wants. The work's going to get
[00:00:18] done in the background. You're going to
[00:00:19] get the good result. There's no
[00:00:21] babysitting. There's no back and forth.
[00:00:22] But then you actually go to try it, and
[00:00:24] the setup's super messy and technical.
[00:00:26] And if you want the best models, you're
[00:00:27] going to pay extra because it's not
[00:00:29] available on Claw subscription. So in
[00:00:31] reality, it looks simple, but it's
[00:00:32] actually not. And I know a lot of you
[00:00:34] are in this exact same spot because I've
[00:00:36] seen your comments on my YouTube videos.
[00:00:38] Some of you are testing Hermes, trying
[00:00:40] Open Claw, or even thinking about
[00:00:41] building your own. And I was there, too.
[00:00:43] And while I was going through it, I
[00:00:45] ended up actually just building my own
[00:00:46] version. One that runs on Claw
[00:00:48] subscription, so it doesn't cost me a
[00:00:49] fortune. Because every single thing in
[00:00:51] this diagram, you can already do inside
[00:00:53] Claw code. [music] And for a business
[00:00:55] owner, the Claw code version is actually
[00:00:57] better because you can see exactly
[00:00:58] what's going on inside the black box. So
[00:01:01] in this video, I'm going to break down
[00:01:02] the five features that actually make a
[00:01:04] system like this and share what I
[00:01:06] learned along the way. So if you're
[00:01:07] thinking about using Hermes, Open Claw,
[00:01:09] or even just building your own, you'll
[00:01:11] know exactly what to focus on to get
[00:01:13] started. So when I ran Hermes and Open
[00:01:15] Claw side by side with my own setup, I
[00:01:17] noticed that they all have different
[00:01:19] wrappers, different UIs, different
[00:01:21] channels you can contact them from. But
[00:01:22] underneath, it's actually just the same
[00:01:24] five features driving everything. So the
[00:01:26] first is persistent memory. So think
[00:01:28] about memory that actually learns about
[00:01:30] you as you work with it. Then you've got
[00:01:32] skills that create themselves, first of
[00:01:34] all, and then get better over time. The
[00:01:36] third is how you actually interact with
[00:01:38] it, which is way bigger than just a chat
[00:01:40] interface on your phone, by the way.
[00:01:42] Then we've got scheduled tasks that
[00:01:43] actually run themselves, so not being at
[00:01:45] the computer window and still getting
[00:01:47] things done. And then finally, this is
[00:01:49] the big one, business context. How to
[00:01:51] inject the right context at the right
[00:01:53] time to make all your results
[00:01:55] contextualized to your business and
[00:01:57] produce therefore better outputs. So get
[00:01:59] all of these five inside Claw code, and
[00:02:02] you don't need a separate framework like
[00:02:04] Open Claw or Hermes, and you can even
[00:02:06] run it on Claw's most powerful models
[00:02:08] like Opus 4.7 released just days ago
[00:02:10] without paying for the API credits. So
[00:02:12] you can use it on your Pro and Max
[00:02:14] subscription. So let me first start with
[00:02:15] the one that most people get wrong. And
[00:02:17] that's persistent memory. It's probably
[00:02:19] the biggest selling point of Hermes and
[00:02:21] Open Claw. So unlike temporary chat
[00:02:23] wrappers, they're supposed to maintain
[00:02:25] long-term searchable memory of past
[00:02:28] conversations and projects. And this is
[00:02:30] what gets us hooked initially because
[00:02:32] the idea that my agent will actually
[00:02:33] remember what we worked on yesterday,
[00:02:35] last week, and therefore contextualize
[00:02:37] and be better for the results going
[00:02:39] forward sounds amazing. And if you've
[00:02:40] worked with Claw code for more than just
[00:02:42] a few sessions, you'll know just how
[00:02:44] important context management actually is
[00:02:46] for getting high-quality outputs. But
[00:02:49] Claw code actually already has all the
[00:02:50] ingredients for this. We just need to
[00:02:52] set them up properly. So I've distilled
[00:02:54] this into just four memory layers that
[00:02:56] you can use. The first is claw.md or
[00:02:59] agents.md if you want to actually use
[00:03:01] this with different models. So think of
[00:03:03] this just as your agent's operating
[00:03:04] instructions, who it is, how it behaves,
[00:03:07] what rules it follows, and it's going to
[00:03:09] load into every single session. Most of
[00:03:11] you will have this layer already. Now
[00:03:12] layer two is brand context. So this is
[00:03:16] where your business context is actually
[00:03:17] going to live. Think your brand voice,
[00:03:20] how you speak, ICP, your positioning,
[00:03:23] all your client details will live in
[00:03:24] this brand context shared folder, and
[00:03:26] therefore every skill inside the
[00:03:28] repository can pull from the same
[00:03:30] folder. So when Claw writes a LinkedIn
[00:03:31] post for you, when it's doing client
[00:03:33] research, when it's building out your
[00:03:34] landing page, it's going to pull from
[00:03:36] the exact same business brain. And as
[00:03:38] you can imagine, it gets much better
[00:03:40] outputs that are hyper-focused on your
[00:03:42] business. Now layer three builds on top
[00:03:44] of that, and this is what makes agents
[00:03:46] like Open Claw and Hermes and those
[00:03:48] frameworks feel so personal. So this is
[00:03:50] the agent context folder. So we have
[00:03:52] things like the soul.md and the user.md
[00:03:54] which describe how it should act and
[00:03:56] feel and the actions that you as a user
[00:03:58] using it commonly do, so it feels like
[00:04:00] it understands you. And finally, layer
[00:04:02] four, we have project memory. So each
[00:04:04] project you run actually keeps a history
[00:04:06] of exactly what's happened, as well as a
[00:04:08] plan that you can refer to. So when you
[00:04:10] actually come back to a content
[00:04:11] repurposing project that you did three
[00:04:12] weeks later, Claw is going to know
[00:04:14] exactly what you built, what worked,
[00:04:17] what didn't work, and where we need to
[00:04:18] pick up on that. Now from this
[00:04:20] four-layer framework, here's the first
[00:04:21] key learning that I wanted to share with
[00:04:23] you. It doesn't matter how you set this
[00:04:25] up. You can put your project briefs
[00:04:27] anywhere, use whatever planning
[00:04:29] frameworks you like to write the plans.
[00:04:31] So for example, we use GSD or the Get
[00:04:33]  Done frameworks for more complex
[00:04:35] projects, for example. But the core
[00:04:36] ingredients are that you actually you're
[00:04:39] just loading in the right context at the
[00:04:41] right time, so you're not bloating
[00:04:43] context and experiencing context rot
[00:04:45] where the outputs are getting worse the
[00:04:46] more context you feed in. So your
[00:04:48] claw.md shouldn't be 2,000 lines long.
[00:04:50] It shouldn't even be 1,000 lines long.
[00:04:52] It should actually just reference the
[00:04:54] most important process steps that are
[00:04:56] going to get loaded in at the start of
[00:04:57] the conversation. So any additional
[00:04:59] context that needs to be pulled in at a
[00:05:00] specific point needs to be stored in a
[00:05:03] separate reference file. So now I keep
[00:05:05] my agents.md, if you want to work across
[00:05:08] models, or your claw.md, succinct and to
[00:05:11] the point, and then just point it to
[00:05:13] reference files. So see here where I've
[00:05:14] separated my brand context and tell it
[00:05:16] to load it in only when it needs it.
[00:05:18] That way, Claw can actually load and
[00:05:20] offload into separate agents and
[00:05:22] maintain high-quality outputs because
[00:05:24] we're not bloating the context. And we
[00:05:26] use exactly the same approach with every
[00:05:28] single skill. Short entry skill.md file,
[00:05:31] detailed references which are only
[00:05:33] loaded and offloaded when needed. So the
[00:05:35] first feature then is a memory layer.
[00:05:37] This is just about organizing context in
[00:05:39] a way that actually suits your business
[00:05:40] and your needs. So you just need to
[00:05:42] structure it properly, segment your
[00:05:43] context, point it to reference files,
[00:05:46] and not overload those context files.
[00:05:47] And by the way, there are a bunch of
[00:05:48] different memory and context storage
[00:05:50] solutions that you can choose from. So
[00:05:51] you've got Obsidian, you've got the Open
[00:05:53] Claw style setup which we're showing
[00:05:55] here. We've got Carpathy's LLM Wiki, and
[00:05:58] even people are building custom-built
[00:05:59] frameworks for memory management. So
[00:06:01] there's a whole host of ones with
[00:06:02] different benefits depending on your use
[00:06:03] cases. So if you do actually want a
[00:06:05] comparison of these different memory
[00:06:06] models and when you use which, then drop
[00:06:08] a comment below and I'll do a full
[00:06:10] comparison about which one works for
[00:06:11] which use cases to help you get this
[00:06:13] memory system set up for your business.
[00:06:15] But anyway, that's memory. So let's look
[00:06:18] at what actually uses that memory to get
[00:06:19] the work done, which is skills. So
[00:06:21] Hermes has two features that often get
[00:06:23] bundled together in all the demos. The
[00:06:25] first is a persistent learning loop. So
[00:06:27] think of skills that actually improve
[00:06:29] themselves over time. So an agent does a
[00:06:31] task, evaluates its performance, and
[00:06:33] then it's going to refine that skill
[00:06:35] over time. And the second is automatic
[00:06:37] skill creation. So you can generate a
[00:06:39] new skill, and then apparently share
[00:06:41] them via agentskills.io. And this is
[00:06:43] genuinely some seriously important
[00:06:45] features. Knowing now what I know about
[00:06:47] how important skills are for actual
[00:06:49] output quality. So skills are basically
[00:06:51] importing expertise to improve our
[00:06:54] output quality by giving it a really
[00:06:56] refined process document for a specific
[00:06:58] task. So you might have LinkedIn post
[00:07:00] creation skills. You might have
[00:07:01] copywriting skills. You might have lead
[00:07:03] generation research skills. All of those
[00:07:05] will be ported in skills. But again, if
[00:07:07] we reflect on the Claw code ecosystem,
[00:07:10] you can actually just build it in
[00:07:11] yourself to that system. And the benefit
[00:07:13] of doing that is you know exactly how it
[00:07:15] works, too, and you can refine and
[00:07:17] iterate on it over time. So if we tackle
[00:07:19] creating skills first, Claw code has the
[00:07:21] skill creator skill, which you might
[00:07:23] have seen before. It's built by
[00:07:24] Anthropic themselves, and basically you
[00:07:25] give it a description of what skill you
[00:07:27] want, or you point it to a GitHub repo
[00:07:29] with an existing skill, or describe a
[00:07:31] process from scratch on how you do it,
[00:07:33] and it's going to build out the entire
[00:07:34] thing, the name, the description, and
[00:07:36] that determines the success rate of
[00:07:37] whether it's called or not. And then
[00:07:39] obviously the step-by-step process
[00:07:40] document of the actual skill.md file
[00:07:42] itself. And if we reflect back on how we
[00:07:44] manage context, what we want to do is
[00:07:46] keep a refined skill.md file less than
[00:07:49] 200 lines and then strip out everything
[00:07:51] that's unnecessary. So we've actually
[00:07:52] adapted the Anthropic skill creator
[00:07:54] skill to do exactly that. Strip out the
[00:07:56] surplus information and keep that
[00:07:58] separate and only load it into context
[00:08:00] exactly when you need it. Now on top of
[00:08:02] creating skills, every skill you build
[00:08:04] should have a self-learning
[00:08:11] for additional context, and you can go
[00:08:13] one step further with a learnings.md
[00:08:15] file or just a rules segment actually
[00:08:18] inside your skill.md, which are
[00:08:19] basically non-negotiable rules that each
[00:08:21] time you use that skill or each time
[00:08:23] Claw is going to use that skill, it will
[00:08:25] get better at abiding by those specific
[00:08:27] rules that we've added in. So as part of
[00:08:29] the skill process, as one of the steps
[00:08:31] in the skill.md, you get it to ask you
[00:08:33] for feedback. So it effectively takes
[00:08:35] the feedback then that you give it,
[00:08:37] applies any rules inside your
[00:08:39] learnings.md or inside that skill file,
[00:08:41] and then always sticks to buy those
[00:08:42] rules when you use that skill again and
[00:08:44] again. So it's effectively a
[00:08:45] self-learning loop where the skills get
[00:08:47] better over time. So inside Claw code,
[00:08:49] you can replace that functionality by
[00:08:51] actually just using the skill creator
[00:08:52] skill, and then you make them get better
[00:08:54] by applying rules inside a learnings.md
[00:08:57] or just rules inside the skill document
[00:08:59] itself if it's asking you for feedback
[00:09:01] every time. So so far we've got memory
[00:09:03] and we've got skills that create
[00:09:05] themselves and get smarter over time.
[00:09:06] The next big question is, how do you
[00:09:08] actually interact with this system
[00:09:10] day-to-day? So it's no secret that every
[00:09:12] agentic framework in 2026 so far has
[00:09:15] been competing on interfaces. So Open
[00:09:18] Claw gave you Telegram, Discord, Slack,
[00:09:21] WhatsApp. Hermes is similar, and Claw
[00:09:23] code has been bringing out features
[00:09:24] left, right, and center to try and
[00:09:26] replicate this to give people access to
[00:09:28] message their agents from phone. So you
[00:09:31] can kick off a task while you're out,
[00:09:33] check the output whilst you're on the
[00:09:34] move. And that's all great, but here's
[00:09:36] the thing that nobody is actually
[00:09:37] talking about. The interface question,
[00:09:39] in my opinion, isn't just, can I chat
[00:09:42] from an agent from my phone? The real
[00:09:43] question now that agents are so good is,
[00:09:45] how do we manage multiple conversations
[00:09:47] and multiple goals at the same time? The
[00:09:49] models are now so, so good that it's
[00:09:51] pushing us into a different role. We're
[00:09:53] now jumping into a supervisor role, and
[00:09:55] we need a better way to actually be able
[00:09:56] to manage multiple agents and multiple
[00:09:58] projects on the go, too. And all of the
[00:10:00] frameworks I've seen give you one
[00:10:02] conversation at a time. So, you're going
[00:10:04] to open Telegram, you chat to one agent,
[00:10:06] you get one output back, which is great
[00:10:08] for a single task, but what happens when
[00:10:10] you've got six business goals all
[00:10:12] running in parallel? What happens when
[00:10:13] you want to set up a zero employee
[00:10:15] company and you run multiple departments
[00:10:17] through different agents? Like flicking
[00:10:19] between those chat threads and trying to
[00:10:21] remember which one was which, which one
[00:10:23] was writing your news letter, which one
[00:10:25] filled its context window is actually
[00:10:27] pretty difficult. So, let me show you
[00:10:28] how you can get Claude code to handle
[00:10:30] this and how I did it myself. So, first,
[00:10:32] for quick asks, you've got the Claude
[00:10:34] code inbuilt channels feature. So, this
[00:10:36] is Anthropic's official feature that's
[00:10:38] going to work with Telegram, iMessage,
[00:10:40] and Discord out of the box. So, you
[00:10:41] don't need to do anything to actually
[00:10:43] access your conversation at your phone
[00:10:45] already. So, exactly what Hermes
[00:10:46] promises, but shipped natively by
[00:10:48] Anthropic now. And here's where it gets
[00:10:50] really interesting. If you're running a
[00:10:51] real business on Claude code, managing
[00:10:53] multiple conversations, then you need to
[00:10:55] actually abstract that and build a UI
[00:10:58] layer on top. So, I did exactly that and
[00:11:00] I call it the command center. And the
[00:11:01] idea is really simple. So, instead of
[00:11:03] managing terminals or chat threads, you
[00:11:06] just manage your business goals. So, you
[00:11:07] drop in a business outcome, Claude is
[00:11:09] going to spin up an instance to handle
[00:11:11] it, and it's going to show up on your
[00:11:12] Kanban style board where you've got full
[00:11:13] visibility of all your goals running in
[00:11:15] parallel. You're able to click into one
[00:11:17] and see the full conversation, and you
[00:11:19] can have sub chats inside those
[00:11:21] conversations, too. And you can even
[00:11:22] have the plan on the right-hand side
[00:11:25] next to the chat window. So, you could
[00:11:27] have four agents working on different
[00:11:28] features here, and then the plan on the
[00:11:30] right-hand side, which is going to auto
[00:11:32] update as you run through the plan. So,
[00:11:34] this is set out for larger, more complex
[00:11:36] projects. You still have the granularity
[00:11:38] of the individual chat interface, but
[00:11:40] you're able to abstract yourself to a
[00:11:42] supervisor role because you can see how
[00:11:44] the chats are working against the plan
[00:11:46] and how that is all working against an
[00:11:47] individual business goal, as well as
[00:11:49] then dig into the other business goals
[00:11:51] that you've currently got on the go. So,
[00:11:53] the workflow becomes then quick
[00:11:55] conversations while you're out and
[00:11:56] about. You can just fire it into
[00:11:58] Telegram via the channels feature, but
[00:12:00] if you've got a big goal that you want
[00:12:01] to manage over a day or a week or a
[00:12:03] complex project, then, for example, I
[00:12:05] would drop it into my command center and
[00:12:07] come back to actually review the outputs
[00:12:09] here and manage multiple goals inside
[00:12:11] that. All of this, for example, you can
[00:12:12] build exactly for yourself. You can
[00:12:14] follow the structure that I'm showing
[00:12:16] you on screen, and it all runs locally
[00:12:17] and acts as just a UI wrapper on top of
[00:12:20] your terminal. So, it abides by
[00:12:21] Anthropic's OAuth usage policies,
[00:12:23] meaning you can actually use it with
[00:12:24] your pro and max subscriptions. you want
[00:12:26] to get this up and running without
[00:12:28] having to build it yourself, it's just a
[00:12:29] one-line install as part of our paid
[00:12:32] community in the description below. And
[00:12:33] it includes all the underlying agentic
[00:12:35] operating system logic that we're
[00:12:37] covering today, too. So, full business
[00:12:39] context out of the box, 20-plus skills,
[00:12:42] scheduled workflows, the lot, all set up
[00:12:45] extremely quickly to handle tasks on
[00:12:47] behalf of you or your business. So,
[00:12:49] check out the link in the description
[00:12:50] below if you're interested in that. So,
[00:12:52] how you interact with it matters way
[00:12:55] more than most people think. Most people
[00:12:56] are just jumping to actually interact
[00:12:58] with it on the phone, but phones are
[00:12:59] only good for quick asks, and you can
[00:13:01] use Claude code channels for that. But
[00:13:03] if you want to build out something
[00:13:04] managing multiple goals, then you need
[00:13:06] your own interaction layer. Now, the one
[00:13:08] caveat I'll put on this, Claude have
[00:13:09] just updated their own Claude desktop to
[00:13:12] actually accommodate for managing
[00:13:13] multiple goals. However, it's still very
[00:13:15] technical, very focused on GitHub
[00:13:17] commits, and not focused on that
[00:13:19] high-level planning view with built-in
[00:13:21] planning frameworks like the way I built
[00:13:22] it out for myself. So, it depends what
[00:13:24] you're looking for as to what is the
[00:13:26] right solution for you. And that's how
[00:13:27] we interact with Claude code in a
[00:13:30] similar way to like Open Claude's
[00:13:31] mission control, for example. So, you've
[00:13:33] got memory, we've got skills, we've got
[00:13:34] the interaction layer. Now, let's look
[00:13:36] at the stuff that you should just be
[00:13:37] able to let run without you actually
[00:13:39] interfering with it. So, Hermes lets you
[00:13:41] set up automated jobs on a schedule, so
[00:13:44] you can install a skill, create a
[00:13:45] recurring job, and then it's going to
[00:13:47] run automatically. And in Claude code,
[00:13:48] you can do exactly the same with the new
[00:13:50] routines feature inside their desktop
[00:13:52] app. But right now, the feature is
[00:13:54] limited to built-in connectors, so it's
[00:13:56] quite difficult with apps that aren't in
[00:13:58] their native built-in connectors,
[00:14:00] especially when you can actually build
[00:14:01] this out using Claude code to leverage
[00:14:03] the built-in functionality on your Mac
[00:14:05] or Windows machine. So, you don't need a
[00:14:07] virtual private server, you don't need
[00:14:08] extra infrastructure. Claude code can
[00:14:10] actually set up this logic for you in
[00:14:12] less than a few hours, so that you can
[00:14:14] just control your scheduled jobs from a
[00:14:16] few files. When they're noted as active,
[00:14:18] we're going to run those scheduled jobs,
[00:14:20] and when they're not active, we're not
[00:14:22] going to run those scheduled jobs. Now,
[00:14:23] most people are creating scheduled jobs
[00:14:25] to just insert a simple prompt, but
[00:14:27] actually the smartest people are
[00:14:28] actually using scheduled workflows to
[00:14:30] chain skills together inside a prompt.
[00:14:33] So, you can schedule a task that's
[00:14:35] effectively going to run multiple skills
[00:14:37] in sequence. You might have a weekly
[00:14:39] content digest that runs every Monday at
[00:14:42] 9:00 a.m. So, it's going to pull the
[00:14:43] previous week's YouTube videos, run an
[00:14:46] analysis across those, and then generate
[00:14:48] three LinkedIn posts using your voice
[00:14:50] profile, and then drop them into a
[00:14:52] review folder. So, you come in on Monday
[00:14:54] morning, you've got all of those already
[00:14:55] ready in the review folder, and they're
[00:14:57] contextualized and followed all of the
[00:14:59] skill process documents that produce
[00:15:01] high-quality outputs. So, many different
[00:15:03] skills all chained together to produce
[00:15:04] one output that you come back and you
[00:15:06] can approve or supervise. And the
[00:15:08] biggest learning when I started building
[00:15:10] this out, my original aim was to build
[00:15:11] out fully autonomous scheduled
[00:15:14] workflows, run the whole thing, ship the
[00:15:16] output, post it to LinkedIn, whatever,
[00:15:18] but it was actually pretty bad because
[00:15:20] 20% of the time, something wouldn't be
[00:15:22] quite right. So, instead, I've actually
[00:15:24] built this framework now around doing
[00:15:26] 80% of the work automatically, the
[00:15:28] research, the narrowing of different
[00:15:30] topics, but what I've added in is always
[00:15:33] having a human checkpoint before
[00:15:34] anything goes live. So, I'm never going
[00:15:36] to post content that's just AI-generated
[00:15:38] stuff. I'm always going to have that
[00:15:40] human supervisor in the process until we
[00:15:42] can get to a level of quality where
[00:15:44] things can run autonomously and we're
[00:15:46] happy with them. So, all of my content
[00:15:47] drafts, for example, land in a folder so
[00:15:49] that I can actually come in and
[00:15:50] supervise them and review them and
[00:15:52] approve the outputs. So, it's basically
[00:15:53] giving you the speed of the automation
[00:15:55] without the risk of shipping something
[00:15:57] that's just pure AI slop, which we do
[00:15:58] not want to contribute. So, you can
[00:16:00] effectively use scheduled jobs to chain
[00:16:03] multiple skills together and then add in
[00:16:05] a human checkpoint to actually approve
[00:16:07] or make sure the quality is high. Right,
[00:16:09] so that is four amazing features. Each
[00:16:11] one you can build inside Claude code
[00:16:13] using what's already there in just a few
[00:16:15] days, but here's the fifth, and
[00:16:17] honestly, this is the one that made me
[00:16:18] stop looking at Hermes and Open Claude
[00:16:20] because I did not see enough capacity
[00:16:23] for it to do this well. Now, because
[00:16:24] Hermes and Open Claude are built solely
[00:16:26] to be agent frameworks, they're very
[00:16:28] tool-focused. So, it's all about
[00:16:30] installing a skill, running a job,
[00:16:32] getting an output, but they don't know
[00:16:33] anything really about your business. You
[00:16:35] can, of course, install ways to actually
[00:16:38] give it information about your business,
[00:16:39] but they don't, out of the box, know
[00:16:41] your brand voice, know your ICP, they
[00:16:43] don't know your positioning, they don't
[00:16:45] know who your clients are, what your
[00:16:46] tone in your emails usually is. All of
[00:16:48] these things are critical for
[00:16:50] high-quality outputs. And it's the
[00:16:51] equivalent of basically starting from
[00:16:53] zero when you run a new skill. And this
[00:16:54] is what shifted me away from systems
[00:16:57] like Hermes and Open Claude to build my
[00:16:59] own system because I realized that the
[00:17:00] real unlock isn't actually the agents.
[00:17:02] The agents and the models are getting
[00:17:04] better and better. It's the layer
[00:17:05] underneath, the context that we
[00:17:07] discussed at the start, the brand
[00:17:08] context folder, the voice profile, the
[00:17:10] audience avatar, all of that preloaded,
[00:17:13] pulling into the right skill at the
[00:17:14] right time is what actually generates
[00:17:17] high-quality outputs. So, I actually
[00:17:18] pulled together myself a set of skills
[00:17:20] that help me generate my voice profile,
[00:17:22] and I make sure that when I build out my
[00:17:24] skills using the skill creator skill,
[00:17:26] all of them reference the right context
[00:17:28] at the right time. So, if I have a skill
[00:17:30] that builds out LinkedIn posts, for
[00:17:31] example, it will always reference my
[00:17:34] brand voice. It will understand the
[00:17:35] positioning because it understands who
[00:17:37] my clients are. And I used content as an
[00:17:39] example because it's relatable to a lot
[00:17:41] of different businesses. It doesn't mean
[00:17:43] you need to use these systems to
[00:17:44] actually generate your content. And the
[00:17:46] way that we've done this is basically
[00:17:47] moving everything, all of that context
[00:17:49] for my business, into a single brand
[00:17:52] context folder that every skill is able
[00:17:53] to reference. So, you update the
[00:17:55] information once, and every skill gets
[00:17:57] that update when it runs. So, business
[00:17:58] context is that compounding advantage
[00:18:01] that you cannot get right now. So, build
[00:18:03] this right, and this totally underpins
[00:18:05] all of the other pillars that we've
[00:18:06] talked about today. You need to inject
[00:18:08] the right context at the right time, and
[00:18:10] that starts with actually having a
[00:18:11] shared context folder that focuses on
[00:18:14] your brand and you. So, when you bring
[00:18:16] this all together, this is exactly how
[00:18:18] it looks in a three-step process to
[00:18:19] compare to the one we showed at the
[00:18:21] start. We have your own agentic
[00:18:22] operating system where we have the
[00:18:24] business brain, which underpins and
[00:18:25] powers Claude code by injecting the
[00:18:27] right context at the right time. We're
[00:18:28] able to then actually just write goals,
[00:18:30] whether that's to create a scheduled job
[00:18:32] or to manage multiple business goals in
[00:18:34] one place. Claude is then going to do
[00:18:36] the work in the background to break it
[00:18:37] down into subtasks, choose the right
[00:18:39] skills, etc. And what that enables is
[00:18:41] your system to deliver you a
[00:18:43] high-quality result that's
[00:18:44] contextualized by your business context,
[00:18:46] completely replacing the need for a
[00:18:48] framework like Hermes or Open Claude and
[00:18:50] without all of the technical overhead
[00:18:52] and cost implications of moving off the
[00:18:54] pro and max plans from Claude. So,
[00:18:56] that's the five features that actually
[00:18:57] matter and how to build each one of them
[00:18:59] inside Claude code yourself. And if
[00:19:01] you're building out your own version
[00:19:02] right now, which a lot of you in the
[00:19:04] comments have told me you are, here's my
[00:19:06] honest advice from three months of
[00:19:08] getting this wrong and rebuilding it.
[00:19:10] Start with this business brain. Don't
[00:19:12] start with the agents. Don't start with
[00:19:13] the multi-agent orchestration. I made
[00:19:16] this same mistake. Every feature I just
[00:19:17] walked through gets multiplied by having
[00:19:19] the solid context, the foundation layer
[00:19:22] underneath it. And none of them are
[00:19:24] going to work without that layer. And if
[00:19:25] you just want to skip the setup and grab
[00:19:27] the whole thing plug and play today,
[00:19:29] then check out the link below in the
[00:19:31] description for the agentic academy. So,
[00:19:32] you've got the agentic OS, the command
[00:19:34] center that you saw today with the
[00:19:35] dashboard, and all 20-plus skills ready
[00:19:38] to go with a one-line install. And if
[00:19:40] you want to see exactly why I built out
[00:19:42] the command center in the first place,
[00:19:43] then check out the next video. Thanks
[00:19:45] for watching.