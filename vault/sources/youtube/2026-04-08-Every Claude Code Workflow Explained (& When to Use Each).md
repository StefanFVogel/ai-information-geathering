---
author: '[[Simon Scrapes]]'
channel_id: UCdCR4-uYOg5ju-IUuDnfnQA
date: '2026-04-07'
duration: 1069
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- '[ai]'
title: Every Claude Code Workflow Explained (& When to Use Each)
type: inbox
url: https://www.youtube.com/watch?v=38t5UBCa4OI
---

## Summary

*Ask Claude to summarize this transcript.*


🚀 Build agentic systems that run your business: https://skool.com/scrapes Don't miss the next build - https://www.youtube.com/@simonscrapes?sub_confirmation...

---

## Transcript

[00:00:00] If you're still using claw code one
[00:00:01] conversation at a time, you're using it
[00:00:03] wrong. And this video is going to change
[00:00:06] how you work with it. So, at the moment,
[00:00:08] you give it a task, you wait for the
[00:00:09] result, and then you move on to the next
[00:00:11] task. Everything's running at one time.
[00:00:13] But that's not how you'd run a team.
[00:00:14] You'd run teams in parallel, and you'd
[00:00:16] bring in specialists when required. And
[00:00:18] claw code is built to work exactly like
[00:00:20] that, too. But most people aren't using
[00:00:22] it that way. So, in this video, you'll
[00:00:23] see five ways on how to actually use it,
[00:00:26] from simple setups to fully hands-off
[00:00:28] workflows. so that you can stop working
[00:00:30] in one conversation and start saving
[00:00:32] some serious time. So, let's get into
[00:00:34] it. And I'll start off with something
[00:00:36] that surprised me when I first found out
[00:00:38] about it. So, every single time you use
[00:00:40] clog code, even in a basic conversation,
[00:00:43] it's already using a version of these
[00:00:44] patterns that we'll run through behind
[00:00:46] the scenes. So, it actually has already
[00:00:48] built-in sub aents that it uses
[00:00:50] automatically without you having to tell
[00:00:52] it to. So, there are actually three
[00:00:53] built-in sub aents baked into claw code.
[00:00:56] The first one is called explore. And
[00:00:58] explore is basically a fast cheap scout.
[00:01:01] So it runs on haiku which is anthropic's
[00:01:03] fastest and cheapest model. And all it
[00:01:05] can do is read your files. So it can
[00:01:07] search your files. It can look through
[00:01:09] folder structures. But it's read only.
[00:01:11] It can't change anything. So when you
[00:01:12] ask Claude something like how does my
[00:01:14] user authentication work in this
[00:01:16] project? Then Claude will often spin up
[00:01:17] an explore agent behind the scenes
[00:01:19] without you asking to. It will go off
[00:01:21] read through your files with its own set
[00:01:23] of context window and it will come back
[00:01:26] with a summary and your main
[00:01:27] conversation therefore can stay clean.
[00:01:29] It doesn't bloat the context. And you'll
[00:01:31] actually see this inside the terminal
[00:01:32] when you run these tasks. You'll see it
[00:01:34] pop up in the terminal as the explore
[00:01:36] tool. The second one is similar. It's
[00:01:38] called plan, but it specifically
[00:01:39] activates when you're in plan mode. So
[00:01:41] if you type / plan or hit shift tab
[00:01:43] twice to enter plan mode, then Claude is
[00:01:45] going to use the plan sub agent to
[00:01:47] research your codebase before it
[00:01:48] presents you with a strategy. Again,
[00:01:50] separate context window, readonly. And
[00:01:52] the third one that they've implemented
[00:01:53] behind the scenes is general purpose.
[00:01:55] And this, as it sounds, is quite general
[00:01:57] purpose. So, it's the one that does the
[00:01:58] heavy lifting. It runs on Sonnet and it
[00:02:01] has full tool access. So, it can read
[00:02:03] and write. And Claude uses it for
[00:02:04] complex multi-step tasks. So, if you're
[00:02:07] asking Claude to do something that
[00:02:09] requires both exploring the code base
[00:02:10] and making changes across multiple
[00:02:12] files, that's when it will often
[00:02:13] delegate that to a general purpose sub
[00:02:16] agent. And the key thing here is you've
[00:02:17] not told it to do anything. And Claude
[00:02:19] is deciding when to use these
[00:02:20] automatically. It's looking at the
[00:02:22] complexity of your task and routting it
[00:02:24] to the right sub aent. And all of those
[00:02:25] sub aents run with their own context
[00:02:27] window so that your main conversation
[00:02:29] never gets bloated with all the reading
[00:02:31] and searching of those files. So even
[00:02:33] before we get into the five patterns,
[00:02:35] just know that claw code is already
[00:02:37] doing some of this work for you. But
[00:02:38] when you understand the full spectrum of
[00:02:40] the patterns, you can take control and
[00:02:42] get so much more out of it. Okay. So
[00:02:44] with that context, let's start at the
[00:02:46] beginning with pattern one. And
[00:02:47] sequential flow is exactly as it sounds.
[00:02:49] You open a terminal, you start a claw
[00:02:52] code session, and every task you give it
[00:02:54] builds on the last one. So we've got you
[00:02:56] here. We assign a task. We then move to
[00:02:58] the next task. Once task one is
[00:02:59] finished, move to the next. Move to the
[00:03:01] next. And our shared context is growing
[00:03:03] over time. So it's building on the
[00:03:05] context that we've been given it
[00:03:07] throughout the different tasks. So it
[00:03:09] might be something like build me a
[00:03:10] landing page. Claude then builds it as
[00:03:12] task one or a first version of it. You
[00:03:14] say add a hero image to page one. Add a
[00:03:17] contact form. All of these are different
[00:03:18] tasks that build on the first task. And
[00:03:20] the output of task one can feed into
[00:03:22] task two. And the outputs of task one
[00:03:25] and two can feed into task three because
[00:03:26] it's all stored in the context window.
[00:03:28] And this might seem like you're not
[00:03:29] using any sub aents, but remember that
[00:03:31] Claude has those built-in sub aents. So
[00:03:33] even in this single conversation, Claude
[00:03:36] might spin up its explore plan or
[00:03:37] general purpose agents that help by
[00:03:39] actually offloading some context at the
[00:03:42] right time to get stuff done faster or
[00:03:44] more effectively on your behalf. And
[00:03:46] you'll see these pop up in the terminal,
[00:03:47] but from your perspective, it's still
[00:03:49] just one conversation flow between you
[00:03:50] and Claude. Now, the really important
[00:03:52] thing to understand about sequential
[00:03:54] flow is that it has a ceiling and that
[00:03:56] ceiling is dictated by the context
[00:03:57] window and that's shown by the little
[00:03:58] green bar on the bottom of the terminal.
[00:04:00] So the longer you work in that one
[00:04:02] session, the more the context is going
[00:04:03] to accumulate. And at that point, Claude
[00:04:06] starts forgetting things or not being
[00:04:07] able to find things, which is what we
[00:04:09] call context rot. So this is where
[00:04:11] skills and commands become super
[00:04:12] valuable because if you've got a well
[00:04:13] structured claude.md and some well
[00:04:15] ststructured skills that are described
[00:04:17] well, then Claude is able to load in
[00:04:19] that skill and any reference files at
[00:04:21] the right time and then offload it at
[00:04:23] the right time also to not bloat the
[00:04:25] conversation window. And then using
[00:04:26] commands like /clear and /compact will
[00:04:29] help you actually keep the summary of
[00:04:31] the conversation in the context. But
[00:04:33] eventually with this you're going to hit
[00:04:35] a wall and that's when we need to move
[00:04:37] to pattern two. And pattern two is
[00:04:39] called the operator. And this time you
[00:04:41] are acting as an orchestrator. So
[00:04:43] instead of running one clawed session,
[00:04:45] you're going to open up multiple
[00:04:46] terminal windows. You might have found
[00:04:47] yourself doing this already to get
[00:04:49] things done quickly. Each has its own
[00:04:50] clawed instance. So you can treat these
[00:04:52] like separate agents. terminal 1 2 3 and
[00:04:55] four completely separate agents. They
[00:04:57] have their own context window and
[00:04:58] therefore you can give them specific
[00:05:00] context for a specific task. So this
[00:05:02] time let's say you're building out a SAS
[00:05:03] app. You need a new onboarding flow
[00:05:05] built. You also need your checkout bug
[00:05:07] fix and you want to experiment with a
[00:05:09] new design for let's say your user
[00:05:12] settings page. All of these tasks that
[00:05:13] we've mentioned don't depend on each
[00:05:15] other. And that's one of the reasons why
[00:05:17] we can actually orchestrate these in
[00:05:19] completely separate terminals that don't
[00:05:21] blow each other's context because
[00:05:22] there's no connection between those
[00:05:24] terminals. We are purely coordinating.
[00:05:26] So you open three terminals like this
[00:05:28] inside VS Code. And Claude actually has
[00:05:30] now a built-in flag to do this much
[00:05:32] easier. So in the first time we type in
[00:05:34] claude-w
[00:05:36] which is important new onboarding flow.
[00:05:38] The second one claude-w
[00:05:40] checkout bug and the third one
[00:05:42] claude-wesign
[00:05:44] user settings. And you'll see that in
[00:05:46] the project folder here, we've now
[00:05:48] opened up what's called a work tree
[00:05:50] where we've got new onboarding flow, fix
[00:05:52] checkout bug, and redesign user
[00:05:54] settings. And now if we go into our doc
[00:05:56] cloud folder, we've effectively got
[00:05:57] these different work trees, which is a
[00:05:59] separate copy of your project with its
[00:06:01] own branch, and it drops it straight
[00:06:03] into the claw code session. Each one in
[00:06:05] its own isolated workspace, and they
[00:06:07] can't interfere with each other. So they
[00:06:09] all have a clean context window, so
[00:06:10] there's no context rot from other tasks.
[00:06:12] and us as the operator are the ones
[00:06:14] coordinating the efforts between these
[00:06:16] different terminals here. So you're
[00:06:18] probably at this point checking in on
[00:06:19] the different terminals, the different
[00:06:20] tasks going on. You're copy and pasting
[00:06:22] findings from one to another if you're
[00:06:24] needed and then you're going to have to
[00:06:26] decide when each one is done and when
[00:06:28] you want to merge that back into the
[00:06:29] main project. But this is a massive
[00:06:31] upgrade from this sequential flow
[00:06:33] because actually we can get multiple
[00:06:34] things done in parallel as long as
[00:06:36] they're not dependent on each other. But
[00:06:38] if they do depend on each other, then
[00:06:40] this flow isn't going to work for us.
[00:06:41] And here's the nice touch about closing
[00:06:43] a work tree session. As soon as we close
[00:06:45] this window, Claude is going to handle
[00:06:47] the cleanup for us. So if nothing's
[00:06:49] changed, it removes that workspace
[00:06:51] automatically. But if there is work to
[00:06:53] keep, then it's going to ask you what to
[00:06:55] do. And you can see as I close these
[00:06:57] sessions, they disappear from the work
[00:07:00] trees up here. So the operator pattern
[00:07:02] is you running multiple clawed sessions
[00:07:04] in parallel, each with its own isolated
[00:07:06] workspace, but you're still the one
[00:07:08] coordinating. So, it's perfect for
[00:07:10] independent tasks where you want maximum
[00:07:12] control and clean context windows where
[00:07:14] they will not interfere with each other.
[00:07:15] Now, the operator pattern is great, but
[00:07:17] as you'll have probably noticed, you can
[00:07:18] only manage a certain number of
[00:07:20] terminals at any one point. Four to five
[00:07:22] terminals and you're flicking between
[00:07:24] those terminals, it becomes really
[00:07:25] difficult checking in on all of the
[00:07:27] sessions. So, what if the claw could
[00:07:28] actually handle the parallel tasks
[00:07:31] itself? So, pattern three then is the
[00:07:33] split and merge. And this is where it
[00:07:35] gets really interesting because the core
[00:07:37] idea is that within a single claw code
[00:07:39] session one terminal claw itself can
[00:07:42] split work across multiple sub aents
[00:07:44] that then run in parallel. So if you're
[00:07:46] thinking about all four of these
[00:07:47] terminals we could effectively spin off
[00:07:49] multiple sub aents inside each terminal
[00:07:52] to get more done quicker. And then
[00:07:54] effectively at the end it's going to
[00:07:55] merge all the results back into the main
[00:07:57] agent so that you can reap the rewards.
[00:07:59] And if you remember those built-in sub
[00:08:00] aents I mentioned earlier, explore,
[00:08:02] plan, and general purpose. Those are
[00:08:04] good examples of that. But you're not
[00:08:06] limited to just those. You can create
[00:08:08] your own custom sub aents inside your
[00:08:10] doc folder. And Claude can spin up
[00:08:12] multiple of them at the same time. And
[00:08:15] here is how that works in practice. You
[00:08:17] give Claude a task. Claude is going to
[00:08:19] analyze that task and realize that it
[00:08:21] can be broken down into independent
[00:08:22] pieces. It will then fan out into
[00:08:24] multiple sub aents, each one running in
[00:08:27] its own context window. and each one
[00:08:29] focused on their specific piece of work.
[00:08:31] And then when it's all done, it will
[00:08:32] merge all those results automatically
[00:08:34] and give you the final output. So, a lot
[00:08:36] is happening in the background here that
[00:08:38] we don't have to manually tell it to do.
[00:08:40] So, let's say you ask Claude to research
[00:08:41] five different competitors for a client
[00:08:43] proposal. Instead of researching them
[00:08:45] one by one, which could take ages if we
[00:08:47] ran it in that sequential flow pattern
[00:08:49] one, Claude can spin up five sub agents,
[00:08:51] one per competitor, and they all
[00:08:53] research simultaneously. So each one is
[00:08:56] going to come back with their findings
[00:08:57] and the main agent is going to
[00:08:58] synthesize the five findings into one
[00:09:01] single report. And Boris Churnney even
[00:09:04] one of the creators of core code has
[00:09:05] talked about sometimes spinning up 15
[00:09:07] sub aents at a time to get things done.
[00:09:09] But actually the limit on this is 10 at
[00:09:12] once. So 10 sub aents at once. Claude
[00:09:14] will actually cue any additional tasks
[00:09:17] as additional sub aents. But here's the
[00:09:19] critical limitation here. Sub agents can
[00:09:21] only report back to the main agent. So
[00:09:23] they can't actually talk to each other.
[00:09:25] So sub agent one and sub agent 3 have no
[00:09:28] idea what each other are doing. It's
[00:09:30] this like hub and spoke methodology
[00:09:32] where the main agent or our main
[00:09:33] instance where we're interacting with
[00:09:35] Claude is acting as the hub and it's
[00:09:37] receiving information back and forth
[00:09:38] from that sub agent. And if you've ever
[00:09:40] used the framework GSD or get done
[00:09:43] by Tash, this is like a framework I'd
[00:09:45] highly recommend for comprehensive
[00:09:47] projects. is basically a planning
[00:09:49] framework that will split your initial
[00:09:50] project brief into subtasks and execute
[00:09:53] on those subtasks for so it's designed
[00:09:55] for big projects but not in an
[00:09:57] enterprise fashion. We can look at their
[00:09:59] agents inside their agents folder.
[00:10:00] They've got quite a few agents in here
[00:10:02] and actually what you can do is go into
[00:10:04] the agents listed and see exactly like
[00:10:06] we do with skills the name the
[00:10:09] description. So researches a single gray
[00:10:11] area decision and returns a structured
[00:10:13] comparison table with rationale. So
[00:10:15] we're effectively giving this agent a
[00:10:16] role to do and a specific set of context
[00:10:20] that it goes out and performs a certain
[00:10:22] process as well as giving that agent a
[00:10:25] certain set of tools that it actually
[00:10:26] has access to. Now Claude will read the
[00:10:28] name of all agents in our docord folder
[00:10:31] and decide when it's suitable to offload
[00:10:33] a task to those sub agents. I.e. it will
[00:10:35] automatically use it when it thinks the
[00:10:37] task matches the description. Or you can
[00:10:39] specifically say I want to use the
[00:10:41] advisor researcher sub agent in this
[00:10:43] task. And one of the most powerful
[00:10:44] applications of this pattern is the
[00:10:46] build a validator chain. So you have one
[00:10:48] sub agent build something and then you
[00:10:51] have another sub agent actually review
[00:10:53] it. But what that requires is the sub
[00:10:55] aent one to build it first, pass it back
[00:10:57] to the main agent, pass that to the
[00:10:59] second sub aent through here and then
[00:11:00] that passes the results back to the main
[00:11:02] agent. So you can see because they can't
[00:11:04] communicate with each other that we're
[00:11:05] actually orchestrating it through this
[00:11:06] main agent. But you can effectively get
[00:11:08] a built-in quality check without doing
[00:11:09] any of the reviewing yourself by using
[00:11:11] that builder validator chain. So split
[00:11:14] and merge is claude doing the
[00:11:15] parallelization
[00:11:17] for you within a single session. So it
[00:11:19] can fan out work to those sub aents and
[00:11:21] merge the results for you. And again
[00:11:23] they keep your context window clean. So
[00:11:25] this is really powerful. So split and
[00:11:26] merge is awesome but it has one
[00:11:28] limitation. Sub agents can't talk to
[00:11:30] each other. So everything has to funnel
[00:11:32] through the main agent and for some
[00:11:34] tasks that is a genuine bottleneck. So
[00:11:36] what if your researcher agent needs to
[00:11:38] check in with your reviewer agent? Or
[00:11:40] what if you have a front-end developer
[00:11:42] that needs to coordinate with a back-end
[00:11:43] developer. So this is where the fourth
[00:11:45] pattern comes in, which is agent teams.
[00:11:47] An agent team is effectively a team of
[00:11:49] agents, as it sounds, that can share
[00:11:51] findings, challenge each other, and
[00:11:53] adapt together. So that the way that
[00:11:54] they share information is through a
[00:11:56] shared task list. So they're no longer
[00:11:57] interacting with the team lead, which is
[00:11:59] our main orchestration window. They're
[00:12:01] interacting with that shared task list.
[00:12:03] Agent one understands what tasks agent
[00:12:05] two is doing. And vice versa, they can
[00:12:07] send messages between the agents. And
[00:12:10] it's the most advanced coordination
[00:12:11] pattern. It's the newest addition to CL
[00:12:14] code and it is genuinely a gamecher for
[00:12:16] complex projects, but it should only be
[00:12:18] used in complex projects because the
[00:12:20] token usage is extremely high when
[00:12:22] you've got cross collaboration between
[00:12:24] the agents. Now, this is completely
[00:12:26] still experimental. It shipped with Opus
[00:12:28] 4.6 as a research preview. So, you need
[00:12:31] to still enable it by adding a flag to
[00:12:33] your settings.json, which is claw code
[00:12:36] experimental agent teams one. and you
[00:12:38] need to add that as an environment
[00:12:39] variable in your settings.json. But once
[00:12:41] it's enabled, you just tell Claude in
[00:12:43] your prompt that you want to use an
[00:12:45] agent team. So you must still specify
[00:12:47] that you want to use an agent team, not
[00:12:48] like sub agents where it will choose
[00:12:50] those automatically. You go in, you
[00:12:52] describe the task you want, you describe
[00:12:54] the team structure or Claude will
[00:12:56] actually determine the team structure
[00:12:57] itself and Claude will then create that
[00:12:58] team, spawn the teammates and coordinate
[00:13:00] the work. And in your terminal, you can
[00:13:02] actually navigate between the teammates
[00:13:04] using shift up and shift down. And you
[00:13:06] can message directly any teammate and
[00:13:08] bypass this team lead entirely or you
[00:13:10] can talk directly to the team lead. Now,
[00:13:12] as I mentioned, they use significantly
[00:13:13] more tokens because we've got this back
[00:13:15] and forth between the shared task list,
[00:13:17] the team lead, between the agents. And
[00:13:19] each teammate is its full CL code
[00:13:21] instance with its own context window
[00:13:23] again. So, it's got a portion of the
[00:13:25] main context passed in it from that
[00:13:27] shared task list and the team lead. And
[00:13:29] they roughly estimate it's going to be
[00:13:31] four to seven times more tokens than a
[00:13:33] single session when you're actually
[00:13:35] using agent teams. And the thing that
[00:13:37] actually matters here is you don't need
[00:13:38] agent teams for most of your work. You
[00:13:40] should actually only reach for them when
[00:13:41] sub agents or even a single session
[00:13:43] couldn't do the job. So say you're
[00:13:45] trying to build out a complex SAS
[00:13:47] application where you have a front-end
[00:13:48] developer, a backend developer, and then
[00:13:50] a testing developer that spins up tests
[00:13:52] and needs to communicate to agent one
[00:13:54] and two as they build. That is an
[00:13:56] example where you would actually want an
[00:13:58] agent team to save from back and forth
[00:14:00] between the orchestration layer. But a
[00:14:02] lot of people in the community are just
[00:14:03] saying that actually this is just a way
[00:14:05] to produce large quantities of work very
[00:14:07] quickly which isn't necessarily a good
[00:14:09] thing. You still need the work to be the
[00:14:11] right work. So it's powerful but
[00:14:13] expensive. So only reach for this when
[00:14:15] the task genuinely needs that cross
[00:14:17] collaboration. So patterns 1 through 4
[00:14:19] all have one thing in common. You're
[00:14:21] there in the terminal. you're either
[00:14:23] typing, coordinating, or at least
[00:14:25] watching the task. But what if you
[00:14:27] didn't need to be there at all? So, this
[00:14:29] brings us on to the last pattern, which
[00:14:31] is Claude working without you. So, this
[00:14:33] is the dream of autonomous workflows,
[00:14:35] where you don't need to be in the loop.
[00:14:37] You just set a task, you walk away, and
[00:14:38] you come back to the results. And this
[00:14:40] is called headless. And it's where
[00:14:41] Claude code goes from being a tool you
[00:14:43] sit with to a team member that's going
[00:14:45] to go and work independently. This
[00:14:47] requires you having no conversation back
[00:14:49] and forth, no terminal window open, and
[00:14:52] no human in the loop at all. So when
[00:14:54] we're running this, we're using the -p
[00:14:56] flag. So we're saying Claude-P, and
[00:14:58] we're entering a prompt after the P
[00:15:00] flag. So we're saying, Claude, process
[00:15:02] this prompt. We don't want any
[00:15:04] interaction, no approvals. You've got
[00:15:06] full permissions. Just go get it done
[00:15:08] and return to me the result when you're
[00:15:10] finished. And that on its own is kind of
[00:15:12] iterating with that task cla prompt and
[00:15:15] will give us that report.json. But when
[00:15:18] it gets really groundbreaking, when it
[00:15:20] gets really powerful is like when you
[00:15:22] plug this into other systems. So if you
[00:15:24] plug this in to your Windows or your Mac
[00:15:27] scheduling function, your cron
[00:15:29] functionality that can say at 7 a.m.
[00:15:31] every day, fire in this command to my
[00:15:33] terminal and then Claude goes and
[00:15:34] iterates and gets the report and sends
[00:15:37] it back to you. That is when it
[00:15:38] genuinely becomes a gamecher because
[00:15:39] then what we're doing is actually
[00:15:41] creating workflows that can run on a
[00:15:43] schedule without your input. So it could
[00:15:45] be review yesterday's work and write a
[00:15:47] summary to a morning report.mmd. So when
[00:15:50] Claude wakes up, it's going to read all
[00:15:52] the work you did yesterday, analyze
[00:15:53] them, write the report, and then you
[00:15:55] just have to go and look at the output
[00:15:57] before you've even done anything. You
[00:15:59] didn't open a terminal, you didn't even
[00:16:00] type a prompt in. It basically just
[00:16:02] happened. Or say you're actually running
[00:16:04] content for your business. You could
[00:16:05] have a script that pulls your latest
[00:16:07] video transcript, runs it through Claude
[00:16:09] with a specific prompt, gets you back a
[00:16:11] set of social media posts, saved to a
[00:16:13] file that you can then just schedule
[00:16:15] automatically. And you can chain these
[00:16:16] together. You can add skills into the
[00:16:18] prompts that invoke specific skills. And
[00:16:21] this is all completely automated. Now,
[00:16:23] the big limitation in this is trust.
[00:16:26] You're not asking for an iterative
[00:16:28] conversation. You're giving Claude
[00:16:30] autonomy to do things on your behalf.
[00:16:32] So, you're not checking each step. So,
[00:16:34] this works best for tasks where the
[00:16:35] output is extremely easy to verify. At
[00:16:38] the moment, you probably don't want to
[00:16:39] go headless on anything that's hard to
[00:16:42] undo, but you can actually put guard
[00:16:44] rails on this as well. If you want it to
[00:16:45] only read and not write, for example, we
[00:16:48] can do d-allowed tools and then make
[00:16:50] sure that we add specific things that it
[00:16:51] can do. And some people in the community
[00:16:52] have taken this even further with things
[00:16:55] like the Ralph loop, which keeps feeding
[00:16:57] the same prompt back in so that Claude
[00:16:59] iterates on its own work until it gets
[00:17:01] it right. And each time it iterates, it
[00:17:03] understands what has been done in the
[00:17:05] last cycle. And people have actually
[00:17:06] been using this to ship entire projects
[00:17:08] overnight. So this is brilliant. This is
[00:17:10] like claude working without you. You set
[00:17:12] a task, you walk away, and you come back
[00:17:14] for the results. But like we said, it's
[00:17:16] best for batch processing things and
[00:17:17] anything where the output is really easy
[00:17:19] to verify. So there you have it, five
[00:17:22] agentic patterns for claw code. And if
[00:17:23] you want to go deeper on any of these or
[00:17:25] on building skills, creating custom sub
[00:17:27] agents, how to structure your claw MD
[00:17:29] and actually put these patterns into
[00:17:31] practice with real projects, then check
[00:17:32] out the first link to the Agentic
[00:17:34] Academy in the description below. We've
[00:17:36] got a full claw code track where we
[00:17:37] build this stuff step by step. And let
[00:17:39] me know in the comments which pattern
[00:17:41] you're looking forward to trying. And if
[00:17:43] this did save you the time of figuring
[00:17:44] out this yourself, then I'd really
[00:17:46] appreciate a like and subscribe. Thanks
[00:17:48] so much for watching.