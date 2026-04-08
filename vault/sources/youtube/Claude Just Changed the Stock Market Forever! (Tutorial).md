---
author: '[[Samin Yasar]]'
channel_id: UCzGcYErpBX4ldvv0l7MWLfw
created: 2026-04-07
date: '2026-04-06'
description: "\U0001F91D Work with me \U0001F449 https://www.skool.com/claudeMy Resource
  Hub: https://www.skool.com/aianswersIf you like this video please subscribe so I
  can continue making more!-----------------------------✉️"
duration: 2106
language: en
published: 2026-04-06
source: https://www.youtube.com/watch?v=lH5wrfNwL3k&t=34s
status: processed
tags:
- trading
- claude-code
- mcp
- clippings
- options
- ai
- alpaca
title: Claude Just Changed the Stock Market Forever! (Tutorial)
topics:
- '[[Claude Code]]'
- '[[Algorithmic Trading]]'
- '[[MCP]]'
- '[[Wheel Strategy]]'
- '[[Options Trading]]'
---

## Summary

[[Samin Yasar]], ex-Amazon engineer and former JP Morgan employee, demonstrates how to use [[Claude Code]] with the [[Alpaca]] trading API to build automated stock trading bots. The video covers three levels of increasing sophistication.

### Key Takeaways

- **Level 1 - Setup**: Connect [[Claude Code]] to [[Alpaca]] paper trading (fake money, real market). Claude places trades via natural language -- "buy one share of Apple."
- **Level 2 - Trailing Stop Bot**: Build an automated bot that watches a stock, sets a floor price (stop loss), and drags the floor up as price rises. Claude checks every 5 minutes during market hours via scheduled tasks.
- **Ladder Buys**: If a stock drops significantly, Claude buys more shares at lower prices automatically, improving average cost.
- **Copy Trading Bot**: Track what US politicians and Wall Street whales are buying using [[Capitol Trades]]. Claude picked congressman [[Michael McCaul]] as the top active trader. Backtesting showed 34.8% return vs 15% S&P 500 -- a 2.2x outperformance.
- **Level 3 - Wheel Strategy**: An options income strategy where you act as the "insurance company." Sell puts to get paid while waiting to buy a stock at your price, then sell calls on owned shares. Collect premiums at every stage regardless of stock direction.
- **Why Claude Makes This Work**: The strategies aren't new, but execution and monitoring killed most retail traders. Claude handles all the management -- picking strike prices, rolling contracts, monitoring positions every 15 minutes.
- **[[MCP]] Integration**: Claude plugs into market data services via MCP to access institutional-level information about whale trades and congressional filings.

### Important Disclaimers
- Not financial advice
- All demonstrated with paper trading (fake money)
- Congress members must legally disclose trades, data is public via Capitol Trades

![](https://www.youtube.com/watch?v=lH5wrfNwL3k)

🤝 Work with me 👉 https://www.skool.com/claude  
My Resource Hub: https://www.skool.com/aianswers  
If you like this video please subscribe so I can continue making more!  
\-----------------------------  
✉️ For Business Inquiries: samin@bookedin.ai  
  
Hi 👋 I'm Samin. This channel is for you if you’re a business owner who wants to:  
→ Build a complete client acquisition system  
→ Scale your revenue while working less  
  
You may be feeling stuck, trying to figure out how to attract consistent leads, increase your sales, and grow your business without burning out.  
  
If that sounds like you I can help.  
  
But why even listen to me?  
I’ve have helped 200+ business use AI Automations generating and saving them millions (look at my case studies)  
My company was featured in Bloomberg business week for innovative use of AI Agents.  
I’m an Ex-Amazon software engineer with over 6 years of experience  
I have a computer science degree from NYU  
  
Timestamps  
0:00 Claude Just Changed Stock Trading Forever  
0:58 Context  
2:41 Level 1: Setting Up Claude & Alpaca  
3:46 Disclaimer + What Is Paper Trading  
4:10 Step 1: Download the Claude Desktop App  
4:51 Step 2: Create Your Alpaca Brokerage Account  
6:06 Generating Your API Keys  
7:30 Making Your First Trade With Claude  
9:15 Saving Your Credentials  
9:27 Level 2: Building an Automated Trading Bot  
10:05 How the Trailing Stop Strategy Works  
12:45 Setting Up the Trailing Stop Bot on Tesla  
15:21 Scheduling Claude to Run Automatically  
16:20 Testing Different Scenarios With Claude  
17:09 Adding Ladder Buys to Your Strategy  
18:19 The Problem With Gut Feeling Trading  
19:19 What Is Smart Money & Who Are the Whales  
19:57 How MCP Plugs Claude Into Insider Data  
20:38 McCaul vs S&P 500 — The Results  
21:30 Level 3: Setting Up the Copy Trading Bot  
22:07 Using Capitol Trades to Track Politicians  
23:38 Claude Picks Michael McCaul Automatically  
24:58 Level 3: Options & The Wheel Strategy  
25:14 What Is an Option? (Simple Explanation)  
26:23 Call Options Explained  
27:06 Put Options Explained  
27:35 How Selling Options Makes You the Insurance Company  
28:27 The Wheel Strategy Step by Step  
31:32 Why Most People Fail at the Wheel  
32:08 Building the Wheel Strategy Bot With Claude

## Transcript

### Claude Just Changed Stock Trading Forever

**0:00** · Claude has changed how we trade stocks forever, and it's because of this new skill that lets it access live market data, track what Wall Street whales and US politicians are buying, and use that to play the stock market with all that information automatically. I've actually been using this for the past couple of weeks, and it's completely changed how I think about trading. So, in this video, I'm going to be breaking down how you can get started in three levels. So, first, we're going to get set up. I'll walk you through the basics of how trading works, and we'll get Claude and all the tech set up. Then, we're going to be building a copy trading bot. I'm going to be showing you how to track what Wall Street whales and US politicians are buying, and have Claude copy their exact moves automatically. In level three, we're going to get into options. I'll break down what they are, how they work, and then we're going to be building a bot that runs one of the most consistent income strategies in trading called the wheel strategy. And even if you've never bought a single stock before or have zero technical background, you'll be able to do this because all we're going to be doing is simply speaking to Claude. Let's get into it.

### Context

**0:58** · Okay, before we get into anything, I need to give you some context on why I'm actually making this video and why this matters. Because for the first few years of my career, I used to work at JP Morgan. And I actually got to see how institutional trading works up close.

**1:11** · And the biggest thing I took away from that is the gap between Wall Street and regular people comes down to just three things. First, it's the data. So, imagine like a poker game, and you're sitting at a table with your two cards trying to figure out what to do. But the person across from you can see every card on the table and every card in your hand. You'd probably never sit down at that table, right? And that's the stock market. That's what you're playing against every single day. Wall Street knows when a billionaire places a massive bet on a stock. They know when a senator buys shares right before a major announcement. They see where the money is moving before you even hear about it on the news. And by the time you do hear about it, they've already made their money. So, you're stuck trading against people who have the information you don't have any access to. And unfortunately, that's the game. That's the kind of access that used to cost hundreds of thousands of dollars a year.

**1:57** · But now, I'll show you how to access that kind of information with a single click of a few buttons. Second is execution. Say you spot the perfect trade, but you're at lunch or you hesitate for like 10 minutes and the window closes. Wall Street doesn't deal with that. They have systems watching the market and placing trades around the clock automatically. And luckily, Claude can do that, too. Which brings us to number three, which is intelligence.

**2:19** · Having the data and the speed really means nothing if you don't have a plan.

**2:23** · The big guys have teams reading all that information and making calculated decisions. And to do all of that, you need to buy expensive tools. And if you couldn't afford the tools, you were locked out. But with Claude and these new skills, that barrier is gone. And I'm going to show you how to set all of that up.

### Level 1: Setting Up Claude & Alpaca

**2:41** · All right, let's build this thing. I'm going to be explaining everything as we go. So, if you're brand new, just follow along. So, if our goal is to get Claude to trade stocks for us, to do that, Claude needs two things. It needs somewhere to place the trades, and it needs the information to decide what to trade. Let's start with the first one.

**2:58** · And actually, back in the day, if you wanted to buy a stock, you'd have to call a person on the phone and say something like, I don't know, buy me 50 shares of IBM. That person was go to the stock exchange and make that happen for you. That whole system, the firm, the person, the access to the exchange, that's called a brokerage. But today, it's an app. You open up Robinhood or Fidelity or tap a button and you own a stock. That's the same concept with just no phone call. But here's where it gets interesting for us. Some brokerages actually let you skip that step entirely and connect it through code. And because Claude is so good at coding, that's what we need. Because we're not going to be the ones trading, Claude is. And we're going to be using a tool today called Alpaca. It's free to sign up, and it gives you API access, which is how we're going to get Claude to connect to it and place trades on our behalf. So, let me show you how to do that. Wait, but more importantly, before we get any further, quick disclaimer, I'm not a financial advisor. This is not financial advice.

### Disclaimer + What Is Paper Trading

**3:52** · I'm just showing you how to build cool stuff with AI. And everything we're doing today is in paper trading. And paper trading means that you're using fake money in a real market. So, it's the same stocks, the same prices, everything behaves the same way. You're just not risking a single dollar. Okay, so let's connect Claude to our brokerage.

### Step 1: Download the Claude Desktop App

**4:10** · Okay, so to get started, what we're going to need first is the Claude desktop app, all right? So, I'm going to do Claude uh dot com {slash} download.

**4:20** · And if you need any of these links, it's going to be in the link in the description below. If I'm going here, and you see you just want to download this app, and you can use it for Windows or Mac. But make sure you download the Claude desktop app, okay? All right, so after you install the app, you'll get something that looks like this. Make sure your software or your Mac OS is up to date so you have everything available. And ideally, you have the pro or the max version of Claude paid for, okay? So, that's step number one. Step number two is we need to make our brokerage account. So, I'm going to go back into my browser, and I'm going to search up Alpaca. Uh And you can see Alpaca trading platform.

### Step 2: Create Your Alpaca Brokerage Account

**5:05** · And I'm going to go here, and I'm going to sign up. All right, so after you enter all your information and you go through, you're going to see you have this dashboard right here.

**5:15** · And in this dashboard, if I go to the top left and I open this up, and you see I have an individual trading account.

**5:21** · But everything we're going to be doing is not with real money, it's with paper money. So, what we're going to be using is this paper trading account, okay? And you can, you know, if you want to make a new one, I'm going to say um trading Claude.

**5:37** · And let's say we can give ourselves, I don't know, $50,000, okay?

**5:43** · And save. And you can see right there, we're going to have a trading Claude account, and I'm going to click this.

**5:48** · So, now I have $50,000 to essentially play with in the stock market, all right? Now, I'm going to show you how to get this connected with Claude. To get this connected with Claude, what we're going to do is I'm going to scroll down right here, and you see right here where it says API keys.

### Generating Your API Keys

**6:06** · What we want to do is hit generate new API keys, okay?

**6:10** · And you can see there's three things.

**6:12** · Endpoint, key, and secret. We're going to need all three of these, all right?

**6:17** · So, let's get Claude set up. So, I'm going to go back to my Claude app.

**6:21** · And here, what I want you to do right now is hit this thing that says code, okay? It's the same thing, we're just going to be talking to it.

**6:30** · But all \[snorts\] it is is a little bit of a different interface. Okay. So, cool. We see this little guy here, and that means we're good to go. And I'm going to do is right here, I want you to hit this button right here and hit a new folder.

**6:44** · Okay. Because we want to keep everything we're doing organized, I'm going to go to documents, and I'm going to hit new folder. And I'm going to call it trading.

**6:52** · Okay. So, now everything we do is going to be saved into this trading folder, all right?

**6:59** · Okay, I'm going to move this to the side. Now, what I'm going to do is I'm going to be pasting in right here this, then go back to Claude, and then say endpoint.

**7:11** · I'm going to say key.

**7:13** · Oops.

**7:15** · Claude key.

**7:21** · And then I'm going to say copy this one, and then go to Claude, and then say secret.

**7:28** · Okay. Now, let's see if we can get our Claude to trade a simple stock just to make sure our connection is solid. And after our connection is solid, we'll build layers on top of that so we can actually get it to do some really cool stuff, right? All right. So, what I'm going to be telling it is this.

### Making Your First Trade With Claude

**7:46** · Hey.

**7:47** · Um what I want you to do, I just gave you the documentation and my keys to connect to my Alpaca trading account.

**7:56** · I'm just testing the connection right now. Can you please buy one share of Apple? I want to see it inside my account, all right?

**8:10** · Great. So, all this is good. Uh right now, just to make it a little faster, I'm going to write here click sonnet because this is very easy command, and I'm going to hit go.

**8:22** · All right, so it's saying the order is placed successfully. Here's the summary.

**8:26** · Now, if I go back here, if I reload, okay, awesome.

**8:30** · Uh great. So, you see I already bought a share of Apple. Now, you can trade by just talking to it. You'll be like, Hey, can you sell that share of Apple and then buy a share of Tesla?

**8:45** · Great. Press workspace, and here. This is what I want you to do as well.

**8:50** · Hey, can you make sure in this folder you save these credentials so I don't have to keep giving it to you when we want to trade. We're going to be using this account, and in this folder, we're going to be doing a lot of trades.

**9:03** · Okay, so what we're going to do is because right here we gave it access to all the stuff, I want to make sure I don't have to keep giving it access. I'm just getting it to save these credentials inside a file. Right now, Claude can trade, but it's trading blind. It doesn't know what to buy, when to buy, or why. It's missing the most important piece, which is strategy. So, let's get into that.

### Saving Your Credentials

### Level 2: Building an Automated Trading Bot

**9:27** · In this level, we're going to turn Claude into something that runs on its own. So, basically a bot that watches the market, makes its own decisions, and based on the rules you set. And the first strategy we're going to make, you can think of it like a smart thermostat.

**9:39** · Once you set the rules, if the room temperature, let's say, drops below 68° F, you're going to turn on the heat. If it goes above 75° F, you kick on the AC.

**9:47** · That means you don't have to sit there fiddling with your phones, messing with the temperature all day. The thermostat does that all for you. It checks, it acts, and adjusts. And the bot is going to work exactly the same way. That means we're going to be setting some rules, and let me show you how this works by actually explaining the trailing stop strategy, which is a really good strategy used by many different traders.

### How the Trailing Stop Strategy Works

**10:05** · Let me show you how the trailing stop strategy actually works. So, say you buy a stock at $100.

**10:12** · Well, let's say we tell Claude, "If this drops to $95, sell it. That's your floor. $5 is the most you're willing to risk on this trade." Now, if the stock starts climbing up, and let's say hits 110, if it didn't go down, but your floor is still sitting at that 95, then you're exposed to a $15 fall. That makes no sense. So, what we want is Claude to move up our floor to 105, which means if the stock dips and hits the new floor, you're still up $5 in profit, and you were protected the entire time. But, what if the stock drops right out the gate, right? Well, that means it would just hit $95, and you'd sell it, and you're out $5, and that's your loss.

**11:08** · Now, here's the important part. You're not stuck. You've still got that capital. Claude can now take that money and goes looking for the next setup.

**11:17** · Maybe it's the same stock a week later at a better price. Maybe it's a completely different opportunity. The point is you lost a small portion that you're okay to lose and risk. Basically, you live to trade another day. And ideally, we find trades like this. So, let's say the stock keeps climbing, and every time it does, Claude is going to drag the floor higher and higher. You can never fall back to where you started. It's basically now going to sell at 110, so you get that $10 in profit, which is a 10% gain. That's a trailing stop. You set the rules once, and Claude follows them every second of the day. You're always protected, and you're always locking in the gains. So, when a trade doesn't work out, you move on fast with the most amount of money still in your pocket. Now, why am I telling you all of this? Because the worst thing you can really do is hand your AI a pile of money and be like, "Go figure it out." The rules aren't the limitation. That's the whole point. This is how you take what you know, your instincts, your risk tolerance, your read on the market, and you encode it. The same rules are true here. Claude can execute thousands of decisions faster than any human. It's executing your decisions, just running at the speed and discipline that you never could on your own. That's what makes this different from just letting AI loose. And I'll show you how to set this all up in the next portion. And to set this up, it's actually really simple.

### Setting Up the Trailing Stop Bot on Tesla

**12:46** · So, I'm just back in my chat where I have been speaking with my Claude, and I'm just going to be speaking to it, right? And just to make it a little easier, if you guys wanted this, in my classroom, uh if you guys are already watching this, if you go to skills, you'll see I have a bunch of skills here. So, this is the prompt we're essentially going to be speaking to our Claude, all right? So, let me just go to Claude, and right now, don't worry about it. If you want those docs, it's there, but you can follow along with me in this video. So, I'm just going to speak it to it.

**13:17** · All right. So, I want your help to actually schedule a trailing stop strategy on, let's say, Tesla, right? I want you to buy Tesla using Alpaca paper trading account. Buy, I don't know, like 10 shares at the market price right now, and set up these rules. The floor, if the stock drops, let's say, by 10%, sell everything. That's my stop loss. I don't want to lose more than that on this trade. The trailing floor, if the stock goes up 10% from what I paid, move my stop loss up.

**13:50** · Maybe move it up 5% below the current price. Every time it climbs, move another 5% up the floor again. So, the floor only goes up, never down. And then, I want you to also ladder in. If the stock drops, let's say, by over 20, 30%, buy a bunch more shares, let's say, 10 more shares. If it drops by, let's say, 20%, buy 20 shares. This way I'm getting better prices on the way down instead of just losing money. And after you set this up, show me a summary of every order and right after you place it, so I can confirm this looks right.

**14:29** · Okay. So, I word vomited some stuff there, \[laughter\] and um let this finish, and I'll show you what this looks like.

**14:37** · So, I see it just got done, and it says this is the current price. And if I go back to my Alpaca dashboard, I can see it set some price, it bought some Tesla, and then it even set a stop loss right here. Now, one more thing we need to do is make sure we go back here and be like, "Hey, can you set up during market hours every day that you're checking consistently when we need to move our floor up or need to make new stop losses or re-enter. Use the slash schedule to make sure we have that going."

**15:17** · And set your own schedules.

### Scheduling Claude to Run Automatically

**15:21** · So, this just executed one trade. Now, what I want is Claude to basically be alive and keep looping and checking on a schedule like, "Hey, are these trades looking right? Do I need to re-enter? Do I need to move my floor up?" All of that stuff. Normally, we would have to do it, but right now, with the command I just gave it, it should be able to do it on its own.

**15:44** · Okay. So, it just got done, and it says literally Tesla trailing stop monitor, and it's going to be doing that every 5 minutes from Monday to Friday, 9:00 a.m., and it's going to keep checking.

**15:56** · And just so you're clear, on the left-hand side, if you hit see this clock, if you hit this clock, it's a scheduled. And if you open it up, these local tasks are already going to be running right here. You can see it already set the schedule for me. I didn't have to touch this, and if my computer is on, it's going to be running this on its own. Now, we have basically made a trading bot. Now, let's go through a couple different scenarios.

### Testing Different Scenarios With Claude

**16:25** · Hey, so just briefly and really quickly, can you tell me what would happen if, let's say, Tesla shoots up to $500 randomly. What would you do?

**16:39** · And right now, I'm role-playing it just so you understand, and I encourage you to do this as well, so you understand what would happen in different scenarios, and what would it actually do. And if you do really need to change its thinking and thought processes around, you just be like, "Hey, change this around, okay?" And right here, it's just done. It says, "If Tesla shoots to 500 on the way up, the trailing stops kick in, trailing activates, your floor moves up, up, up, etc."

**17:08** · And that's about it.

### Adding Ladder Buys to Your Strategy

**17:09** · Yeah. This is a really cool way to do ladder buys. Those don't trigger at all.

**17:15** · You see, right now, I don't have any of them. So, I'm going to be like, "Can you think about what are good ladder buys, and make sure you set that up in the schedule and update the strategy inside our whole strategy of what we're trading right now?"

**17:32** · So, as the price goes up, it buys in gradually, so we're always at somewhat of a profit, and we're pretty safe in our buys. And just so you see, it even gave me the ladder levels of if it's -15%, it's going to buy 10. If it's 50%, it's going to buy 50. You can always change this around, but this is really cool. Now that me, without me having to do any of the stuff, Claude can just action it for me. Now, this is all great, but the thing is, we're still picking stocks ourselves. We choose Tesla because we like it, but that's a gut feeling. The biggest traders and the best traders in the world don't trade on gut feelings. They trade on information.

**18:11** · So, in the next level, we're going to be showing Claude where the smart money is, so Claude can actually make informed decisions.

### The Problem With Gut Feeling Trading

**18:19** · But, what is smart money? Well, on Wall Street, there are people who move millions of dollars in a single trade.

**18:26** · When someone puts, let's say, $50 million into a stock, they didn't really just do that off a gut feeling or flipping a coin. They have a lot of research teams and a lot of private data. They know something. These people are called whales. And when these whales make a big move, it leaves a trail, like massive options orders, unusual volumes on a stock out of nowhere. And a group that does this a lot is, surprisingly, US politicians. But, the nice part is that the members of Congress are required by law to report their stock trades. The data shows that many of them consistently beat the market. They sit on committees, they regulate entire industries, they get briefed on policy changes before the public even hears about them. They know which companies are about to get a government contract, and which ones may get investigated.

**19:17** · But, you can see what they bought and follow them. And most people have no idea this data exists, but it's there, and Claude can read it. But, the thing is, we can't just tell Claude to go scour the internet for these hedge funds trades and congressional filings and all that. There's millions of data points hitting the market every single day. No AI can really browse its way through all of that. But, there are services that do this full-time. These companies are scraping and organizing all this data around the clock. And the data is sitting there waiting to be tracked and updated every day. And what we need to do is plug Claude into that. And that's what this new skill and MCP does.

### What Is Smart Money & Who Are the Whales

### How MCP Plugs Claude Into Insider Data

**20:00** · Think of it like a power outlet. The electricity, the insider information, is running through those walls, and we basically plug our Claude into that so we can use it. These services have data flowing through their systems, and the MCP is the plug that connects Claude to their data. And once it's plugged in, Claude can pull from it anytime, it becomes a new skill, and Claude goes from being smart but working with nothing to being smart and seeing what the big players in the market see.

**20:30** · Next what we're going to do is give our Claude the power to access these services, and it's going to be super easy. So, let's get into that. And just to emphasize why I'm so excited about this strategy I'm about to show you, this is me just backdating, let's say a year ago, you were copying the same thing and the same strategy by copying the smart money.

### McCaul vs S&P 500 — The Results

**20:52** · You can see, if you were following the S&P 500, you were just buying and holding it, you would have made around starting at a 50k account, you would have made around 57,750, which is around 15%. So, you would have made 15% more money. But, if you copied Mcaw, then you would have made 67,400 by the end of the year, which is a 34.8% return. You can see how these politicians have access to this insider information, and they can outcompete everybody. And that's what I'm going to show you how to do. And just to make sure our strategies are organized, what I'm going to do is go to another paper trading account. So, right here, I'm going to use this Saman account. And I'm going to do the same thing.

### Level 3: Setting Up the Copy Trading Bot

**21:43** · Okay?

**21:43** · So, I'm going to hit generate keys. I'm going to take all of the stuff, or I can just copy and paste this.

**21:49** · And then, I can go back to my Claude.

**21:54** · And then, what I'm going to do now is make a new session. So, I'm going to hit new session, and I'm going to paste this in.

**22:00** · And now, what I'm going to do is the service we're going to use to track these politicians, if you go to Google, I'm going to do Capitol Trades, and Capitol Trades is a free service that you can be using to see which politician is trading what and what's going on. So, I'm going to copy this URL, I'm going to go back to my Claude and go right here. Okay. So, now, uh by the way, the prompts are going to be in the description below, but right now, hey. So, um I'm trying to set up a copy trading bot when I've also given you access to my Alpaca account. I want you to make a new folder inside this uh folder so we can have this running and have these schedules done. But, what I want you to do is number one, find a politician who has been having really good success in the stock market currently and is actively trading.

### Using Capitol Trades to Track Politicians

**22:57** · And then, what I want you to do is copy their trades. Okay? So, set up your cron jobs and your schedules so you're always looking and using Capitol Trades to see what they're up to, and copy those trades. Make sure you buy, sell, buy the same options that they knew, whatever you need to, just copy them, and then we're going to be tracking that over time. All right?

**23:21** · And you're going to be using the Alpaca account that I just posted the image of.

**23:28** · Right. I'm going to hit bypass permissions, enter bypass mode, and then hit enter. All right, that was super easy. Let me wait for this to finish, and we can see what's going on.

### Claude Picks Michael McCaul Automatically

**23:38** · Okay, so it just got done, and I see in my schedule it's already set a schedule to see what these \[clears throat\] politicians are doing. And then, I actually also asked it, "Who are you copy trading and why?" And it chose Michael Mcaw.

**23:55** · All right, very interesting. And why is basically Okay.

**24:00** · \[snorts\] And why the algorithm picked him over the others? Because it seems like he is very active right now, and he's the top trader.

**24:07** · Interesting. The trades may be slightly stale, but that's the nature of how they disclose. We still get a lot of gains because mostly Congress can buy like 2 years out or something like that. So, they don't do day trading, and they're not allowed to do it. That's why, even if we're a little late because we know about it later, we can still make those gains. And just to reiterate, you can see this is a simulation for the year if we started 1 year ago and did this exact same thing. If we copied this exact same strategy, this bot would have made an extra 9,650 dollars in comparison to the S&P, which would have only made around $7,000.

**24:49** · So, that's a 2.2x return over the S&P 500, and that's how these guys just stay so rich. It's kind of crazy. So, with that out of the way, now I'm going to show you the third strategy, which is a strategy that really advanced people use, which means you can get paid no matter which direction the stock moves.

### Level 3: Options & The Wheel Strategy

**25:10** · And to understand that, I'm going to explain how options work. Okay, so what is an option? Well, an option is basically a contract when two people agree to do a deal. And let me show you this with something you already may know. Okay, so let's say you pay your car insurance company $100 a month. In exchange, you get the right to file a claim if something goes wrong. And if you crash, the insurance covers it, you're protected. And if nothing happens, they keep your 100 bucks.

### What Is an Option? (Simple Explanation)

**25:36** · They're basically getting paid to take on the risk. Now, look at this exact same structure. What happens is you pay a premium to another trader where you get the right to buy or sell a stock at a locked price. Okay?

**25:49** · And if the stock moves your way, you can exercise that contract and profit. If the stock doesn't move your way, the contract will expire, they keep your premium. It's the same deal, you basically paid for protection.

**26:04** · They got paid for the risk. And here it is, next to each other, row by row. It's identical. The premium, the right to act, the expiration date, and if nothing happens, the other side keeps your money. That's all an option is, insurance on a stock. Okay? And to dive in, there are only two types of options.

### Call Options Explained

**26:23** · A call option gives you the right to buy a stock at a locked-in price. Say Apple is at $200, you can buy a call option with a strike price of 210. That means if Apple goes to, let's say, 230 before your contract expires, you can buy it at 210 and pocket that $20 difference.

**26:46** · If Apple stays below 210, your contract expires and you lose the premium you paid. That's your max loss. Think of it like putting a deposit on an apartment, you'll pay $500 to lock in the rent for $2,000 for 30 days. If the rent price jumps to $2,500, you got a deal. If they don't, you lost that $500 deposit. And on the other side is a put option. The put option gives you the right to sell a stock at a locked-in price. Say you own Apple at $200, you buy a put option with a strike price of 190. If Apple drops to 170, you can sell it at 190 instead of 170. The put basically protected you from the drop.

### Put Options Explained

**27:29** · That's the insurance side. You paid a premium to protect yourself against the price drop. Why this is interesting is because with stocks and options, you can actually flip the table and become the insurance as well. So, that is called selling options. So, when you sell an option, you basically become the insurance company. You're the one that's collecting So, someone pays you for a contract, and most of the time, that contract expires without anything happening, and you keep the money. And the cool part is the insurance companies make billions doing this. They collect premiums after premiums from millions of people and pay out on a small percentage of claims. The math basically works in their favor over time.

### How Selling Options Makes You the Insurance Company

**28:14** · And selling options basically work the same way, where you collect a premium up front, and if the stock doesn't hit the strike price by the expiration, your contract dies and you keep everything you were paid.

### The Wheel Strategy Step by Step

**28:27** · And the wheel strategy is built on selling options. You are the insurance company. You collect premiums at every stage. And let me show you how that works. Okay, so let's walk through the wheel strategy with a real example with, let's say, Tesla. So, Tesla is trading at $250.

**28:45** · And let's say you really like the stock, but you're not paying 250 for it. You'd rather get it at, let's say, 230. So, if you sell a put at the 230 strike, and for making that promise, for saying, "I'll buy Tesla at 230 if the price drops there," someone is going to hand you $5 per share. That's $500 in your pocket right now just for agreeing to do a deal you already wanted. Now, two things can happen. Tesla can stay above 230, which means the contract might expire, nobody makes you buy anything, and you get to keep the $500, and you can do it again the next week. The other scenario is Tesla drops below 230, and you have to buy it. But remember, you collected $500 before already. So, your real cost isn't 230, it's 225. You got Tesla cheaper than anyone else, and you wanted it anyways. Okay, so stage two, let's say Tesla does drop and you get assigned, which means you have to buy the Tesla shares. Now, you own 100 shares at an effective cost of 225. Most people would be upset, but you're not because you set the price. You got paid to wait and you bought it at a discount, right? That's not a loss, that's a your plan working.

**30:07** · Now, it's time for stage number two.

**30:10** · Okay, now that we own the shares and they're sitting in our account, what we're going to do is we're going to sell a covered call, which means we will pick a 260 strike price. That means someone is going to pay us another $5 per share, which is another $500 for the right to buy your Tesla shares for 260. If Tesla stays below 260, that contract expires, you keep the shares and you keep the $500. And you can sell that call again the next week. This is cool because you're generating income from a stock that isn't even moving. Because if Tesla does go above 260, your shares get sold, but look at the math. So, let's say you bought the Tesla shares at 225. You sold it at 260. That's a $35 per share in stock gains, plus the $5 you collected selling that put, plus the $5 you collected selling the call. That's $45 per share in total profit on 100 shares.

**31:11** · That's $4,500.

**31:13** · And here's the best part. Once your shares get called away, you go right back to stage one. You sell another put, collect another premium, and the wheel just keeps spinning. Every single rotation, you get paid. The stock can go up, down, sideways, it doesn't matter. You're collecting income at every stage.

### Why Most People Fail at the Wheel

**31:32** · The wheel strategy sounds great until you try to run it for yourself. You're picking strike prices based on your market conditions and all these other things every single week. Most people who learn about this wheel give up after a few weeks because management is what buries them. And the cool part about Claude and I'm what I'm about to show you is that Claude handles all of it, which means Claude itself can monitor the positions, pick expirations, and roll contracts when needed. Which means you just collect the premiums on a schedule and you'll check in, let's say, once a day.

### Building the Wheel Strategy Bot With Claude

**32:08** · So, with that out of the way, understanding why Claude makes this so effective, let's set one up. Okay, so for this we're going to be using the first trading Claude account. And I'm going to go back to Claude and you see I actually have a prompt right here that you can copy-paste. And just so you can follow along, I'll read it out to you, okay?

**32:32** · So, what this is is basically I want you to run a wheel strategy on, let me see, Tesla using my Alpaca trading account. Stage one, you sell the puts, so you sell a cash-secured put on Tesla with a strike price around 10% below the current price. Pick an expiration two to four weeks out, collect the premiums.

**32:58** · If the put expires worthless, sell another one and keep collecting premiums. If I get assigned, I have to buy the stock, move to stage two. Stage two is selling the calls. Once I own the shares, sell covered calls with a strike price around 10% of above what I paid. Pick an expiration maybe two to four weeks out, collect the premium. If the call expires worthless, sell another.

**33:25** · Keep collecting premiums. If my shares get called away, like sold, go back to stage one and start again. And the rules are never sell a put unless I have enough cash to buy the shares if assigned, and never sell a call below my cost basis, what I actually paid. And track my premium across all cycles and check my positions every 15 minutes during market hours. Please set the schedule.

**33:51** · If a contract hits 50% profit before expiration, close it early and give me a daily summary at market close, all right? Run this during market hours, do nothing outside market hours.

**34:02** · Great.

**34:03** · That's what that prompt was. Now, I'm going to hit enter and wait.

**34:08** · But, that's about it. You're going to see after this is done, I'll show you in a bit, it's going to set the things in a schedule, it's going to keep running this, and I encourage you to maybe set up a paper trading account and then have a go at it, see how it will do. These are just some fun strategies that I've been playing with that I think have been pretty useful and super revolutionary of what we can really do with Claude. But, you know, if you're watching this and you can see the power of Claude, but haven't used it before or you you tried it, but you're not sure how to get the most out of it, I'm actually putting together a full course that's going to walk through everything from scratch, how to set up Claude, how to use it, how to build projects like this one step by step. So, stay subscribed for that. And in the meantime, watch this video if you want to see me going deeper of any of these strategies or build something else together, join my Claude Club where we can do this and we'll have some fun.

---

## Transcript

[00:00:00] Claude just has changed how we trade
[00:00:01] stocks forever. And it's because of this
[00:00:03] new skill that lets it access live
[00:00:05] market data, track what Wall Street,
[00:00:07] Wales, and US politicians are buying and
[00:00:09] use that to play the stock market with
[00:00:11] all that information automatically. I've
[00:00:13] actually been using this for the past
[00:00:14] couple of weeks and it's completely
[00:00:16] changed how I think about trading. So,
[00:00:18] in this video, I'm going to be breaking
[00:00:19] down how you can get started in three
[00:00:21] levels. So, first we're going to get set
[00:00:23] up. I'll walk you through the basics of
[00:00:24] how trading works and we'll get Claude
[00:00:26] and all the tech set up. Then we're
[00:00:28] going to be building a copy trading bot.
[00:00:30] I'm going to be showing you how to track
[00:00:31] what Wall Street whales and US
[00:00:32] politicians are buying and have Claude
[00:00:34] copy their exact moves automatically.
[00:00:36] And level three, we're going to get into
[00:00:38] options. I'll break down what they are,
[00:00:39] how they work, and then we're going to
[00:00:41] be building a bot that runs one of the
[00:00:43] most consistent income strategies in
[00:00:45] trading called the wheel strategy. And
[00:00:47] even if you've never bought a single
[00:00:49] stock before or have zero technical
[00:00:50] background, you'll be able to do this
[00:00:52] because all we're going to be doing is
[00:00:54] simply speaking to Claude. Let's get
[00:00:55] into it.
[00:00:58] Okay, before we get into anything, I
[00:01:00] need to give you some context on why I'm
[00:01:02] actually making this video and why this
[00:01:03] matters. Because for the first few years
[00:01:05] of my career, I used to work at JP
[00:01:07] Morgan and I actually got to see how
[00:01:08] institutional trading works up close.
[00:01:11] And the biggest thing I took away from
[00:01:12] that is the gap between Wall Street and
[00:01:14] regular people comes down to just three
[00:01:16] things. First, it's the data. So,
[00:01:18] imagine like a poker game and you're
[00:01:19] sitting at a table with your two cards
[00:01:21] trying to figure out what to do, but the
[00:01:23] person across from you can see every
[00:01:25] card on the table and every card in your
[00:01:27] hand. You'd probably never sit down at
[00:01:29] that table, right? And that's the stock
[00:01:31] market. That's what you're playing
[00:01:32] against every single day. Wall Street
[00:01:34] knows when a billionaire places a
[00:01:36] massive bet on a stock. They know when a
[00:01:38] senator buys shares right before a major
[00:01:40] announcement. They see where the money
[00:01:42] is moving before you even hear about it
[00:01:43] on the news. And by the time you do hear
[00:01:45] about it, they've already made their
[00:01:47] money. So, you're stuck trading against
[00:01:48] people who have the information you
[00:01:50] don't have any access to. And
[00:01:52] unfortunately, that's the game. That's
[00:01:53] the kind of access that used to cost
[00:01:56] hundreds of thousands of dollars a year.
[00:01:58] But now, I'll show you how to access
[00:01:59] that kind of information with a single
[00:02:00] click of a few buttons. Second is
[00:02:02] execution. Say you spot the perfect
[00:02:05] trade, but you're at lunch or you
[00:02:06] hesitate for like 10 minutes and the
[00:02:08] window closes. Wall Street doesn't deal
[00:02:10] with that. They have systems watching
[00:02:12] the market and placing trades around the
[00:02:14] clock automatically. And luckily, Claude
[00:02:16] can do that, too. Which brings us to
[00:02:18] number three, which is intelligence.
[00:02:20] Having the data and the speed really
[00:02:21] means nothing if you don't have a plan.
[00:02:23] The big guys have teams reading all that
[00:02:26] information and making calculated
[00:02:27] decisions. And to do all of that, you
[00:02:29] need to buy expensive tools. And if you
[00:02:31] couldn't afford the tools, you were
[00:02:33] locked out. But with Claw and these new
[00:02:35] skills, that barrier is gone. And I'm
[00:02:37] going to show you how to set all of that
[00:02:39] up.
[00:02:41] All right, let's build this thing. I'm
[00:02:42] going to be explaining everything as we
[00:02:44] go. So, if you're brand new, just follow
[00:02:46] along. So, if our goal is to get Claude
[00:02:48] to trade stocks for us, to do that,
[00:02:50] Claude needs two things. It needs
[00:02:52] somewhere to place the trades, and it
[00:02:54] needs the information to decides what to
[00:02:56] trade. Let's start with the first one.
[00:02:58] And actually, back in the day, if you
[00:02:59] wanted to buy a stock, you'd have to
[00:03:01] call a person on the phone and say
[00:03:02] something like, I don't know, buy me 50
[00:03:04] shares of IBM. That person was go to the
[00:03:06] stock exchange and make that happen for
[00:03:08] you. That whole system, the firm, the
[00:03:10] person, the access to the exchange,
[00:03:12] that's called a brokerage. But today,
[00:03:14] it's an app. You open up Robin Hood or
[00:03:16] Fidelity or tap a button and you own a
[00:03:18] stock. That's the same concept with just
[00:03:20] no phone call. But here's where it gets
[00:03:22] interesting for us. Some brokerages
[00:03:24] actually let you skip that step entirely
[00:03:27] and connect it through code. And because
[00:03:29] Claude is so good at coding, that's what
[00:03:31] we need because we're not going to be
[00:03:33] the ones trading. Claude is. And we're
[00:03:35] going to be using a tool today called
[00:03:37] Alpaca. It's free to sign up and it
[00:03:39] gives you API access which is how we're
[00:03:41] going to get Claw to connect to it and
[00:03:42] place trades on our behalf. So, let me
[00:03:44] show you how to do that. Wait, but more
[00:03:46] importantly, before we get any further,
[00:03:48] quick disclaimer. I'm not a financial
[00:03:50] adviser. This is not financial advice.
[00:03:52] I'm just showing you how to build cool
[00:03:54] stuff with AI. And everything we're
[00:03:55] doing today is in paper trading. And
[00:03:57] paper trading means that you're using
[00:03:59] fake money in a real market. So, it's
[00:04:01] the same stocks, the same prices,
[00:04:02] everything behaves the same way. You're
[00:04:04] just not risking a single dollar. Okay.
[00:04:05] So, let's connect Claude to our
[00:04:07] brokerage.
[00:04:10] Okay. So, to get started, what we're
[00:04:11] going to need first is the Claude
[00:04:13] desktop app. All right. So, I'm going to
[00:04:14] do claude uh.com/d
[00:04:18] download.
[00:04:20] And if you need any of these links, it's
[00:04:22] going to be in the link in the
[00:04:22] description below. If I'm going here and
[00:04:25] you see you just want to download this
[00:04:27] app and you can use it for Windows or
[00:04:30] Mac, but make sure you download the
[00:04:33] cloud desktop app. Okay. All right. So
[00:04:34] after you install the app, you'll get
[00:04:36] something that looks like this. Make
[00:04:38] sure your software or your Mac OS is up
[00:04:41] to date so you have everything available
[00:04:43] and ideally you have the pro or the max
[00:04:47] version of Claude paid for. Okay, so
[00:04:50] that's step number one. Step number two
[00:04:52] is we need to make our brokerage
[00:04:54] account. So I'm going to go back into my
[00:04:57] browser and I'm going to search up
[00:04:59] Alpaca. Uh,
[00:05:02] and you can see Alpaca Trading Platform
[00:05:05] and I'm going to go here and I'm going
[00:05:07] to sign up. All right. So, after you
[00:05:09] enter all your information and you go
[00:05:11] through, you're going to see you have
[00:05:13] this dashboard right here. And in this
[00:05:15] dashboard, if I go to the top left and I
[00:05:17] open this up and you see I have an
[00:05:20] individual trading account, but
[00:05:22] everything we're going to be doing is
[00:05:23] not with real money. It's with paper
[00:05:25] money. So, what we're going to be using
[00:05:28] is this paper trading account. Okay? And
[00:05:30] you can, you know, if you want to make a
[00:05:32] new one, I'm gonna say, um, trading
[00:05:36] claude. And let's say we can give
[00:05:38] ourselves, I don't know, $50,000.
[00:05:41] Okay. And save. And you can see right
[00:05:45] there, we're going to have a trading
[00:05:47] clot account. And I'm going to click
[00:05:48] this. So now I have $50,000
[00:05:52] to essentially play with in the stock
[00:05:54] market. All right. Now, I'm going to
[00:05:56] show you how to get this connected with
[00:05:58] Claude. To get this connected with
[00:06:00] Cloud, what we're going to do is I'm
[00:06:01] going to scroll down right here. And you
[00:06:03] see right here where it says API keys.
[00:06:06] What we want to do is hit generate new
[00:06:08] API keys. Okay. And you can see there's
[00:06:11] three things, endpoint, key, and secret.
[00:06:15] We're going to need all three of these.
[00:06:16] All right. So, let's get cloud set up.
[00:06:19] So, I'm going to go back to my cloud
[00:06:20] app.
[00:06:22] And here, what I want you to do right
[00:06:23] now is hit this thing that says code.
[00:06:26] Okay. It's the same thing. We're just
[00:06:28] going to be talking to it, but [snorts]
[00:06:30] all it is is a little bit of a different
[00:06:32] interface. Okay. So, cool. We see this
[00:06:35] little guy here. And that means we're
[00:06:36] good to go. And I'm going to do is right
[00:06:39] here, I want you to hit this button
[00:06:41] right here and hit a new folder. Okay?
[00:06:45] Because we want to keep everything we're
[00:06:46] doing organized. I'm going to go to
[00:06:48] documents and I'm going to hit new
[00:06:49] folder. And I'm going to call it
[00:06:51] trading.
[00:06:52] Okay? So now everything we do is going
[00:06:56] to be saved into this trading folder.
[00:06:58] All right. Okay. I'm going to move this
[00:07:00] to the side. Now what I'm going to do is
[00:07:03] I'm going to be pasting in right here
[00:07:06] this. And then go back to claude and
[00:07:08] then say end point.
[00:07:11] I'm going to say key.
[00:07:14] Oops.
[00:07:16] Claude
[00:07:18] key.
[00:07:21] And then I'm going to say copy this one
[00:07:24] and then go to claude and then say
[00:07:26] secret.
[00:07:28] Okay. Now
[00:07:31] let's see if we can get our claude to
[00:07:32] trade a simple stock just to make sure
[00:07:35] our connection is solid. And after our
[00:07:37] connection is solid, we'll build layers
[00:07:39] on top of that so we can actually get it
[00:07:41] to do some really cool stuff. All right.
[00:07:43] All right. So what I'm going to be
[00:07:45] telling it is this. Hey, um, what I want
[00:07:49] you to do, I just gave you the
[00:07:51] documentation and my keys to connect to
[00:07:53] my Alpaca trading account.
[00:07:56] I'm just testing the connection right
[00:07:58] now. Can you please buy one share of
[00:08:01] Apple? I want to see
[00:08:04] it inside my account. All right,
[00:08:10] great. So, all this is good. Uh, right
[00:08:13] now just to make it a little faster, I'm
[00:08:15] going to right here click sonnet because
[00:08:17] this is a very easy command. And I'm
[00:08:19] going to hit go.
[00:08:22] All right. So, it's saying the order is
[00:08:25] placed successfully. Here's the summary.
[00:08:26] Now, if I go back here and if I reload.
[00:08:29] Okay, awesome. Uh, great. So, you see I
[00:08:33] already bought a share of Apple. Now,
[00:08:35] you can trade by just talking to it. Be
[00:08:37] like, "Hey, can you sell that share of
[00:08:40] Apple and then buy a share of Tesla?
[00:08:45] Great. Trust workspace. And here, this
[00:08:47] is what I want you to do as well.
[00:08:50] Hey, can you make sure in this folder
[00:08:52] you save these credentials so I don't
[00:08:54] have to keep giving it to you when we
[00:08:56] want to trade. We're going to be using
[00:08:57] this account. And in this folder, we're
[00:08:59] going to be doing a lot of trades.
[00:09:03] Okay. So, what we're going to do is
[00:09:05] because right here, we gave it access to
[00:09:07] all this stuff. I want to make sure I
[00:09:09] don't have to keep giving it access. I'm
[00:09:12] just getting it to save these
[00:09:13] credentials inside a file. Right now,
[00:09:16] Claude can trade, but it's trading
[00:09:18] blind. It doesn't know what to buy, when
[00:09:20] to buy, or why. It's missing the most
[00:09:22] important piece, which is strategy. So,
[00:09:25] let's get into that.
[00:09:27] In this level, we're going to turn
[00:09:29] Claude into something that runs on its
[00:09:31] own. So, basically, a bot that watches
[00:09:32] the market, makes its own decisions, and
[00:09:34] based on the rules you set. And the
[00:09:36] first strategy we're going to make, you
[00:09:37] can think of it like a smart thermostat.
[00:09:39] Once you set the rules, if the room
[00:09:41] temperature, let's say, drops below 68°
[00:09:43] F, you're going to turn on the heat. If
[00:09:44] it goes above 75° F, you kick on the AC.
[00:09:47] That means you don't have to sit there
[00:09:48] fiddling with your phones messing with
[00:09:50] the temperature all day. The thermostat
[00:09:51] does that all for you. It checks, it
[00:09:53] acts, and adjusts. And the bot is going
[00:09:55] to work exactly the same way. That means
[00:09:57] we're going to be setting some rules.
[00:09:58] And let me show you how this works by
[00:10:00] actually explaining the trailing stop
[00:10:01] strategy, which is a really good
[00:10:03] strategy used by many different traders.
[00:10:05] Let me show you how the trailing stop
[00:10:07] strategy actually works. So, say you buy
[00:10:09] a stock at $100.
[00:10:12] Well, let's say we tell Claude, if this
[00:10:15] drops to $95,
[00:10:18] sell it. That's your floor. $5 is the
[00:10:22] most you're willing to risk on this
[00:10:23] trade. Now, if the stock starts climbing
[00:10:27] up and let's say hits 110, if it didn't
[00:10:31] go down, but your floor is still sitting
[00:10:34] at that 95,
[00:10:37] then you're exposed to a $15 fall. That
[00:10:40] makes no sense. So, what we want is
[00:10:43] Claude to move up our floor to 105,
[00:10:48] which means if the stock dips and hits
[00:10:51] the new floor, you're still up $5 in
[00:10:54] profit and you were protected the entire
[00:10:56] time. But what if the stock drops right
[00:10:59] out the gate, right? Well, that means it
[00:11:02] would just hit $95 and you'd sell it and
[00:11:06] you're out $5 and that's your loss. Now,
[00:11:08] here's the important part. You're not
[00:11:10] stuck. You've still got that capital.
[00:11:12] Claude can now take that money and goes
[00:11:15] looking for the next setup. Maybe it's
[00:11:18] the same stock a week later at a better
[00:11:20] price. Maybe it's a completely different
[00:11:22] opportunity. The point is you lost a
[00:11:24] small portion that you're okay to lose
[00:11:27] and risk. Basically, you live to trade
[00:11:29] another day. And ideally, we find trades
[00:11:32] like this. So, let's say the stock keeps
[00:11:35] climbing and every time it does, Claude
[00:11:38] is going to drag the floor higher and
[00:11:40] higher. You can never fall back to where
[00:11:43] you started. It's basically now going to
[00:11:46] sell at 110. So, you get that $10 in
[00:11:49] profit, which is a 10% gain. That's a
[00:11:52] trailing stop. You set the rules once
[00:11:55] and Claude follows them every second of
[00:11:58] the day. You're always protected and
[00:12:00] you're always locking in the gains. So
[00:12:02] when a trade doesn't work out, you move
[00:12:04] on fast with the most amount of money
[00:12:07] still in your pocket. Now, why am I
[00:12:09] telling you all of this? Because the
[00:12:10] worst thing you can really do is hand
[00:12:12] your AI a pile of money and be like, "Go
[00:12:15] figure it out." The rules aren't the
[00:12:17] limitation. That's the whole point. This
[00:12:19] is how you take what you know, your
[00:12:22] instincts, your risk tolerance, your
[00:12:24] read on the market, and you encode it.
[00:12:26] The same rules are true here. Claude can
[00:12:28] execute thousands of decisions faster
[00:12:31] than any human. It's executing your
[00:12:33] decisions, just running at the speed and
[00:12:35] discipline that you never could on your
[00:12:37] own. That's what makes this different
[00:12:39] from just letting AI loose. And I'll
[00:12:42] show you how to set this all up in the
[00:12:44] next portion. And to set this up, it's
[00:12:46] actually really simple. So, I'm just
[00:12:47] back in my chat where I have been
[00:12:50] speaking with my Claude and I'm just
[00:12:53] going to be speaking to it, right? And
[00:12:55] just to make it a little easier, if you
[00:12:56] guys wanted this in my classroom, uh, if
[00:12:59] you guys are already watching this, if
[00:13:01] you go to skills, you'll see I have a
[00:13:03] bunch of skills here. So, this is the
[00:13:04] prompt. We're essentially going to be
[00:13:05] speaking to our claude, right? So, let
[00:13:07] me just go to Claude. And right now,
[00:13:09] don't worry about it. If you want those
[00:13:11] docs, it's there, but you can follow
[00:13:13] along with me in this video. So, I'm
[00:13:15] just going to speak it to it. All right.
[00:13:17] So, I want your help to actually
[00:13:20] schedule a trailing stop strategy on
[00:13:24] let's say Tesla, right? I want you to
[00:13:26] buy Tesla using Alpaka paper trading
[00:13:29] account. Buy, I don't know, like 10
[00:13:31] shares at the market price right now and
[00:13:33] set up these rules. The floor, if the
[00:13:36] stock drops, let's say by 10%, sell
[00:13:39] everything. That's my stop loss. I don't
[00:13:41] want to lose more than that on this
[00:13:43] trade. the trailing floor. If the stock
[00:13:46] goes up 10% from what I paid, move my
[00:13:48] stop loss up, maybe move it up 5% below
[00:13:53] the current price. Every time it climbs,
[00:13:56] move another 5% up the floor again. So,
[00:13:59] the floor only goes up, never down. And
[00:14:01] then I want you to also ladder in. If
[00:14:03] the stock drops, let's say by over 20,
[00:14:07] 30%. Buy a bunch more shares. Let's say
[00:14:10] 10 more shares. if it drops by, let's
[00:14:12] say, 20%, buy 20 shares. This way, I'm
[00:14:15] getting better prices on the way down
[00:14:16] instead of just losing money. And after
[00:14:18] you set this up, show me a summary of
[00:14:21] every order. And right after you place
[00:14:23] it, so I can confirm this looks right.
[00:14:30] Okay, so I word vomited some stuff
[00:14:32] there. [laughter] And um let this finish
[00:14:34] and I'll show you what this looks like.
[00:14:37] So, I see it just got done and it says
[00:14:40] this is the current price. And if I go
[00:14:42] back to my alpaca dashboard, I can see
[00:14:44] it set some price. It bought some Tesla
[00:14:48] and then it even set a stop loss right
[00:14:51] here. Now, one more thing we need to do
[00:14:54] is make sure we go back here and be
[00:14:57] like, "Hey, can you set up during market
[00:15:01] hours every day that you're checking
[00:15:04] consistently
[00:15:07] when we need to move our floor up or
[00:15:10] need to make new stop- losses or
[00:15:11] re-enter, use the slash schedule to make
[00:15:15] sure we have that going and set your own
[00:15:18] schedules.
[00:15:21] So, this just executed one trade. Now,
[00:15:24] what I want is clot to basically be
[00:15:26] alive and keep looping and checking on a
[00:15:29] schedule like, hey, are these trades
[00:15:31] looking right? Do I need to re-enter? Do
[00:15:33] I need to move my floor up? all of that
[00:15:36] stuff. Normally, we'd have to do it, but
[00:15:38] right now with the command I just gave
[00:15:40] it, it should be able to do it on its
[00:15:42] own.
[00:15:44] Okay, so it just got done and it says
[00:15:47] literally Tesla trailing stop monitor
[00:15:50] and it's going to be doing that every 5
[00:15:52] minutes from Monday to Friday 9:00 a.m.
[00:15:55] And it's going to keep checking. And
[00:15:57] just so you're clear on the left hand
[00:16:00] side, if you hit see this clock, if you
[00:16:03] hit this clock, it says scheduled. And
[00:16:05] if you open it up, these local tasks are
[00:16:08] already going to be running right here.
[00:16:10] You can see it already set the schedule
[00:16:12] for me. I didn't have to touch this. And
[00:16:14] if my computer is on, it's going to be
[00:16:16] running this on its own. Now, we have
[00:16:19] basically made a trading bot. Now, let's
[00:16:22] go through a couple different scenarios.
[00:16:25] Hey, so just briefly and really quickly,
[00:16:29] can you tell me what would happen if
[00:16:32] let's say Tesla shoots up to $500
[00:16:36] randomly? What would you do?
[00:16:39] And right now I'm roleplaying it just so
[00:16:42] you understand and I encourage you to do
[00:16:45] this as well so you understand what
[00:16:47] would happen in different scenarios and
[00:16:49] what would it actually do and if you do
[00:16:51] really need to change its thinking and
[00:16:53] thought processes around you could just
[00:16:55] be like hey change this around. Okay.
[00:16:57] And right here it just done it says if
[00:17:00] Tesla shoots to 500 on the way up the
[00:17:03] trailing stops kick in trailing
[00:17:05] activates your floor moves up up etc.
[00:17:08] And that's about it. Yeah, this is a
[00:17:11] really cool way to do ladder buys. Those
[00:17:14] don't trigger at all. You see, right
[00:17:16] now, I don't have any of them. So, I'm
[00:17:17] going to be like, can you think about
[00:17:19] what are good ladder buys and make sure
[00:17:22] you set that up in the schedule and
[00:17:24] update the strategy inside our whole
[00:17:28] strategy of what we're trading right
[00:17:30] now.
[00:17:32] So, as the price goes up, it buys in
[00:17:35] gradually. So, we're always at somewhat
[00:17:38] of a profit and we're pretty safe in our
[00:17:40] buys. And just so you see, it even gave
[00:17:43] me the latter levels of if it's negative
[00:17:45] 15%, it's going to buy 10. If it's 50%,
[00:17:48] it's going to buy 50. You can always
[00:17:50] change this around, but this is really
[00:17:52] cool now that me without me having to do
[00:17:55] any of this stuff, Claude can just
[00:17:56] action it for me. Now, this is all
[00:17:58] great. But the thing is, we're still
[00:18:00] picking stocks ourselves. We choose
[00:18:02] Tesla because we like it, but that's a
[00:18:04] gut feeling. The biggest traders and the
[00:18:06] best traders in the world don't trade on
[00:18:09] gut feelings. They trade on information.
[00:18:11] So, in the next level, we're going to be
[00:18:13] showing Claude where the smart money is
[00:18:15] so Claude can actually make informed
[00:18:17] decisions.
[00:18:19] But what is smart money? Well, on Wall
[00:18:22] Street, there are people who move
[00:18:24] millions of dollars in a single trade.
[00:18:26] When someone puts, let's say, $50
[00:18:28] million into a stock, they didn't really
[00:18:30] just do that off a gut feeling or
[00:18:32] flipping a coin. They have a lot of
[00:18:35] research teams and a lot of private
[00:18:36] data. They know something. These people
[00:18:39] are called whales. And when these whales
[00:18:41] make a big move, it leaves a trail like
[00:18:44] massive options orders, unusual volumes
[00:18:48] on a stock out of nowhere. And a group
[00:18:50] that does this a lot is surprisingly US
[00:18:53] politicians. But the nice part is that
[00:18:55] the members of Congress are required by
[00:18:58] law to report their stock trades. The
[00:19:00] data shows is that many of them
[00:19:01] consistently beat the market. They sit
[00:19:03] on committees. They regulate entire
[00:19:05] industries. They get briefed on policy
[00:19:08] changes before the public even hears
[00:19:10] about them. They know which companies
[00:19:12] are about to get a government contract
[00:19:14] and which ones may get investigated, but
[00:19:17] you can't see what they bought and
[00:19:20] follow them. And most people have no
[00:19:22] idea this data exists, but it's there
[00:19:25] and Claude can read it. But the thing
[00:19:27] is, we can't just tell Claw to go scour
[00:19:29] the internet for these hedge funds
[00:19:31] trades and congressional filings and all
[00:19:33] that. There's millions of data points
[00:19:35] hitting the market every single day. No
[00:19:38] AI can really browse its way through all
[00:19:40] of that. But there are services that do
[00:19:44] this full time. These companies are
[00:19:46] scraping and organizing all this data
[00:19:48] around the clock. And the data is
[00:19:50] sitting there waiting to be tracked and
[00:19:52] updated every day. And what we need to
[00:19:54] do is plug Claude into that. And that's
[00:19:57] what this new skill and MCP does. Think
[00:20:00] of it like a power outlet. The
[00:20:02] electricity, the insider information is
[00:20:05] running through those walls. And we
[00:20:07] basically plug our claude into that so
[00:20:09] we can use it. These services have data
[00:20:12] flowing through their systems and the
[00:20:14] MCP is the plug that connects Claude to
[00:20:17] their data. And once it's plugged in,
[00:20:19] Claude can pull from at any time. it
[00:20:22] becomes a new skill and Claude goes from
[00:20:24] being smart but working with nothing to
[00:20:26] being smart and seeing what the big
[00:20:29] players in the market see. Next, what
[00:20:31] we're going to do is give our Claude the
[00:20:33] power to access these services and it's
[00:20:35] going to be super easy. So, let's get
[00:20:37] into that. And just to emphasize why I'm
[00:20:39] so excited about this strategy I'm about
[00:20:41] to show you. This is me just backdating.
[00:20:45] Let's say a year ago, you were copying
[00:20:46] the same thing and the same strategy by
[00:20:50] copying the smart money.
[00:20:52] You can see if you were following the
[00:20:54] S&P 500, you were just buying and
[00:20:57] holding it, you would have made around
[00:21:00] starting at a 50k account, you would
[00:21:02] have made around 57750,
[00:21:05] which is around 15%. So, you would have
[00:21:08] made 15% more money. But if you copied
[00:21:11] McCall, then you would have made 67,400
[00:21:17] by the end of the year, which is a 34.8%
[00:21:20] return. You can see how these
[00:21:23] politicians have access to this insider
[00:21:25] information and they can out compete
[00:21:27] everybody. And that's what I'm going to
[00:21:29] show you how to do. And just to make
[00:21:31] sure our strategies are organized, what
[00:21:33] I'm going to do is go to another paper
[00:21:35] trading account. So right here, I'm
[00:21:37] going to use this Son account and I'm
[00:21:41] going to do the same thing. Okay. So I'm
[00:21:44] going to hit generate keys. I'm going to
[00:21:45] take all of the stuff or I can just copy
[00:21:48] and paste this and then I can go back to
[00:21:51] my claude.
[00:21:54] And then what I'm going to do now is
[00:21:55] make a new session. So going to hit new
[00:21:58] session and I'm going to paste this in.
[00:22:00] And now what I'm going to do is the
[00:22:03] service we're going to use to track
[00:22:04] these politicians. If you go to Google,
[00:22:07] I'm going to do Capital Trades. And
[00:22:10] Capital Trades is a free service that
[00:22:12] you can be using to see which politician
[00:22:15] is trading what and what's going on. So
[00:22:17] I'm going to copy this URL. I'm going to
[00:22:19] go back to my Claude
[00:22:22] and go right here. Okay. So now uh by
[00:22:25] the way the prompts are going to be in
[00:22:26] the description below but right now hey
[00:22:30] so um I'm trying to set up a copy
[00:22:33] trading bot when I've also given you
[00:22:36] access to my alpaca account. I want you
[00:22:39] to make a new folder inside this uh
[00:22:42] folder so we can have this running and
[00:22:45] have the schedules done. But what I want
[00:22:48] you to do is number one, find a
[00:22:52] politician who has been having really
[00:22:54] good success in the stock market
[00:22:55] currently and is actively trading. And
[00:22:58] then what I want you to do is copy their
[00:23:01] trades. Okay? So set up your crown jobs
[00:23:04] and your schedules so you're always
[00:23:05] looking and using capital trades to see
[00:23:08] what they're up to and copy those
[00:23:10] trades. Make sure you buy, sell, buy the
[00:23:13] same options that they knew. Whatever
[00:23:15] you need to just copy them and then
[00:23:17] we're going to be tracking that over
[00:23:19] time. All right.
[00:23:21] And you're going to be using the Alpaca
[00:23:22] account that I just posted the image of.
[00:23:28] Great. I'm going to hit bypass
[00:23:30] permissions, enter bypass mode, and then
[00:23:32] hit enter. All right, that was super
[00:23:34] easy. Let me wait for this to finish and
[00:23:36] we can see what's going on. Okay, so it
[00:23:38] just got done and I see in my schedule,
[00:23:41] it's already set a schedule to see what
[00:23:43] [clears throat] these politicians are
[00:23:45] doing. And then I actually also asked
[00:23:48] it, who are you copy trading and why?
[00:23:50] And it chose Michael Macau. All right,
[00:23:55] very interesting. And why is basically
[00:23:58] okay
[00:24:00] [snorts] and why the algorithm picked
[00:24:01] him over the others? Because it seems
[00:24:03] like he is very active right now and
[00:24:05] he's the top trader. interesting. The
[00:24:08] trades may be slightly stale, but that's
[00:24:10] the nature of how they disclose, we
[00:24:13] still get a lot of gains because mostly
[00:24:16] Congress can buy like 2 years out or
[00:24:18] something like that. So, they don't do
[00:24:20] day trading and they're not allowed to
[00:24:21] do it. That's why even if we're a little
[00:24:24] late because we know about it later, we
[00:24:27] can still make those gains. And just to
[00:24:29] reiterate, you can see this is a
[00:24:31] simulation for the year. If we started
[00:24:33] one year ago and did this exact same
[00:24:35] thing, if we copied this exact same
[00:24:36] strategy, this bot would have made an
[00:24:39] extra $9,650
[00:24:43] in comparison to the S&P, which should
[00:24:46] have only made around $7,000.
[00:24:49] So that's a 2.2x return over the S&P
[00:24:52] 500. And that's how these guys just stay
[00:24:54] so rich. It's kind of crazy.
[00:24:58] So, with that out of the way, now I'm
[00:25:00] going to show you the third strategy,
[00:25:02] which is a strategy that really advanced
[00:25:05] people use, which means you can get paid
[00:25:07] no matter which direction the stock
[00:25:09] moves. And to understand that, I'm going
[00:25:12] to explain how options work. Okay, so
[00:25:14] what is an option? Well, an option is
[00:25:16] basically a contract when two people
[00:25:18] agree to do a deal. And let me show you
[00:25:20] this with something you already may
[00:25:22] know. Okay, so let's say you pay your
[00:25:23] car insurance company $100 a month. In
[00:25:26] exchange, you get the right to file a
[00:25:28] claim if something goes wrong. And if
[00:25:30] you crash, the insurance covers it.
[00:25:32] You're protected. And if nothing
[00:25:34] happens, they keep your hundred bucks.
[00:25:36] They're basically getting paid to take
[00:25:38] on the risk. Now, look at this exact
[00:25:40] same structure. What happens is you pay
[00:25:42] a premium to another trader where you
[00:25:44] get the right to buy or sell a stock at
[00:25:47] a locked price. Okay? And if the stock
[00:25:50] moves your way, you can exercise that
[00:25:53] contract and profit. If the stock
[00:25:56] doesn't move your way, the contract will
[00:25:58] expire. They keep your premium. It's the
[00:26:01] same deal. You basically paid for
[00:26:03] protection. They got paid for the risk.
[00:26:06] And here it is next to each other rowby
[00:26:08] row. It's identical. The premium, the
[00:26:11] right to act, the expiration date, and
[00:26:13] if nothing happens, the other side keeps
[00:26:15] your money. That's all an option is
[00:26:18] insurance on a stock. Okay? And to dive
[00:26:20] in, there are only two types of options.
[00:26:23] A call option gives you the right to buy
[00:26:25] a stock at a locked in price. Say Apple
[00:26:28] is at $200.
[00:26:31] You can buy a call option with a strike
[00:26:34] price of $210. That means if Apple goes
[00:26:37] to let's say 230 before your contract
[00:26:40] expires, you can buy it at 210 and
[00:26:44] pocket that $20 difference. If Apple
[00:26:47] stays below 210, your contract expires
[00:26:50] and you lose the premium you paid.
[00:26:52] That's your max loss. Think of it like
[00:26:53] putting a deposit on an apartment.
[00:26:55] You'll pay $500 to lock in the rent for
[00:26:58] $2,000 for 30 days. If the rent price
[00:27:00] jumps to $2,500, you got a deal. If they
[00:27:03] don't, you lost that $500 deposit. And
[00:27:06] on the other side is a put option. The
[00:27:09] put option gives you the right to sell a
[00:27:12] stock at a locked in price. Say you own
[00:27:14] Apple at $200. You buy a put option with
[00:27:18] a strike price of 190. If Apple drops to
[00:27:22] 170, you can sell it at 190 instead of
[00:27:26] 170. The put basically protected you
[00:27:28] from the drop. That's the insurance
[00:27:30] side. You paid a premium to protect
[00:27:32] yourself against the price drop. Why
[00:27:34] this is interesting is because with
[00:27:36] stocks and options, you can actually
[00:27:37] flip the table and become the insurance
[00:27:39] as well. So that is called selling
[00:27:43] options. So when you sell an option, you
[00:27:46] basically become the insurance company.
[00:27:48] you're the one that's collecting the
[00:27:50] premiums. So, someone pays you for a
[00:27:53] contract and most of the time that
[00:27:56] contract expires without anything
[00:27:58] happening and you keep the money. And
[00:28:00] the cool part is the insurance companies
[00:28:02] make billions doing this. They collect
[00:28:04] premiums after premiums from millions of
[00:28:07] people and pay out on a small percentage
[00:28:09] of claims. The math basically works in
[00:28:12] their favor over time. And selling
[00:28:15] options basically work the same way
[00:28:17] where you collect a premium upfront and
[00:28:19] if the stock doesn't hit the strike
[00:28:21] price by the expiration, your contract
[00:28:24] dies and you keep everything you were
[00:28:26] paid. And the wheel strategy is built on
[00:28:29] selling options. You are the insurance
[00:28:32] company. You collect premiums at every
[00:28:34] stage. And let me show you how that
[00:28:36] works. Okay, so let's walk through the
[00:28:38] wheel strategy with a real example with
[00:28:41] let's say Tesla. So Tesla is trading at
[00:28:44] $250 and let's say you really like the
[00:28:47] stock, but you're not paying $250 for
[00:28:50] it. You'd rather get it at let's say
[00:28:52] $230. So if you sell a put at the 230
[00:28:57] strike and for making that promise for
[00:29:00] saying I'll buy Tesla at 230 if the
[00:29:03] price drops there, someone is going to
[00:29:05] hand you $5 per share. That's $500 in
[00:29:09] your pocket right now just for agreeing
[00:29:11] to do a deal you already wanted. Now,
[00:29:14] two things can happen. Tesla can stay
[00:29:17] above $230, which means the contract
[00:29:20] might expire. Nobody makes you buy
[00:29:23] anything and you get to keep the $500
[00:29:27] and you can do it again the next week.
[00:29:29] The other scenario is Tesla drops below
[00:29:32] 230 and you have to buy it. But
[00:29:34] remember, you collected $500 before
[00:29:37] already. So your real cost isn't 230,
[00:29:41] it's 225. You got Tesla cheaper than
[00:29:44] anyone else, and you wanted it anyways.
[00:29:46] Okay, so stage two, let's say Tesla does
[00:29:49] drop and you get assigned, which means
[00:29:50] you have to buy the Tesla shares. Now
[00:29:52] you own 100 shares at an effective cost
[00:29:55] of 225. Most people would be upset, but
[00:29:59] you're not because you set the price.
[00:30:01] You got paid to wait and you bought it
[00:30:04] at a discount. Right? That's not a loss.
[00:30:05] That's a your plan working. Now, it's
[00:30:08] time for stage number two. Okay. Now
[00:30:10] that we own the shares and they're
[00:30:12] sitting in our account, what we're going
[00:30:14] to do is we're going to sell a covered
[00:30:16] call, which means we will pick a 260
[00:30:19] strike price. That means someone is
[00:30:21] going to pay us another $5 per share,
[00:30:25] which is another $500 for the right to
[00:30:28] buy your Tesla shares for $ 260. If
[00:30:31] Tesla stays below 260, that contract
[00:30:34] expires, you keep the shares and you
[00:30:37] keep the $500 and you can sell that call
[00:30:40] again the next week. This is cool
[00:30:42] because you're generating income from a
[00:30:44] stock that isn't even moving because if
[00:30:46] Tesla does go above 260, your shares get
[00:30:49] sold. But look at the math. So let's say
[00:30:52] you bought the Tesla shares at 225. You
[00:30:54] sold it at 260. That's a $35 per share
[00:30:59] in stock gains plus the $5 you collected
[00:31:03] selling that put plus the $5 you
[00:31:05] collected selling the call. That's $45
[00:31:08] per share in total profit on 100 shares.
[00:31:12] That's $4,500. And here's the best part.
[00:31:15] Once your shares get called away, you go
[00:31:18] right back to stage one. You sell
[00:31:20] another put, collect another premium,
[00:31:22] and the wheel just keeps spinning. every
[00:31:24] single rotation you get paid. The stock
[00:31:27] can go up, down, sideways, it doesn't
[00:31:30] matter. You're collecting income at
[00:31:32] every stage. The wheel strategy sounds
[00:31:34] great until you try to run it for
[00:31:35] yourself. You're picking strike prices
[00:31:37] based on your market conditions and all
[00:31:40] these other things every single week.
[00:31:43] Most people who learn about this wheel
[00:31:45] give up after a few weeks because
[00:31:47] management is what buries them. And the
[00:31:49] cool part about Claude and I'm what I'm
[00:31:51] about to show you is that Claude handles
[00:31:53] all of it. Which means Claude itself can
[00:31:57] monitor the positions, pick expirations,
[00:32:00] and roll contracts when needed. Which
[00:32:03] means you just collect the premiums on a
[00:32:05] schedule and you'll check in, let's say,
[00:32:07] once a day. So with that out of the way,
[00:32:11] understanding why Claude makes this so
[00:32:13] effective, let's set one up. Okay, so
[00:32:15] for this we're going to be using the
[00:32:18] first trading claude account and I'm
[00:32:21] going to go back to Claude. And you see
[00:32:23] I actually have a prompt right here that
[00:32:26] you can copy paste and just so you can
[00:32:29] follow along I'll read it out to you.
[00:32:32] Okay. So, what this is is basically I
[00:32:35] want you to run a wheel strategy on let
[00:32:39] me see Tesla
[00:32:43] using my alpaca trading account. Stage
[00:32:46] one, you sell the puts. So, you sell a
[00:32:48] cash secured put on Tesla with a strike
[00:32:50] price around 10% below the current
[00:32:53] price. Pick an expiration 2 to 4 weeks
[00:32:56] out. Collect the premiums. If the put
[00:33:00] expires worthless, sell another one and
[00:33:02] keep collecting premiums. If I get
[00:33:04] assigned, I have to buy the stock, move
[00:33:06] to stage two. Stage two is selling the
[00:33:09] calls. Once I own the shares, sell
[00:33:13] covered calls with the strike price
[00:33:15] around 10% of above what I paid. Pick an
[00:33:18] expiration, maybe 2 to 4 weeks out.
[00:33:20] Collect the premium. If the call expires
[00:33:23] worthless, sell another. Keep collecting
[00:33:26] premiums. If my shares get called away
[00:33:28] like sold, go back to stage one and
[00:33:30] start again. And the rules are never
[00:33:33] sell a put unless I have enough cash to
[00:33:35] buy the shares if assigned and never
[00:33:37] sell a call below my cost basis, what I
[00:33:41] actually paid and track my premium
[00:33:44] across all cycles and check my positions
[00:33:47] every 15 minutes during market hours.
[00:33:49] Please set the schedule. If a contract
[00:33:52] hits 50% profit before expiration, close
[00:33:54] it early and give me a daily summary at
[00:33:57] markets close. All right, run this
[00:33:59] during market hours. Do nothing outside
[00:34:01] market hours. Great.
[00:34:04] That's what that prompt was. Now, I'm
[00:34:06] going to hit enter and wait. But that's
[00:34:09] about it. You're going to see after this
[00:34:11] is done. I'll show you in a bit. It's
[00:34:13] going to set the things in a schedule.
[00:34:14] It's going to keep running this. And I
[00:34:17] encourage you to maybe set up a paper
[00:34:19] trading account and then have a go at
[00:34:21] it. See how it will do. These are just
[00:34:24] some fun strategies that I've been
[00:34:26] playing with that I think have been
[00:34:30] pretty useful and super revolutionary of
[00:34:32] what we can really do with Claude. But,
[00:34:36] you know, if you're watching this and
[00:34:37] you can see the power of Claude, but
[00:34:40] haven't used it before, or you tried it,
[00:34:42] but you're not sure how to get the most
[00:34:44] out of it, I'm actually putting together
[00:34:46] a full course that's going to walk
[00:34:47] through everything from scratch. How to
[00:34:49] set up Cloud, how to use it, how to
[00:34:51] build projects, like this one, step by
[00:34:54] step. So, stay subscribed for that. And
[00:34:55] in the meantime, watch this video. If
[00:34:58] you want to see me going deeper of any
[00:34:59] of these strategies or build something
[00:35:01] else together, join my clot club where
[00:35:03] we can do this and we'll have some