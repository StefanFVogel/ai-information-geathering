---
author: '[[Nate Herk | AI Automation]]'
channel_id: UC2ojq-nuP8ceeHqiroeKhBA
date: '2026-04-17'
duration: 1995
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- '[ai]'
title: I Turned Claude Opus 4.7 Into a 24/7 Trader
type: inbox
url: https://www.youtube.com/watch?v=6MC1XqZSltw&t=80s
---

## Summary

[[Nate Herk]] zeigt, wie er seinen OpenClaw-Trading-Agent aus dem vorherigen 30-Tage-Duell auf [[Opus 4.7]] umstellt und dabei komplett auf [[Claude Code]] + [[Claude Code Routines]] setzt — ohne Hermes oder [[OpenClaw]]-Framework. Motivation: Opus 4.7 liefert laut Benchmarks ~4% mehr in Agentic Financial Analysis und wurde explizit für "full-throttle agentic work, judgment over ambiguity, self-verifying outputs" designt — ideale Eigenschaften für 24/7-Trading-Routinen.

**Architektur:**
- **Scheduler:** Claude Code Routines mit vier Cron-Events (Pre-Market, Market Open, Midday, Close)
- **Model:** Opus 4.7
- **Skills:** selbstgebaut für Research, Trade-Entscheidungen, Order-Placement, Logging
- **Brokerage:** [[Alpaca]] (API-Endpoints statt MCP-Server)
- **Research:** [[Perplexity]] API (alternativ native Web-Fetch/Search)
- **Notifications:** [[ClickUp]] für tägliches End-of-Day-Summary (statt Telegram)

**Workflow pro Cron-Slot:**
1. Research Markt und relevante News
2. Platziere Trades via Alpaca
3. Journaling — Agent schreibt Context in File, um daraus zu lernen
4. Am Tagesende: Summary an ClickUp

**Ziel:** S&P schlagen. Im vorherigen 30-Tage-Experiment schlug der Bot den S&P um 8% — dieses Setup ist die Weiterentwicklung. Basis ist das vorherige OpenClaw-Duell mit [[Samin Yasar]].

**Kernaussage:** Die Kombination aus Opus 4.7 + Routines macht 24/7-Agents praktikabel, weil das Modell selbst-verifizierend arbeitet. Der Tech-Stack ist modular und austauschbar (Alpaca ↔ andere Broker, Perplexity ↔ Web-Search, ClickUp ↔ Slack/Telegram).


Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=opus-4-7-trader
All my FREE resources: https://www.skool.com/ai-automation-society/about?el=opus-4-7-trader

---

## Transcript

[00:00:00] So, Claude Opus 4.6 is finally here. And
[00:00:02] it got me thinking because as I was
[00:00:03] scrolling down and I started looking at
[00:00:04] the benchmarks, I noticed right here we
[00:00:06] have Agentic Financial Analysis and we
[00:00:08] have about a 4% jump from Opus 4.6. And
[00:00:11] about a week ago, I dropped this video
[00:00:13] where me and Salmon traded stocks for 30
[00:00:16] days with our OpenClaw agents and my
[00:00:18] OpenClaw agent was set up with Opus 4.6
[00:00:21] and I was able to beat the S&P by about
[00:00:23] 8%. As you can see right here, this
[00:00:24] green line is my chart and this gray
[00:00:27] line is the S&P. So, if you guys want to
[00:00:28] check out this full video, I will link
[00:00:29] that right up here. So, after this
[00:00:31] challenge, I wanted to keep my agent
[00:00:32] running to see if it could keep beating
[00:00:33] the S&P, but now I want to upgrade it to
[00:00:36] 4.7 instead of 4.6. So, that's exactly
[00:00:38] what I want to cover with you guys
[00:00:39] today. How do we build a 24/7 AI trading
[00:00:42] agent with Opus 4.6 inside of Claude
[00:00:45] Code? We're not even going to touch Open
[00:00:46] Claw or Hermes agent. We're going to
[00:00:48] just do this with Claude Code. And this
[00:00:49] is all going to be thanks to another
[00:00:51] feature that we just got from the
[00:00:52] Enthropic team called routines. If you
[00:00:54] don't know what that is, I'm going to
[00:00:55] break it down in this video, but I also
[00:00:56] made a full one if you want to check
[00:00:57] that out. Also, right up here. So,
[00:00:58] basically, this is the unlock 4.7 plus
[00:01:01] routines means you can have a 24/7 AI
[00:01:03] agent. And 4.7 was built for full
[00:01:06] throttle agentic work, judgment over
[00:01:07] ambiguity, and self-verifying outputs.
[00:01:10] So, it's perfect for these types of
[00:01:11] routines. And that's how I'm going to
[00:01:12] set up my 247 trading agent with Cloud
[00:01:15] Code routines. So, if you follow along
[00:01:17] with this video, you'll be able to
[00:01:18] pretty much duplicate my exact setup and
[00:01:20] have yourself a working agent and start
[00:01:23] trading with it. So, let's go ahead and
[00:01:25] get started. What are we building? We're
[00:01:27] going to create a cloud code project
[00:01:28] that runs on a schedule, something like
[00:01:30] a pre-market cron, a market open, a
[00:01:32] midday, and a close. It's going to
[00:01:34] research the market. It's going to place
[00:01:35] trades via the alpaca API. It's going to
[00:01:38] journal and make sure that it's writing
[00:01:40] context into the file so it can learn.
[00:01:42] And then it's going to send me every
[00:01:43] day, every day of the week, an end of
[00:01:44] day summary to my ClickUp. The goal
[00:01:47] obviously is just to beat the S&P. We're
[00:01:48] not looking to do any crazy crypto or
[00:01:50] crazy day trading stuff. I'm just kind
[00:01:52] of doing this as a fun long-term
[00:01:54] investment. Just beat the S&P challenge.
[00:01:56] Like I said, in my first 30 days, I gave
[00:01:58] Opus $10,000 and we were able to beat
[00:02:00] the S&P by about 8%, which is really
[00:02:02] good, especially in such a short amount
[00:02:04] of time. So, what is the tech stack?
[00:02:06] We're going to be using Cloud Code
[00:02:08] routines. That's kind of our scheduler.
[00:02:09] For the AI model, we're going to use
[00:02:10] Opus 4.7. For the skills, we're going to
[00:02:13] be using just kind of like building our
[00:02:15] own as we go. It'll be stuff like how
[00:02:16] the agent does research or how it makes
[00:02:18] decisions or how it places trades or,
[00:02:20] you know, makes logs, things like that.
[00:02:22] We're going to use the Alpaca API as our
[00:02:24] brokerage. We're going to use the
[00:02:25] Perplexity API for research. You could
[00:02:27] also just use the native web fetch and
[00:02:29] web search, but I'm going to use
[00:02:30] Perplexity here. And then I'm going to
[00:02:32] get my notifications in ClickUp this
[00:02:34] time rather than Telegram just cuz I
[00:02:36] live in ClickUp a lot more. So obviously
[00:02:37] some of these things can be
[00:02:38] interchangeable for you, but if you want
[00:02:40] to just copy my exact setup in this
[00:02:41] video, then feel free. Okay, so how to
[00:02:43] get started with these different tools
[00:02:44] that we need for this video. The first
[00:02:46] one is going to be alpaca. So go to
[00:02:48] alpaca.markets. You can see up at the
[00:02:50] top we even see want to trade using AI.
[00:02:52] We launched an alpaca's MCP server to
[00:02:54] help you trade with natural language. So
[00:02:55] you could use that. I'm just using the
[00:02:56] endpoints. I honestly like to use
[00:02:58] endpoints a lot more. But anyways,
[00:03:00] you're going to sign up right here and
[00:03:01] you'll click on trading API. Now once
[00:03:03] you get in there, you will have
[00:03:04] basically a paper trading account. And
[00:03:06] right here, you can see I've got a paper
[00:03:07] trading account with 100K. You could
[00:03:09] also open up a new account right here.
[00:03:10] And that's how you could put real money
[00:03:12] in. You might, like I said, though, have
[00:03:13] to just verify your account, which could
[00:03:15] take a couple days. And then they're
[00:03:17] both the same as far as the credentials.
[00:03:18] You basically scroll down and on the
[00:03:20] right hand side, you have your API keys
[00:03:21] right here. You get an endpoint and you
[00:03:23] get a key, but you also need like a
[00:03:25] secret key. So you have like a secret
[00:03:26] key and then you need like an ID. So
[00:03:27] you'd hit regenerate, generate new keys,
[00:03:30] and this is where you get your key and
[00:03:31] your secret. And once you copy and paste
[00:03:35] this, just make sure to save it because
[00:03:36] then it's going to go away and you'll
[00:03:38] only be able to see the key. But you
[00:03:39] need both of them. Next up, I have
[00:03:41] ClickUp. This is where I want to get my
[00:03:42] notifications. You don't have to use
[00:03:43] ClickUp. You can use Slack. You could
[00:03:45] use, you know, whatever, Telegram,
[00:03:47] WhatsApp. I would go up here and go to
[00:03:49] my settings. And then I scroll down and
[00:03:51] find ClickUp API. And then I would just
[00:03:52] copy this token right here. And then
[00:03:54] similarly with Plexity, I would go down
[00:03:56] here and I would click on all settings,
[00:03:59] I think. And then in here, I can see API
[00:04:01] platform. And this is where I would be
[00:04:02] able to go find my actual API key. If I
[00:04:05] went down to right here, API keys, I can
[00:04:07] make a new one or copy an old one. But
[00:04:08] basically, the way it works is every
[00:04:10] platform has typically API keys. You
[00:04:12] just have to find them in the settings
[00:04:13] somewhere. If you can't find them, just
[00:04:14] do a quick perplexity or Google search
[00:04:16] or even ask cloud code and it should be
[00:04:18] able to help you get to your API keys.
[00:04:20] And now that you know how to get these
[00:04:21] keys, just hold on to them. We're going
[00:04:22] to actually plug them in later in the
[00:04:24] video. And then the final piece of the
[00:04:25] puzzle is going to be the cloud desktop
[00:04:26] app. You can see here you can have cloud
[00:04:28] chat, you can have cloud co-work, or you
[00:04:30] can be in cloud code. And this is where
[00:04:32] we're going to set up these actual
[00:04:34] routines where now if I go to my
[00:04:35] calendar, you can see every single day
[00:04:37] I've got bull, which is my trading
[00:04:39] agent, waking up at 6:00, 8:30, um,
[00:04:42] noon, 3 p.m. And then on certain days,
[00:04:44] like on Fridays, he's doing a weekly
[00:04:46] review. So, this is the way I currently
[00:04:47] have mine set up. And we're able to
[00:04:49] manage everything right from here inside
[00:04:50] of the Claude Desktop app because of
[00:04:52] this whole routine feature. So, all you
[00:04:54] need to do to use the claw desktop app
[00:04:56] is just type in cloud desktop app
[00:04:58] download and you should be able to
[00:04:59] install it right here. You go to the
[00:05:00] downloads page and then you just have to
[00:05:02] choose the claw desktop for your
[00:05:04] operating system. And then the only
[00:05:06] other thing you need to do is make sure
[00:05:07] that you are on an actual subscription.
[00:05:09] So, it has to be a paid either 20 bucks
[00:05:11] a month plan or the max plans. Now, in
[00:05:13] this video, you might also see me use
[00:05:15] cloud code inside of something that
[00:05:16] looks like this, which is the VS Code
[00:05:18] IDE, and then we use Cloud Code
[00:05:20] extension inside of it. It's not
[00:05:21] mandatory, but that is where I typically
[00:05:24] prefer to use cloud code because I can
[00:05:25] see all of my files over here. So, if
[00:05:27] you want to do that, just type in VS
[00:05:28] Code in your browser. Open this up. It's
[00:05:30] completely free to download and then go
[00:05:31] ahead and download it and connect your
[00:05:33] Cloud Code account. So, that is pretty
[00:05:35] much the tech stack that we're going to
[00:05:36] be using today to get all of this set
[00:05:38] up. And let's get back to the video.
[00:05:40] Okay, so before we get into the actual
[00:05:42] step-by-step kind of build, we are going
[00:05:44] to need to talk about the mental model.
[00:05:46] So, understand this before you write
[00:05:48] anything. The trading strategy is a
[00:05:50] piece of the work, but the memory
[00:05:51] architecture that you're going to use is
[00:05:53] going to be huge. So, every time a
[00:05:55] routine fires at 7 a.m., cloud code
[00:05:58] basically wakes up essentially
[00:05:59] stateless. It doesn't really know
[00:06:00] anything. So, how do you make a
[00:06:01] stateless agent act disciplined and
[00:06:03] remember rules and learn over time? You
[00:06:05] do that with files and with context. So
[00:06:08] every routine basically wakes up, reads
[00:06:11] files, does the job, and then writes
[00:06:14] back any important lessons or anything
[00:06:16] like that the next agent when it wakes
[00:06:18] up needs to know. It just writes that
[00:06:19] down. And that's kind of at a very high
[00:06:21] level the type of framework that we're
[00:06:23] going to be using here. So the final
[00:06:25] thing I wanted to talk about before we
[00:06:26] get into this is the context budget. So
[00:06:29] treat tokens like money. Obviously,
[00:06:30] every file that you ask the agent to
[00:06:32] read, it's going to cost you. Each
[00:06:33] routine gets about 200,000 tokens to
[00:06:35] work with. I mean we do have the a
[00:06:37] million token context window models now
[00:06:38] but I don't really like to think of it
[00:06:40] like I have a million tokens to play
[00:06:41] with because context rot. So system
[00:06:44] instructions will take some up strategy
[00:06:46] files, your trade log, your API, your
[00:06:48] research. Every run is going to take a
[00:06:50] different amount of tokens. But just
[00:06:51] keep that in mind. And the reason here
[00:06:52] that we're using, if I go back to the
[00:06:54] stack, cloud code instead of just using
[00:06:56] something like, you know, the agents SDK
[00:06:58] or I mean I guess that could work, but
[00:07:00] rather than just using like a standard
[00:07:01] automation is because if we do this with
[00:07:04] routines, we basically get the full
[00:07:07] autonomy of us working with cloud code
[00:07:10] manually because it goes through that
[00:07:11] whole agent caress loop of figuring
[00:07:13] things out. And especially with Opus
[00:07:14] 4.7, it's apparently going to be really,
[00:07:16] really good. Whereas, if you just had
[00:07:18] like an automation that would do
[00:07:20] research and then, you know, make a
[00:07:21] trade, you're not getting that super
[00:07:23] variability that you probably want with
[00:07:26] something that could be very volatile
[00:07:28] like trading. All right, so now that we
[00:07:29] got all of that stuff out of the way,
[00:07:31] let's get into the strategy. So, step
[00:07:33] one, think of this like you're teaching
[00:07:35] a kid to ride a bike. You have to
[00:07:37] explain how to balance before you go.
[00:07:40] You have to explain to the kid that he's
[00:07:41] going to steer with his hands and he's
[00:07:43] going to pedal with his feet. And even
[00:07:45] once you put him on the bike, you're not
[00:07:47] just going to let him go. You're going
[00:07:48] to hold the handlebars. You're going to
[00:07:49] put your hand on his back and you're
[00:07:50] going to walk with him until he gets a
[00:07:52] little more comfortable. And then slowly
[00:07:53] you might take off. You know, you might
[00:07:55] stop steering, but you might just run
[00:07:56] behind him. And then slowly you'll put
[00:07:58] on some training wheels. And like you
[00:07:59] just keep bumping it up in phases. You
[00:08:01] can't expect to just throw a kid on a
[00:08:02] bike and it's instantly going to be
[00:08:04] magic. So maybe you want to start with
[00:08:06] paper trading. This is obviously not
[00:08:08] financial advice and I'm not, you know,
[00:08:09] recommending that you go put all of your
[00:08:10] life savings in here and expect to make
[00:08:12] money and then get mad at me. This is an
[00:08:14] experiment for me and I'm trying to show
[00:08:16] you guys what's possible. So just keep
[00:08:17] that in mind. Start with paper trading
[00:08:19] first if you're not comfortable. But
[00:08:20] anyways, the idea is you need a
[00:08:22] strategy. So for me, what I'm going to
[00:08:24] do is I'm basically going to extract all
[00:08:26] of the strategy that we've been using
[00:08:27] from my openclaw agent and I'm just
[00:08:30] going to say, "Hey, let's take this over
[00:08:31] to Claude Code." So for me, it's a
[00:08:32] little easier. But for you, if you
[00:08:34] actually are like a manual trader and
[00:08:35] every day you think about things and you
[00:08:37] do research and you place trades or you
[00:08:39] sell things, then just write down your
[00:08:40] strategy. How often are you checking the
[00:08:42] news? What are the signals that make you
[00:08:44] realize I'm going to buy this or I'm
[00:08:45] going to sell this? As much of your gut
[00:08:47] intuition and your routine about trading
[00:08:50] that you can get into this cloud code
[00:08:51] project, the better. And then over time,
[00:08:53] you're going to help it learn from its
[00:08:55] mistakes. You're going to iterate and
[00:08:57] it's going to get better and better
[00:08:58] every time you use it. But if you're
[00:08:59] starting completely fresh, which in my
[00:09:02] case of the open claw trading challenge,
[00:09:04] I literally just said, "Hey, I'm doing a
[00:09:07] 30-day challenge. I'm trying to compete
[00:09:08] against my friend Salmon. Go do
[00:09:10] research. Spin up a team of sub agents.
[00:09:12] you're my wealth adviser. Try to beat
[00:09:13] the S&P. Figure out the best plan
[00:09:15] possible. And that's like genuinely all
[00:09:17] that I said to it, which I think is
[00:09:18] pretty cool. And it went off and it did
[00:09:20] a bunch of research. It figured out a
[00:09:21] strategy for me and then for the next 30
[00:09:23] days, it just did that. And I barely had
[00:09:24] to touch it at all. So, if you want to
[00:09:26] start off by playing around with some
[00:09:28] research like that, then certainly do
[00:09:29] that. But if you guys remember at the
[00:09:30] beginning of this video, I kind of
[00:09:32] alluded to this benchmark here. So, in
[00:09:35] the official release, and by the way, I
[00:09:36] just dropped a full video on this new
[00:09:38] release. I'll tag that up here. So in
[00:09:40] the official release of claude obus 4.7
[00:09:42] they always drop the benchmarks and they
[00:09:43] compare it to other models that are kind
[00:09:45] of leading in the industry as well and
[00:09:47] so this is the one I wanted to talk
[00:09:48] about in this case we have aentic
[00:09:50] financial analysis 64.4%.
[00:09:53] We also have stuff like graduate level
[00:09:55] reasoning and you know just the ability
[00:09:56] to think really well um agentic search
[00:09:59] actually is worse than opus 4.6 which is
[00:10:01] interesting but yeah agentic financial
[00:10:03] analysis. So what does that actually
[00:10:04] mean? This basically means that it is
[00:10:06] really good at analyzing a company, but
[00:10:08] it's not basically a signal or a
[00:10:11] benchmark for how good this model is at
[00:10:13] trading and specifically day trading.
[00:10:15] Like this doesn't mean that it's going
[00:10:16] to be able to look at like a technical
[00:10:18] analysis and look at the candlesticks
[00:10:19] and the MACD and figure out the exact
[00:10:21] best moment to buy and then the exact
[00:10:23] moment to sell. I'm not going to try to
[00:10:24] day trade with these agents. I just
[00:10:26] don't know enough about it to do it. But
[00:10:28] that's not what this metric is saying.
[00:10:29] This benchmark rewards models that can
[00:10:31] digest fillings and write coherent
[00:10:33] fundamentals driven thesises or thesis,
[00:10:36] I guess. And that maps to long-term or
[00:10:38] swing or fundamentals driven strategies,
[00:10:40] not day trading. So that's why once
[00:10:42] again, we're just going to be trying to
[00:10:43] beat the S&P here. Okay, so that is the
[00:10:45] overall strategy. Let's talk about the
[00:10:47] scaffold. So what you need to do to spin
[00:10:49] up the Cloud Code project in about 60
[00:10:51] seconds is you're going to open up a new
[00:10:53] folder and we're going to open up Cloud
[00:10:54] Code. So let me hop over to my project
[00:10:56] right here. This is a new folder. It's
[00:10:58] called trading I think trading routine.
[00:11:01] This is basically just a settings file.
[00:11:03] There's hardly anything in there. The
[00:11:04] cloudmd is blank and then we have a
[00:11:06] readme just because I turned this into a
[00:11:08] GitHub repo so I can pull it into a
[00:11:09] routine later. If you haven't done that
[00:11:11] yet, it's fine. We'll talk about that in
[00:11:13] a sec. The reason why we're starting
[00:11:14] here in VS Code is because I want to get
[00:11:16] started in a place where I can see all
[00:11:18] of my files on this left-hand side.
[00:11:20] Because if you're in the desktop app,
[00:11:21] which we will move over to here later,
[00:11:23] you don't get to see all your files open
[00:11:24] on the lefth hand side. On the lefth
[00:11:26] hand side, you see your routines and
[00:11:27] your other sessions, which is great, but
[00:11:29] when we're first getting set up, I like
[00:11:31] to be able to see everything in one
[00:11:32] spot. So, we're going to start here in
[00:11:33] the VS Code um either terminal or the
[00:11:36] cloud code extension. So, let me show
[00:11:38] you guys what I did. This is my Telegram
[00:11:40] chat with Bull, my trading bot, and I
[00:11:42] said, "Hey, I want to completely migrate
[00:11:44] you to different AI agent setup. I need
[00:11:46] you to break down the strategy, the cron
[00:11:48] jobs, what are you looking for when
[00:11:49] you're doing your research, what type of
[00:11:50] sub agents do you have, what are the
[00:11:52] different signals, give me the full
[00:11:54] breakdown, all of your learnings. And so
[00:11:56] it gave me all this stuff. And so what
[00:11:58] I'm going to do is I'm just going to
[00:11:59] basically migrate over this strategy
[00:12:01] into my cloud code project. You can see
[00:12:03] we have all of these cell signals. We
[00:12:05] have all of these key learnings and
[00:12:07] these kind of main frameworks. And we
[00:12:09] have our current portfolio. Real quick
[00:12:10] guys, when it comes time for you to get
[00:12:12] set up, I have this free resource for
[00:12:14] you. It's a 13-page PDF and I'm assuming
[00:12:17] if you dropped this thing into cloud
[00:12:19] code and then started to brainstorm with
[00:12:20] it, it would help you out a lot as far
[00:12:22] as the infrastructure and the folder
[00:12:24] structure and the way you want to get
[00:12:25] things set up and the way you want to
[00:12:26] create your routines and things like
[00:12:27] that. So, it should be very helpful.
[00:12:29] This you can download for completely
[00:12:30] free in my free school community. The
[00:12:32] link for that is down in the
[00:12:33] description. Once you get in there, just
[00:12:34] head over to the classroom, click on
[00:12:36] YouTube resources, and you'll be able to
[00:12:37] find it right in there. So, let's get
[00:12:39] back to the video. So, if I pull that up
[00:12:40] real quick, you can see here's today. We
[00:12:42] had a bit of a a jump and then we came
[00:12:44] back down today. Here is the past month.
[00:12:46] So, this is where we were with the um
[00:12:48] OpenClaw agent, but you guys are going
[00:12:50] to want to go to Alpaca and make an
[00:12:51] account, especially if you want to put
[00:12:52] real money in. You might have to take a
[00:12:54] few days for your account to get
[00:12:55] approved. So, head over there and get an
[00:12:57] account. Then, I also told it to give me
[00:12:59] a technical cheat sheet as far as like
[00:13:00] the different API endpoints it uses and
[00:13:02] how it makes those requests. as you can
[00:13:04] see, just because it already has all
[00:13:05] this knowledge. So why waste time trying
[00:13:07] to train a new agent if we could just
[00:13:09] migrate over all of these memories and
[00:13:11] knowledge to this new agent. And then at
[00:13:14] the end of that, it even gave me an
[00:13:15] export of all of these important files
[00:13:17] like the agent instructions, the trading
[00:13:18] strategy, the trade log, the research
[00:13:20] log, the weekly review. And I'm just
[00:13:22] basically going to migrate all this
[00:13:23] over. So let me show you what that's
[00:13:24] going to look like. So you can see that
[00:13:26] it gave me this zip file of all of those
[00:13:29] seven files, and I'm just basically
[00:13:30] going to extract those into this project
[00:13:32] right here. So, I'm choosing the trading
[00:13:34] routine project. Select folder and then
[00:13:36] extract. And we should see all those
[00:13:38] files just popped up right over here on
[00:13:39] this lefth hand side. Now, what I'm
[00:13:40] going to do is just talk to my claude.
[00:13:42] I'm going to switch over here to plan
[00:13:43] mode. And I'm just going to start
[00:13:44] talking. All right. So, I am creating
[00:13:47] you as a 24/7 AI agent trade bot for me.
[00:13:50] I had a project set up with OpenClaw and
[00:13:54] we were trading, you know, $10,000 using
[00:13:56] Alpaca for the past 30 days and we were
[00:13:58] doing pretty well, but now I want to
[00:14:00] move it over here so we can set you up
[00:14:02] as a cloud code routine. So, I just
[00:14:04] dropped in a ton of context for you.
[00:14:05] There's a ton of files in this project.
[00:14:07] Um, if you want to just take a second to
[00:14:09] get sort of like acclimated to what I
[00:14:12] dropped in there. There's going to be a
[00:14:13] lot of information, but basically that's
[00:14:15] like all of the knowledge and all of the
[00:14:17] strategies and all of the signals that
[00:14:18] our OpenClaw agent had and how it was
[00:14:21] able to be successful. And I just want
[00:14:23] to migrate that over here to you so that
[00:14:25] we're not losing any of our knowledge.
[00:14:27] I'm also going to paste in some of the
[00:14:28] key things that it told me that you
[00:14:30] should make sure to know. So, I'm going
[00:14:31] to drop in that stuff right below. Now,
[00:14:34] some of this stuff you can take with a
[00:14:35] grain of salt because it might have been
[00:14:36] set up and optimized for an openclaw
[00:14:38] agent harness, but you're cla code. You
[00:14:41] understand the best way to set up your
[00:14:43] projects and to do things. So, what's
[00:14:45] really important is that you're
[00:14:46] ingesting this information and you're
[00:14:48] understanding it and then you're helping
[00:14:49] yourself organize this project in the
[00:14:51] way that makes the most sense to you.
[00:14:53] Okay, so I know that that is a ton of
[00:14:55] information that I just chucked into
[00:14:56] there and you guys might be sitting
[00:14:57] there like, "Okay, well, I don't have
[00:14:58] all those files. What do I do?" This is
[00:15:00] where you just start to brainstorm.
[00:15:01] Literally treat this thing as if it is
[00:15:03] your best friend who is the best trader
[00:15:05] in the world and you are just trying to
[00:15:06] give it your strategy. Now, so if we
[00:15:08] think back to earlier in step one where
[00:15:10] I talked about this strategy when you
[00:15:11] open up a piece of paper or sorry, you
[00:15:13] take out a piece of paper, you open up a
[00:15:14] Google doc and you just start writing
[00:15:16] down how do you actually trade? What's
[00:15:19] your approach? Once you write down all
[00:15:21] this stuff and you basically just brain
[00:15:22] dump about how you want to do it, then
[00:15:24] you plug it into the cloud code. And
[00:15:26] that's where you see how I set up this
[00:15:27] project here. I'm just helping it get
[00:15:29] situated with what we want to do right
[00:15:31] now. And honestly, the more context and
[00:15:32] details that you give it right now, the
[00:15:34] more it asks you questions, the better.
[00:15:36] As you can see, I'm using the
[00:15:37] brainstorming skill from Superpowers,
[00:15:39] and it's going to start off by asking me
[00:15:40] some questions. Okay, so I just answered
[00:15:42] some questions, and I did want to show
[00:15:43] you guys this. So, it alerted me about
[00:15:45] something with security inside of this
[00:15:48] template that OpenClaw gave me. It had
[00:15:50] my live alpaca key in there. So, I'm
[00:15:53] going to go ahead and rotate those
[00:15:54] before we actually push this new one
[00:15:56] into production. But just something to
[00:15:58] be thinking about when you're migrating
[00:16:00] stuff or when you're feeding in API keys
[00:16:02] directly to a chat. Just be careful of
[00:16:04] that kind of stuff. And I'm going to
[00:16:05] show you how we get our API keys set up
[00:16:06] in routines because you don't want to
[00:16:08] put them straight into a GitHub repo.
[00:16:09] You're going to have to set them up in
[00:16:10] the environment variables. So I will
[00:16:12] show you guys that as well. Okay. So at
[00:16:13] this point it's come back with a plan.
[00:16:15] So Nate ran a live money alaka trading
[00:16:17] bot called bull on the open claw harness
[00:16:19] for 30 days. And now we have all these
[00:16:21] context files with strategy with trade
[00:16:23] history with research notes blah blah
[00:16:25] blah. The goal of this migration is to
[00:16:26] make cloud code a first class home for
[00:16:28] this bot. So we will set up the chron
[00:16:30] scheduling, the notifications. We're
[00:16:31] getting rid of that agent mail step. So
[00:16:33] me and Salmon were having our agents
[00:16:35] trash talk each other. We're going to
[00:16:36] rotate our credentials of course and
[00:16:38] then it's proposing a layout for the way
[00:16:40] that the file should be set up. So you
[00:16:41] can see it's going to put the files in
[00:16:44] here into the memory and then we're
[00:16:45] going to be able to prompt our routines
[00:16:47] to always check the memory first and
[00:16:48] update the memory. So this is where it
[00:16:50] will really help for you guys to
[00:16:51] brainstorm with how the project should
[00:16:53] be set up. Oh, one other thing that I
[00:16:54] forgot to give it here is that I want it
[00:16:56] to use perplexity for research. So, I'm
[00:16:58] going to come down here to the bottom of
[00:16:59] the plan and I'm going to say, yeah,
[00:17:01] this all looks pretty much good to go,
[00:17:04] but one thing I forgot to tell you is
[00:17:05] that we want to use perplexity for
[00:17:06] research rather than just the native
[00:17:08] cloud code web search and web fetch
[00:17:10] function. So, add in that perplexity
[00:17:12] will be used for web search. And once
[00:17:14] again, once we set up the routine,
[00:17:15] that's when I'll give you the perplexity
[00:17:16] API key. Okay. So after this change has
[00:17:18] been made, we should be ready to start
[00:17:20] migrating over to setting up the
[00:17:22] routines. All right, so the new plan has
[00:17:24] come back. So here's the end to end
[00:17:26] check. Secrets, Alpaca, memory files,
[00:17:29] slashcomands, dryr run, clickup,
[00:17:31] perplexity. Nice. We're going to go
[00:17:33] ahead and accept these changes. And you
[00:17:35] also notice that we have auto mode on.
[00:17:37] So I think with this new update with
[00:17:38] Opus 4.7, when you auto accept a plan,
[00:17:41] it turns on auto mode, which means it
[00:17:43] lets cloud handle permission prompts
[00:17:44] automatically. Now, you will have to be
[00:17:47] careful, though, because doing this is a
[00:17:48] little bit more expensive. So, if you
[00:17:49] don't want it to be auto mode, then you
[00:17:51] can just switch it right off of auto
[00:17:52] mode, of course. But, um, yeah, just
[00:17:54] something I wanted to point out. All
[00:17:55] right, so while all of that still
[00:17:56] getting set up, let's talk about step
[00:17:58] three, which is guard rails. So, before
[00:18:00] you start working in the trading logic,
[00:18:02] think about this kind of stuff. I
[00:18:04] obviously talked about how you could
[00:18:05] start with paper mode and then you
[00:18:07] toggle on real trading and put in money
[00:18:09] when you feel comfortable. You could do
[00:18:10] things like, hey, max 5% of my portfolio
[00:18:12] per position. You could have a daily
[00:18:14] loss cap. You could tell the agent what
[00:18:16] not to do, like only buy three new
[00:18:17] positions per week or no options ever or
[00:18:20] don't do this or always do this because
[00:18:22] the agent is going to be autonomous.
[00:18:23] It's going to be eager. And if you don't
[00:18:24] give it guardrails, it might just kind
[00:18:26] of start to, you know, go off the rails.
[00:18:28] But like I said, even though I'm
[00:18:29] migrating a system over, I know it's not
[00:18:31] going to be perfect. So, I'm going to
[00:18:32] watch every single run and I'm going to
[00:18:34] read through the conversation history of
[00:18:36] every run and I'm going to see if
[00:18:37] there's things that I needed to tweak in
[00:18:38] the prompt or things that I need to
[00:18:40] tweak in the project settings or the
[00:18:42] context files. And like I said, just
[00:18:44] kind of keep building the plane as we're
[00:18:45] flying it here. And then that's where we
[00:18:47] also start to develop skills because
[00:18:49] right now we have skills maybe for like
[00:18:51] a research skill or for a trade skill,
[00:18:53] but we're going to make sure that we're
[00:18:54] getting them actually explicitly
[00:18:55] invoked. And we're going to be making
[00:18:57] sure that that increases the
[00:18:58] consistency. And we're going to make
[00:19:00] sure that the agent is able to give us
[00:19:02] insights every day of, hey, here's what
[00:19:04] worked well and here's what I noticed
[00:19:05] and hey, here's where I think that maybe
[00:19:07] we should update these skills X, Y, and
[00:19:09] Z, you know, whatever. So, a combination
[00:19:11] of thinking about the guardrails and
[00:19:13] thinking about skills is how you can
[00:19:15] continuously make this thing better over
[00:19:16] time. And now that we've talked about
[00:19:17] all that, we will get to the routines
[00:19:19] and the deployment. Let's check in on
[00:19:21] our guy right here. And because I turned
[00:19:24] it off auto mode, it was sitting and
[00:19:25] waiting for me to do a permission. All
[00:19:27] right. So, everything has been migrated.
[00:19:29] We're looking good, but we're getting a
[00:19:31] little bit to the point where I like to
[00:19:32] reset the context. So, before we move
[00:19:34] on, I'm going to say, "Hey, give me a
[00:19:36] summary of what we've done." And then
[00:19:38] I'm going to clear the context and we'll
[00:19:39] get started again. All right. So, here's
[00:19:40] the session summary that it gave me.
[00:19:42] Copy that. Do a slashclear.
[00:19:46] Paste that in. Hit enter. And now we're
[00:19:47] basically right back at the beginning
[00:19:49] with a fresh window of context. So, this
[00:19:52] is where it gets pretty cool. You can
[00:19:53] see on the lefth hand side, it has
[00:19:54] reorganized things. We have our scripts.
[00:19:56] We have our memory files. We even have
[00:19:58] some commands in here. And it built all
[00:19:59] of that just because I told it that I
[00:20:01] was trying to migrate stuff over. It
[00:20:03] also updated this claude.mmd file
[00:20:05] because now we have Bull back in all of
[00:20:08] his glory. And we have our cloud. MD
[00:20:10] file that is about 156 lines. So now
[00:20:12] it's time to start planning out step
[00:20:14] five, which is the routines. So we
[00:20:16] basically need to figure out what are
[00:20:17] the different daily triggers that we
[00:20:18] actually want. And we also don't maybe
[00:20:20] want them every day because the market's
[00:20:21] only open 5 days a week. So this is kind
[00:20:23] of like a baseline. This is kind of how
[00:20:24] it worked with my bull trading agent.
[00:20:27] But I'm actually just going to come into
[00:20:29] VS Code and we're just going to
[00:20:30] brainstorm once again. So I'm going to
[00:20:31] go in plan mode and I'm just going to
[00:20:33] start asking. All right. All right. So,
[00:20:34] now that you know everything about this
[00:20:36] project and you understand what we did
[00:20:38] with OpenClaw, I want you to help me
[00:20:39] figure out what is the best way that we
[00:20:41] should be setting up these cloud code
[00:20:43] routines to basically simulate that
[00:20:45] exact same type of environment. So, we
[00:20:47] have those cron jobs, but each one is
[00:20:49] kind of doing a bit of a different
[00:20:50] thing. You know, the pre-market one does
[00:20:52] a bit of a different job than the
[00:20:53] mid-market one, and the the day close
[00:20:56] one does a bit of a different job. So
[00:20:58] you have a better idea of all of our
[00:21:00] memory files and our skills and you
[00:21:03] understand the structure of every time
[00:21:04] the agent wakes up and the routine is
[00:21:06] triggered. They need to read the files
[00:21:08] first to, you know, kind of get
[00:21:09] acclimated with the environment. Do what
[00:21:11] they need to do, research, potentially
[00:21:14] make a trade, potentially sell
[00:21:15] something, you know, whatever it is
[00:21:16] based on their best judgment and then
[00:21:18] update all of the memory files so that
[00:21:20] next time the next agent wakes up, they
[00:21:22] understand what's going on. So, what I
[00:21:24] want you to do is help me figure out
[00:21:25] what are the right structure for these
[00:21:28] um cron jobs. And
[00:21:31] most likely, we only want them during
[00:21:32] the week when the market's actually
[00:21:34] open. And just like that, I'm able to
[00:21:36] brain dump and Claude's going to do the
[00:21:37] heavy lifting for me and propose some
[00:21:39] ideas. Okay, let's see the plan that it
[00:21:41] came up with. So, stand up five
[00:21:43] recurring Claude code scheduled triggers
[00:21:46] and we've got these different slash
[00:21:47] commands that it's going to be able to
[00:21:49] utilize. So all five triggers will run
[00:21:51] on the weekdays only except for the
[00:21:52] weekly review which is Friday only. So
[00:21:54] we have a pre-market which is for
[00:21:56] research catalysts and draft trade
[00:21:57] ideas. It won't message me unless it's
[00:21:59] urgent. We have a market open which is
[00:22:01] going to execute the planned trades and
[00:22:04] set 10% trailing stops. That'll go to
[00:22:06] the trade log only if a trade is placed
[00:22:08] will I get a notification. We have
[00:22:09] midday which will cut minus 7% losers
[00:22:12] and tighten stops on winners. Also going
[00:22:14] to trade log. So here you guys can see
[00:22:15] basically it was able to analyze our
[00:22:17] strategy and analyze what we have access
[00:22:19] to and then build me a plan. And now
[00:22:21] what I want to do is basically just have
[00:22:23] it create those prompts for me so that I
[00:22:25] can go ahead and go set up those
[00:22:26] routines in cloud code. All right. So
[00:22:28] those crons look great. So I don't need
[00:22:31] you to actually create them. What I need
[00:22:33] you to create for me is the prompts. As
[00:22:35] if I was going to run one of those
[00:22:37] commands into a fresh cloud code session
[00:22:39] and I wanted it to do all the right
[00:22:40] stuff. what is the exact prompt that I
[00:22:42] would enter into that session? And the
[00:22:44] one thing that you need to keep in mind
[00:22:46] here is reminding it to obviously um
[00:22:48] read the files before it does anything
[00:22:50] and update the files at the end. And
[00:22:52] then also when it needs to use an API
[00:22:54] like Perplexity or ClickUp or Alpaca
[00:22:56] that it should be grabbing those keys
[00:22:58] from the environment variables of that
[00:23:01] environment, not inside AENV file. All
[00:23:04] right. And now with that feedback, it
[00:23:06] should be able to give us those prompts
[00:23:07] and then we should be able to just set
[00:23:08] up the routines and go ahead and test
[00:23:10] them out. Okay, so while this is writing
[00:23:12] up, there is one more thing that I
[00:23:13] wanted to show you guys that is very
[00:23:14] important. So in the cloud code desktop
[00:23:16] app, when you go to routines and you go
[00:23:18] to create a new one, you can see that
[00:23:19] you can create them locally or remote.
[00:23:22] So if you create them locally, like some
[00:23:23] of these I have, this just basically
[00:23:25] means that it lives in your local
[00:23:27] directory. It can still talk to the
[00:23:28] internet and do all those things, but it
[00:23:29] lives in your machine essentially. And
[00:23:32] that means if you closed out of this
[00:23:34] desktop app, that local routine would
[00:23:37] not fire off. And that's why these
[00:23:39] remote routines are so cool because your
[00:23:41] computer can be off, but they're still
[00:23:42] running because they run in the cloud.
[00:23:44] But what that means is when you do a
[00:23:46] remote run, you have to have a GitHub
[00:23:48] repository to have this run in, which is
[00:23:50] why I have this trading routine repo set
[00:23:52] up. And so when they run via a cloud,
[00:23:56] you know, routine, it basically clones
[00:23:59] that repo in the cloud. It spins up a
[00:24:00] copy. It works out of it. It does what
[00:24:02] it needs to do. And then it basically
[00:24:04] like destroys that cloud environment. So
[00:24:06] if you want them to run remotely and you
[00:24:07] want those files to persist every
[00:24:09] session, you just have to talk to cloud
[00:24:10] code and say, "Hey, make sure you know
[00:24:12] because we're doing a routine, make sure
[00:24:14] that all of these files that it's
[00:24:15] actually updating, it's able to push
[00:24:17] back and commit back to that main actual
[00:24:21] branch, back to that main and we just
[00:24:22] got a notification from my trading bot
[00:24:25] because it was market close." But
[00:24:27] anyways, I was saying make sure that
[00:24:29] it's able to push those changes back to
[00:24:31] the main repo. Otherwise, the next
[00:24:32] agent's not going to pick it up and then
[00:24:34] what's even the point? So you can start
[00:24:35] local if you want and then you can um
[00:24:37] sort of graduate to the cloud if you
[00:24:39] want. But I definitely just wanted to
[00:24:40] make sure you guys understood that
[00:24:42] difference there. Okay, so that's done.
[00:24:44] You can see it created this new folder
[00:24:45] right here called routines. And this is
[00:24:47] basically the prompt that we'd be
[00:24:48] feeding into each of the different
[00:24:50] routines that we make in order to make
[00:24:52] sure that Bull actually understands what
[00:24:54] to do. And the last thing we need to do
[00:24:56] is actually push all of these new
[00:24:58] changes to this GitHub repo. Because
[00:25:00] right now here is my trading routine
[00:25:01] private repo. All that's in there is a
[00:25:03] readme and I don't think there's
[00:25:04] anything in here. So, we need to get all
[00:25:05] of these files that we just created, you
[00:25:07] know, these commands, these scripts,
[00:25:09] these memory files. We just have to get
[00:25:10] all of this into that repo so that our
[00:25:12] routine can actually access it. So, all
[00:25:14] I have to do is say, "Hey, push all of
[00:25:16] these changes, commit everything to the
[00:25:17] repo." By the way, if you've never done
[00:25:19] that before, it's super super simple.
[00:25:20] You go to github.com, create an account.
[00:25:22] It's free to create an account. And
[00:25:23] GitHub is really just like um it's like
[00:25:26] working on um a Microsoft Word on your
[00:25:29] computer and that's like local. And if
[00:25:31] you wanted to share it with someone, you
[00:25:32] would have to put it into like the
[00:25:34] shared drive or, you know, a a Google
[00:25:36] Drive or something. It just means that
[00:25:38] you could grab a codebase from a
[00:25:40] different machine because you've
[00:25:41] uploaded it somewhere on the cloud. So
[00:25:43] that's kind of why we're doing this
[00:25:44] whole thing with the routines in the
[00:25:45] cloud. So when you get to GitHub, you
[00:25:47] come here, you create a new repository
[00:25:48] or the easiest way to do it is you just
[00:25:51] come to your cloud code and you say,
[00:25:52] "Hey, help me turn this into a GitHub
[00:25:54] repo." And it will say, "Okay, I need to
[00:25:56] authenticate you. Can I use the CLI?"
[00:25:58] And you say, "Yes, go ahead and do
[00:26:00] that." And then it will basically open
[00:26:01] up a tab and it will say, "Hey, can you
[00:26:03] sign in with your GitHub?" You sign in
[00:26:05] and now your Cloud Code just has your
[00:26:06] GitHub credentials. And whenever you
[00:26:08] need to push changes or clone a repo or
[00:26:11] whatever you need to do with GitHub, it
[00:26:13] can just take care of it because
[00:26:14] GitHub's been around for a long time.
[00:26:16] So, it knows it way better than you
[00:26:17] probably do. It knows it way better than
[00:26:18] I do. So, when in doubt, just ask Claude
[00:26:21] Code. All right. So, if I give this
[00:26:23] puppy a refresh, we should see we now
[00:26:25] have all of these files popped in here.
[00:26:26] We've got bold trading routine. Awesome.
[00:26:29] So, let's head over to the Clog desktop
[00:26:31] app now and start getting set up. So,
[00:26:33] what you're going to do is you're going
[00:26:34] to click on new session and you want to
[00:26:36] open up the local project right here of
[00:26:38] whichever thing you just set up there.
[00:26:40] So, right here you can see that I'm in
[00:26:42] the folder called trading routine which
[00:26:43] we were just working in in VS Code. And
[00:26:45] if you guys remember in VS Code, we had
[00:26:47] these five different routine prompts.
[00:26:49] And inside of each of these, they had
[00:26:50] the cron, they had the actual like
[00:26:53] steps, and then they had like any of the
[00:26:55] skills or commands that they need to
[00:26:56] run. And this is in a folder once again
[00:26:58] called routines. So before we start
[00:27:00] talking to our new project, we need to
[00:27:02] set up an actual environment for this.
[00:27:04] So if I go to new routine and I go to
[00:27:06] remote and I go over here to my um cloud
[00:27:09] environments, you can see that you can
[00:27:10] add one. And so just add one. And I'm
[00:27:13] going to pull up my trading one so you
[00:27:14] guys can see. But here, this is where we
[00:27:16] set up things like our API keys and our
[00:27:18] network access. So I called mine
[00:27:19] trading. I gave it full network access.
[00:27:21] And this is where I'm going to put in my
[00:27:23] API keys for Alpaca and for Perplexity
[00:27:25] and for ClickUp. And then you basically
[00:27:27] just go ahead and save the changes of
[00:27:29] that environment. And this is the one
[00:27:30] that you want your actual routines to be
[00:27:34] scheduled inside of. I am going to
[00:27:36] basically just talk to it right here to
[00:27:38] help us get these remote routines set
[00:27:40] up. Look inside the routines folder
[00:27:43] inside of this project and help me set
[00:27:45] up all of these different schedule
[00:27:47] routine runs. They should all have a
[00:27:50] cron job in there. They should all have
[00:27:51] a prompt in there already. And we will
[00:27:53] be working out of this GitHub repo and
[00:27:55] scheduling off these routines. So, let
[00:27:57] me know if you have any questions. Do
[00:27:58] not exit the planning phase until you're
[00:28:00] 95% confident that you know exactly what
[00:28:03] to do and exactly what I'm looking for.
[00:28:05] So, now I'll shoot that off and it
[00:28:06] should be able to come back with a plan
[00:28:07] to actually go create all of those cron
[00:28:09] jobs for us. Okay, now you can see it's
[00:28:11] coming back and asking us some
[00:28:12] questions. So, the first one is which
[00:28:13] cloud environment should they run in?
[00:28:15] We're going to do trading. That's the
[00:28:16] one you guys saw me set up. We want to
[00:28:17] use Claude Opus 4.7 and we're going to
[00:28:20] use this GitHub repo. Yes, trading
[00:28:22] routine. All right. So, it set up all of
[00:28:24] those routines for us. You see that all
[00:28:26] I had to do was talk to it. It set up
[00:28:28] these crons cuz I don't know what
[00:28:29] exactly this means, but basically that
[00:28:30] means 6:00 a.m. Monday through Friday
[00:28:32] for all of these Monday through Friday,
[00:28:34] 8:30 a.m., noon, 3 p.m., and then this
[00:28:36] one is just 400 p.m. on Friday. So, if I
[00:28:38] go over here to my routines and I scroll
[00:28:40] down, you can see that we have these new
[00:28:41] five routines for Bull. And these are
[00:28:44] all remote. If I click in, this one for
[00:28:46] example says every Friday at 4 PM
[00:28:48] central. We're in the right repo. If I
[00:28:50] click into here, we should see we see
[00:28:52] this entire prompt, which is correct,
[00:28:54] and we're in the right environment,
[00:28:55] which is my trading cloud environment.
[00:28:57] And then one other important thing that
[00:28:59] you have to do is inside of your actual
[00:29:01] um routine, what you want to do is go to
[00:29:03] permissions and you want to turn on
[00:29:05] allow unrestricted branch pushes. This
[00:29:07] removes the branch push restrictions and
[00:29:09] Claude will be able to actually push to
[00:29:11] any branch, not just the
[00:29:12] clawed/branches.
[00:29:13] So turn that on for all five of these
[00:29:15] routines here. So I'm going to turn that
[00:29:17] on for all five of these routines here.
[00:29:18] So let's just pretend that it is Friday.
[00:29:20] I'm going to do a run now to see if this
[00:29:22] is able to actually work. And when you
[00:29:24] run these, you can actually click right
[00:29:25] here and you can watch them actually
[00:29:27] work in real time. And best practice
[00:29:29] with routines is that every single time
[00:29:30] you build a new one, you should always
[00:29:32] do a run now at least a few times to
[00:29:34] make sure that they are working as
[00:29:35] expected. And exactly why we test out
[00:29:37] you can see what happened is when it
[00:29:38] tried to hit alpaca it wasn't able to
[00:29:40] find the API key because for some reason
[00:29:42] once again it thought it was going to be
[00:29:43] in aenv but as you guys know we don't
[00:29:45] haveenv because we don't put that into
[00:29:47] GitHub. So I'm coming back into this
[00:29:48] session that set up these five and I'm
[00:29:50] just going to say hey remember all of
[00:29:51] the API keys are going to be stored in
[00:29:53] the environment variables. So all of the
[00:29:54] prompts must explicitly state that.
[00:29:56] Okay. So the issue was they weren't
[00:29:58] spelled exactly word for word letter for
[00:30:01] letter. So I fixed that. And you can
[00:30:02] even see for example this one. They're
[00:30:04] all now coming through. But for example,
[00:30:05] in this one, I have the word API right
[00:30:08] here between Alpaca and secret. So they
[00:30:10] have to be matching one for one,
[00:30:12] otherwise it will think that they're not
[00:30:14] there. But anyways, now that that has
[00:30:15] been figured out, it's actually able to
[00:30:17] look through all these things. It's able
[00:30:19] to look through the memory and it's
[00:30:20] going to execute our weekly review here.
[00:30:22] And there we go. Just like that, the
[00:30:23] weekly review has been ran. I also told
[00:30:25] it that I fixed the alpaca secret key.
[00:30:27] So now all of that's been updated. And
[00:30:29] if you go over to my GitHub, you can see
[00:30:30] that it was able to push these actual
[00:30:32] commits to this repo. This one was just
[00:30:35] a test one that it was running on the
[00:30:37] background as well, but it was able to
[00:30:38] actually give us the weekly review. And
[00:30:40] you can see it was committed by Claude
[00:30:42] and it made changes to this actual MD
[00:30:44] file. So now the next time it actually
[00:30:46] will be able to pick it up and we have
[00:30:47] our stuff all synced up. And alongside
[00:30:49] that weekly review, you can see that in
[00:30:51] my internal automations channel
[00:30:52] sandwiched between two YouTube
[00:30:54] notifications, we have the weekly review
[00:30:57] that the Run just sent us, we have our
[00:30:59] portfolio, we have versus the S&P, and
[00:31:01] we have any trades that we were making.
[00:31:03] And then, you know, some bests and worst
[00:31:05] and also it graded itself a C for the
[00:31:07] week. So, we'll see how this is able to
[00:31:09] improve. So, I just spun up this test so
[00:31:11] you guys could see that we are able to
[00:31:12] talk to Alpaca right now. You can see
[00:31:14] that we were able to get the current
[00:31:16] balance. And if I go into here, we
[00:31:18] should see 9859. And back in Cloud
[00:31:20] Desktop where it pulled it, 9859. And
[00:31:23] just like that, we have set up a 247 AI
[00:31:26] agent trade system with Opus 4.7. We've
[00:31:28] got our 6 a.m., our 8:30 a.m. We've got
[00:31:30] our noon and our 3 p.m. And then on
[00:31:32] Fridays, we have our actual weekly
[00:31:34] review as well. Now, of course, like I
[00:31:36] talked about earlier, it is on you to
[00:31:38] now keep testing, keep iterating, making
[00:31:39] sure that everything's working and
[00:31:41] upgrading your strategy as you go. And
[00:31:43] maybe you want to add some more crrons
[00:31:44] in. Maybe you want to take some away.
[00:31:45] Maybe you want to add one on just like a
[00:31:47] Sunday night to do some more research to
[00:31:48] prep for the week. However, you would
[00:31:50] actually want to set up your trading
[00:31:52] strategy if you were doing it manually.
[00:31:53] Now, I know you guys are thinking like,
[00:31:55] I have four automations per day
[00:31:57] basically plugged in now with clawed
[00:31:59] routines and that's going to eat away at
[00:32:01] my session limits, right? I mean, yes
[00:32:03] and no. I'm definitely going to be
[00:32:04] watching it obviously, but keep in mind
[00:32:05] when I did this with my OpenClaw agent
[00:32:07] for 30 days, I was also plugged into my
[00:32:09] cloud subscription and I was still doing
[00:32:11] my own workflows and I was never really
[00:32:13] hitting my limits. It's all about
[00:32:15] managing your context. And I'm going to
[00:32:16] have a full video dropping about that,
[00:32:18] another one coming out soon. But I can
[00:32:20] tell you for certain that if I were to
[00:32:21] set up all of these crrons and have the
[00:32:22] same sort of autonomy and agentic
[00:32:25] workflowess and I was just doing this
[00:32:28] via API, then that would 100% be way
[00:32:30] more expensive than what I've got set up
[00:32:32] here. We have now deployed and now we
[00:32:34] just go ahead and track. And what is the
[00:32:35] hidden lesson here? The hidden lesson is
[00:32:37] that files aren't just memory, but
[00:32:38] they're essentially the agent's full
[00:32:40] personality and discipline. Like with
[00:32:42] OpenClaw, you set up your sold.mmd file
[00:32:43] and you've got your agents.mmd file and
[00:32:45] you got all these different files. So,
[00:32:46] it's really about how do you make sure
[00:32:48] that you orchestrate this in the right
[00:32:49] way so that it can access the right ones
[00:32:51] when it needs to. So, anyways, I hope by
[00:32:53] the end of this video you guys are able
[00:32:54] to follow along and set this up. I'm
[00:32:56] going to be giving away this document
[00:32:57] and it's going to have way more
[00:32:58] information in there about basically
[00:32:59] about everything that we've gone over
[00:33:00] today and I'll drop that in my free
[00:33:02] school community. The link for that is
[00:33:04] down in the description. Once again,
[00:33:05] completely free. But that is going to do
[00:33:07] it for today. So, if you enjoyed the
[00:33:08] video or you learned something new,
[00:33:09] please give it a like. It helps me out a
[00:33:10] ton. And as always, I appreciate you
[00:33:12] guys making it to the end and I'll see
[00:33:13] you in the next one.