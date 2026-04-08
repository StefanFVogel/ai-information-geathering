---
author: '[[Nate Herk | AI Automation]]'
channel_id: UC2ojq-nuP8ceeHqiroeKhBA
date: '2026-03-24'
duration: 341
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- claude-code
- auto-mode
- security
- '[ai]'
- permissions
title: STOP Using Bypass Permissions, Use This New Feature Instead
topics:
- '[[Claude Code]]'
- '[[Auto Mode]]'
- '[[Permissions]]'
type: inbox
url: https://www.youtube.com/watch?v=pkSxISewcw8
---

## Summary

[[Nate Herk]] covers [[Claude Code]]'s new **Auto Mode** -- a safer alternative to bypass permissions for long-running tasks.

### Key Takeaways

- **The Problem**: In "ask before edits" mode, Claude stops and asks permission for every edit, bash command, or web fetch. This interrupts your workflow constantly. Bypass permissions mode removes all checks but is dangerous.
- **The Old Fix**: Custom `.claude/settings.local.json` with allow/deny lists per project. Still the best option for fine-grained control.
- **Auto Mode**: A middle path -- Claude automatically classifies each tool call as safe or risky before executing. Safe actions run automatically, risky ones get blocked and Claude tries a different approach.
- **How It Works**: A classifier reviews every tool call for destructive actions (deleting files, sensitive data access). Reduces risk but does not eliminate it entirely.
- **Trade-offs**: Sessions are slightly more expensive (extra AI classification per tool call). Still recommended to use in isolated environments.
- **Availability**: Research preview, currently only for Claude Team users. Enable via org settings.
- **Usage**: `claude --enable-auto-mode` in terminal, or switch via VS Code permission mode selector.

### Permission Modes Compared

| Mode | Interruptions | Risk | Cost |
|------|--------------|------|------|
| Ask before edits | High | Low | Normal |
| Auto mode | Low | Medium | Slightly higher |
| Bypass permissions | None | High | Normal |
| Custom settings.json | Low | Low (controlled) | Normal |

Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=stop-using-bypass-permissions-use-this-new
All my FREE resources: https://www.skool.com/ai-automation-societ

---

## Transcript

[00:00:00] Well, I'm back with another Claude code
[00:00:01] update. Today, we have auto mode. Auto
[00:00:04] mode provides a safer long-running
[00:00:05] alternative to dangerously skip
[00:00:07] permissions. So, what that means is when
[00:00:09] you're in Claude code and you shoot off
[00:00:11] a message, you are in some sort of
[00:00:12] permission mode. In this case, we are in
[00:00:14] ask before edits. So, that means exactly
[00:00:16] what it sounds like. Every time before
[00:00:18] it does an edit, it's going to stop
[00:00:20] working and it's going to ask me. Which
[00:00:21] means if I wanted to step away or, you
[00:00:23] know, work on something else, it would
[00:00:25] keep interrupting my workflow. So, right
[00:00:26] here you can see that it's able to read
[00:00:28] things, but now when it wants to
[00:00:29] actually make changes, it's going to pop
[00:00:31] up this tab. It's going to say, "Hey, am
[00:00:32] I allowed to do this?" You can either
[00:00:33] say yes for one time only or you can say
[00:00:36] yes every time in this session. And as
[00:00:38] you can see, it's popping it up again
[00:00:39] and stopping my session because it has
[00:00:41] to make two edits. And it's not just
[00:00:43] about the writing functions. Sometimes
[00:00:44] it'll stop your workflow and say, "Hey,
[00:00:45] can I do this web fetch or can I run
[00:00:47] this bash command?" So, the other option
[00:00:49] that a lot of people have been using and
[00:00:50] what I've shown sometimes in my videos
[00:00:52] is that you can use bypass permissions
[00:00:54] mode, which basically means Claude will
[00:00:56] do anything at whatever it wants and it
[00:00:58] won't ask for any permission. Which
[00:01:00] sounds great because a lot of times when
[00:01:01] you're working on stuff, you just want
[00:01:03] it to go through and not interrupt you.
[00:01:04] But it's called dangerously skip
[00:01:05] permissions for a reason because at the
[00:01:07] end of the day, if you're not watching
[00:01:08] it, it could go do anything. So, the fix
[00:01:10] that I had been using for a long time is
[00:01:11] within my .claude folder, I would have a
[00:01:14] local settings file, which looks like
[00:01:16] this. And this basically says, "Okay,
[00:01:18] Claude code, you can do anything on your
[00:01:19] allow list, but you can't do anything on
[00:01:21] your deny list. And anything here, you
[00:01:23] have to ask me explicitly before."
[00:01:26] And so, this gave me a lot more control
[00:01:27] over what Claude code does and what it
[00:01:29] can't do. And in some cases, I still
[00:01:31] think that this is the actual best
[00:01:32] option to use because you can change
[00:01:34] these per project and you could also set
[00:01:36] this globally if you'd like. But with
[00:01:38] Claude code's new release of auto mode,
[00:01:39] it basically makes those permission
[00:01:41] decisions on your behalf. So, now
[00:01:42] instead of having to copy and paste this
[00:01:44] settings file over to all of my new
[00:01:46] projects, I could basically just come
[00:01:47] into the permissions mode. I could
[00:01:48] change this to auto mode right here,
[00:01:50] which says Claude will automatically
[00:01:51] choose the best permission mode for each
[00:01:53] task. And you can do this in VS Code
[00:01:55] like you're seeing me do right here. Or
[00:01:57] if you open up a terminal and you run
[00:01:59] Claude like this, which is Claude enable
[00:02:01] auto mode, it will launch up Claude and
[00:02:03] then when you shift tab through, you can
[00:02:04] see that we now have the auto mode
[00:02:06] setting. And right here you can see that
[00:02:07] it says auto mode let's Claude handle
[00:02:08] permissions automatically. Claude checks
[00:02:11] each tool for risky actions and prompt
[00:02:12] injection before executing. Actions
[00:02:15] Claude identify as safe are executed
[00:02:16] while actions Claude identifies as risky
[00:02:18] are blocked and Claude may try a
[00:02:20] different approach. It's ideal for
[00:02:21] long-running tasks. Sessions are
[00:02:23] slightly more expensive. Claude can make
[00:02:25] mistakes that allow harmful commands to
[00:02:27] run. So, it's recommended to only use in
[00:02:28] isolated environments. So, auto mode is
[00:02:31] the middle path that lets you run longer
[00:02:32] tasks with fewer interruptions while
[00:02:34] introducing less risk than skipping all
[00:02:36] permissions. And that's pretty cool
[00:02:38] because basically
[00:02:44] before every single tool call, a
[00:02:45] classifier reviews it to check for
[00:02:47] potentially destructive actions like
[00:02:49] deleting or sensitive data, things like
[00:02:51] that. So, basically it reduces risk, but
[00:02:54] it does not eliminate it entirely. And
[00:02:56] we also did see in the terminal, if I go
[00:02:58] back over here and go to the terminal,
[00:03:00] it basically said here that these
[00:03:01] sessions are slightly more expensive
[00:03:04] because I'm assuming before every tool
[00:03:05] call, it uses AI to say, "Hey, is this
[00:03:07] dangerous? What should I do?" And that
[00:03:09] would explain why it's more expensive.
[00:03:11] So, like I said, in order to use this,
[00:03:12] it is right now research preview and
[00:03:14] it's only available for Claude team
[00:03:16] users. But if you are on a team, all you
[00:03:18] have to do is you come in here and you
[00:03:19] go to your organization settings and
[00:03:21] then you right here are able to enable
[00:03:23] allowing auto permissions mode. Same way
[00:03:25] that you would allow bypass permissions
[00:03:27] mode. And then you guys saw earlier, all
[00:03:29] we had to do was we had to run this
[00:03:31] command right here, Claude {dash} {dash}
[00:03:32] enable auto mode. Or if you're in VS
[00:03:34] Code and you're just using it like this,
[00:03:36] you should be able to see it right
[00:03:37] there. And then also, if you want to be
[00:03:39] able to disable it, you can do that like
[00:03:41] that. So, anyways, I know that was a
[00:03:42] super
[00:06:26] quick one, but I want to keep you guys
[00:06:27] up to date because I'm talking and
[00:06:29] shipping every single day. So, if you
[00:06:31] learned something new or you enjoyed the
[00:06:32] video, please give it a like. Definitely
[00:06:33] helps me out a ton. And as always, I
[00:06:35] appreciate you guys making it to the end
[00:06:36] of the video. I'll see you on the next
[00:06:37] one.
[00:06:38] Thanks, everyone.