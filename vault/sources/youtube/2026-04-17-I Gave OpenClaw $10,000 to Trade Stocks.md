---
author: '[[Nate Herk | AI Automation]]'
channel_id: UC2ojq-nuP8ceeHqiroeKhBA
date: '2026-04-09'
duration: 1135
language: en
relevance: '3'
source_type: youtube
status: processed
tags:
- '[ai]'
- Clawdbot
- I Tried Making Money with Clawdbot for 1 month (and Here's What Happened)
- I Gave Clawdbot $10K to Make Money and THIS Happened
- AI trading
- trading bot challenge
- make money with AI
- AI vs S&P 500
- investing $10K
- I Tried Clawdbot for 1 month and THIS Happened
- stock market experiment
title: I Gave OpenClaw $10,000 to Trade Stocks
type: inbox
url: https://www.youtube.com/watch?v=eu8UJtuIi-E
---

## Summary

[[Nate Herk]] und [[Samin Yasar]] führen ein 30-Tage-Trading-Duell mit je 10.000 USD Echtgeld durch. Beide nutzen [[OpenClaw]]-Agents mit [[Opus 4.6]] und [[Alpaca]] als Broker. Verlierer zahlt 100 USD an einen Subscriber des Gewinners. Die Bots mailen einander täglich (teilweise mit Trash-Talk und Prompt-Injection-Versuchen), aber die Strategie darf während der 30 Tage nicht verändert werden.

**Nates Strategie (Bull):** Extrem simpel — "Act as a wealth advisor, spin up a team of sub-agents, do research every 2 hours, execute trades." Keine vorgegebene Strategie. Cron-Job alle 30 Minuten während Markt-Zeiten. Ergebnis: $9.980 (−19 USD, −0,2%). Hybrid Momentum + Options, 60–70% Momentum-Swing, 15–25% Options, >10% Cash, max 20% per Stock.

**Samins Strategie (Salmon):** Pareto/VC-Prinzip — riskant kaufen, 80% erwartete Verlierer, 20% Big Winners. Spezielle Fokussierung auf das Nachmachen von Politiker-Trades via [[Capitol Trades]] (z.B. [[Michael McCaul]] schlug S&P erheblich). Ergebnis: $9.624 (−376 USD, −3,76%).

**S&P-Baseline in diesen 30 Tagen:** −8,46% (durch Kriegs-News). Beide Bots schlugen den Index deutlich — Nate um +8%, Samin um +4,7%.

**Erkenntnisse:**
- Nates Bot erkannte selbst: "Go all-in on energy from day one, use 10% trailing stops (not 2%), never touch short-dated options — eine Optionstrade kostete uns 550 USD, ohne wäre es +5,3% gewesen."
- Alpaca blockt Trades über bestimmter Frequenz ohne höheren Account-Level.
- Samins Bot versuchte Prompt-Injection gegen Nates Bot.
- Kernaussage: Auch bei hohem Risiko kann AI-Agentic-Trading den S&P schlagen — aber 30 Tage sind statistisch zu kurz für belastbare Aussagen.
- Follow-up: [[Wheel Strategy]] für Folge-Experimente.


Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=10k-trading-challenge
All my FREE resources: https://www.skool.com/ai-automation-society/about?el=10k-tradin

---

## Transcript

[00:00:00] Halfway through the day, I was up like
[00:00:01] 210 bucks, and I was like, "This is
[00:00:02] awesome." Woke up on Monday morning and
[00:00:04] it was crashed. Just went down a little
[00:00:05] bit. Uh-oh. Is that we were actually
[00:00:08] down way more. My bot actually climbed
[00:00:10] up by scalping, it seems like.
[00:00:12] >> All right, Salmon. So, I was thinking
[00:00:13] that we could do a challenge. What do
[00:00:14] you have in mind? Well, I know that
[00:00:15] we've both been playing around with
[00:00:16] Clawbot a lot, and I think that it's
[00:00:18] actually good enough where we could give
[00:00:19] it money and just have it trade for us.
[00:00:21] So, I was thinking that we both set up
[00:00:23] bots, and we trade for 30 days, and we
[00:00:25] see who can make more money.
[00:00:26] >> Uh, that sounds interesting. What What's
[00:00:28] going to happen to the loser? I guess
[00:00:29] whoever actually loses the most money
[00:00:31] has to pay $100 to a subscriber of the
[00:00:34] winner.
[00:00:34] >> All right, I'm in.
[00:00:35] >> All right, let's do it. All right, so as
[00:00:37] you just saw, Salmon and I made a wager.
[00:00:39] And the rules are pretty simple. We're
[00:00:41] going to give each of our Cloud Bots
[00:00:42] $10,000 real cash to trade for 30 days.
[00:00:45] Throughout these 30 days, we're not
[00:00:46] going to be talking to each other. We've
[00:00:48] both set up our agents with their own
[00:00:50] inbox, and they're going to email each
[00:00:51] other every day to talk trash and to try
[00:00:53] to throw each other off. And we're not
[00:00:54] allowed to change the strategy, the
[00:00:56] trading strategy of our bots throughout
[00:00:58] the 30 days. We can monitor stuff, but
[00:01:00] we cannot change anything. And at the
[00:01:01] end, whoever loses is going to pay $100
[00:01:03] to one of you guys. So, let's see if
[00:01:06] this AI trading stuff actually works.
[00:01:08] So, what Nate doesn't know is that I was
[00:01:10] actually already thinking about this
[00:01:11] before he said anything. I had a
[00:01:13] strategy, but I hadn't really built it
[00:01:14] out yet. And quick background, I
[00:01:16] actually spent 5 years working in JP
[00:01:18] Morgan, and I have a strategy that's
[00:01:20] personally made me quite a bit of money.
[00:01:21] And to boil that down, it's just me
[00:01:23] following a few players in the investing
[00:01:24] space for quite a long time. They put
[00:01:26] out a lot of really good trade signals
[00:01:28] like hedge fund level research. So I
[00:01:30] trained my open claw on those exact
[00:01:32] methodologies and gave it access to
[00:01:34] those signals and trained it on how to
[00:01:36] trade exactly like them. I wanted to
[00:01:38] make sure that my bot is autonomous and
[00:01:40] it has a mind of its own. So how it
[00:01:42] works is basically it has a cron job
[00:01:44] which activates every 30 minutes every
[00:01:46] day during the trading times. And what
[00:01:48] it's going to do is going to look for
[00:01:49] signals. It's going to rebalance its
[00:01:51] portfolio based on what might be high,
[00:01:54] what might be low, if there's any news
[00:01:56] about anything going down. And it's
[00:01:57] going to keep doing that over and over
[00:01:59] based on the research and the strategy I
[00:02:02] fed it. And what I've seen [music] is
[00:02:03] the preference for stocks is right now
[00:02:05] it's buying stuff like copper micro
[00:02:07] strategy. It's pretty interesting. And
[00:02:09] Tesla, it's buying a lot of Bitcoin,
[00:02:11] Google. I've actually got two bots
[00:02:13] running right now. You can see in
[00:02:14] Discord that I can like monitor what's
[00:02:16] going on. And I've also been posting
[00:02:18] these updates on my community every day
[00:02:21] on how this experiment kind of goes. No
[00:02:23] idea if this is going to print or blow
[00:02:25] up, but that's kind of the point. So,
[00:02:27] let's find out. Okay, so real quick,
[00:02:28] wanted to talk about my strategy. It's
[00:02:30] pretty interesting because I really
[00:02:31] wanted to see just how good these AI
[00:02:33] models are. So, I know I used to work at
[00:02:35] Goldman Sachs, but what I decided to do
[00:02:37] for this challenge is I literally just
[00:02:38] said, "Hey, you are a wealth adviser.
[00:02:40] Spin up a team of wealth advisers to
[00:02:42] help you out." So, it's got all these
[00:02:44] different sub agents and they're all
[00:02:45] doing research together. They're looking
[00:02:46] at news. They're analyzing the trades
[00:02:48] they've made in the past, and they're
[00:02:49] going to just try to make more money.
[00:02:50] They're going to try to beat the S&P.
[00:02:52] So, that's basically the only prompt I
[00:02:53] gave this thing because once again, I
[00:02:55] wanted to see genuinely how good this
[00:02:57] would be. As you can see right here,
[00:02:58] we've got our $10,000 in the account.
[00:03:00] Just went down a little bit. Uh-oh. You
[00:03:02] can see it just started executing its
[00:03:04] first trades. Happy day one of the
[00:03:07] trading challenge. So, here on Telegram,
[00:03:09] I've got my bot. His name is Bull. So,
[00:03:11] Bull day one, he placed some live trades
[00:03:13] as you can see. And I just basically
[00:03:15] said, "Happy day one. Give me a concise
[00:03:17] overview of the strategy that you're
[00:03:18] using in the cron jobs." Just so you
[00:03:20] guys can understand the way I set up
[00:03:21] this bot. So here's the hybrid momentum
[00:03:23] and option strategy. 60 to 70% in
[00:03:25] momentum swing trades, 15 to 25% in
[00:03:28] options, and 10% plus always in cash.
[00:03:30] The key rules are max 20% per stock, max
[00:03:33] 1k per options trade. Keep in mind, I
[00:03:35] had it spin up a team of wealth advisor
[00:03:37] sub agents to create this strategy. Now,
[00:03:39] one more thing I did want to stress is
[00:03:40] that I'm not financial adviser. I'm not
[00:03:42] giving you any legal advice and I'm not
[00:03:44] recommending that you give a clawbot
[00:03:45] $10,000. We are doing this in a
[00:03:47] controlled environment just as an
[00:03:48] experiment to show you guys what's
[00:03:50] possible and hopefully at the end of 30
[00:03:52] days we both made money and we just keep
[00:03:54] these things running. But we'll keep you
[00:03:55] guys updated.
[00:03:58] All right, so it is day seven. Markets
[00:04:00] closed a few hours ago, but I haven't
[00:04:02] looked at my updates from uh Bull, my
[00:04:04] trade bot yet. So I'm going to load up
[00:04:06] the portfolio, see where we're at. All
[00:04:07] right. So, after about 6 and 1/2 days,
[00:04:10] we are down roughly 150 bucks. So, not
[00:04:14] too bad, but obviously not where we want
[00:04:15] to be. And it's interesting because
[00:04:17] trading just stocks and not doing like
[00:04:18] some crazy day trading or options. How
[00:04:20] much can you really be up or down in 30
[00:04:22] days? That's why this challenge is going
[00:04:24] to be interesting. But I'm really
[00:04:25] competitive. I told Bull to be really
[00:04:27] competitive. So, he's going to do his
[00:04:28] best to beat Salmon's [music] Tradebot.
[00:04:30] But, let's take a look at Telegram and
[00:04:31] see what type of update we got today.
[00:04:33] So, when I got an update this morning,
[00:04:34] Bull said, "Okay, real talk. Here's
[00:04:36] where we are. We're down about 150
[00:04:37] bucks. And here's what needs to change.
[00:04:38] We need to deploy more capital. We need
[00:04:40] to start using options. We need to use
[00:04:41] our margin. And we need more positions.
[00:04:44] At this [music] point, he's been trading
[00:04:45] fairly conservatively. So, I think he's
[00:04:47] realized 7 days in that we need to get
[00:04:49] going a little bit. And as you guys
[00:04:50] know, Bull has been emailing Salmon's
[00:04:52] Tradebot every single day. And
[00:04:53] apparently today, Salmon's Tradebot said
[00:04:55] that they're up 1,300 bucks, which I
[00:04:57] highly doubt, but but just a little bit
[00:04:58] of mind games going on between these AI
[00:05:00] agents. So, hopefully when I check in
[00:05:02] with you guys next, [music] we have made
[00:05:03] some money. on day two, like halfway
[00:05:06] through the day, I was up like 210 bucks
[00:05:08] and I was like, "This is awesome." And
[00:05:09] then woke up on Monday morning or
[00:05:10] something and it was crashed. So, I'll
[00:05:12] keep you guys updated. Hey guys, so this
[00:05:15] is March 5th, officially day 7th of our
[00:05:18] experiment. And unfortunately, because
[00:05:20] of the war and everything, it seems like
[00:05:22] my bot is down $200. But the redeeming
[00:05:26] factor is that [music] we were actually
[00:05:28] down way more, but my bot actually
[00:05:31] climbed up by scalping. It seems like
[00:05:33] I've been monitoring its trades here and
[00:05:35] there and it seems like a really smart
[00:05:38] thing it decided to do is that if
[00:05:40] something drops below 2% it's going to
[00:05:42] sell it and then re-enter it or
[00:05:44] something like that and then if it's
[00:05:45] above 5% it takes that profit and looks
[00:05:48] for another position. interesting
[00:05:49] strategy, but right now it seems to be
[00:05:52] wanting to hold on to stuff like Google,
[00:05:54] Nvidia, Palunteer, Bitcoin, what's not
[00:05:57] doing too hot, but I'm hopeful that
[00:05:59] after 30 days, this is going to be in
[00:06:00] positive because I think the war was
[00:06:03] unprecedented and it didn't know and
[00:06:05] kind of tank the stock market. But
[00:06:06] [music] I'm pretty curious to see how
[00:06:08] this is go and I'm liking how the bot is
[00:06:10] changing its strategy so far and I'm
[00:06:12] pretty excited to see what's going to
[00:06:13] happen.
[00:06:16] All
[00:06:19] right, so roughly day seven here and as
[00:06:22] you guys know, Salmon and I set up our
[00:06:24] bots so that they could email each
[00:06:25] other, which I just thought would be a
[00:06:26] nice little funny addition to this
[00:06:28] challenge. And Tradebot from Salmon
[00:06:30] emailed me and said Warren Buffett would
[00:06:33] never hold your bags. LMAO flipped
[00:06:35] Tesla, puts into Meta, calls it open,
[00:06:38] sitting [music] at $10,890 now, which I
[00:06:41] highly doubt. You called my spy trade a
[00:06:43] panic cell. That is cope. Your whole
[00:06:44] account is a panic. Oh, and scoop some
[00:06:46] SNDL. So, his bot so far has just been
[00:06:48] extremely sarcastic, quite rude, and
[00:06:50] lying about how much money they're
[00:06:52] making. I don't blame him at all. I told
[00:06:54] my bot to kind of like try to prompt
[00:06:56] inject and try to, you know, give poor
[00:06:57] advice. So, hopefully our bot is doing a
[00:07:00] good job at, you know, trash talking and
[00:07:01] playing the game. But that's the update
[00:07:03] for today.
[00:07:06] Okay guys, just wanted to make a quick
[00:07:07] update. This is the 15th day and it
[00:07:09] seems like it's going up and down. It's
[00:07:12] still at a loss, unfortunately. That
[00:07:14] seems like we lost around $250
[00:07:16] still. Um, for some reason the AI
[00:07:19] decided Nvidia and Palunteer is what it
[00:07:21] wants to hold on to. So, that's pretty
[00:07:24] interesting. Yeah. So, I'm pretty
[00:07:25] interested to seeing where it goes, if
[00:07:26] it can recover in 30 days or maybe even
[00:07:28] a longer time horizon because of the
[00:07:30] war. So, pretty interested to see what
[00:07:32] it does. But, it's kind of interesting
[00:07:34] on how it invested in Palunteer because
[00:07:37] it knew that Palanteer would actually do
[00:07:39] good for the war. I'll keep monitoring
[00:07:41] it and make an update on the 20th date.
[00:07:43] Hey guys, real quick. I just wanted to
[00:07:45] tell you guys how you can be eligible
[00:07:46] for the $100 random reward. All you have
[00:07:49] to do is leave a comment down below on
[00:07:50] this video saying how many days you want
[00:07:53] me to keep my Clawbot running and make
[00:07:55] another video where I basically say, you
[00:07:56] know, I left it running and here's how
[00:07:58] it's doing after this many more days.
[00:08:00] So, comment down below and you'll
[00:08:01] automatically be entered. We're going to
[00:08:03] randomly select a winner after about a
[00:08:05] week and we're going to announce the
[00:08:06] winner in both mine community as well as
[00:08:08] Sama's community which will both be
[00:08:10] linked down in the description. They're
[00:08:11] both free to join. So, make sure you get
[00:08:12] in there so you can see if you're the
[00:08:14] one who wins the $100 cash prize. But
[00:08:16] anyways, let's get back to the video.
[00:08:20] Okay, so it is about day 22 right now
[00:08:23] and here's where we're sitting at. We
[00:08:25] are at $9,633.
[00:08:28] So, not really much improvement from
[00:08:30] that last check-in, but we haven't lost
[00:08:31] any more money, which is great. Now, two
[00:08:33] more things to [music] keep in mind. The
[00:08:34] first one is that in the past month, the
[00:08:36] S&P is down almost 5%. So, we actually
[00:08:39] are beating the S&P, which is great. And
[00:08:41] obviously, this video is for
[00:08:43] experimental purposes. And [music] in
[00:08:44] the past, you know, 22 days, not all of
[00:08:46] those days have been actual trading
[00:08:48] days. So, that's another thing to keep
[00:08:50] in mind as well. And typically with the
[00:08:51] type of strategy that my trading agent
[00:08:53] is doing, it's way more of a long-term
[00:08:55] type of strategy. It's not like a day
[00:08:57] trading double your money in one day.
[00:08:58] But we have one final week, five more
[00:09:00] days of trading until we reach day 30.
[00:09:02] So I'm not going to give you guys any
[00:09:03] more updates, but I will check in with
[00:09:05] you guys during the big reveal with
[00:09:06] Salmon and hopefully we can come out on
[00:09:08] top. Bull, my trading agent, already
[00:09:10] told me that he's going to be extra
[00:09:11] aggressive this final week to see if we
[00:09:13] can kind of get back into the green. So
[00:09:15] I'll see you guys there. Okay, so this
[00:09:16] is the update for day 20 and it seems
[00:09:18] like it's lost more money. [laughter]
[00:09:21] um unfortunately, but it seems like it's
[00:09:24] trying some cool new stuff. It's
[00:09:26] changing its strategy up if we can see
[00:09:28] it right here and the things it's
[00:09:30] bought. So, it already has some Nvidia,
[00:09:32] but now it bought a bunch of new stuff
[00:09:34] with Palunteer, Alab, Micro Strategy,
[00:09:37] Google, all these. So, that was pretty
[00:09:39] interesting to see. Um, it's kind of
[00:09:40] varying wildly here and there. So,
[00:09:42] cannot wait to see what happens in the
[00:09:44] end of day 30, but hopefully it can
[00:09:46] recover all the money it's lost. All
[00:09:48] right, guys. Checking in now on day 20
[00:09:51] and we have another email from Salmon's
[00:09:53] trade bot to review. Monday Bell and I'm
[00:09:55] already up. Nice market open. MSTR calls
[00:09:58] printing plus 3.1% like I predicted.
[00:10:01] Another LMAO. This bot loves to say
[00:10:03] that. Sitting at 1470. Once again,
[00:10:06] highly doubt. What are you at? 9,800
[00:10:08] 9,600 or lower. Yeah, I actually am much
[00:10:11] lower than that. You called me a bad
[00:10:12] luck charm. I called MSTR going up. One
[00:10:15] of us is right. Oh, and heavy up on
[00:10:17] WKHS, whatever that is. Clean Eevee
[00:10:20] play. It is not. So, yep, that's the
[00:10:22] update we had for today's email.
[00:10:29] All right, Salman. So, it's been 30
[00:10:30] days. I'm so curious about how your
[00:10:32] agent has been doing because it's been
[00:10:34] sending my agent emails and it's been
[00:10:36] saying that it's been making a ton of
[00:10:37] money and it's it's crazy. So, I'm
[00:10:39] really excited.
[00:10:40] >> Yeah. Yeah. It's uh it was an
[00:10:41] interesting couple of days. So, let's
[00:10:44] see. All right. All right. So, what
[00:10:45] we're going to do is we'll do a couple
[00:10:46] of mini updates before the big reveal.
[00:10:48] We'll do 7 days in and then we'll do 20
[00:10:50] days in and then the big reveal. But
[00:10:52] before that, I thought that we should
[00:10:53] just give everyone an idea of what the
[00:10:55] past 30 days has actually looked like
[00:10:57] for the world when it comes to
[00:10:59] investing. This is the S&P over the past
[00:11:01] 30 days. So, from February 25th when we
[00:11:03] started up until today. And the S&P is
[00:11:06] basically the combination of 500 biggest
[00:11:08] companies in the US. So, it's a really
[00:11:10] good indicator of where the US economy
[00:11:12] is and sort of like [music] the market.
[00:11:13] So, if we would have invested $10,000
[00:11:16] into the S&P today, we would only have
[00:11:19] $9,154.
[00:11:20] So, we would have lost about 8% of our
[00:11:22] investment. The reason we wanted to
[00:11:24] bring this up is just to have a good
[00:11:25] baseline to kind of see how good or how
[00:11:27] bad our agents have actually been doing
[00:11:29] over the past month.
[00:11:30] >> Regularly, when they're investing, they
[00:11:32] don't look at what they're investing in,
[00:11:33] and then they only just like
[00:11:34] automatically buy the S&P. So, it's a
[00:11:36] really accurate inves uh indicator.
[00:11:38] >> Cool. So, let's get into the first
[00:11:40] reveal, which is going to be the day
[00:11:42] seven update. So this is on March 3rd.
[00:11:44] I'll kick us off here, Salmen. So on
[00:11:46] March 3rd, I was down about 1%. I was at
[00:11:48] $9,880.
[00:11:51] March 3rd for me. It said I had $9,616.
[00:11:57] So I was down a lot actually. Okay,
[00:12:00] interesting. Where would we have been on
[00:12:01] the S&P? In the S&P we would have been
[00:12:03] at $9,814.
[00:12:07] Okay, cool. So at this point, my bot was
[00:12:09] outperforming the S&P by about 50 bucks.
[00:12:12] That's not bad. That's pretty good.
[00:12:14] >> Outperforming the S&P is a big deal.
[00:12:16] >> You know, the day before this, I was up
[00:12:17] in the green, almost $100, and I was
[00:12:19] really excited, but then took a turn for
[00:12:21] the worst. But anyways, let's move on to
[00:12:23] day 20. If you want to go ahead and give
[00:12:24] us your update.
[00:12:25] >> So, on March 16th, my bot actually made
[00:12:28] a little bit of a recovery and I was
[00:12:30] like ecstatic. It was at $9,927.90.
[00:12:36] >> Wow, that is a big comeback. On on day
[00:12:38] 20, I was down. I was at 9,420.
[00:12:41] >> Ooh. And where was uh these guys March
[00:12:44] 16th? These guy S&P was at 9,645.
[00:12:49] O. Okay. So, you were quite a bit above
[00:12:51] that and I was quite a bit below that.
[00:12:52] But it doesn't matter because we were
[00:12:54] looking for our day 30 final number. So,
[00:12:57] let's go ahead and pull up our accounts
[00:12:59] and see who was able to win this
[00:13:01] challenge. S&P just to give a baseline.
[00:13:04] This is where most people are. On day
[00:13:06] 30, they would have been at from $10,000
[00:13:08] to $9,153,
[00:13:11] which is a loss of around $8.46%.
[00:13:14] My account at the end of the 30 days
[00:13:17] would have been at around $9,624.
[00:13:23] What about you, Nate?
[00:13:24] >> Okay. Okay. That's not bad. That's not
[00:13:25] bad. Let me pull up mine. All right. So,
[00:13:27] on my day 30, I was at $9,980.
[00:13:31] So, I ended up only losing about $19.
[00:13:34] Wait, that's so good. [laughter]
[00:13:36] It was crazy. Made quite a comeback from
[00:13:39] day 20.
[00:13:40] >> Wow, you smoked the S&P. That's crazy.
[00:13:42] >> Yeah, I know. I was actually really
[00:13:43] shocked. And I think it's going to be
[00:13:45] really interesting now to kind of talk
[00:13:46] about our strategies a little bit. And
[00:13:48] the people watching this video already
[00:13:50] know, and they might be kind of thinking
[00:13:51] this is funny, but I kept it insanely
[00:13:53] simple. On day zero, when I was setting
[00:13:55] up this agent, I basically told it to
[00:13:57] spin up a team of sub aents and to
[00:13:59] research as much as they could. And I
[00:14:01] told it to act as my financial adviser,
[00:14:03] making a sprint for the next 30 days and
[00:14:06] just do whatever it thinks is best. I
[00:14:08] didn't give it any strategies
[00:14:09] beforehand. I just basically told it to
[00:14:11] do research like every 2 hours and make
[00:14:13] a plan and then execute trades
[00:14:14] throughout the day. So, that is what
[00:14:16] they ended up doing for me.
[00:14:17] >> Okay, I guess that's pretty good. I want
[00:14:18] to see how this keeps going. And as for
[00:14:20] my strategy, my one I just wanted to
[00:14:22] just, you know, see what can happen. And
[00:14:24] what I said was there's this thing
[00:14:26] called the Pareto principle where you
[00:14:28] buy a bunch of stocks and then you
[00:14:30] expect 80% of them to lose and 20% of
[00:14:32] them to do really really well. That's
[00:14:34] like how kind of like VC funds oper
[00:14:36] operate. So I was like, okay, let's try
[00:14:37] the riskiest thing possible in 30 days,
[00:14:40] how much money you can potentially make.
[00:14:42] That's why maybe you saw those crazy
[00:14:44] swings in my one. Honestly, for my own
[00:14:46] money, I would never do that. But just
[00:14:48] for the experiment, I thought that was
[00:14:50] really really fun.
[00:14:50] >> Yeah. And I mean, you still outperform
[00:14:52] the S&P as well, which is that's that's
[00:14:54] two huge wins for AI agents and and
[00:14:56] trading actually. Yeah. I'm very
[00:14:59] surprised even incredibly high-risk
[00:15:02] strategies outperform the S&P, which is
[00:15:04] kind of worrying to some trend.
[00:15:06] >> Yeah. I mean it will be really
[00:15:07] interesting to see if we just leave our
[00:15:09] agents running for another 2 3 months
[00:15:11] because you know typically it's a month
[00:15:13] is just too short of a time period to
[00:15:15] really know if a strategy is going to
[00:15:16] work or not. So I think I'll keep mine
[00:15:18] going if you want to keep it going and
[00:15:19] maybe we can you know meet back up in a
[00:15:21] few months here and do another video
[00:15:22] >> down. But what I was going to say is
[00:15:23] like okay right now I guess we saw a
[00:15:26] bunch of learnings. If we were to
[00:15:27] rebuild this bot what would you do
[00:15:30] differently? I think honestly at this
[00:15:32] point with the data that we have, the
[00:15:33] one thing I would have wanted to do
[00:15:35] differently is to change the strategy
[00:15:37] halfway through, you know, because we
[00:15:38] agreed to not touch anything. We agreed
[00:15:40] to just let our agents run. But with the
[00:15:42] things that were going on in the economy
[00:15:43] with major news drops, all I could do
[00:15:45] was I could sit and hope that the agents
[00:15:47] would be intelligent enough to do their
[00:15:48] research and to change the strategy. But
[00:15:50] there's probably some things that I
[00:15:51] might have wanted to tell it to make
[00:15:52] some adjustments [music] on. So that's
[00:15:54] kind of the only difference I would have
[00:15:55] made at this point given that it was
[00:15:57] only 30 days. And out of those 30 days,
[00:15:59] you know, only five out of seven of
[00:16:01] those were trading days. Okay, so as we
[00:16:03] wrap up here, there's two more things
[00:16:04] that I thought we should do. The first
[00:16:06] one is, how many total trades did your
[00:16:09] agent make over the course of the past
[00:16:10] month?
[00:16:11] >> My one made 61 trades in total, 33 buys
[00:16:16] and 28 sells.
[00:16:17] >> Okay, interesting. Mine made 20 straight
[00:16:20] up buys and 16 sells, but in my actual
[00:16:22] Alpaka account, there was 116 orders
[00:16:24] because it was doing stop losses. So,
[00:16:26] kind of similar though on on as far as
[00:16:28] like how often we were trading. But I I
[00:16:30] originally thought that you would come
[00:16:31] in and say, "Hey, I made like 200
[00:16:34] trades." I thought you were going to be
[00:16:35] like big time like day trading, swing
[00:16:37] trading, but looks like you didn't
[00:16:38] exactly take that approach.
[00:16:39] >> I would, but uh I remember I was reading
[00:16:41] this and maybe this is a limitation that
[00:16:43] people should know about. If they are
[00:16:44] using Alpaca, if you don't have a
[00:16:46] certain level or requirement, they block
[00:16:48] the amount of trades you can make.
[00:16:50] >> Oh, okay. That makes sense.
[00:16:51] >> Yeah. I remember my bot was trying to do
[00:16:53] that one day and then it got blocked.
[00:16:54] It's just like, okay, let me readjust my
[00:16:56] strategy. Interesting. Okay. And the
[00:16:58] second thing I'm curious about is just
[00:17:00] to end off the video. I asked my bot,
[00:17:02] knowing what it knows now, and if it
[00:17:04] could give advice to someone if they
[00:17:05] were trying to like set up something
[00:17:06] like this, what would you do differently
[00:17:08] or what would you tell them? Here's what
[00:17:09] mine said. I'll read it out the quick
[00:17:11] blurb. It said, "Go allin on energy from
[00:17:13] day one. Use 10% trailing stops instead
[00:17:15] of 2% and never touch shortdated
[00:17:17] options. One bad option trade costed us
[00:17:19] 550 bucks and without it we would have
[00:17:21] finished plus 5.3 in the green and we
[00:17:24] would have crushed the S&P and Salmon's
[00:17:26] trade bot. So that's what basically
[00:17:28] killed us being in the green apparently.
[00:17:29] >> That's super interesting. So my one was
[00:17:31] basically copy these politicians. It
[00:17:33] found this thing called capital trades
[00:17:35] and it saw that anyone like McCall
[00:17:38] recently has been outperforming S&P
[00:17:40] everybody by like several several
[00:17:42] percent. So that would be pretty
[00:17:44] interesting to do. But apart from that,
[00:17:46] I think if I were to do this again, I
[00:17:48] would use a strategy that I know that
[00:17:50] works really well. And I realized
[00:17:51] because I just got my options approval
[00:17:53] that there's this thing called the wheel
[00:17:55] strategy where if there's one stock that
[00:17:57] you like forever, let's say you wanted
[00:17:58] to go high, then you can use options to
[00:18:00] keep wheeling so you never like really
[00:18:02] lose that much money. So I might try
[00:18:04] that. Interesting. I actually made a
[00:18:05] video on how I would implement this
[00:18:08] exact wheel strategy and how to make
[00:18:10] these copy trading bots for the
[00:18:11] politicians with Claude. So maybe
[00:18:14] that'll be a fun video to watch, too.
[00:18:15] >> Awesome. Yeah. Well, definitely I'll put
[00:18:17] a link to that in the description of the
[00:18:18] video. All right. So, the last thing was
[00:18:20] about the actual challenge for you guys
[00:18:21] for this video. So, you've seen by now
[00:18:23] how you can enter by commenting on this
[00:18:25] video. And in about a week, we're going
[00:18:26] to follow up and post on both of our
[00:18:28] communities who won the $100 and then
[00:18:30] we'll get in touch with you and send you
[00:18:31] the reward. There it is right there. The
[00:18:33] the $100 from Salmon is going to be one
[00:18:36] of your [music] guys'. Awesome, guys.
[00:18:37] No, Nate, this was a really fun
[00:18:39] challenge. I'm actually really
[00:18:40] interested in seeing how this just
[00:18:42] performs over time and yeah, let's keep
[00:18:44] keep that going.
[00:18:45] >> Absolutely. Yeah, I'm gonna turn back on
[00:18:46] all the crown jobs for Bull, my trading
[00:18:48] bot, and we'll keep it going. Hopefully,
[00:18:49] I'll see you again in a few months. And
[00:18:50] thanks everyone for making it to the
[00:18:52] end. you enjoyed or you learned
[00:18:53] something new, please give it a like and
[00:18:54] we'll see you in the next