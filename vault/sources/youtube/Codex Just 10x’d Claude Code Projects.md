---
author: '[[Nate Herk | AI Automation]]'
channel_id: UC2ojq-nuP8ceeHqiroeKhBA
created: 2026-04-07
date: '2026-03-31'
description: 'Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=codex-just-10xd-claude-code-projectsAll
  my FREE resources: https:...'
duration: 791
language: en
published: 2026-03-31
source: https://www.youtube.com/watch?v=B2Kh_ZoLVTM
status: processed
tags:
- codex
- claude-code
- benchmarks
- openai
- code-review
- clippings
- ai
title: Codex Just 10x’d Claude Code Projects
topics:
- '[[Codex]]'
- '[[Claude Code]]'
- '[[GPT 5.4]]'
- '[[Code Review]]'
- '[[AI Benchmarks]]'
---

## Summary

[[Nate Herk]] reviews OpenAI's official [[Codex]] plugin for [[Claude Code]], which lets you use [[GPT 5.4]] for code reviews directly inside Claude Code workflows.

### Key Takeaways

- **What It Is**: An official OpenAI plugin that brings [[Codex]] into [[Claude Code]] as a set of slash commands (/codex review, /codex adversarial-review, /codex rescue, etc.)
- **Why It Exists**: OpenAI noticed Claude Code users were already bringing in Codex for code reviews. The plugin formalizes this workflow.
- **Free**: Works with a free ChatGPT subscription -- no paid plan required for Codex reviews.
- **Benchmarks**: [[GPT 5.4]] beats [[Opus 4.6]] on most coding benchmarks (by 1-13 points) except SWE-bench verified where Opus leads slightly. GPT 5.4 is also cheaper.
- **Complementary Strengths**: Claude Code excels at planning, creativity, asking right questions. Codex excels at catching edge cases, code review, and avoiding overengineering. Claude Code tends to overengineer and get "long run drift"; Codex is more rigid but catches bugs.
- **Best Workflow**: Use Claude Code for planning and initial build, then bring in Codex for adversarial review and production polish. Split tasks between both and compare.
- **Adversarial Review Demo**: Codex found high and medium priority issues with scores, recommendations, and next steps -- all read-only, doesn't modify code.
- **Game Build Comparison**: Same prompt given to both. Codex produced a more polished UI; Claude Code finished faster. Codex flagged it had more work to do (3 tasks), showing more self-awareness about spec compliance.

### Tools Mentioned
- [[Codex]] (OpenAI) -- code review plugin for Claude Code
- [[GPT 5.4]] -- OpenAI's model used by Codex
- [[Opus 4.6]] -- Anthropic's model powering Claude Code

![](https://www.youtube.com/watch?v=B2Kh_ZoLVTM)

## Transcript

### Was ist das Codex-Plugin?

**0:00** · So today, OpenAI released an official codec plugin for cloud code. You can see here it says if you already use cloud code, this codeex plugin gives you a simple way to pull codeex into that same workflow. Now this isn't like groundbreaking technology. People have already been kind of using a combination of codec and claude code together, but this plugin makes it a lot easier. And so obviously I've been focusing a lot on cloud code, but I have played around with codecs a little bit and they felt very similar to me. But as of lately, I've been seeing more and more people talk about how they've been using codecs inside of their cloud code workflows and projects to help do code reviews and to help get a second pair of eyes on their code. So here you can see the head of developer experience at OpenAI said that they've been seeing cloud code users bring in codecs for code reviews and use GBT 5.4 for some more complex tasks. So that's kind of why they decided to do this. And the cool thing is, which I didn't actually know, you can use codecs for free. So, you can just use your free Chatbt subscription, which means there's basically no reason for you to get this plugin, put it into some of your Cloud Code projects where you're building some software or game or whatever it is, and then just have it do some code reviews and see what you might have missed with Claude Code. So, you might be wondering to yourself, is this just overkill? And is it actually needed? And so, I was thinking the exact same thing, and I decided to do a little bit of research to compare the benchmarks. So, starting off, Opus 4.6 versus GBT 5.4. Opus is the purple, GBT is the green, and we're looking at different coding benchmarks.

### Opus 4.6 vs. GPT 5.4 Benchmarks

**1:21** · So, the S. S. S. S. S. S. S. S. S. S. S.

**1:22** · Opus has a slight edge. But in all of these other ones, you'll notice that GBT 5.4 is actually ahead of Opus 4.6. And if you actually break them down headto-head, you can see here's the S SWB verified where Opus leads by almost a point. But in all these other ones, 13 points, 10 points, 1, 2.5, 3.5, GBT 5.4 actually beats out Opus 4.6. And when you think about those benchmarks and then you realize that Opus 4.5 is also much more expensive than GPT 5x4, it definitely makes you think. Now, all of these are the benchmarks, right? So, I think they're always important to look at and to sort of be aware of like what models are supposed to be good at certain things, but I always want to get in there, get my hands dirty, and see how I like them, see what they feel like, rather than just basing my assumptions off of benchmarks. So I did some research on X and Reddit and I scraped information and thoughts from people who have been using both of them a lot and I threw together some of the pitfalls of both of them. And it's interesting because when you hear the weaknesses of both, the strengths of both kind of complement each other really well. So for cloud code, some of the things that people have been saying are weaknesses are that it overengineers, that it can be really token hungry, and that it can sort of get into long run drift. So it can miss edge cases and just build bugs. And the important part of that is when it goes and reviews its own code, sometimes it misses those because it just can't see them. And these things right here are some of the things that Codeex is known for being really good at. But then if we switch over to Codeex weaknesses, people complain that it's not super good at planning and it doesn't ask the right questions and sometimes you don't get a lot of good creative outputs from it and it's just a little bit more rigid in that way. And it's interesting because some of these things that people complain about codecs, cloud code or opus does really well. And so naturally, that's why you've seen a lot of people on X talking about, oh, I like to plan and maybe build the initial PC with cloud code, but then I'll bring in codeex to execute the rest of it, kind of push it into production and do all of the reviewing. Now, what this really makes me think about is just the fact that you should be trying different tools and understanding like where to use them together. It's not always like, oh, I'm all in on this one and I'm only going to use this one. It's about understanding like, okay, for this specific use case, I might use 30% Claude and 70% OpenAI, and for this next use case, I'm probably going to use Claude Code pretty much all the way through until the very end. So, I'll leave a link to this article down in the description of this video, but it's really, really simple to set up. All you have to do is run these three commands in order. So, this one basically installs the marketplace, this one installs the plugin, and then this one helps you get set up. And you can also go to the actual GitHub documentation, which has been growing in stars pretty quickly since the release. And you pretty much can read every single thing about this. You can see that you can also use your free chatbt subscription once again, but you would just run these in order. And it also breaks down all of the different functions that are in here. So we have like a review, we have an adversarial review, we have rescue, we have all these different little functions that you can run, which almost you can think of them like skills now.

### Stärken und Schwächen der einzelnen Tools

### Gemeinsame Nutzung beider Tools

### Einrichtung

**4:11** · And you can do some other things that are pretty cool by adding these flags that let them run in the background or wait for things. And you get a lot of extra functionality here. So in a session, if you come over here and you do /plugins, you would basically have to, you know, try to install that marketplace. You can see that I have the OpenAI Codex one right here. And then you can see right here I've got the codeex plugin installed and enabled. So now if I went ahead to do a /codex, you can see all of these different things that I could actually call on. And all of these would be using GBT 5.4 instead of Opus. So real quick example of what that may look like. Here's a project where I'm setting up just some sort of dashboard for an internal system. And keep in mind, a lot of this is mock data. This is something that I just recently spun up and right now I'm just working on sort of the flow and the feel rather than like having the data synced in. But anyways, I built this obviously using Opus. So now in this project, if I do /codeex, I can see all these different things to run. And right now I want to decide between a review or an adversarial review. So if I go over back to the GitHub, we can read the difference between the two, which is a review runs a normal codeex review on your current work, which is the same quality of code review as running a slash review inside of Codex directly.

### Live-Demo zur Gegneranalyse

**5:14** · So you can use this for reviewing uncommitted changes or comparing branches. And this is a readonly type of skill. Now the adversarial review is kind of just like a review on steroids.

**5:25** · It's steerable and it questions the chosen implementation and design and it can be used to pressure test things, look at trade-offs, failure modes, and whether different approaches would be safer or more simple. This is also a readonly command that does not change code. Essentially, these are both just kind of giving you uh a nice audit. So, I'm going to go ahead and try the adversarial review right here. So, what you'll notice is right away it has to get familiarized and acclimated with the environment. So, it's going to look at the working tree size. It's going to check the differences between what's staged and what's unstaged. And after that, it should come back and ask us how we want to run this review. So, it's asking me how we want to run it. I'm just going to go ahead and say in the background and shoot that off. You can see that it also said that this is a pretty large review. So, we'll see how long this takes. So, by the way, I'm on Windows and when I was using this, I've gotten a bug a few times which basically said that there was something wrong with like path, but it was able to do research and fix that for me. And now you can see that that adversarial review has been complete. So, let's take a look and see what we got here. It gives us a target. It gives us a verdict. It tells things that we don't need to ship. And here are the things that it found. And it also looks like it has priority scores. So, we have some high priority things. We have a recommendation. Same thing right here. And then we also have a medium priority thing as well as some next steps. So from here it would be up to you to either continue on using codeex to build out these changes or switch back to cloud code or what I would probably do is I would split them off do one with opus one with GBT and then just see which one's better. So that was a lot of the use cases that I've been seeing on X and just when I started looking into this, right? But then I of course wanted to try okay let's give both of them the exact same prompt and see what the outputs actually look like. So, I gave them both this prompt, which was basically just like to build me a game. I gave them some, you know, specifications and things like that. And it's detailed, but it's not like super super detailed. I didn't put them into plan mode. I just shot it off in bypass permissions to see what the outputs looked like. And so, here's codecs open up in VS Code as well with the extension. And you can see that I gave them the exact same prompt, and then I just shot them off to see what happened. Now, before we open up the outputs, there's two things I wanted to tell you. The first thing is that Opus finished way quicker than Codeex did. So whether you take that as a good thing or a bad thing, just something I wanted to call out. Codex ran for a lot longer.

### Vergleichsspiel

**7:36** · And the second thing is Opus came back and basically said, "Hey, the server started, you can open it up and you can play the game." But when Codex came back, it basically said like, "Hey, this is only task one out of three, but the game's finished and you're ready to play." And then after that, I said, "Okay, well, um, is the game done?" And it said, "Not fully. It's playable and it's local, but there's still a lot of things that I need to do to meet the original spec." Now, let's take a look at the games. This first version right here, this is the version that was built by Claude Code. So, we have dungeon crawler, a roglike adventure. We're going to go ahead and start up a new game. And you can see here we have a little navbar on the right with our floor. I think maybe our health, our stats, our XP, equipment, gold, combat log. We have a little mini map. And then we have our controls. So, if I start moving around here, you can see that I can kind of see what's going on. I can break through these little barriers. And here's like a goblin, apparently. I can move up here. There's a skeleton. Here's some gold. I don't know how to pick that up exactly. Um I don't know exactly what all this stuff is, but you can see that it is, you know, it's a 2D playable game. It's nothing crazy, but the mini map starts to unlock. And honestly, like for one prompt and maybe like about a 5minute workflow, this is not too bad.

**8:45** · But now, let's just go ahead and close out of that and let's go over to Codeex's version. This is what the initial UI looks like. And already it looks a little bit more polished and it feels more like an app. And I can go ahead and start this new game here. And let me just zoom in a little bit more now. This one already looks a lot less pixy. And I guess I died really quick.

**9:05** · But this one looks a lot less pixy and it just feels a little bit more polished as you can see. Um I don't actually see on this right hand side though. I guess the mini map is down there. So there is still the mini map. But overall I would have definitely said that Codeex did a better job of this game on the first oneshot prompt than Claude Code did. So now what I would do is I would come back into this game, the version that was built with cloud code, and I would just want to do an adversarial review. And then what I'm going to do after Codex comes back with this review, I'm just going to tell Opus, go implement all of these changes, and then we're going to open up the game again and see how much different it is. But that's why it's always interesting to test things out yourself because some people were saying that Codex does a worse job with like UI design. Although clearly from this example with the same prompt, Codex's version in my mind was a lot better.

### Warum nicht einfach Codex verwenden?

**9:53** · \[snorts\] Now, as this is running, I did want to just address something real quick, which is basically like, okay, you know, if Codeex is just better than Cloud Code and it's cheaper, then why would I not just use Codex instead? And that's honestly a very fair question. And the only answer that I can give you is download it, try it, and just see which one you like better. From what I've been playing around with so far, I think there's definitely very clear strengths where Codeex is better than Cloud Code.

**10:17** · But overall, I really like the way Cloud Code feels. I think that it's a lot more forgiving, especially for me because I don't come from a formal software engineering background. And that type of feel aligns with a lot of the stuff that I've been seeing other people say as well. But I'll tell you for sure that I'm definitely going to be using this codeex plugin to help review stuff and to help build on extra features. And maybe one day I'll get to the point where I decide that I want to use codeex 80% and cloud code 20 rather than the other way around. So this is now running in the background and I wanted to show you guys what it looks like when you do the codec status. It basically just shows you the exact job that has, you know, been running and how long it's been running. And it looks like that's actually finished up because now it's giving us another output. And this is interesting because I just spun up this game as a demo. There was no actual branch to compare itself with or there was no commit. So what it decided to do is rerun it properly by creating a review branch so that codeex can actually diff the actual game code. So, this has come back and keep in mind that these changes that it's suggesting are probably not going to be anything to do with the UI. So, that won't really see any changes. It's about the actual game play and it's about the actual like functionality of the code and how this works. So, we have just two high things.

### Codex-Analysedaten in Opus einspielen

**11:26** · We have final floor stairs let the player soft lock the run permanently. But the ancient amulet is only ever spawned when floor equals 10. So, there's no matching upward travel mechanic and victory only triggers from using the amulet. So a player can therefore step on floor 10 stairs before collecting the amulet, get sent to floor 11, and then the run becomes unwinable. So that's definitely a flaw in the way that this was actually built from Opus.

**11:50** · And then there's another issue over here, as you can see, which is a real data loss rollback bug for a game that exposes a continue entry point. So it gives us a recommendation for how to fix both of these. We can gate floor 10 stairs, and we can also persist after state changing player actions or debounce an auto save after each turn.

**12:07** · and on major events like new game blah blah blah blah blah. So I'm just going to go ahead on bypass permissions mode just say implements. But obviously all of this stuff is kind of more of a demo.

**12:16** · I would be taking this feedback and I would be once again going into a plan mode with cloud code and then taking that plan and telling it to go ahead and make the changes. So those changes have been made as you can see. And if I go ahead and open up the game and I give it a quick refresh, like I said, nothing really about the UI of the game has changed, but apparently those changes have been fixed. And actually, it does already look a little bit better for some reason. I'm probably just making that up. But anyways, the point being that was a super strong combination. As you can see, we're using Cloud Code and then the adversarial review with Codeex.

### Fazit

**12:48** · So, anyways, that is going to do it for this one. I know that I haven't made a video on Codeex yet on this channel, but I've been playing around with all these different tools and focusing mainly on Cloud Code because I don't want to just confuse you guys with throwing a bunch of different tools at you. But, I do think that this one is definitely something that is worth checking out.

**13:02** · So, if you enjoyed the video or you learned something new, please give it a like. It helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one. Thanks, everyone.

---

## Transcript

[00:00:00] So today, OpenAI released an official
[00:00:02] codec plugin for cloud code. You can see
[00:00:04] here it says if you already use cloud
[00:00:05] code, this codeex plugin gives you a
[00:00:07] simple way to pull codeex into that same
[00:00:09] workflow. Now this isn't like
[00:00:10] groundbreaking technology. People have
[00:00:12] already been kind of using a combination
[00:00:13] of codec and claude code together, but
[00:00:15] this plugin makes it a lot easier. And
[00:00:17] so obviously I've been focusing a lot on
[00:00:18] cloud code, but I have played around
[00:00:20] with codecs a little bit and they felt
[00:00:21] very similar to me. But as of lately,
[00:00:23] I've been seeing more and more people
[00:00:24] talk about how they've been using codecs
[00:00:26] inside of their cloud code workflows and
[00:00:28] projects to help do code reviews and to
[00:00:31] help get a second pair of eyes on their
[00:00:33] code. So here you can see the head of
[00:00:35] developer experience at OpenAI said that
[00:00:37] they've been seeing cloud code users
[00:00:38] bring in codecs for code reviews and use
[00:00:40] GBT 5.4 for some more complex tasks. So
[00:00:43] that's kind of why they decided to do
[00:00:44] this. And the cool thing is, which I
[00:00:46] didn't actually know, you can use codecs
[00:00:48] for free. So, you can just use your free
[00:00:50] Chatbt subscription, which means there's
[00:00:52] basically no reason for you to get this
[00:00:54] plugin, put it into some of your Cloud
[00:00:56] Code projects where you're building some
[00:00:58] software or game or whatever it is, and
[00:01:00] then just have it do some code reviews
[00:01:02] and see what you might have missed with
[00:01:03] Claude Code. So, you might be wondering
[00:01:05] to yourself, is this just overkill? And
[00:01:07] is it actually needed? And so, I was
[00:01:09] thinking the exact same thing, and I
[00:01:10] decided to do a little bit of research
[00:01:12] to compare the benchmarks. So, starting
[00:01:14] off, Opus 4.6 versus GBT 5.4. Opus is
[00:01:17] the purple, GBT is the green, and we're
[00:01:20] looking at different coding benchmarks.
[00:01:21] So, the S. S. S. S. S. S. S. S. S. S. S.
[00:01:22] Opus has a slight edge. But in all of
[00:01:24] these other ones, you'll notice that GBT
[00:01:26] 5.4 is actually ahead of Opus 4.6. And
[00:01:30] if you actually break them down
[00:01:31] headto-head, you can see here's the S
[00:01:32] SWB verified where Opus leads by almost
[00:01:34] a point. But in all these other ones, 13
[00:01:37] points, 10 points, 1, 2.5, 3.5, GBT 5.4
[00:01:44] actually beats out Opus 4.6. And when
[00:01:46] you think about those benchmarks and
[00:01:47] then you realize that Opus 4.5 is also
[00:01:50] much more expensive than GPT 5x4, it
[00:01:52] definitely makes you think. Now, all of
[00:01:54] these are the benchmarks, right? So, I
[00:01:55] think they're always important to look
[00:01:56] at and to sort of be aware of like what
[00:01:58] models are supposed to be good at
[00:01:59] certain things, but I always want to get
[00:02:01] in there, get my hands dirty, and see
[00:02:03] how I like them, see what they feel
[00:02:05] like, rather than just basing my
[00:02:06] assumptions off of benchmarks. So I did
[00:02:09] some research on X and Reddit and I
[00:02:11] scraped information and thoughts from
[00:02:12] people who have been using both of them
[00:02:14] a lot and I threw together some of the
[00:02:15] pitfalls of both of them. And it's
[00:02:17] interesting because when you hear the
[00:02:19] weaknesses of both, the strengths of
[00:02:21] both kind of complement each other
[00:02:22] really well. So for cloud code, some of
[00:02:24] the things that people have been saying
[00:02:25] are weaknesses are that it
[00:02:27] overengineers, that it can be really
[00:02:29] token hungry, and that it can sort of
[00:02:31] get into long run drift. So it can miss
[00:02:33] edge cases and just build bugs. And the
[00:02:35] important part of that is when it goes
[00:02:37] and reviews its own code, sometimes it
[00:02:39] misses those because it just can't see
[00:02:41] them. And these things right here are
[00:02:42] some of the things that Codeex is known
[00:02:44] for being really good at. But then if we
[00:02:46] switch over to Codeex weaknesses, people
[00:02:48] complain that it's not super good at
[00:02:49] planning and it doesn't ask the right
[00:02:51] questions and sometimes you don't get a
[00:02:52] lot of good creative outputs from it and
[00:02:55] it's just a little bit more rigid in
[00:02:56] that way. And it's interesting because
[00:02:58] some of these things that people
[00:02:59] complain about codecs, cloud code or
[00:03:01] opus does really well. And so naturally,
[00:03:04] that's why you've seen a lot of people
[00:03:05] on X talking about, oh, I like to plan
[00:03:07] and maybe build the initial PC with
[00:03:09] cloud code, but then I'll bring in
[00:03:10] codeex to execute the rest of it, kind
[00:03:12] of push it into production and do all of
[00:03:14] the reviewing. Now, what this really
[00:03:15] makes me think about is just the fact
[00:03:17] that you should be trying different
[00:03:18] tools and understanding like where to
[00:03:21] use them together. It's not always like,
[00:03:23] oh, I'm all in on this one and I'm only
[00:03:24] going to use this one. It's about
[00:03:26] understanding like, okay, for this
[00:03:27] specific use case, I might use 30%
[00:03:29] Claude and 70% OpenAI, and for this next
[00:03:32] use case, I'm probably going to use
[00:03:33] Claude Code pretty much all the way
[00:03:34] through until the very end. So, I'll
[00:03:37] leave a link to this article down in the
[00:03:38] description of this video, but it's
[00:03:39] really, really simple to set up. All you
[00:03:41] have to do is run these three commands
[00:03:42] in order. So, this one basically
[00:03:43] installs the marketplace, this one
[00:03:45] installs the plugin, and then this one
[00:03:46] helps you get set up. And you can also
[00:03:48] go to the actual GitHub documentation,
[00:03:50] which has been growing in stars pretty
[00:03:51] quickly since the release. And you
[00:03:53] pretty much can read every single thing
[00:03:54] about this. You can see that you can
[00:03:56] also use your free chatbt subscription
[00:03:57] once again, but you would just run these
[00:03:59] in order. And it also breaks down all of
[00:04:01] the different functions that are in
[00:04:02] here. So we have like a review, we have
[00:04:04] an adversarial review, we have rescue,
[00:04:07] we have all these different little
[00:04:08] functions that you can run, which almost
[00:04:10] you can think of them like skills now.
[00:04:11] And you can do some other things that
[00:04:12] are pretty cool by adding these flags
[00:04:14] that let them run in the background or
[00:04:15] wait for things. And you get a lot of
[00:04:17] extra functionality here. So in a
[00:04:18] session, if you come over here and you
[00:04:20] do /plugins, you would basically have
[00:04:22] to, you know, try to install that
[00:04:23] marketplace. You can see that I have the
[00:04:25] OpenAI Codex one right here. And then
[00:04:26] you can see right here I've got the
[00:04:28] codeex plugin installed and enabled. So
[00:04:30] now if I went ahead to do a /codex, you
[00:04:33] can see all of these different things
[00:04:34] that I could actually call on. And all
[00:04:35] of these would be using GBT 5.4 instead
[00:04:37] of Opus. So real quick example of what
[00:04:40] that may look like. Here's a project
[00:04:42] where I'm setting up just some sort of
[00:04:43] dashboard for an internal system. And
[00:04:46] keep in mind, a lot of this is mock
[00:04:47] data. This is something that I just
[00:04:48] recently spun up and right now I'm just
[00:04:50] working on sort of the flow and the feel
[00:04:52] rather than like having the data synced
[00:04:53] in. But anyways, I built this obviously
[00:04:55] using Opus. So now in this project, if I
[00:04:57] do /codeex, I can see all these
[00:04:59] different things to run. And right now I
[00:05:01] want to decide between a review or an
[00:05:02] adversarial review. So if I go over back
[00:05:04] to the GitHub, we can read the
[00:05:06] difference between the two, which is a
[00:05:07] review runs a normal codeex review on
[00:05:09] your current work, which is the same
[00:05:11] quality of code review as running a
[00:05:12] slash review inside of Codex directly.
[00:05:14] So you can use this for reviewing
[00:05:16] uncommitted changes or comparing
[00:05:17] branches. And this is a readonly type of
[00:05:21] skill. Now the adversarial review is
[00:05:23] kind of just like a review on steroids.
[00:05:25] It's steerable and it questions the
[00:05:27] chosen implementation and design and it
[00:05:29] can be used to pressure test things,
[00:05:31] look at trade-offs, failure modes, and
[00:05:32] whether different approaches would be
[00:05:34] safer or more simple. This is also a
[00:05:37] readonly command that does not change
[00:05:38] code. Essentially, these are both just
[00:05:40] kind of giving you uh a nice audit. So,
[00:05:42] I'm going to go ahead and try the
[00:05:44] adversarial review right here. So, what
[00:05:46] you'll notice is right away it has to
[00:05:47] get familiarized and acclimated with the
[00:05:49] environment. So, it's going to look at
[00:05:51] the working tree size. It's going to
[00:05:52] check the differences between what's
[00:05:53] staged and what's unstaged. And after
[00:05:55] that, it should come back and ask us how
[00:05:57] we want to run this review. So, it's
[00:05:59] asking me how we want to run it. I'm
[00:06:00] just going to go ahead and say in the
[00:06:01] background and shoot that off. You can
[00:06:03] see that it also said that this is a
[00:06:04] pretty large review. So, we'll see how
[00:06:07] long this takes. So, by the way, I'm on
[00:06:09] Windows and when I was using this, I've
[00:06:10] gotten a bug a few times which basically
[00:06:12] said that there was something wrong with
[00:06:14] like path, but it was able to do
[00:06:16] research and fix that for me. And now
[00:06:17] you can see that that adversarial review
[00:06:20] has been complete. So, let's take a look
[00:06:21] and see what we got here. It gives us a
[00:06:23] target. It gives us a verdict. It tells
[00:06:25] things that we don't need to ship. And
[00:06:28] here are the things that it found. And
[00:06:29] it also looks like it has priority
[00:06:30] scores. So, we have some high priority
[00:06:32] things. We have a recommendation. Same
[00:06:34] thing right here. And then we also have
[00:06:35] a medium priority thing as well as some
[00:06:37] next steps. So from here it would be up
[00:06:39] to you to either continue on using
[00:06:42] codeex to build out these changes or
[00:06:44] switch back to cloud code or what I
[00:06:45] would probably do is I would split them
[00:06:47] off do one with opus one with GBT and
[00:06:49] then just see which one's better. So
[00:06:51] that was a lot of the use cases that
[00:06:52] I've been seeing on X and just when I
[00:06:54] started looking into this, right? But
[00:06:56] then I of course wanted to try okay
[00:06:57] let's give both of them the exact same
[00:06:59] prompt and see what the outputs actually
[00:07:02] look like. So, I gave them both this
[00:07:03] prompt, which was basically just like to
[00:07:05] build me a game. I gave them some, you
[00:07:07] know, specifications and things like
[00:07:08] that. And it's detailed, but it's not
[00:07:10] like super super detailed. I didn't put
[00:07:12] them into plan mode. I just shot it off
[00:07:14] in bypass permissions to see what the
[00:07:16] outputs looked like. And so, here's
[00:07:18] codecs open up in VS Code as well with
[00:07:20] the extension. And you can see that I
[00:07:22] gave them the exact same prompt, and
[00:07:23] then I just shot them off to see what
[00:07:24] happened. Now, before we open up the
[00:07:26] outputs, there's two things I wanted to
[00:07:28] tell you. The first thing is that Opus
[00:07:30] finished way quicker than Codeex did. So
[00:07:32] whether you take that as a good thing or
[00:07:33] a bad thing, just something I wanted to
[00:07:34] call out. Codex ran for a lot longer.
[00:07:36] And the second thing is Opus came back
[00:07:38] and basically said, "Hey, the server
[00:07:39] started, you can open it up and you can
[00:07:41] play the game." But when Codex came
[00:07:42] back, it basically said like, "Hey, this
[00:07:43] is only task one out of three, but the
[00:07:46] game's finished and you're ready to
[00:07:47] play." And then after that, I said,
[00:07:48] "Okay, well, um, is the game done?" And
[00:07:51] it said, "Not fully. It's playable and
[00:07:52] it's local, but there's still a lot of
[00:07:54] things that I need to do to meet the
[00:07:56] original spec." Now, let's take a look
[00:07:57] at the games. This first version right
[00:08:00] here, this is the version that was built
[00:08:02] by Claude Code. So, we have dungeon
[00:08:04] crawler, a roglike adventure. We're
[00:08:05] going to go ahead and start up a new
[00:08:06] game. And you can see here we have a
[00:08:08] little navbar on the right with our
[00:08:10] floor. I think maybe our health, our
[00:08:12] stats, our XP, equipment, gold, combat
[00:08:16] log. We have a little mini map. And then
[00:08:18] we have our controls. So, if I start
[00:08:20] moving around here, you can see that I
[00:08:22] can kind of see what's going on. I can
[00:08:23] break through these little barriers. And
[00:08:25] here's like a goblin, apparently. I can
[00:08:27] move up here. There's a skeleton. Here's
[00:08:29] some gold. I don't know how to pick that
[00:08:30] up exactly. Um I don't know exactly what
[00:08:32] all this stuff is, but you can see that
[00:08:34] it is, you know, it's a 2D playable
[00:08:36] game. It's nothing crazy, but the mini
[00:08:38] map starts to unlock. And honestly, like
[00:08:40] for one prompt and maybe like about a
[00:08:42] 5minute workflow, this is not too bad.
[00:08:45] But now, let's just go ahead and close
[00:08:46] out of that and let's go over to
[00:08:48] Codeex's version. This is what the
[00:08:50] initial UI looks like. And already it
[00:08:52] looks a little bit more polished and it
[00:08:54] feels more like an app. And I can go
[00:08:56] ahead and start this new game here. And
[00:08:58] let me just zoom in a little bit more
[00:08:59] now. This one already looks a lot less
[00:09:02] pixy. And I guess I died really quick.
[00:09:05] But this one looks a lot less pixy and
[00:09:08] it just feels a little bit more polished
[00:09:10] as you can see. Um I don't actually see
[00:09:12] on this right hand side though. I guess
[00:09:14] the mini map is down there. So there is
[00:09:15] still the mini map. But overall I would
[00:09:17] have definitely said that Codeex did a
[00:09:19] better job of this game on the first
[00:09:22] oneshot prompt than Claude Code did. So
[00:09:25] now what I would do is I would come back
[00:09:26] into this game, the version that was
[00:09:28] built with cloud code, and I would just
[00:09:29] want to do an adversarial review. And
[00:09:31] then what I'm going to do after Codex
[00:09:33] comes back with this review, I'm just
[00:09:34] going to tell Opus, go implement all of
[00:09:36] these changes, and then we're going to
[00:09:37] open up the game again and see how much
[00:09:39] different it is. But that's why it's
[00:09:40] always interesting to test things out
[00:09:42] yourself because some people were saying
[00:09:44] that Codex does a worse job with like UI
[00:09:47] design. Although clearly from this
[00:09:49] example with the same prompt, Codex's
[00:09:51] version in my mind was a lot better.
[00:09:53] >> [snorts]
[00:09:53] >> Now, as this is running, I did want to
[00:09:54] just address something real quick, which
[00:09:56] is basically like, okay, you know, if
[00:09:57] Codeex is just better than Cloud Code
[00:09:59] and it's cheaper, then why would I not
[00:10:01] just use Codex instead? And that's
[00:10:02] honestly a very fair question. And the
[00:10:05] only answer that I can give you is
[00:10:07] download it, try it, and just see which
[00:10:09] one you like better. From what I've been
[00:10:11] playing around with so far, I think
[00:10:12] there's definitely very clear strengths
[00:10:14] where Codeex is better than Cloud Code.
[00:10:17] But overall, I really like the way Cloud
[00:10:19] Code feels. I think that it's a lot more
[00:10:21] forgiving, especially for me because I
[00:10:22] don't come from a formal software
[00:10:24] engineering background. And that type of
[00:10:26] feel aligns with a lot of the stuff that
[00:10:28] I've been seeing other people say as
[00:10:29] well. But I'll tell you for sure that
[00:10:30] I'm definitely going to be using this
[00:10:32] codeex plugin to help review stuff and
[00:10:34] to help build on extra features. And
[00:10:36] maybe one day I'll get to the point
[00:10:37] where I decide that I want to use codeex
[00:10:39] 80% and cloud code 20 rather than the
[00:10:41] other way around. So this is now running
[00:10:43] in the background and I wanted to show
[00:10:44] you guys what it looks like when you do
[00:10:45] the codec status. It basically just
[00:10:47] shows you the exact job that has, you
[00:10:49] know, been running and how long it's
[00:10:51] been running. And it looks like that's
[00:10:52] actually finished up because now it's
[00:10:53] giving us another output. And this is
[00:10:55] interesting because I just spun up this
[00:10:57] game as a demo. There was no actual
[00:11:00] branch to compare itself with or there
[00:11:02] was no commit. So what it decided to do
[00:11:04] is rerun it properly by creating a
[00:11:06] review branch so that codeex can
[00:11:07] actually diff the actual game code. So,
[00:11:10] this has come back and keep in mind that
[00:11:12] these changes that it's suggesting are
[00:11:14] probably not going to be anything to do
[00:11:16] with the UI. So, that won't really see
[00:11:18] any changes. It's about the actual game
[00:11:20] play and it's about the actual like
[00:11:22] functionality of the code and how this
[00:11:24] works. So, we have just two high things.
[00:11:26] We have final floor stairs let the
[00:11:28] player soft lock the run permanently.
[00:11:30] But the ancient amulet is only ever
[00:11:32] spawned when floor equals 10. So,
[00:11:34] there's no matching upward travel
[00:11:35] mechanic and victory only triggers from
[00:11:37] using the amulet. So a player can
[00:11:38] therefore step on floor 10 stairs before
[00:11:41] collecting the amulet, get sent to floor
[00:11:42] 11, and then the run becomes unwinable.
[00:11:45] So that's definitely a flaw in the way
[00:11:47] that this was actually built from Opus.
[00:11:50] And then there's another issue over
[00:11:51] here, as you can see, which is a real
[00:11:53] data loss rollback bug for a game that
[00:11:55] exposes a continue entry point. So it
[00:11:57] gives us a recommendation for how to fix
[00:12:00] both of these. We can gate floor 10
[00:12:01] stairs, and we can also persist after
[00:12:03] state changing player actions or
[00:12:05] debounce an auto save after each turn.
[00:12:07] and on major events like new game blah
[00:12:09] blah blah blah blah. So I'm just going
[00:12:10] to go ahead on bypass permissions mode
[00:12:12] just say implements. But obviously all
[00:12:14] of this stuff is kind of more of a demo.
[00:12:16] I would be taking this feedback and I
[00:12:17] would be once again going into a plan
[00:12:19] mode with cloud code and then taking
[00:12:21] that plan and telling it to go ahead and
[00:12:24] make the changes. So those changes have
[00:12:26] been made as you can see. And if I go
[00:12:27] ahead and open up the game and I give it
[00:12:29] a quick refresh, like I said, nothing
[00:12:31] really about the UI of the game has
[00:12:32] changed, but apparently those changes
[00:12:35] have been fixed. And actually, it does
[00:12:37] already look a little bit better for
[00:12:38] some reason. I'm probably just making
[00:12:39] that up. But anyways, the point being
[00:12:42] that was a super strong combination. As
[00:12:43] you can see, we're using Cloud Code and
[00:12:46] then the adversarial review with Codeex.
[00:12:48] So, anyways, that is going to do it for
[00:12:49] this one. I know that I haven't made a
[00:12:51] video on Codeex yet on this channel, but
[00:12:53] I've been playing around with all these
[00:12:54] different tools and focusing mainly on
[00:12:55] Cloud Code because I don't want to just
[00:12:57] confuse you guys with throwing a bunch
[00:12:58] of different tools at you. But, I do
[00:13:00] think that this one is definitely
[00:13:01] something that is worth checking out.
[00:13:02] So, if you enjoyed the video or you
[00:13:03] learned something new, please give it a
[00:13:04] like. It helps me out a ton. And as
[00:13:06] always, I appreciate you guys making it
[00:13:07] to the end of the video. I'll see you on
[00:13:08] the next one. Thanks, everyone.