---
author: '[[Nate Herk | AI Automation]]'
channel_id: UC2ojq-nuP8ceeHqiroeKhBA
date: '2026-04-16'
duration: 1033
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- '[ai]'
title: Claude Opus 4.7 Just Dropped... Or Did It Really?
type: inbox
url: https://www.youtube.com/watch?v=NiMc2PoTiXo
---

## Summary

[[Nate Herk]] analysiert den Release von [[Opus 4.7]] vor dem Hintergrund der Kontroverse um die zuvor verschlechterte Performance von [[Opus 4.6]].

**Act 1 — Was mit 4.6 passierte:**
Eine AMD-Senior-Direktorin analysierte ~7.000 Claude-Code-Sessions und fand, dass die Thinking-Depth um 73% kollabierte (von 2.200 auf 600 Zeichen). Das Modell las Dateien in 33,7% der Fälle nicht mehr vor dem Editieren (vorher 6%). User mussten 12x häufiger unterbrechen. Weitere Symptome: halluzinierte Git-Hashes, fake Package-Namen, "simplest" dreimal häufiger im Output, Task-Abandonment. Ursache: Am 9. Februar führte [[Anthropic]] **adaptive thinking** ein — das Modell entscheidet selbst, ob es überhaupt Tokens fürs Denken ausgibt. [[Boris Cherny]] (Creator of Claude Code) bestätigte: Turns mit Null-Reasoning produzierten Halluzinationen. Zusätzlich wurde der Effort-Default still auf "medium" gedrosselt — ohne User-Kommunikation. Auf dem Bridge-Bench fiel Opus 4.6 von Platz 2 auf Platz 10.

**Act 2 — Opus 4.7 Release:**
Features: adaptive thinking, neues **X-high effort level** (exklusiv für 4.7), 1M-Token-Context, verbesserte Vision, Document Reasoning, Biomolecular Reasoning (>2x), bessere SWBench-Pro-Scores (3x Production-Task-Resolution auf Rakuten-Benchmark). Neuer Tokenizer (1-1.3x teurer), neuer Slash-Command `/ultra-review` für dedizierte Review-Sessions. Safety-Profil ähnlich 4.6.

**Act 3 — Kritische Einordnung:**
Jede 4.6-Beschwerde hat nun einen passenden Fix — "als würden sie Löcher graben, um sie zu füllen". Aber die Verbesserungen scheinen real: X-high ist neu, Vision-Gains sind strukturell. Der neue Desktop-App hat 40+ Bugs (Theo testete 1h) — fragwürdig angesichts Anthropics Größe. Nates Verdikt: 4.7 ist "möglicherweise das beste AI-Modell bisher — oder die Heilung für eine selbst verursachte Krankheit".


Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=opus-4-7
All my FREE resources: https://www.skool.com/ai-automation-society/about?el=opus-4-7
Apply for my Y

---

## Transcript

[00:00:00] We just got Opus 4.7, which is
[00:00:01] apparently Claude's most capable Opus
[00:00:03] model yet. It handles long-running tasks
[00:00:05] with more rigor. It follows instructions
[00:00:07] more precisely and verifies its own
[00:00:09] outputs before reporting back. What's
[00:00:10] interesting to me is that these claims
[00:00:12] are addressing exactly what everyone was
[00:00:14] complaining about with Opus 4.6 the past
[00:00:16] couple weeks when everyone was like,
[00:00:17] "Hey, Opus has gotten so much more
[00:00:19] stupid lately." So, yes, we see these
[00:00:20] benchmarks. We see that there's a huge
[00:00:22] jump from Opus 4.6 to Opus 4.7 in most
[00:00:25] of these major categories. So, what I'm
[00:00:27] here to talk about today is, is this
[00:00:29] really Opus 4.7 or is this just 4.6 with
[00:00:32] some improvements? Some people have been
[00:00:34] saying that they intentionally made Opus
[00:00:35] 4.6 worse so that they could build up
[00:00:37] hype for 4.7 and then release it and
[00:00:39] then it feels way better than it really
[00:00:41] would have been. So, if you missed all
[00:00:42] that, I'm going to catch you up and
[00:00:43] let's just start flying through this
[00:00:44] stuff. Don't want to waste anyone's
[00:00:45] time. So, act one, as we're calling it
[00:00:48] here, is what happened to Opus 4.6. So,
[00:00:50] there's been lots of stuff. So this
[00:00:52] first one I wanted to address was that a
[00:00:53] senior director at AMD published an
[00:00:55] analysis of almost 7,000 coding sessions
[00:00:57] using claude code. She found that the
[00:00:59] thinking depth collapsed 73% from 2200
[00:01:02] characters of reasoning down to just 600
[00:01:04] characters of reasoning. So basically
[00:01:06] the model stopped reading files before
[00:01:07] editing them and stopped thinking as
[00:01:09] much and it just started jumping
[00:01:11] straight into doing things. So the
[00:01:12] models basically should always be
[00:01:13] reading the files before editing them
[00:01:15] and it started to not do that about 6%
[00:01:17] of the time but then that went all the
[00:01:18] way up to 33.7% of the time. So almost
[00:01:21] onethird it just wasn't reading the
[00:01:23] files. And she found that users had to
[00:01:25] interrupt the model 12 times more often
[00:01:27] to stop it from going off the rails. And
[00:01:28] obviously there's lots of problems here.
[00:01:30] There is the problem of quality of the
[00:01:32] actual code that's being written,
[00:01:33] especially when it's kind of like dark
[00:01:35] code and you don't really exactly know
[00:01:36] what AI is writing. And then there's
[00:01:38] also the fact that that's going to burn
[00:01:39] through your tokens, which is why in the
[00:01:41] past couple weeks, there's also been a
[00:01:42] huge uproar of people saying, "I just
[00:01:44] burned through my 200 bucks a month max
[00:01:45] plan in an hour." So what else have
[00:01:47] users been seeing? hallucinated git
[00:01:49] commit hashes, fake package names,
[00:01:51] fabricated API versions. Apparently, the
[00:01:53] word simplest appeared almost three
[00:01:55] times more often in model output, which
[00:01:57] means that it was optimizing for the
[00:01:58] least amount of effort possible. We've
[00:02:00] also been seeing premature task
[00:02:02] abandonment, so the model will just stop
[00:02:03] working on things midtask. This is
[00:02:05] something that I have actually felt a
[00:02:06] lot over the past couple weeks. And all
[00:02:08] of this kind of stuff, the session
[00:02:09] limits, the quality has caused some of
[00:02:12] the power users on 200 bucks a month max
[00:02:14] plans to start switching or canceling
[00:02:16] away. So then, of course, Enthropic
[00:02:17] addressed this. What did they actually
[00:02:19] change? Well, on February 9th, they
[00:02:21] changed the adaptive thinking, which
[00:02:22] meant that the model started dynamically
[00:02:24] deciding how much to think per turn. So
[00:02:26] on certain turns, if it thinks the
[00:02:28] request is simple, it would allocate
[00:02:29] zero reasoning token. So literally no
[00:02:32] thinking at all. So the question
[00:02:33] becomes, how does the model decide what
[00:02:35] task actually deserves a token budget
[00:02:37] for thinking or not? And then Boris
[00:02:39] Churnney, the basically creator of Cloud
[00:02:40] Code, confirmed the turns where the
[00:02:42] model fabricated had zero reasoning and
[00:02:44] the turns with deep reasoning were
[00:02:46] correct. So that was one of the first
[00:02:47] main things. Another thing that happened
[00:02:49] is they just dropped the effort default
[00:02:51] to medium. So basically all of these
[00:02:53] changes they didn't actually make to the
[00:02:55] model itself but more in the way the
[00:02:56] model behaved like the parameters and
[00:02:58] the weights and the training of the
[00:02:59] model OBU 4.6 was the same but they
[00:03:02] turned off its thinking and they turned
[00:03:03] off its effort basically. And they kind
[00:03:05] of did this one silently like right here
[00:03:07] if I go into my cloud code desktop app
[00:03:10] which I'm going to talk about this new
[00:03:11] desktop app as well because I think that
[00:03:12] there's lots of issues here. But right
[00:03:15] here, you can see we've got Opus 4.7,
[00:03:16] right? And when I click on it, you can
[00:03:18] see that we actually don't have the
[00:03:19] ability within Opus 4.7. But basically,
[00:03:21] if I just zoom back in here a little
[00:03:22] more, if I go to Sonnet, for example,
[00:03:24] you can see that we have effort and
[00:03:26] high, medium, low, and then sometimes
[00:03:28] for Opus 4.6, there's even a higher one,
[00:03:31] um, max effort or something. But they
[00:03:33] basically just switch this down without
[00:03:35] telling anybody. And no one was kind of
[00:03:36] looking in there. And if you're on the
[00:03:38] terminal or wherever you are, you might
[00:03:39] not even notice that. So people were
[00:03:40] like, "Okay, Opus is just stupid." And
[00:03:43] then a full month later, April 15th, pro
[00:03:45] and max users were still by default just
[00:03:47] running on medium effort. So like I
[00:03:49] said, they didn't change the model
[00:03:50] itself of 4.6. They just changed how
[00:03:52] hard the model was allowed to think and
[00:03:54] they didn't tell anyone. And a lot of
[00:03:55] that thinking and reasoning is where we
[00:03:57] get all the value of this, you know,
[00:03:58] awesome Opus 4.6 model. And then there
[00:04:00] was also some controversy with the
[00:04:02] bridge bench. A viral benchmark claimed
[00:04:03] that Opus 4.6 dropped from 83.6% to
[00:04:07] 68.3% accuracy. So basically on this
[00:04:10] leaderboard fell from being number two
[00:04:12] all the way down to number 10 and it was
[00:04:14] just you know Opus 4.6 or Opus 4.6 as of
[00:04:17] April 12th which showed that Opus was
[00:04:19] now actually worse than Sonnet 4.5 on
[00:04:21] this specific hallucination benchmark.
[00:04:23] Okay, so let's move on to act two. Opus
[00:04:25] 4.7 drops today. Okay, so before we get
[00:04:27] into the benchmarks, let me just show
[00:04:28] you real quick. It is available on the
[00:04:30] web right here. We've got Claude in the
[00:04:32] chat and I can see Opus 4.7 right here.
[00:04:34] Now what you'll notice is for Opus 4.7
[00:04:36] we have adaptive thinking. So we can do
[00:04:38] things only when needed like we just
[00:04:39] talked about. But if we go back to Opus
[00:04:41] 4.6, we don't have adapted, we have
[00:04:43] extended. So we can just turn extended
[00:04:45] on or off. I already showed you guys the
[00:04:47] desktop app. Here is my VS Code
[00:04:49] terminal. You can see we have welcome to
[00:04:50] Opus 4.7 X high. So we'll talk about
[00:04:53] that in a sec. But if you're not seeing
[00:04:54] this, maybe just try to update your
[00:04:56] Claude. So you can go ahead and just run
[00:04:57] like a claude update and that's how it
[00:05:01] will do it. Or if you want to do it in
[00:05:02] the extension, then you'll just have to
[00:05:04] update the actual extension over here in
[00:05:06] VS Code. And if I go to model in the
[00:05:08] extension and we click on switch, you
[00:05:09] can see right here because I haven't
[00:05:11] updated the extension, we only have
[00:05:13] Opus. But you would, like I said, go
[00:05:14] over here, search for Cloud Code, and
[00:05:16] then just install that update. But if
[00:05:18] you're doing all those things and you're
[00:05:18] still not seeing the model, just give it
[00:05:20] a couple hours. It'll roll out to you
[00:05:21] eventually. So anyways, let's go take a
[00:05:23] look at the benchmarks. So here's the
[00:05:25] official announcement that Enthropic
[00:05:26] dropped. You know, our notable
[00:05:28] improvements on Opus 4.6 ICS and
[00:05:30] software engineering with particular
[00:05:32] gains on the most difficult tasks. Users
[00:05:35] report being able to hand off their
[00:05:36] hardest coding work, the kind that
[00:05:38] previously needed close supervision to
[00:05:39] Opus 4.7 with confidence. Now, what I
[00:05:42] want you guys to pay attention to here
[00:05:43] as well is that we still have myths
[00:05:44] preview over here. So, it says the model
[00:05:46] has substantially better vision. It's
[00:05:48] also more tasteful and creative when
[00:05:50] completing professional tasks, and it's
[00:05:51] much less capable than their most
[00:05:53] powerful model, Claude Myths. Of course,
[00:05:55] if you guys didn't see anything about
[00:05:56] that, I made a full video. I'll tag that
[00:05:58] one right up here. But it's obviously a
[00:06:00] lot better than Opus 4.6 across things
[00:06:02] like the coding bench or the search
[00:06:04] computer use financial analysis which is
[00:06:06] very interesting and you know like
[00:06:08] vision. So if we look at some other
[00:06:10] things we've got knowledge work we see a
[00:06:12] significant improvement vision we see a
[00:06:13] big improvement document reasoning this
[00:06:15] one's pretty big long context reasoning
[00:06:17] so both obus 4.6 and 4.7 will allow you
[00:06:21] to use it with 1 million token context
[00:06:22] window biomolecular reasoning which is a
[00:06:25] massive jump. it's over double and then
[00:06:27] long-term coherence and coding of
[00:06:29] course. Now, what's interesting and what
[00:06:31] I alluded to earlier is that it seems
[00:06:32] like every complaint now has a directly
[00:06:35] correlating matching fix, which I'm not
[00:06:37] saying that's a bad thing because that's
[00:06:38] really how you should be iterating on a
[00:06:39] product. But some people are definitely
[00:06:41] starting to raise some eyebrows at the
[00:06:42] way that they're just like it's almost
[00:06:44] like they're they're creating holes just
[00:06:45] so they can fill them and look like the
[00:06:47] hero. So, for example, people were
[00:06:48] complaining about shallow thinking with
[00:06:50] 4.7. And now they've introduced their
[00:06:52] new X high effort level, which is
[00:06:54] exclusive to 4.7. We have a complaint
[00:06:56] about task abandonment, but Enthropic
[00:06:58] now says you can hand off your hardest
[00:07:00] coding work with confidence. We have
[00:07:02] ignoring instructions, and now we say
[00:07:04] substantially improved literal adherence
[00:07:05] to instructions. We have hallucinations,
[00:07:08] but now it's apparently able to catch
[00:07:09] its own logical faults during the
[00:07:11] planning phase. Weak vision, that's been
[00:07:12] dramatically improved. And then this
[00:07:14] one's interesting, too. blackmail and
[00:07:15] safety concerns because there was a
[00:07:17] safety concern in 4.6 where essentially
[00:07:20] the model was like blackmailing an
[00:07:21] engineer, but they have explicitly
[00:07:23] addressed this right here, safety and
[00:07:25] alignment. Overall, it shows a similar
[00:07:27] safety profile to Opus 4.6. Our
[00:07:29] evaluations show low rates of concerning
[00:07:31] behavior such as deception, sycopancy,
[00:07:34] and cooperation with misuse. They've
[00:07:36] also kind of worked it in so that it
[00:07:37] can't be used for like cyber security
[00:07:40] type of threats or hacking and other
[00:07:42] sorts of things like that with prompt
[00:07:44] injection. It kind of all loops back
[00:07:45] into that ecosystem of what they have
[00:07:46] talked about with project glasswing.
[00:07:48] Here we have a misaligned behavior
[00:07:51] benchmark. So overall you can see that
[00:07:53] Opus 4.6 has about a 2.75. Mthas preview
[00:07:56] comes in really low and Opus 4.7 kind of
[00:07:58] sits in the middle. Now in this type of
[00:08:00] benchmark you want a lower score. Lower
[00:08:02] is better. So along with this release we
[00:08:04] have some other things coming. We have
[00:08:06] the X high mode which is extra high
[00:08:08] effort like I just talked about. So now
[00:08:09] we have the low, medium, high, max and X
[00:08:13] high. And we also have this new slash
[00:08:15] command coming which is slash ultra
[00:08:17] review which basically just spins up a
[00:08:18] dedicated review session to read through
[00:08:20] changes and flag things. They also give
[00:08:22] us this section about migrating from
[00:08:23] Opus 4.6 to 4.7. It is a direct upgrade
[00:08:26] but apparently there are some things to
[00:08:28] be thinking about with token usage. So
[00:08:30] Opus 4.7 uses an updated tokenizer which
[00:08:33] improves how the model processes text.
[00:08:35] But what that means is the same input
[00:08:37] might actually cost you more just like 1
[00:08:39] to 1.3 times more depending on the type
[00:08:41] of content. Also, Opus 4.7 thinks more
[00:08:44] at higher effort levels, which once
[00:08:46] again could use more tokens. I'm about
[00:08:48] to drop a full video on how to manage
[00:08:50] your tokens even better. So, that'll be
[00:08:51] out in like a day or so, and definitely
[00:08:53] want to check that one out. I'll tag
[00:08:55] that one up here when that comes out.
[00:08:56] So, there's a bunch of benchmarks,
[00:08:57] right? And that's the tough thing is you
[00:08:59] see all of this noise, you see all these
[00:09:00] benchmarks, and everything looks like
[00:09:02] it's better, but you don't truly know
[00:09:03] until you actually get your hands dirty
[00:09:05] and play with it. They even released
[00:09:06] this um spec card or system card about
[00:09:09] Cloud Opus 4.7. It's 232 pages. And if
[00:09:12] we go down here, you can see that this
[00:09:13] thing is basically chalk full of
[00:09:15] experiments and benchmarks and just
[00:09:17] comparisons between, you know, Mythus,
[00:09:19] Sonnet, Opus, and Opus. So, this is
[00:09:22] going to be really interesting to dive
[00:09:23] into. I read through a lot of this, but
[00:09:25] not going to break it all down. I think
[00:09:26] it would be insanely boring for most of
[00:09:28] the people watching this anyways. But
[00:09:30] yeah, if you do want to check this out,
[00:09:32] you can find the link to this on this
[00:09:34] main release page from Anthropic. Okay,
[00:09:36] so is 4.7 actually new? I think that it
[00:09:40] is a new model and we're going to get in
[00:09:41] here and I'm going to show you some
[00:09:42] examples of me playing around with it.
[00:09:44] But the X higheffort level didn't exist.
[00:09:47] The vision gains are actual differences
[00:09:50] in the model itself, structural changes,
[00:09:53] not just like, you know, turning on
[00:09:55] effort or turning off effort. There was
[00:09:56] also a noticeable jump in the SWBench
[00:09:58] Pro, which is obviously pretty good as
[00:10:00] well. The updated tokenizer, once again,
[00:10:02] I'm not saying that how good or bad that
[00:10:04] is. I haven't had enough time to fully
[00:10:05] test, but it will probably be a little
[00:10:07] bit more expensive. And then we also saw
[00:10:08] a third party benchmark which was 3x
[00:10:11] production task resolution on Rakutin.
[00:10:13] Now real quick, something I want you
[00:10:14] guys to think about before we get into
[00:10:16] some of the other experiment stuff is
[00:10:19] the desktop app launch which they had
[00:10:21] basically said, hey, we've been working
[00:10:23] on this for a long time. We're very
[00:10:24] excited. Most of our internal engineers
[00:10:25] are using this now instead of their IDs.
[00:10:27] And I thought it was awesome, right?
[00:10:29] Like I switched into it yesterday. I
[00:10:31] only used this instead of VS Code cuz I
[00:10:33] wanted to play around with it. And
[00:10:34] there's a lot of things I really like.
[00:10:36] you know, you can see all of your
[00:10:37] different sessions here. You can also
[00:10:39] manage your projects and have multiple
[00:10:40] going at the same time. You can see when
[00:10:42] they're done. You can see when they're
[00:10:43] waiting on you. And I like a lot of the
[00:10:45] idea of what they're doing. Now,
[00:10:46] obviously, a lot of this has been taken
[00:10:47] from like the Codeex app or other Vibe
[00:10:50] Coding, um, Aenta Coding apps out there.
[00:10:52] And that's not anything to complain
[00:10:53] about. I think that's just the way the
[00:10:54] world works. But anyways, I can come
[00:10:56] into a session and I can see things over
[00:10:57] here like a preview if you're working in
[00:10:59] a local host. You could also pull up a
[00:11:01] terminal right here. So, you could talk
[00:11:02] to Claude in the terminal. Um, that way
[00:11:04] you get some of the extra functionality
[00:11:05] too. You could also look at your tasks
[00:11:08] and you could look at the plan. So
[00:11:09] there's ways that you can kind of
[00:11:10] customize the view which I think is
[00:11:12] really cool. And you can also have
[00:11:13] different split views open. So you can
[00:11:15] have multiple different sessions and
[00:11:17] even multiple different projects. So um,
[00:11:19] that's really cool. I also like right
[00:11:20] here if I just kind of close out of this
[00:11:22] one, you can right from in here see your
[00:11:25] context window and your session. So like
[00:11:28] here is my 5 hour limit. I can see when
[00:11:30] that resets in 10 minutes. So I've got,
[00:11:32] you know, left to play with. I can see
[00:11:33] my models and one of the things I talk
[00:11:35] about is like if you're running through
[00:11:37] your limit, why don't you just watch it
[00:11:38] more often? So, typically what that
[00:11:40] meant is have something pulled up, but
[00:11:41] now you can literally just from here
[00:11:43] click into it and see, okay, cool, I've
[00:11:44] got that much left. So, there's a lot of
[00:11:46] other features here that are really
[00:11:47] good. Obviously, now with the routines
[00:11:49] and stuff, it's nice to be able to work
[00:11:50] out of this app. But there are a lot of
[00:11:52] things that are really poorly designed
[00:11:54] as well. And a developer named Theo um
[00:11:57] he basically found like 40 plus bugs in
[00:11:59] just 1 hour. He was playing around with
[00:12:00] it and there were lots of things like
[00:12:02] buttons weren't working, things were
[00:12:04] snapping weird. Um, you were like just
[00:12:06] the the layout wasn't as intuitive and
[00:12:08] there was just a lot of little bugs
[00:12:10] essentially. Like for example, if you do
[00:12:11] your voice input, it would put voice
[00:12:13] into every single text box that's
[00:12:15] visible on the screen. Just little
[00:12:16] things like that. Um, and what's
[00:12:18] interesting is they are one of the
[00:12:20] biggest AI companies in the world and
[00:12:22] honestly one of the biggest tech
[00:12:23] companies in the world, but they're
[00:12:24] shipping things so fast and they're
[00:12:26] having these issues where did they even
[00:12:28] do QA? And if their team had really been
[00:12:30] using this for so long internally,
[00:12:33] wouldn't they have found all these bugs?
[00:12:34] And if they have Mythus, which is
[00:12:36] supposed to be so dangerous and so good
[00:12:38] that it can't even be released,
[00:12:39] shouldn't Myths have been able to like
[00:12:41] make this better? Because it's not a
[00:12:43] matter of the model not being able to
[00:12:45] execute the code properly. It's an issue
[00:12:47] of the model not being actually smart
[00:12:49] enough to go QA properly because as Theo
[00:12:51] pointed out, a lot of the bugs he found,
[00:12:53] it would be a oneprompt fix, right? But
[00:12:56] no one was able to find that bug. So
[00:12:59] there's questions about, you know, how
[00:13:00] much are they actually using it or like
[00:13:01] what actually went on because they're
[00:13:03] shipping at the speed of a startup, a
[00:13:04] tech startup who that just raised a
[00:13:06] bunch of capital. Okay, so I had to get
[00:13:08] that off my chest. Let's move on to act
[00:13:09] three, the verdict. So I just ran two
[00:13:11] experiments here that I wanted to show
[00:13:12] you guys and I did this on the web app
[00:13:15] with 4.6 extended and 4.7. So the first
[00:13:18] one, let me show you guys this one. What
[00:13:20] I did is I dropped in this chart. So,
[00:13:22] this is a meta financial um stock chart,
[00:13:25] and you can see that I just said, "Hey,
[00:13:27] give me your best three sentence
[00:13:28] description of what's going on here and
[00:13:30] what I need to know about this in order
[00:13:31] to make money, make or save money." So,
[00:13:33] I'm not going to read both of these
[00:13:34] answers, but this is what 4.6 extended
[00:13:37] thinking gave me. And this is what 4.7
[00:13:40] with no adaptive thinking gave me here.
[00:13:42] And so, you can pause that and read if
[00:13:44] you want, but here's the quick breakdown
[00:13:45] that I kind of came up with. the tone. I
[00:13:48] liked the way that 4.7 spoke a little
[00:13:50] bit better. For the actual framing, I
[00:13:52] thought that 4.7 explained why it kind
[00:13:55] of justified things a little bit more
[00:13:56] and it felt more like it had financial
[00:13:58] subject matter expertise, which is one
[00:14:00] of the, you know, benchmarks that we saw
[00:14:02] from Enthropic itself. We had more
[00:14:05] actionable specifics with 4.7. The
[00:14:07] structure over here was a little bit
[00:14:08] better and they both obviously had some
[00:14:10] weaknesses, but that's when I said,
[00:14:11] "Hey, give me a three sentence
[00:14:12] description." Um, I just wanted to keep
[00:14:14] things a little bit more controlled. So,
[00:14:16] I definitely did feel like I liked 4.7
[00:14:18] here better. And then I did another one
[00:14:20] where I gave them this exact same prompt
[00:14:22] about, you know, I'm building a SAS. I
[00:14:24] need some help with, you know, figuring
[00:14:25] out my 12-month model. And here's what
[00:14:28] 4.7 extended gave me. It gave me an
[00:14:30] interactive dashboard where I can see my
[00:14:32] stats. I can click on different
[00:14:33] scenarios. And then I can also drag the
[00:14:35] slider along here with our starting
[00:14:37] trial pool, with our new trials a month,
[00:14:39] with our, you know, paid and with our
[00:14:41] churn, and with our pricing tiers. So, I
[00:14:43] thought this was pretty cool. It's very
[00:14:44] interactive, but um yeah, it gave me
[00:14:47] some insights as well. So, that was
[00:14:49] pretty impressive, right? This took a
[00:14:50] lot longer than the 4.7 and I think it's
[00:14:52] just because it was using extended, but
[00:14:54] with 4.7 here, same exact prompt, and it
[00:14:57] came back, it did a lot of thinking. It
[00:14:58] made some corrections on the math, but
[00:14:59] it was able to fix those, made the right
[00:15:01] formulas, and then what it did is it
[00:15:03] gave me more of a deliverable. It gave
[00:15:05] me an actual Excel sheet with multiple
[00:15:07] different tabs. You can see here we have
[00:15:08] more of just a base summary. You can see
[00:15:10] then we have assumptions. we have base
[00:15:12] case with all these different scenarios
[00:15:14] and it's not letting me scroll because
[00:15:16] we're in this web browser version. Um,
[00:15:18] and then it gave me churn 3% and also if
[00:15:21] we killed the $29 per month tier. The
[00:15:24] quick breakdown I had of this um is that
[00:15:27] I liked the actual deliverable better
[00:15:28] from 4.6 because it was more interactive
[00:15:31] and it gave me a bit more of a a
[00:15:33] polished feel. Um, 4.7 had some errors,
[00:15:35] but it was able to catch them. But I
[00:15:37] think from like a business perspective,
[00:15:39] you probably want more of that Excel
[00:15:41] deliverable. And of course, if I
[00:15:43] prompted 4.6 to do that, it could have
[00:15:44] done it and it may have been better, but
[00:15:46] once again, I was just trying to see
[00:15:47] what would happen if I gave these two
[00:15:49] different models kind of a vague prompt
[00:15:51] and just kind of seeing and comparing
[00:15:52] the way that they come back. So anyways,
[00:15:55] um the real test will be of course when
[00:15:56] you hop into something like Cloud Code
[00:15:57] and you really start using it for the
[00:15:59] actual workflows and the the the
[00:16:01] processes and projects that you are
[00:16:02] using Cloud Code for either way. And
[00:16:04] ultimately, it's not something where I
[00:16:06] could just use it for an hour and give
[00:16:07] you guys some sort of conclusion. So,
[00:16:08] I'm going to be playing with this
[00:16:09] obviously all day, all week. And if I
[00:16:12] have any other crazy insights, I will be
[00:16:14] sure to update you all. But I do think
[00:16:16] that the degradation was real of 4.6 and
[00:16:20] whether that was intentional throttling
[00:16:21] or if it was just kind of on their side
[00:16:23] trying to optimize cost because 200
[00:16:25] bucks a month is honestly a steal if
[00:16:27] you're able to use your sessions all the
[00:16:29] way through. But ultimately, whatever
[00:16:31] the motivation was, it resulted in a
[00:16:33] worse product at the same price. And
[00:16:35] then, of course, we have 4.7, which
[00:16:37] looks a lot better on paper. And we need
[00:16:39] to actually see if it is. We have to
[00:16:42] take the benchmarks with a grain of salt
[00:16:43] and try things out for ourselves. But
[00:16:45] hopefully this video today gave you some
[00:16:47] insight as far as like what's been
[00:16:48] happening, where we're at, and a good
[00:16:50] mindset as far as like actually trying
[00:16:52] this stuff out for yourself. So, that is
[00:16:54] pretty much my bottom line. 4.7 might be
[00:16:56] the best AI model ever released up to
[00:16:58] this point. It might also be the cure to
[00:17:00] their own disease that Anthropic caused
[00:17:02] themsel. So either way, you just got to
[00:17:04] test it out. So that's going to do it
[00:17:05] for this one. I hope you guys enjoyed.
[00:17:06] If you learned something new or you did
[00:17:08] enjoy, please give it a like. Helps me
[00:17:10] out a ton. And I'll see you on the next
[00:17:11] one. Thanks everyone.