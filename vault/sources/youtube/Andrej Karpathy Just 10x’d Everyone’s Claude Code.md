---
author: '[[Nate Herk | AI Automation]]'
channel_id: UC2ojq-nuP8ceeHqiroeKhBA
created: 2026-04-07
date: '2026-04-05'
description: 'Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=karpathy-obsidianAll
  my FREE resources: https://www.skool.com/ai-automation-society/about?el=karpathy-obsid'
duration: 1066
language: en
published: 2026-04-05
source: https://www.youtube.com/watch?v=sboNwYmH3AY&t=11s
status: processed
tags:
- obsidian
- knowledge-management
- clippings
- ai
- claude-code
- llm-wiki
title: Andrej Karpathy Just 10x’d Everyone’s Claude Code
topics:
- '[[LLM Wiki]]'
- '[[RAG]]'
- '[[Claude Code]]'
- '[[Obsidian]]'
- '[[Knowledge Management]]'
---

## Summary

[[Nate Herk]] walks through [[Andrej Karpathy]]'s viral LLM Wiki concept -- a method for building personal knowledge bases using nothing but markdown files and [[Claude Code]], with [[Obsidian]] as a visual frontend.

### Key Takeaways

- **The Core Idea**: Instead of using traditional [[RAG]] with vector databases and embeddings, you give an LLM well-organized markdown files. The LLM reads indexes, follows wikilinks, and understands relationships -- producing deeper understanding than similarity search.
- **Three-Layer Architecture**: Raw sources (articles, transcripts, PDFs) go into a `raw/` folder. The LLM processes them into a `wiki/` folder with entity pages, concept pages, and cross-references. An `index.md` and `log.md` track everything.
- **Setup in 5 Minutes**: Download [[Obsidian]], create a vault, open it in [[Claude Code]], paste Karpathy's gist, and start ingesting content. The [[Obsidian Web Clipper]] extension makes capturing web content effortless.
- **Two Use Cases Demonstrated**: (1) A YouTube transcript wiki with 36 videos auto-organized into tools, techniques, concepts, and people. (2) A personal "second brain" for business, meetings, and initiatives.
- **Executive Assistant Integration**: The wiki can be referenced by other Claude Code projects via a wiki path in CLAUDE.md, enabling an AI assistant that has persistent memory of your knowledge.
- **Hot Cache**: A small (~500 word) cache of the most recent context, useful for executive assistant workflows but not needed for research wikis.
- **Linting**: Periodic health checks to find inconsistencies, missing data, and suggest new connections or articles to ingest.
- **LLM Wiki vs RAG**: Wiki works great for hundreds of pages with good indexes. Traditional RAG is better for millions of documents. Wiki costs are essentially just tokens; RAG requires embedding models, vector DBs, and chunking pipelines.
- **Cost Efficiency**: One user turned 383 scattered files into a compact wiki and dropped token usage by 95%.

### Mentioned Resources
- [Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [AI 2027 Article](https://ai-2027.com/)

![](https://www.youtube.com/watch?v=sboNwYmH3AY)

Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=karpathy-obsidian  
All my FREE resources: https://www.skool.com/ai-automation-society/about?el=karpathy-obsidian  
Apply for my YT podcast: https://podcast.nateherk.com/apply  
Work with me: https://uppitai.com/  
  
My Tools💻  
14 day FREE n8n trial: https://n8n.partnerlinks.io/22crlu8afq5r  
Code NATEHERK to Self-Host Claude Code for 10% off (annual plan): https://www.hostinger.com/vps/claude-code-hosting  
Voice to text: https://ref.wisprflow.ai/nateherk  
  
Karpathy's idea gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
AI 2027 article: https://ai-2027.com/  
  
Andrej Karpathy just shared his method for building LLM-powered knowledge bases using nothing but markdown files and Claude Code.  
  
In this video, I walk you through exactly how to set it up in about 5 minutes using Obsidian as a front end. I also show you two of my own wikis, one for YouTube transcripts and one for my personal second brain, and break down how this compares to traditional semantic search RAG.  
  
Sponsorship Inquiries:  
📧 sponsorships@nateherk.com  
  
TIMESTAMPS  
0:00 What We're Building  
1:40 Karpathy's LLM Wiki Idea  
3:12 Why It Matters & How It Works  
5:39 Setting Up Obsidian & Claude Code  
8:35 Ingesting Your First Article  
13:02 Querying & Connecting Projects  
15:36 LLM Wiki vs Traditional RAG  
17:20 Final Thoughts

## Transcript

### What We're Building

**0:00** · What you're looking at right here is 36 of my most recent YouTube videos organized into an actual knowledge system that makes sense. And in today's video, I'm going to show you how you can set this up in 5 minutes. It's super super easy. You can see here how we have these different nodes and different patterns emerging. And as we zoom in, we can see what each of these little dots represents. So, for example, this is one of my videos, $10,000 aentic workflows.

**0:22** · We can see it's got some tags. It's got the video link. It's got the raw file.

**0:26** · And it gives an explanation of what this video is about and what the takeaways are. And the coolest part is I can follow the back links to get where I want. There's a backlink for the WAT framework. There's a backlink for Claude Code. There's a backlink for all these different tools I mentioned like Perplexity, Visual Studio Code, Nano Banana, Naden N. It also has techniques like the WT framework or bypass permissions mode or human review checkpoint. So, as this continues to fill up, we can start to see patterns and relationships between every tool or every skill or every MCP server that I might have talked about in a YouTube video. And I can just query it in a really efficient way now that we have this actual system set up. And the crazy part is I said, "Hey, Cloud Code, go grab the transcripts from my recent videos and organize everything. I literally didn't have to do any manual relationship building here. It just figured it all out on its own." And then right here, I have a much smaller one, but this is more of my personal brain.

**1:16** · So this is stuff going on in my personal life. This is stuff going on with, you know, UpAI or my YouTube channel or my different businesses and my employees and our quarter 2 initiatives and things like that. This is more of my own second brain. So I've got one second brain here and then I've got one basically YouTube knowledge system and I could combine these or I could keep them separate and I can just keep building more knowledge systems and plug them all into other AI agents that I need to have this context.

### Karpathy's LLM Wiki Idea

**1:40** · It's just super cool. So Andre Carpathy just released this little post about LLM knowledge bases and explaining what he's been doing with them. And in just a matter of few days, it got a ton of traction on X. So let's do a quick breakdown and then I'm going to show you guys how you can get this set up in basically 5 minutes. It's way more simple than you may think. Something I've been finding very useful recently is using LLM to build personal knowledge bases for various topics of research interest. So there's different stages.

**2:03** · The first part is data ingest. He puts in basically source documents. So he basically takes a PDF and puts it into Cloud Code and then Cloud Code does the rest. He uses Obsidian as the IDE. So this is nothing really too game-changing. Obsidian just lets you visually see your markdown files. But for example, this Obsidian project right here with all this YouTube transcript stuff that actually lives right here.

**2:23** · This is the exact same thing. Here are the raw YouTube transcripts. And here's that wiki that I showed you guys with the different um folders for what Cloud Code did with my YouTube transcripts.

**2:32** · And then there's a Q&A phase where you basically can ask questions about YouTube or about the research and it can look through the entire wiki in a much more efficient way and it can give you answers that are super intelligent. He said here, "I thought that I had to reach for fancy rag, but the LLM has been pretty good about automaintaining index files and brief summaries of all documents and it reads all the important related data fairly easily at this small scale." So right now he's doing about 100 articles and about half a million words. So there's a few other things that we'll cover later, but the TLDDR is you give raw data to cloud code. It compares it, it organizes it, and then it puts it into the right spots with relationships, and then you can query it about anything. And it can help you identify where there's gaps in that node or in that, you know, relationship, and it can go do research and fill in the gaps. All right. So why is this a big deal? Because normal AI chats are ephemeral, meaning the knowledge disappears after the conversation. But this method, using Karpathy's LLM wiki, makes knowledge compound like interest in a bank. People on X are calling it a game changanger because it finally makes AI feel like a tireless colleague who actually remembers everything and it stays organized. It's also super simple.

### Why It Matters & How It Works

**3:36** · It will take you five minutes to set up.

**3:37** · I'll show you guys. You don't need a fancy vector database embeddings or complex infrastructure. It's literally just a folder with markdown files.

**3:44** · That's it. You literally just have a vault up top. So in this example, it's called my wiki. You've got a raw folder where you put all of the stuff. And then you've got a wiki folder, which is what the LLM takes from your raw and puts it into the wiki. So in here you have all the wiki pages which it will create but then you also have an index and you have a log. So for example in my YouTube transcripts vault here is the index. You can see that I have all these different tools which I could obviously click on and it would take me right to that page or after that I have all the different techniques agent teams sub agents permission modes the WAT framework and then we've got different concepts MCP servers rag vibe coding we've got all these different sources which are you know the YouTube videos and then when I have people or when I have comparisons they will be put in here in the index and then we also have a log which is the operation history so in this case in the YouTube project the log isn't huge cuz I only ran one huge batch of the initial 36 YouTube videos, but now every time I have one, I say, "Hey, can you go ahead and ingest the new YouTube video into the wiki and then we'll see every single time we update this." And then, of course, you need your claw. MD to explain how the project works and how to search through things and how to, you know, update things. It's also a big deal from a cost perspective, token efficiency, and long-term value. One X user turned 383 scattered files and over a 100 meeting transcripts into a compact wiki and dropped token usage by 95% when querying with Claude. And obviously token management and efficiency is a huge conversation right now and will always be. The other thing that's really cool about this is there's not really like a GitHub repo you go copy or there's not a complicated setup. You literally just say hey cloud code read this idea from Andre Karpathy and implement it. And people on X are now talking about like this is how 2026 AI agentic software and products will be made. You just give it a highle idea and it goes and builds it out. And Karpathy even said, "Hey, you know, I left this prompt vague so that you guys can customize it." And I'll show you the ways in my two different vaults right now that it changed things a little bit based on the context and understanding of what the project is actually for.

### Setting Up Obsidian & Claude Code

**5:39** · Okay, so this was the original tweet I just showed you guys and then he followed up and said, "Hey, this one went viral. So here is the idea in a gist format." So if you open this up, this is basically just another explanation of the core idea of how this works and why the architecture, indexing, all this kind of stuff. And by the way, this is the part where he says, "Hey, this is left vague so that you can hack it and customize it to your own project." So we're going to come right back to this in a sec, but the first prerec that we're going to do, it's not necessary, but I like to have a nice little front end to see the relationships, is we're going to go to Obsidian and download it. So, if you just go to obsidian.mmd, you can see this is the completely free tool and you're going to go ahead and download it. So, just for your operating system, download this and then open up the wizard and open up the app. So, when you open up the app, it'll look like this.

**6:23** · And what we're going to do here is we're going to create a new vault. So, down here, you can see I have Herk Brain and I have YouTube transcripts. I'll just make it a little bigger. I'm going to go to manage vaults. I'm going to create a new one. And now, we just have to give this a name. So, I'm just going to call this one demo vault. and you're going to choose a location where you want to put this. So, I'm just throwing this on my desktop and I'm going to go ahead and create this vault. Then, what you're going to do is go to wherever you like to run Cloud Code. So, in this case, I'm doing it in VS Code. And I open up that folder. So, demo vault. We get an Obsidian and then we get a welcome.md.

**6:54** · So, I'm going to open up Claude. So, I'm going to do it in my terminal. I'm going to run Claude. And lately, I've been liking using my terminal better for Claude. I like to do it inside of VS Code, but the reason is just because I like to see the status line and I have, you know, a little bit more functionality. So, anyways, now that we have Cloud Code open, here's what we're going to do. We're going to go back over to the LLM wiki thing that we got from Andre Carpathy. We're going to copy all of this and we're going to go back into Cloud Code and then just paste it in there. So, that is the prompt from Carpathy that's going to build out everything we need. And then before we send that off, we're dropping this in which you guys can screenshot and then just throw into yours. But I'm saying you are now my LLM wiki agent. Implement this exact idea file as my complete second brain. Guide me step by step.

**7:38** · Create the cloudmd schema blah blah blah. So this is just telling it what it needs to do with this idea that we just got from kpathy. So anyways, on the right we have this cloud code running and on the left we have our obsidian vault and you can see it just created those two folders. So it created the raw and it created the wiki as you can see.

**7:54** · Now, by default, it threw in four folders. It threw in analysis, concepts, entities, and sources. Once we start to populate stuff, we can talk to it to see if that's actually the way we want to do it or not. Because it's interesting in my personal kind of second brain, the wiki is literally just markdown files.

**8:08** · There's no structure to it. And in some cases, that's good. Carpathy actually said, "Sometimes I like to keep it really simple and really flat, which means like no subfolders and not a bunch of over organizing." But then you guys did see in my YouTube transcript one, there were different subfolders. And I think that in this case it actually makes more sense. But you can see that it went ahead and it created a claw.md.

**8:27** · It created an index and a log and then a few different folders in our wiki. But now it's saying, "Hey, let's go ahead and try it out. Drop in your first source into the raw folder and tell me to ingest it." Okay, so I'm at this website called AI2027. If you guys haven't read this before, it's kind of an interesting read. So go check it out.

### Ingesting Your First Article

**8:42** · And now let's say I want to get this into my vault. What I could do is just copy the whole page, right? And it might just come through a little weird. or we can just get an Obsidian extension which lets us basically take articles right from the web and just put it right into our vault. Super easy. So search for this extension called Obsidian Web Clipper. You would go ahead and add this to Chrome. So then when you're in the article that you want, you basically just click on your extensions, you open up Obsidian Web Clipper, and then you can just chuck it into your vault. And then right here, you're going to want to set this to RAW because this is the actual folder that it's going to put it in. So you can go ahead and click add to Obsidian. Open Obsidian. And then now you can see in my raw section we have this AI 2027 source with the title the source and it's not super super populated yet because the LLM in cloud code is going to do that. So here is our file. I'm going to open up cloud code and say awesome. I just threw in an article called AI 2027 into the raw. Can you please go ahead and ingest that? It might ask you some questions. It might also be helpful to before you start ingesting stuff say hey by the way this project is specifically for my second brain. So, personal things, business things, whatever. Or this is just a research project. This is where I'm going to chuck you all the articles and all the things that I want to learn about and all the things that I know.

**9:50** · So, there's different ways that you can set up the project as you saw with mine.

**9:53** · One for YouTube, one for just personal second brain. So, now what it's doing is it's going to read through this article and then it's going to figure out where should I chuck everything into the wiki.

**10:02** · It's not just going to create one MD file for this. It might create five or it might create 10. And there's going to be relationships between each of the different sections that it creates. So, it's kind of doing its own method of chunking. Now, one thing I want to call out real quick is with this extension, if you go here and you open up the options for it, you can see that you can actually change where by default the folders are dropped, which is in the location section. By default, it'll be going to a place called clippings, but just go ahead and change that to raw.

**10:29** · Okay. So, here it came back with all these questions, right? It said, "Here are my key takeaways from this article, blah blah blah." And now it'll ask you, "What do you want to emphasize from this article? What's your focus? How granular do you want to be? what's your plan? So, I'm just going to say I want this to be extremely thorough. This is my passion looking at where AI is going to go. Um, and this whole project, by the way, that you're setting up in this vault is basically just going to be my place to dump in research about AI. So, help me keep all that organized so that I can query it and that I can, you know, keep my thoughts related. So, that's just a quick example of what it might look like for you to give it some more context to continuously build your project. So, I'm going to switch over over here to the graph view because I think it it'll be interesting to see as it is starting to go through and create those different wiki files. It's going to go ahead and it's going to create all those relationships and we'll be able to watch it in real time. All right, so it's creating all of the wiki pages now and you can see that it said it's going to make about 25 because there's so much stuff going on in the original AI 2027 article. Okay, so our first one just popped in here and there a second one just came through and now you can understand you're starting to see where do you have hubs or where do you just have little individual nodes? So this is a major hub. Someone named Eli, someone named Thomas, Daniel, and you can see all the different relationships here with things like AI governance with things like OpenBrain, superhuman coder.

**11:46** · Okay, so that ingest took about 10 minutes. So sometimes you have to be a little patient with, you know, it reading through everything and organizing everything, but it does a lot of heavy lifting, of course. When I uploaded the 36 YouTube transcripts in batch, it took about 14 minutes. So it kind of just depends, but it created 23 wiki pages. We have the source. We have six people, five organizations and one AI systems page, different concepts, so technical alignment and geopolitical and then an analysis and then it asks some questions about it so that it can help make the relationships and make the structure even better. Now let's just open this one up a little bit deeper and see what it actually did in here with this stuff. So we have this is the source with all the main relationships.

**12:27** · So as we start to add other articles, we will see other big kind of like nodes and maybe in some cases we'll have relationships between like compute scaling with different articles that we upload as well. So let's just see if I click into the main source, we can see the tags that it got. We can see the authors and we can click around. So here's a link to OpenAI. Okay, what's OpenAI? Here's references in AI 2027.

**12:46** · Here's some other connections with OpenAI like modelsp spec. Okay, we're in model spec. Let's take a look. We can see other things about modelsp spec. And we could also go to how the LLM psychology model works. So this is just super super cool all the relationships that we get. And once again, all of this stuff that we're looking at was derived from one article and automatically organized and related. So the question now is like what do we do from here? Do we query it inside of this environment?

### Querying & Connecting Projects

**13:10** · Do we query it from somewhere else? And that's completely up to the way that you want to use this. So for example, with my YouTube project, I'm probably just going to keep this here. And whenever I want to ask questions about YouTube or if I want to turn this into like a website, I can just do that from here.

**13:23** · Or if I need to, I can point a different project at this folder since everything's here and it can crawl through the wiki, it can read the index and it knows how this stuff works because you can give it the clawmd so it understands the project as well. So for example, in this one which is just my second brain where we have all of the different things about like I drop in my meeting recordings, I drop in, you know, ClickUp channels, summaries and things like that. This is something that I want to use in my executive assistant. So what I did in my executive assistant here called Herk 2, if I go to this cloud.MD, MD you can see that we have a wiki path. So whenever you need to read things about me and my business that you don't have already, you would basically go to my herkbrain vault. You would go to that directory and then you would read through the wiki. You can read the hot cache which I'll explain in just a sec. You can read the index. You can read the domain subindex and then you can also just search through everything here. And I said don't read from the wiki unless you actually need it. Here are some things that you might do that you don't need to go read the wiki for.

**14:16** · And all of this is my business knowledge. Now, if you guys remember, if you watched my video on setting up an executive assistant, I used to do this with context files inside of this project. And when I changed over to this method, I actually saw a reduction in tokens that I was actually calling in this project. So, the thing about the hot cache, right, I didn't actually have this in my YouTube one. So, if I go to YouTube, you can see there's no hot cache. But, if I go to the herk brain in the wiki, you can see there's a hot.mmd right here. And this is basically just a cache of like 500 words or 500 characters that it saves, which is like what is the most recent thing that Nate just gave me or that we talked about. In the context of my executive assistant, this is really helpful. You know, it might save me from having to crawl different wiki pages. But in something like the YouTube transcript project, I don't really need a hot cache. So, another thing that I alluded to but didn't really cover was the idea of linting. So Karpathi says that he runs some LLM health checks over the wiki to find inconsistent data, impute missing data with web searches, find interesting connections for new article candidates, things like that. So it basically helps you run a lint, you know, every day, every week, whenever you want, which helps make sure that everything is scalable and structured in the right way. And it might even come back and say, "Hey, I don't fully understand this. Can you give me some more info or can you grab some more articles that might help me out here?" So now the final question about this that I wanted to cover is like does this kill semantic search rag? And the answer is no, but kind of yes. And it all depends on the goal of the project and the goal of the context, how much context you have. So here's a really quick chart that I had my cloud code make. I was in my Herk brain where I dumped in a bunch of information about Karpathy's LLM knowledge and I just said, "Hey, can you please explain Karpathy knowledge as simple as possible, keep it super concise, and um compare it to typical semantic search rag." So, it found Carpathy's idea. Instead of a database, you just give the LM well organized markdown files and it compares it here to the actual semantic search rag. So, actually, I might as well just read it off from here. So it finds it by reading indexes and follows links rather than using similarity search. So we're getting a deeper understanding of relationships because they're links rather than just saying, "Hey, these chunks seem similar." As far as infrastructure, it is literally just markdown. So like I said, you don't even need the obsidian. You just need these markdown files. Whereas with semantic search, you need an embedding model. You need a vector database and a chunking pipeline. The cost over here is basically free. Your only cost is going to be tokens. Whereas over here, you might have ongoing compute and storage.

### LLM Wiki vs Traditional RAG

**16:42** · And for maintenance, you just run a lint. You clean up things. You add more articles. You give it more context rather than having to re-mbed when things change. But right now, the weakness of course with the uh LLM knowledge wiki is that it doesn't scale huge across enterprises, right? Because it's just a bunch of files. Um and that is where the cost will probably get more and more expensive than going to something like standard semantic search or knowledger graph or light rag or whatever other tool is out there for that. So here you can see if you have hundreds of pages with good indexes, you're fine with wiki graph. But if you were getting up to the millions of documents, then you're going to want to actually do more of a traditional rag pipeline, at least for now with how the current models are and everything we know right now in April 2026. So that is going to do it for today. I hope you guys learned something new or enjoyed the video. And if you did, please give it a like. It helps me out a ton. Now, after this video, if you're interested in learning how you can create your own sort of executive assistant and then plug it into this Obsidian vault, then definitely check out this video up here where I go over how I built my executive assistant and the way that you should be thinking about it. So hopefully I'll see you guys over there, but if not, I'll see you in the next

---

## Transcript

[00:00:00] What you're looking at right here is 36
[00:00:02] of my most recent YouTube videos
[00:00:03] organized into an actual knowledge
[00:00:05] system that makes sense. And in today's
[00:00:07] video, I'm going to show you how you can
[00:00:08] set this up in 5 minutes. It's super
[00:00:10] super easy. You can see here how we have
[00:00:12] these different nodes and different
[00:00:13] patterns emerging. And as we zoom in, we
[00:00:15] can see what each of these little dots
[00:00:17] represents. So, for example, this is one
[00:00:19] of my videos, $10,000 aentic workflows.
[00:00:22] We can see it's got some tags. It's got
[00:00:23] the video link. It's got the raw file.
[00:00:26] And it gives an explanation of what this
[00:00:27] video is about and what the takeaways
[00:00:29] are. And the coolest part is I can
[00:00:31] follow the back links to get where I
[00:00:32] want. There's a backlink for the WAT
[00:00:34] framework. There's a backlink for Claude
[00:00:36] Code. There's a backlink for all these
[00:00:38] different tools I mentioned like
[00:00:39] Perplexity, Visual Studio Code, Nano
[00:00:41] Banana, Naden N. It also has techniques
[00:00:43] like the WT framework or bypass
[00:00:45] permissions mode or human review
[00:00:47] checkpoint. So, as this continues to
[00:00:49] fill up, we can start to see patterns
[00:00:50] and relationships between every tool or
[00:00:53] every skill or every MCP server that I
[00:00:55] might have talked about in a YouTube
[00:00:56] video. And I can just query it in a
[00:00:58] really efficient way now that we have
[00:01:00] this actual system set up. And the crazy
[00:01:02] part is I said, "Hey, Cloud Code, go
[00:01:04] grab the transcripts from my recent
[00:01:05] videos and organize everything. I
[00:01:07] literally didn't have to do any manual
[00:01:10] relationship building here. It just
[00:01:11] figured it all out on its own." And then
[00:01:13] right here, I have a much smaller one,
[00:01:14] but this is more of my personal brain.
[00:01:16] So this is stuff going on in my personal
[00:01:18] life. This is stuff going on with, you
[00:01:19] know, UpAI or my YouTube channel or my
[00:01:21] different businesses and my employees
[00:01:23] and our quarter 2 initiatives and things
[00:01:25] like that. This is more of my own second
[00:01:27] brain. So I've got one second brain here
[00:01:28] and then I've got one basically YouTube
[00:01:30] knowledge system and I could combine
[00:01:33] these or I could keep them separate and
[00:01:34] I can just keep building more knowledge
[00:01:36] systems and plug them all into other AI
[00:01:38] agents that I need to have this context.
[00:01:40] It's just super cool. So Andre Carpathy
[00:01:42] just released this little post about LLM
[00:01:44] knowledge bases and explaining what he's
[00:01:46] been doing with them. And in just a
[00:01:47] matter of few days, it got a ton of
[00:01:48] traction on X. So let's do a quick
[00:01:50] breakdown and then I'm going to show you
[00:01:51] guys how you can get this set up in
[00:01:52] basically 5 minutes. It's way more
[00:01:54] simple than you may think. Something
[00:01:56] I've been finding very useful recently
[00:01:57] is using LLM to build personal knowledge
[00:01:59] bases for various topics of research
[00:02:01] interest. So there's different stages.
[00:02:03] The first part is data ingest. He puts
[00:02:05] in basically source documents. So he
[00:02:07] basically takes a PDF and puts it into
[00:02:09] Cloud Code and then Cloud Code does the
[00:02:11] rest. He uses Obsidian as the IDE. So
[00:02:13] this is nothing really too
[00:02:14] game-changing. Obsidian just lets you
[00:02:16] visually see your markdown files. But
[00:02:18] for example, this Obsidian project right
[00:02:20] here with all this YouTube transcript
[00:02:21] stuff that actually lives right here.
[00:02:23] This is the exact same thing. Here are
[00:02:24] the raw YouTube transcripts. And here's
[00:02:26] that wiki that I showed you guys with
[00:02:27] the different um folders for what Cloud
[00:02:31] Code did with my YouTube transcripts.
[00:02:32] And then there's a Q&A phase where you
[00:02:34] basically can ask questions about
[00:02:36] YouTube or about the research and it can
[00:02:38] look through the entire wiki in a much
[00:02:40] more efficient way and it can give you
[00:02:42] answers that are super intelligent. He
[00:02:44] said here, "I thought that I had to
[00:02:45] reach for fancy rag, but the LLM has
[00:02:47] been pretty good about automaintaining
[00:02:48] index files and brief summaries of all
[00:02:50] documents and it reads all the important
[00:02:52] related data fairly easily at this small
[00:02:54] scale." So right now he's doing about
[00:02:56] 100 articles and about half a million
[00:02:58] words. So there's a few other things
[00:02:59] that we'll cover later, but the TLDDR is
[00:03:02] you give raw data to cloud code. It
[00:03:04] compares it, it organizes it, and then
[00:03:05] it puts it into the right spots with
[00:03:07] relationships, and then you can query it
[00:03:09] about anything. And it can help you
[00:03:10] identify where there's gaps in that node
[00:03:12] or in that, you know, relationship, and
[00:03:14] it can go do research and fill in the
[00:03:16] gaps. All right. So why is this a big
[00:03:17] deal? Because normal AI chats are
[00:03:19] ephemeral, meaning the knowledge
[00:03:21] disappears after the conversation. But
[00:03:23] this method, using Karpathy's LLM wiki,
[00:03:25] makes knowledge compound like interest
[00:03:27] in a bank. People on X are calling it a
[00:03:29] game changanger because it finally makes
[00:03:30] AI feel like a tireless colleague who
[00:03:32] actually remembers everything and it
[00:03:33] stays organized. It's also super simple.
[00:03:36] It will take you five minutes to set up.
[00:03:37] I'll show you guys. You don't need a
[00:03:39] fancy vector database embeddings or
[00:03:40] complex infrastructure. It's literally
[00:03:42] just a folder with markdown files.
[00:03:44] That's it. You literally just have a
[00:03:46] vault up top. So in this example, it's
[00:03:47] called my wiki. You've got a raw folder
[00:03:49] where you put all of the stuff. And then
[00:03:51] you've got a wiki folder, which is what
[00:03:53] the LLM takes from your raw and puts it
[00:03:55] into the wiki. So in here you have all
[00:03:57] the wiki pages which it will create but
[00:03:59] then you also have an index and you have
[00:04:00] a log. So for example in my YouTube
[00:04:02] transcripts vault here is the index. You
[00:04:05] can see that I have all these different
[00:04:06] tools which I could obviously click on
[00:04:07] and it would take me right to that page
[00:04:09] or after that I have all the different
[00:04:10] techniques agent teams sub agents
[00:04:13] permission modes the WAT framework and
[00:04:15] then we've got different concepts MCP
[00:04:17] servers rag vibe coding we've got all
[00:04:19] these different sources which are you
[00:04:20] know the YouTube videos and then when I
[00:04:22] have people or when I have comparisons
[00:04:24] they will be put in here in the index
[00:04:26] and then we also have a log which is the
[00:04:28] operation history so in this case in the
[00:04:30] YouTube project the log isn't huge cuz I
[00:04:31] only ran one huge batch of the initial
[00:04:33] 36 YouTube videos, but now every time I
[00:04:36] have one, I say, "Hey, can you go ahead
[00:04:38] and ingest the new YouTube video into
[00:04:40] the wiki and then we'll see every single
[00:04:42] time we update this." And then, of
[00:04:44] course, you need your claw. MD to
[00:04:45] explain how the project works and how to
[00:04:47] search through things and how to, you
[00:04:49] know, update things. It's also a big
[00:04:51] deal from a cost perspective, token
[00:04:52] efficiency, and long-term value. One X
[00:04:54] user turned 383 scattered files and over
[00:04:57] a 100 meeting transcripts into a compact
[00:04:59] wiki and dropped token usage by 95% when
[00:05:02] querying with Claude. And obviously
[00:05:04] token management and efficiency is a
[00:05:06] huge conversation right now and will
[00:05:08] always be. The other thing that's really
[00:05:09] cool about this is there's not really
[00:05:11] like a GitHub repo you go copy or
[00:05:12] there's not a complicated setup. You
[00:05:14] literally just say hey cloud code read
[00:05:16] this idea from Andre Karpathy and
[00:05:18] implement it. And people on X are now
[00:05:20] talking about like this is how 2026 AI
[00:05:22] agentic software and products will be
[00:05:24] made. You just give it a highle idea and
[00:05:26] it goes and builds it out. And Karpathy
[00:05:28] even said, "Hey, you know, I left this
[00:05:30] prompt vague so that you guys can
[00:05:31] customize it." And I'll show you the
[00:05:33] ways in my two different vaults right
[00:05:34] now that it changed things a little bit
[00:05:36] based on the context and understanding
[00:05:38] of what the project is actually for.
[00:05:39] Okay, so this was the original tweet I
[00:05:41] just showed you guys and then he
[00:05:42] followed up and said, "Hey, this one
[00:05:43] went viral. So here is the idea in a
[00:05:45] gist format." So if you open this up,
[00:05:47] this is basically just another
[00:05:48] explanation of the core idea of how this
[00:05:50] works and why the architecture,
[00:05:52] indexing, all this kind of stuff. And by
[00:05:54] the way, this is the part where he says,
[00:05:55] "Hey, this is left vague so that you can
[00:05:56] hack it and customize it to your own
[00:05:58] project." So we're going to come right
[00:06:00] back to this in a sec, but the first
[00:06:01] prerec that we're going to do, it's not
[00:06:03] necessary, but I like to have a nice
[00:06:05] little front end to see the
[00:06:06] relationships, is we're going to go to
[00:06:08] Obsidian and download it. So, if you
[00:06:10] just go to obsidian.mmd, you can see
[00:06:12] this is the completely free tool and
[00:06:14] you're going to go ahead and download
[00:06:15] it. So, just for your operating system,
[00:06:17] download this and then open up the
[00:06:20] wizard and open up the app. So, when you
[00:06:22] open up the app, it'll look like this.
[00:06:23] And what we're going to do here is we're
[00:06:24] going to create a new vault. So, down
[00:06:25] here, you can see I have Herk Brain and
[00:06:27] I have YouTube transcripts. I'll just
[00:06:29] make it a little bigger. I'm going to go
[00:06:30] to manage vaults. I'm going to create a
[00:06:32] new one. And now, we just have to give
[00:06:34] this a name. So, I'm just going to call
[00:06:35] this one demo vault. and you're going to
[00:06:38] choose a location where you want to put
[00:06:39] this. So, I'm just throwing this on my
[00:06:41] desktop and I'm going to go ahead and
[00:06:42] create this vault. Then, what you're
[00:06:44] going to do is go to wherever you like
[00:06:46] to run Cloud Code. So, in this case, I'm
[00:06:47] doing it in VS Code. And I open up that
[00:06:50] folder. So, demo vault. We get an
[00:06:51] Obsidian and then we get a welcome.md.
[00:06:54] So, I'm going to open up Claude. So, I'm
[00:06:56] going to do it in my terminal. I'm going
[00:06:57] to run Claude. And lately, I've been
[00:06:59] liking using my terminal better for
[00:07:00] Claude. I like to do it inside of VS
[00:07:02] Code, but the reason is just because I
[00:07:04] like to see the status line and I have,
[00:07:06] you know, a little bit more
[00:07:06] functionality. So, anyways, now that we
[00:07:08] have Cloud Code open, here's what we're
[00:07:10] going to do. We're going to go back over
[00:07:12] to the LLM wiki thing that we got from
[00:07:13] Andre Carpathy. We're going to copy all
[00:07:15] of this and we're going to go back into
[00:07:19] Cloud Code and then just paste it in
[00:07:21] there. So, that is the prompt from
[00:07:23] Carpathy that's going to build out
[00:07:25] everything we need. And then before we
[00:07:26] send that off, we're dropping this in
[00:07:28] which you guys can screenshot and then
[00:07:29] just throw into yours. But I'm saying
[00:07:31] you are now my LLM wiki agent. Implement
[00:07:34] this exact idea file as my complete
[00:07:36] second brain. Guide me step by step.
[00:07:38] Create the cloudmd schema blah blah
[00:07:39] blah. So this is just telling it what it
[00:07:41] needs to do with this idea that we just
[00:07:43] got from kpathy. So anyways, on the
[00:07:45] right we have this cloud code running
[00:07:47] and on the left we have our obsidian
[00:07:48] vault and you can see it just created
[00:07:50] those two folders. So it created the raw
[00:07:52] and it created the wiki as you can see.
[00:07:54] Now, by default, it threw in four
[00:07:55] folders. It threw in analysis, concepts,
[00:07:57] entities, and sources. Once we start to
[00:07:59] populate stuff, we can talk to it to see
[00:08:00] if that's actually the way we want to do
[00:08:02] it or not. Because it's interesting in
[00:08:04] my personal kind of second brain, the
[00:08:06] wiki is literally just markdown files.
[00:08:08] There's no structure to it. And in some
[00:08:10] cases, that's good. Carpathy actually
[00:08:11] said, "Sometimes I like to keep it
[00:08:13] really simple and really flat, which
[00:08:14] means like no subfolders and not a bunch
[00:08:17] of over organizing." But then you guys
[00:08:19] did see in my YouTube transcript one,
[00:08:20] there were different subfolders. And I
[00:08:22] think that in this case it actually
[00:08:23] makes more sense. But you can see that
[00:08:25] it went ahead and it created a claw.md.
[00:08:27] It created an index and a log and then a
[00:08:29] few different folders in our wiki. But
[00:08:31] now it's saying, "Hey, let's go ahead
[00:08:31] and try it out. Drop in your first
[00:08:33] source into the raw folder and tell me
[00:08:35] to ingest it." Okay, so I'm at this
[00:08:36] website called AI2027. If you guys
[00:08:38] haven't read this before, it's kind of
[00:08:40] an interesting read. So go check it out.
[00:08:42] And now let's say I want to get this
[00:08:43] into my vault. What I could do is just
[00:08:45] copy the whole page, right? And it might
[00:08:47] just come through a little weird. or we
[00:08:49] can just get an Obsidian extension which
[00:08:51] lets us basically take articles right
[00:08:53] from the web and just put it right into
[00:08:54] our vault. Super easy. So search for
[00:08:56] this extension called Obsidian Web
[00:08:58] Clipper. You would go ahead and add this
[00:08:59] to Chrome. So then when you're in the
[00:09:00] article that you want, you basically
[00:09:02] just click on your extensions, you open
[00:09:03] up Obsidian Web Clipper, and then you
[00:09:05] can just chuck it into your vault. And
[00:09:06] then right here, you're going to want to
[00:09:07] set this to RAW because this is the
[00:09:09] actual folder that it's going to put it
[00:09:10] in. So you can go ahead and click add to
[00:09:12] Obsidian. Open Obsidian. And then now
[00:09:14] you can see in my raw section we have
[00:09:16] this AI 2027 source with the title the
[00:09:20] source and it's not super super
[00:09:22] populated yet because the LLM in cloud
[00:09:24] code is going to do that. So here is our
[00:09:27] file. I'm going to open up cloud code
[00:09:28] and say awesome. I just threw in an
[00:09:30] article called AI 2027 into the raw. Can
[00:09:32] you please go ahead and ingest that? It
[00:09:35] might ask you some questions. It might
[00:09:36] also be helpful to before you start
[00:09:38] ingesting stuff say hey by the way this
[00:09:39] project is specifically for my second
[00:09:41] brain. So, personal things, business
[00:09:43] things, whatever. Or this is just a
[00:09:45] research project. This is where I'm
[00:09:46] going to chuck you all the articles and
[00:09:48] all the things that I want to learn
[00:09:49] about and all the things that I know.
[00:09:50] So, there's different ways that you can
[00:09:51] set up the project as you saw with mine.
[00:09:53] One for YouTube, one for just personal
[00:09:56] second brain. So, now what it's doing is
[00:09:57] it's going to read through this article
[00:09:59] and then it's going to figure out where
[00:10:01] should I chuck everything into the wiki.
[00:10:02] It's not just going to create one MD
[00:10:04] file for this. It might create five or
[00:10:06] it might create 10. And there's going to
[00:10:07] be relationships between each of the
[00:10:09] different sections that it creates. So,
[00:10:10] it's kind of doing its own method of
[00:10:12] chunking. Now, one thing I want to call
[00:10:13] out real quick is with this extension,
[00:10:15] if you go here and you open up the
[00:10:17] options for it, you can see that you can
[00:10:19] actually change where by default the
[00:10:22] folders are dropped, which is in the
[00:10:24] location section. By default, it'll be
[00:10:26] going to a place called clippings, but
[00:10:27] just go ahead and change that to raw.
[00:10:29] Okay. So, here it came back with all
[00:10:30] these questions, right? It said, "Here
[00:10:32] are my key takeaways from this article,
[00:10:34] blah blah blah." And now it'll ask you,
[00:10:35] "What do you want to emphasize from this
[00:10:36] article? What's your focus? How granular
[00:10:38] do you want to be? what's your plan? So,
[00:10:40] I'm just going to say I want this to be
[00:10:42] extremely thorough. This is my passion
[00:10:45] looking at where AI is going to go. Um,
[00:10:47] and this whole project, by the way, that
[00:10:49] you're setting up in this vault is
[00:10:50] basically just going to be my place to
[00:10:52] dump in research about AI. So, help me
[00:10:54] keep all that organized so that I can
[00:10:55] query it and that I can, you know, keep
[00:10:57] my thoughts related. So, that's just a
[00:11:00] quick example of what it might look like
[00:11:01] for you to give it some more context to
[00:11:03] continuously build your project. So, I'm
[00:11:06] going to switch over over here to the
[00:11:07] graph view because I think it it'll be
[00:11:09] interesting to see as it is starting to
[00:11:10] go through and create those different
[00:11:12] wiki files. It's going to go ahead and
[00:11:14] it's going to create all those
[00:11:14] relationships and we'll be able to watch
[00:11:16] it in real time. All right, so it's
[00:11:17] creating all of the wiki pages now and
[00:11:19] you can see that it said it's going to
[00:11:20] make about 25 because there's so much
[00:11:23] stuff going on in the original AI 2027
[00:11:26] article. Okay, so our first one just
[00:11:27] popped in here and there a second one
[00:11:28] just came through and now you can
[00:11:30] understand you're starting to see where
[00:11:31] do you have hubs or where do you just
[00:11:33] have little individual nodes? So this is
[00:11:35] a major hub. Someone named Eli, someone
[00:11:38] named Thomas, Daniel, and you can see
[00:11:40] all the different relationships here
[00:11:41] with things like AI governance with
[00:11:43] things like OpenBrain, superhuman coder.
[00:11:46] Okay, so that ingest took about 10
[00:11:47] minutes. So sometimes you have to be a
[00:11:49] little patient with, you know, it
[00:11:50] reading through everything and
[00:11:51] organizing everything, but it does a lot
[00:11:53] of heavy lifting, of course. When I
[00:11:54] uploaded the 36 YouTube transcripts in
[00:11:57] batch, it took about 14 minutes. So it
[00:11:59] kind of just depends, but it created 23
[00:12:01] wiki pages. We have the source. We have
[00:12:04] six people, five organizations and one
[00:12:06] AI systems page, different concepts, so
[00:12:08] technical alignment and geopolitical and
[00:12:11] then an analysis and then it asks some
[00:12:13] questions about it so that it can help
[00:12:15] make the relationships and make the
[00:12:16] structure even better. Now let's just
[00:12:19] open this one up a little bit deeper and
[00:12:20] see what it actually did in here with
[00:12:22] this stuff. So we have this is the
[00:12:25] source with all the main relationships.
[00:12:27] So as we start to add other articles, we
[00:12:28] will see other big kind of like nodes
[00:12:30] and maybe in some cases we'll have
[00:12:32] relationships between like compute
[00:12:33] scaling with different articles that we
[00:12:35] upload as well. So let's just see if I
[00:12:37] click into the main source, we can see
[00:12:39] the tags that it got. We can see the
[00:12:41] authors and we can click around. So
[00:12:42] here's a link to OpenAI. Okay, what's
[00:12:44] OpenAI? Here's references in AI 2027.
[00:12:46] Here's some other connections with
[00:12:47] OpenAI like modelsp spec. Okay, we're in
[00:12:50] model spec. Let's take a look. We can
[00:12:51] see other things about modelsp spec. And
[00:12:53] we could also go to how the LLM
[00:12:55] psychology model works. So this is just
[00:12:57] super super cool all the relationships
[00:12:59] that we get. And once again, all of this
[00:13:01] stuff that we're looking at was derived
[00:13:02] from one article and automatically
[00:13:04] organized and related. So the question
[00:13:06] now is like what do we do from here? Do
[00:13:08] we query it inside of this environment?
[00:13:10] Do we query it from somewhere else? And
[00:13:12] that's completely up to the way that you
[00:13:14] want to use this. So for example, with
[00:13:15] my YouTube project, I'm probably just
[00:13:17] going to keep this here. And whenever I
[00:13:18] want to ask questions about YouTube or
[00:13:20] if I want to turn this into like a
[00:13:21] website, I can just do that from here.
[00:13:23] Or if I need to, I can point a different
[00:13:26] project at this folder since
[00:13:27] everything's here and it can crawl
[00:13:28] through the wiki, it can read the index
[00:13:30] and it knows how this stuff works
[00:13:32] because you can give it the clawmd so it
[00:13:34] understands the project as well. So for
[00:13:36] example, in this one which is just my
[00:13:37] second brain where we have all of the
[00:13:39] different things about like I drop in my
[00:13:40] meeting recordings, I drop in, you know,
[00:13:42] ClickUp channels, summaries and things
[00:13:44] like that. This is something that I want
[00:13:45] to use in my executive assistant. So
[00:13:47] what I did in my executive assistant
[00:13:48] here called Herk 2, if I go to this
[00:13:50] cloud.MD, MD you can see that we have a
[00:13:52] wiki path. So whenever you need to read
[00:13:55] things about me and my business that you
[00:13:56] don't have already, you would basically
[00:13:58] go to my herkbrain vault. You would go
[00:14:00] to that directory and then you would
[00:14:02] read through the wiki. You can read the
[00:14:03] hot cache which I'll explain in just a
[00:14:05] sec. You can read the index. You can
[00:14:06] read the domain subindex and then you
[00:14:08] can also just search through everything
[00:14:10] here. And I said don't read from the
[00:14:11] wiki unless you actually need it. Here
[00:14:13] are some things that you might do that
[00:14:14] you don't need to go read the wiki for.
[00:14:16] And all of this is my business
[00:14:17] knowledge. Now, if you guys remember, if
[00:14:19] you watched my video on setting up an
[00:14:20] executive assistant, I used to do this
[00:14:22] with context files inside of this
[00:14:24] project. And when I changed over to this
[00:14:26] method, I actually saw a reduction in
[00:14:28] tokens that I was actually calling in
[00:14:30] this project. So, the thing about the
[00:14:31] hot cache, right, I didn't actually have
[00:14:34] this in my YouTube one. So, if I go to
[00:14:36] YouTube, you can see there's no hot
[00:14:37] cache. But, if I go to the herk brain in
[00:14:40] the wiki, you can see there's a hot.mmd
[00:14:42] right here. And this is basically just a
[00:14:44] cache of like 500 words or 500
[00:14:46] characters that it saves, which is like
[00:14:48] what is the most recent thing that Nate
[00:14:50] just gave me or that we talked about. In
[00:14:52] the context of my executive assistant,
[00:14:53] this is really helpful. You know, it
[00:14:55] might save me from having to crawl
[00:14:56] different wiki pages. But in something
[00:14:58] like the YouTube transcript project, I
[00:15:00] don't really need a hot cache. So,
[00:15:02] another thing that I alluded to but
[00:15:03] didn't really cover was the idea of
[00:15:05] linting. So Karpathi says that he runs
[00:15:07] some LLM health checks over the wiki to
[00:15:09] find inconsistent data, impute missing
[00:15:12] data with web searches, find interesting
[00:15:14] connections for new article candidates,
[00:15:16] things like that. So it basically helps
[00:15:18] you run a lint, you know, every day,
[00:15:20] every week, whenever you want, which
[00:15:21] helps make sure that everything is
[00:15:23] scalable and structured in the right
[00:15:24] way. And it might even come back and
[00:15:26] say, "Hey, I don't fully understand
[00:15:28] this. Can you give me some more info or
[00:15:29] can you grab some more articles that
[00:15:30] might help me out here?" So now the
[00:15:32] final question about this that I wanted
[00:15:33] to cover is like does this kill semantic
[00:15:36] search rag? And the answer is no, but
[00:15:38] kind of yes. And it all depends on the
[00:15:41] goal of the project and the goal of the
[00:15:43] context, how much context you have. So
[00:15:45] here's a really quick chart that I had
[00:15:47] my cloud code make. I was in my Herk
[00:15:49] brain where I dumped in a bunch of
[00:15:50] information about Karpathy's LLM
[00:15:52] knowledge and I just said, "Hey, can you
[00:15:54] please explain Karpathy knowledge as
[00:15:56] simple as possible, keep it super
[00:15:58] concise, and um compare it to typical
[00:16:01] semantic search rag." So, it found
[00:16:04] Carpathy's idea. Instead of a database,
[00:16:06] you just give the LM well organized
[00:16:07] markdown files and it compares it here
[00:16:09] to the actual semantic search rag. So,
[00:16:12] actually, I might as well just read it
[00:16:13] off from here. So it finds it by reading
[00:16:15] indexes and follows links rather than
[00:16:17] using similarity search. So we're
[00:16:19] getting a deeper understanding of
[00:16:20] relationships because they're links
[00:16:22] rather than just saying, "Hey, these
[00:16:23] chunks seem similar." As far as
[00:16:25] infrastructure, it is literally just
[00:16:26] markdown. So like I said, you don't even
[00:16:28] need the obsidian. You just need these
[00:16:30] markdown files. Whereas with semantic
[00:16:32] search, you need an embedding model. You
[00:16:33] need a vector database and a chunking
[00:16:35] pipeline. The cost over here is
[00:16:37] basically free. Your only cost is going
[00:16:38] to be tokens. Whereas over here, you
[00:16:40] might have ongoing compute and storage.
[00:16:42] And for maintenance, you just run a
[00:16:43] lint. You clean up things. You add more
[00:16:45] articles. You give it more context
[00:16:47] rather than having to re-mbed when
[00:16:49] things change. But right now, the
[00:16:51] weakness of course with the uh LLM
[00:16:53] knowledge wiki is that it doesn't scale
[00:16:56] huge across enterprises, right? Because
[00:16:58] it's just a bunch of files. Um and that
[00:17:00] is where the cost will probably get more
[00:17:02] and more expensive than going to
[00:17:04] something like standard semantic search
[00:17:05] or knowledger graph or light rag or
[00:17:08] whatever other tool is out there for
[00:17:09] that. So here you can see if you have
[00:17:10] hundreds of pages with good indexes,
[00:17:12] you're fine with wiki graph. But if you
[00:17:14] were getting up to the millions of
[00:17:15] documents, then you're going to want to
[00:17:16] actually do more of a traditional rag
[00:17:18] pipeline, at least for now with how the
[00:17:20] current models are and everything we
[00:17:22] know right now in April 2026. So that is
[00:17:25] going to do it for today. I hope you
[00:17:27] guys learned something new or enjoyed
[00:17:28] the video. And if you did, please give
[00:17:29] it a like. It helps me out a ton. Now,
[00:17:31] after this video, if you're interested
[00:17:32] in learning how you can create your own
[00:17:33] sort of executive assistant and then
[00:17:35] plug it into this Obsidian vault, then
[00:17:37] definitely check out this video up here
[00:17:38] where I go over how I built my executive
[00:17:40] assistant and the way that you should be
[00:17:42] thinking about it. So hopefully I'll see
[00:17:43] you guys over there, but if not, I'll
[00:17:45] see you in the next

---

## Transcript

[00:00:00] What you're looking at right here is 36
[00:00:02] of my most recent YouTube videos
[00:00:03] organized into an actual knowledge
[00:00:05] system that makes sense. And in today's
[00:00:07] video, I'm going to show you how you can
[00:00:08] set this up in 5 minutes. It's super
[00:00:10] super easy. You can see here how we have
[00:00:12] these different nodes and different
[00:00:13] patterns emerging. And as we zoom in, we
[00:00:15] can see what each of these little dots
[00:00:17] represents. So, for example, this is one
[00:00:19] of my videos, $10,000 aentic workflows.
[00:00:22] We can see it's got some tags. It's got
[00:00:23] the video link. It's got the raw file.
[00:00:26] And it gives an explanation of what this
[00:00:27] video is about and what the takeaways
[00:00:29] are. And the coolest part is I can
[00:00:31] follow the back links to get where I
[00:00:32] want. There's a backlink for the WAT
[00:00:34] framework. There's a backlink for Claude
[00:00:36] Code. There's a backlink for all these
[00:00:38] different tools I mentioned like
[00:00:39] Perplexity, Visual Studio Code, Nano
[00:00:41] Banana, Naden N. It also has techniques
[00:00:43] like the WT framework or bypass
[00:00:45] permissions mode or human review
[00:00:47] checkpoint. So, as this continues to
[00:00:49] fill up, we can start to see patterns
[00:00:50] and relationships between every tool or
[00:00:53] every skill or every MCP server that I
[00:00:55] might have talked about in a YouTube
[00:00:56] video. And I can just query it in a
[00:00:58] really efficient way now that we have
[00:01:00] this actual system set up. And the crazy
[00:01:02] part is I said, "Hey, Cloud Code, go
[00:01:04] grab the transcripts from my recent
[00:01:05] videos and organize everything. I
[00:01:07] literally didn't have to do any manual
[00:01:10] relationship building here. It just
[00:01:11] figured it all out on its own." And then
[00:01:13] right here, I have a much smaller one,
[00:01:14] but this is more of my personal brain.
[00:01:16] So this is stuff going on in my personal
[00:01:18] life. This is stuff going on with, you
[00:01:19] know, UpAI or my YouTube channel or my
[00:01:21] different businesses and my employees
[00:01:23] and our quarter 2 initiatives and things
[00:01:25] like that. This is more of my own second
[00:01:27] brain. So I've got one second brain here
[00:01:28] and then I've got one basically YouTube
[00:01:30] knowledge system and I could combine
[00:01:33] these or I could keep them separate and
[00:01:34] I can just keep building more knowledge
[00:01:36] systems and plug them all into other AI
[00:01:38] agents that I need to have this context.
[00:01:40] It's just super cool. So Andre Carpathy
[00:01:42] just released this little post about LLM
[00:01:44] knowledge bases and explaining what he's
[00:01:46] been doing with them. And in just a
[00:01:47] matter of few days, it got a ton of
[00:01:48] traction on X. So let's do a quick
[00:01:50] breakdown and then I'm going to show you
[00:01:51] guys how you can get this set up in
[00:01:52] basically 5 minutes. It's way more
[00:01:54] simple than you may think. Something
[00:01:56] I've been finding very useful recently
[00:01:57] is using LLM to build personal knowledge
[00:01:59] bases for various topics of research
[00:02:01] interest. So there's different stages.
[00:02:03] The first part is data ingest. He puts
[00:02:05] in basically source documents. So he
[00:02:07] basically takes a PDF and puts it into
[00:02:09] Cloud Code and then Cloud Code does the
[00:02:11] rest. He uses Obsidian as the IDE. So
[00:02:13] this is nothing really too
[00:02:14] game-changing. Obsidian just lets you
[00:02:16] visually see your markdown files. But
[00:02:18] for example, this Obsidian project right
[00:02:20] here with all this YouTube transcript
[00:02:21] stuff that actually lives right here.
[00:02:23] This is the exact same thing. Here are
[00:02:24] the raw YouTube transcripts. And here's
[00:02:26] that wiki that I showed you guys with
[00:02:27] the different um folders for what Cloud
[00:02:31] Code did with my YouTube transcripts.
[00:02:32] And then there's a Q&A phase where you
[00:02:34] basically can ask questions about
[00:02:36] YouTube or about the research and it can
[00:02:38] look through the entire wiki in a much
[00:02:40] more efficient way and it can give you
[00:02:42] answers that are super intelligent. He
[00:02:44] said here, "I thought that I had to
[00:02:45] reach for fancy rag, but the LLM has
[00:02:47] been pretty good about automaintaining
[00:02:48] index files and brief summaries of all
[00:02:50] documents and it reads all the important
[00:02:52] related data fairly easily at this small
[00:02:54] scale." So right now he's doing about
[00:02:56] 100 articles and about half a million
[00:02:58] words. So there's a few other things
[00:02:59] that we'll cover later, but the TLDDR is
[00:03:02] you give raw data to cloud code. It
[00:03:04] compares it, it organizes it, and then
[00:03:05] it puts it into the right spots with
[00:03:07] relationships, and then you can query it
[00:03:09] about anything. And it can help you
[00:03:10] identify where there's gaps in that node
[00:03:12] or in that, you know, relationship, and
[00:03:14] it can go do research and fill in the
[00:03:16] gaps. All right. So why is this a big
[00:03:17] deal? Because normal AI chats are
[00:03:19] ephemeral, meaning the knowledge
[00:03:21] disappears after the conversation. But
[00:03:23] this method, using Karpathy's LLM wiki,
[00:03:25] makes knowledge compound like interest
[00:03:27] in a bank. People on X are calling it a
[00:03:29] game changanger because it finally makes
[00:03:30] AI feel like a tireless colleague who
[00:03:32] actually remembers everything and it
[00:03:33] stays organized. It's also super simple.
[00:03:36] It will take you five minutes to set up.
[00:03:37] I'll show you guys. You don't need a
[00:03:39] fancy vector database embeddings or
[00:03:40] complex infrastructure. It's literally
[00:03:42] just a folder with markdown files.
[00:03:44] That's it. You literally just have a
[00:03:46] vault up top. So in this example, it's
[00:03:47] called my wiki. You've got a raw folder
[00:03:49] where you put all of the stuff. And then
[00:03:51] you've got a wiki folder, which is what
[00:03:53] the LLM takes from your raw and puts it
[00:03:55] into the wiki. So in here you have all
[00:03:57] the wiki pages which it will create but
[00:03:59] then you also have an index and you have
[00:04:00] a log. So for example in my YouTube
[00:04:02] transcripts vault here is the index. You
[00:04:05] can see that I have all these different
[00:04:06] tools which I could obviously click on
[00:04:07] and it would take me right to that page
[00:04:09] or after that I have all the different
[00:04:10] techniques agent teams sub agents
[00:04:13] permission modes the WAT framework and
[00:04:15] then we've got different concepts MCP
[00:04:17] servers rag vibe coding we've got all
[00:04:19] these different sources which are you
[00:04:20] know the YouTube videos and then when I
[00:04:22] have people or when I have comparisons
[00:04:24] they will be put in here in the index
[00:04:26] and then we also have a log which is the
[00:04:28] operation history so in this case in the
[00:04:30] YouTube project the log isn't huge cuz I
[00:04:31] only ran one huge batch of the initial
[00:04:33] 36 YouTube videos, but now every time I
[00:04:36] have one, I say, "Hey, can you go ahead
[00:04:38] and ingest the new YouTube video into
[00:04:40] the wiki and then we'll see every single
[00:04:42] time we update this." And then, of
[00:04:44] course, you need your claw. MD to
[00:04:45] explain how the project works and how to
[00:04:47] search through things and how to, you
[00:04:49] know, update things. It's also a big
[00:04:51] deal from a cost perspective, token
[00:04:52] efficiency, and long-term value. One X
[00:04:54] user turned 383 scattered files and over
[00:04:57] a 100 meeting transcripts into a compact
[00:04:59] wiki and dropped token usage by 95% when
[00:05:02] querying with Claude. And obviously
[00:05:04] token management and efficiency is a
[00:05:06] huge conversation right now and will
[00:05:08] always be. The other thing that's really
[00:05:09] cool about this is there's not really
[00:05:11] like a GitHub repo you go copy or
[00:05:12] there's not a complicated setup. You
[00:05:14] literally just say hey cloud code read
[00:05:16] this idea from Andre Karpathy and
[00:05:18] implement it. And people on X are now
[00:05:20] talking about like this is how 2026 AI
[00:05:22] agentic software and products will be
[00:05:24] made. You just give it a highle idea and
[00:05:26] it goes and builds it out. And Karpathy
[00:05:28] even said, "Hey, you know, I left this
[00:05:30] prompt vague so that you guys can
[00:05:31] customize it." And I'll show you the
[00:05:33] ways in my two different vaults right
[00:05:34] now that it changed things a little bit
[00:05:36] based on the context and understanding
[00:05:38] of what the project is actually for.
[00:05:39] Okay, so this was the original tweet I
[00:05:41] just showed you guys and then he
[00:05:42] followed up and said, "Hey, this one
[00:05:43] went viral. So here is the idea in a
[00:05:45] gist format." So if you open this up,
[00:05:47] this is basically just another
[00:05:48] explanation of the core idea of how this
[00:05:50] works and why the architecture,
[00:05:52] indexing, all this kind of stuff. And by
[00:05:54] the way, this is the part where he says,
[00:05:55] "Hey, this is left vague so that you can
[00:05:56] hack it and customize it to your own
[00:05:58] project." So we're going to come right
[00:06:00] back to this in a sec, but the first
[00:06:01] prerec that we're going to do, it's not
[00:06:03] necessary, but I like to have a nice
[00:06:05] little front end to see the
[00:06:06] relationships, is we're going to go to
[00:06:08] Obsidian and download it. So, if you
[00:06:10] just go to obsidian.mmd, you can see
[00:06:12] this is the completely free tool and
[00:06:14] you're going to go ahead and download
[00:06:15] it. So, just for your operating system,
[00:06:17] download this and then open up the
[00:06:20] wizard and open up the app. So, when you
[00:06:22] open up the app, it'll look like this.
[00:06:23] And what we're going to do here is we're
[00:06:24] going to create a new vault. So, down
[00:06:25] here, you can see I have Herk Brain and
[00:06:27] I have YouTube transcripts. I'll just
[00:06:29] make it a little bigger. I'm going to go
[00:06:30] to manage vaults. I'm going to create a
[00:06:32] new one. And now, we just have to give
[00:06:34] this a name. So, I'm just going to call
[00:06:35] this one demo vault. and you're going to
[00:06:38] choose a location where you want to put
[00:06:39] this. So, I'm just throwing this on my
[00:06:41] desktop and I'm going to go ahead and
[00:06:42] create this vault. Then, what you're
[00:06:44] going to do is go to wherever you like
[00:06:46] to run Cloud Code. So, in this case, I'm
[00:06:47] doing it in VS Code. And I open up that
[00:06:50] folder. So, demo vault. We get an
[00:06:51] Obsidian and then we get a welcome.md.
[00:06:54] So, I'm going to open up Claude. So, I'm
[00:06:56] going to do it in my terminal. I'm going
[00:06:57] to run Claude. And lately, I've been
[00:06:59] liking using my terminal better for
[00:07:00] Claude. I like to do it inside of VS
[00:07:02] Code, but the reason is just because I
[00:07:04] like to see the status line and I have,
[00:07:06] you know, a little bit more
[00:07:06] functionality. So, anyways, now that we
[00:07:08] have Cloud Code open, here's what we're
[00:07:10] going to do. We're going to go back over
[00:07:12] to the LLM wiki thing that we got from
[00:07:13] Andre Carpathy. We're going to copy all
[00:07:15] of this and we're going to go back into
[00:07:19] Cloud Code and then just paste it in
[00:07:21] there. So, that is the prompt from
[00:07:23] Carpathy that's going to build out
[00:07:25] everything we need. And then before we
[00:07:26] send that off, we're dropping this in
[00:07:28] which you guys can screenshot and then
[00:07:29] just throw into yours. But I'm saying
[00:07:31] you are now my LLM wiki agent. Implement
[00:07:34] this exact idea file as my complete
[00:07:36] second brain. Guide me step by step.
[00:07:38] Create the cloudmd schema blah blah
[00:07:39] blah. So this is just telling it what it
[00:07:41] needs to do with this idea that we just
[00:07:43] got from kpathy. So anyways, on the
[00:07:45] right we have this cloud code running
[00:07:47] and on the left we have our obsidian
[00:07:48] vault and you can see it just created
[00:07:50] those two folders. So it created the raw
[00:07:52] and it created the wiki as you can see.
[00:07:54] Now, by default, it threw in four
[00:07:55] folders. It threw in analysis, concepts,
[00:07:57] entities, and sources. Once we start to
[00:07:59] populate stuff, we can talk to it to see
[00:08:00] if that's actually the way we want to do
[00:08:02] it or not. Because it's interesting in
[00:08:04] my personal kind of second brain, the
[00:08:06] wiki is literally just markdown files.
[00:08:08] There's no structure to it. And in some
[00:08:10] cases, that's good. Carpathy actually
[00:08:11] said, "Sometimes I like to keep it
[00:08:13] really simple and really flat, which
[00:08:14] means like no subfolders and not a bunch
[00:08:17] of over organizing." But then you guys
[00:08:19] did see in my YouTube transcript one,
[00:08:20] there were different subfolders. And I
[00:08:22] think that in this case it actually
[00:08:23] makes more sense. But you can see that
[00:08:25] it went ahead and it created a claw.md.
[00:08:27] It created an index and a log and then a
[00:08:29] few different folders in our wiki. But
[00:08:31] now it's saying, "Hey, let's go ahead
[00:08:31] and try it out. Drop in your first
[00:08:33] source into the raw folder and tell me
[00:08:35] to ingest it." Okay, so I'm at this
[00:08:36] website called AI2027. If you guys
[00:08:38] haven't read this before, it's kind of
[00:08:40] an interesting read. So go check it out.
[00:08:42] And now let's say I want to get this
[00:08:43] into my vault. What I could do is just
[00:08:45] copy the whole page, right? And it might
[00:08:47] just come through a little weird. or we
[00:08:49] can just get an Obsidian extension which
[00:08:51] lets us basically take articles right
[00:08:53] from the web and just put it right into
[00:08:54] our vault. Super easy. So search for
[00:08:56] this extension called Obsidian Web
[00:08:58] Clipper. You would go ahead and add this
[00:08:59] to Chrome. So then when you're in the
[00:09:00] article that you want, you basically
[00:09:02] just click on your extensions, you open
[00:09:03] up Obsidian Web Clipper, and then you
[00:09:05] can just chuck it into your vault. And
[00:09:06] then right here, you're going to want to
[00:09:07] set this to RAW because this is the
[00:09:09] actual folder that it's going to put it
[00:09:10] in. So you can go ahead and click add to
[00:09:12] Obsidian. Open Obsidian. And then now
[00:09:14] you can see in my raw section we have
[00:09:16] this AI 2027 source with the title the
[00:09:20] source and it's not super super
[00:09:22] populated yet because the LLM in cloud
[00:09:24] code is going to do that. So here is our
[00:09:27] file. I'm going to open up cloud code
[00:09:28] and say awesome. I just threw in an
[00:09:30] article called AI 2027 into the raw. Can
[00:09:32] you please go ahead and ingest that? It
[00:09:35] might ask you some questions. It might
[00:09:36] also be helpful to before you start
[00:09:38] ingesting stuff say hey by the way this
[00:09:39] project is specifically for my second
[00:09:41] brain. So, personal things, business
[00:09:43] things, whatever. Or this is just a
[00:09:45] research project. This is where I'm
[00:09:46] going to chuck you all the articles and
[00:09:48] all the things that I want to learn
[00:09:49] about and all the things that I know.
[00:09:50] So, there's different ways that you can
[00:09:51] set up the project as you saw with mine.
[00:09:53] One for YouTube, one for just personal
[00:09:56] second brain. So, now what it's doing is
[00:09:57] it's going to read through this article
[00:09:59] and then it's going to figure out where
[00:10:01] should I chuck everything into the wiki.
[00:10:02] It's not just going to create one MD
[00:10:04] file for this. It might create five or
[00:10:06] it might create 10. And there's going to
[00:10:07] be relationships between each of the
[00:10:09] different sections that it creates. So,
[00:10:10] it's kind of doing its own method of
[00:10:12] chunking. Now, one thing I want to call
[00:10:13] out real quick is with this extension,
[00:10:15] if you go here and you open up the
[00:10:17] options for it, you can see that you can
[00:10:19] actually change where by default the
[00:10:22] folders are dropped, which is in the
[00:10:24] location section. By default, it'll be
[00:10:26] going to a place called clippings, but
[00:10:27] just go ahead and change that to raw.
[00:10:29] Okay. So, here it came back with all
[00:10:30] these questions, right? It said, "Here
[00:10:32] are my key takeaways from this article,
[00:10:34] blah blah blah." And now it'll ask you,
[00:10:35] "What do you want to emphasize from this
[00:10:36] article? What's your focus? How granular
[00:10:38] do you want to be? what's your plan? So,
[00:10:40] I'm just going to say I want this to be
[00:10:42] extremely thorough. This is my passion
[00:10:45] looking at where AI is going to go. Um,
[00:10:47] and this whole project, by the way, that
[00:10:49] you're setting up in this vault is
[00:10:50] basically just going to be my place to
[00:10:52] dump in research about AI. So, help me
[00:10:54] keep all that organized so that I can
[00:10:55] query it and that I can, you know, keep
[00:10:57] my thoughts related. So, that's just a
[00:11:00] quick example of what it might look like
[00:11:01] for you to give it some more context to
[00:11:03] continuously build your project. So, I'm
[00:11:06] going to switch over over here to the
[00:11:07] graph view because I think it it'll be
[00:11:09] interesting to see as it is starting to
[00:11:10] go through and create those different
[00:11:12] wiki files. It's going to go ahead and
[00:11:14] it's going to create all those
[00:11:14] relationships and we'll be able to watch
[00:11:16] it in real time. All right, so it's
[00:11:17] creating all of the wiki pages now and
[00:11:19] you can see that it said it's going to
[00:11:20] make about 25 because there's so much
[00:11:23] stuff going on in the original AI 2027
[00:11:26] article. Okay, so our first one just
[00:11:27] popped in here and there a second one
[00:11:28] just came through and now you can
[00:11:30] understand you're starting to see where
[00:11:31] do you have hubs or where do you just
[00:11:33] have little individual nodes? So this is
[00:11:35] a major hub. Someone named Eli, someone
[00:11:38] named Thomas, Daniel, and you can see
[00:11:40] all the different relationships here
[00:11:41] with things like AI governance with
[00:11:43] things like OpenBrain, superhuman coder.
[00:11:46] Okay, so that ingest took about 10
[00:11:47] minutes. So sometimes you have to be a
[00:11:49] little patient with, you know, it
[00:11:50] reading through everything and
[00:11:51] organizing everything, but it does a lot
[00:11:53] of heavy lifting, of course. When I
[00:11:54] uploaded the 36 YouTube transcripts in
[00:11:57] batch, it took about 14 minutes. So it
[00:11:59] kind of just depends, but it created 23
[00:12:01] wiki pages. We have the source. We have
[00:12:04] six people, five organizations and one
[00:12:06] AI systems page, different concepts, so
[00:12:08] technical alignment and geopolitical and
[00:12:11] then an analysis and then it asks some
[00:12:13] questions about it so that it can help
[00:12:15] make the relationships and make the
[00:12:16] structure even better. Now let's just
[00:12:19] open this one up a little bit deeper and
[00:12:20] see what it actually did in here with
[00:12:22] this stuff. So we have this is the
[00:12:25] source with all the main relationships.
[00:12:27] So as we start to add other articles, we
[00:12:28] will see other big kind of like nodes
[00:12:30] and maybe in some cases we'll have
[00:12:32] relationships between like compute
[00:12:33] scaling with different articles that we
[00:12:35] upload as well. So let's just see if I
[00:12:37] click into the main source, we can see
[00:12:39] the tags that it got. We can see the
[00:12:41] authors and we can click around. So
[00:12:42] here's a link to OpenAI. Okay, what's
[00:12:44] OpenAI? Here's references in AI 2027.
[00:12:46] Here's some other connections with
[00:12:47] OpenAI like modelsp spec. Okay, we're in
[00:12:50] model spec. Let's take a look. We can
[00:12:51] see other things about modelsp spec. And
[00:12:53] we could also go to how the LLM
[00:12:55] psychology model works. So this is just
[00:12:57] super super cool all the relationships
[00:12:59] that we get. And once again, all of this
[00:13:01] stuff that we're looking at was derived
[00:13:02] from one article and automatically
[00:13:04] organized and related. So the question
[00:13:06] now is like what do we do from here? Do
[00:13:08] we query it inside of this environment?
[00:13:10] Do we query it from somewhere else? And
[00:13:12] that's completely up to the way that you
[00:13:14] want to use this. So for example, with
[00:13:15] my YouTube project, I'm probably just
[00:13:17] going to keep this here. And whenever I
[00:13:18] want to ask questions about YouTube or
[00:13:20] if I want to turn this into like a
[00:13:21] website, I can just do that from here.
[00:13:23] Or if I need to, I can point a different
[00:13:26] project at this folder since
[00:13:27] everything's here and it can crawl
[00:13:28] through the wiki, it can read the index
[00:13:30] and it knows how this stuff works
[00:13:32] because you can give it the clawmd so it
[00:13:34] understands the project as well. So for
[00:13:36] example, in this one which is just my
[00:13:37] second brain where we have all of the
[00:13:39] different things about like I drop in my
[00:13:40] meeting recordings, I drop in, you know,
[00:13:42] ClickUp channels, summaries and things
[00:13:44] like that. This is something that I want
[00:13:45] to use in my executive assistant. So
[00:13:47] what I did in my executive assistant
[00:13:48] here called Herk 2, if I go to this
[00:13:50] cloud.MD, MD you can see that we have a
[00:13:52] wiki path. So whenever you need to read
[00:13:55] things about me and my business that you
[00:13:56] don't have already, you would basically
[00:13:58] go to my herkbrain vault. You would go
[00:14:00] to that directory and then you would
[00:14:02] read through the wiki. You can read the
[00:14:03] hot cache which I'll explain in just a
[00:14:05] sec. You can read the index. You can
[00:14:06] read the domain subindex and then you
[00:14:08] can also just search through everything
[00:14:10] here. And I said don't read from the
[00:14:11] wiki unless you actually need it. Here
[00:14:13] are some things that you might do that
[00:14:14] you don't need to go read the wiki for.
[00:14:16] And all of this is my business
[00:14:17] knowledge. Now, if you guys remember, if
[00:14:19] you watched my video on setting up an
[00:14:20] executive assistant, I used to do this
[00:14:22] with context files inside of this
[00:14:24] project. And when I changed over to this
[00:14:26] method, I actually saw a reduction in
[00:14:28] tokens that I was actually calling in
[00:14:30] this project. So, the thing about the
[00:14:31] hot cache, right, I didn't actually have
[00:14:34] this in my YouTube one. So, if I go to
[00:14:36] YouTube, you can see there's no hot
[00:14:37] cache. But, if I go to the herk brain in
[00:14:40] the wiki, you can see there's a hot.mmd
[00:14:42] right here. And this is basically just a
[00:14:44] cache of like 500 words or 500
[00:14:46] characters that it saves, which is like
[00:14:48] what is the most recent thing that Nate
[00:14:50] just gave me or that we talked about. In
[00:14:52] the context of my executive assistant,
[00:14:53] this is really helpful. You know, it
[00:14:55] might save me from having to crawl
[00:14:56] different wiki pages. But in something
[00:14:58] like the YouTube transcript project, I
[00:15:00] don't really need a hot cache. So,
[00:15:02] another thing that I alluded to but
[00:15:03] didn't really cover was the idea of
[00:15:05] linting. So Karpathi says that he runs
[00:15:07] some LLM health checks over the wiki to
[00:15:09] find inconsistent data, impute missing
[00:15:12] data with web searches, find interesting
[00:15:14] connections for new article candidates,
[00:15:16] things like that. So it basically helps
[00:15:18] you run a lint, you know, every day,
[00:15:20] every week, whenever you want, which
[00:15:21] helps make sure that everything is
[00:15:23] scalable and structured in the right
[00:15:24] way. And it might even come back and
[00:15:26] say, "Hey, I don't fully understand
[00:15:28] this. Can you give me some more info or
[00:15:29] can you grab some more articles that
[00:15:30] might help me out here?" So now the
[00:15:32] final question about this that I wanted
[00:15:33] to cover is like does this kill semantic
[00:15:36] search rag? And the answer is no, but
[00:15:38] kind of yes. And it all depends on the
[00:15:41] goal of the project and the goal of the
[00:15:43] context, how much context you have. So
[00:15:45] here's a really quick chart that I had
[00:15:47] my cloud code make. I was in my Herk
[00:15:49] brain where I dumped in a bunch of
[00:15:50] information about Karpathy's LLM
[00:15:52] knowledge and I just said, "Hey, can you
[00:15:54] please explain Karpathy knowledge as
[00:15:56] simple as possible, keep it super
[00:15:58] concise, and um compare it to typical
[00:16:01] semantic search rag." So, it found
[00:16:04] Carpathy's idea. Instead of a database,
[00:16:06] you just give the LM well organized
[00:16:07] markdown files and it compares it here
[00:16:09] to the actual semantic search rag. So,
[00:16:12] actually, I might as well just read it
[00:16:13] off from here. So it finds it by reading
[00:16:15] indexes and follows links rather than
[00:16:17] using similarity search. So we're
[00:16:19] getting a deeper understanding of
[00:16:20] relationships because they're links
[00:16:22] rather than just saying, "Hey, these
[00:16:23] chunks seem similar." As far as
[00:16:25] infrastructure, it is literally just
[00:16:26] markdown. So like I said, you don't even
[00:16:28] need the obsidian. You just need these
[00:16:30] markdown files. Whereas with semantic
[00:16:32] search, you need an embedding model. You
[00:16:33] need a vector database and a chunking
[00:16:35] pipeline. The cost over here is
[00:16:37] basically free. Your only cost is going
[00:16:38] to be tokens. Whereas over here, you
[00:16:40] might have ongoing compute and storage.
[00:16:42] And for maintenance, you just run a
[00:16:43] lint. You clean up things. You add more
[00:16:45] articles. You give it more context
[00:16:47] rather than having to re-mbed when
[00:16:49] things change. But right now, the
[00:16:51] weakness of course with the uh LLM
[00:16:53] knowledge wiki is that it doesn't scale
[00:16:56] huge across enterprises, right? Because
[00:16:58] it's just a bunch of files. Um and that
[00:17:00] is where the cost will probably get more
[00:17:02] and more expensive than going to
[00:17:04] something like standard semantic search
[00:17:05] or knowledger graph or light rag or
[00:17:08] whatever other tool is out there for
[00:17:09] that. So here you can see if you have
[00:17:10] hundreds of pages with good indexes,
[00:17:12] you're fine with wiki graph. But if you
[00:17:14] were getting up to the millions of
[00:17:15] documents, then you're going to want to
[00:17:16] actually do more of a traditional rag
[00:17:18] pipeline, at least for now with how the
[00:17:20] current models are and everything we
[00:17:22] know right now in April 2026. So that is
[00:17:25] going to do it for today. I hope you
[00:17:27] guys learned something new or enjoyed
[00:17:28] the video. And if you did, please give
[00:17:29] it a like. It helps me out a ton. Now,
[00:17:31] after this video, if you're interested
[00:17:32] in learning how you can create your own
[00:17:33] sort of executive assistant and then
[00:17:35] plug it into this Obsidian vault, then
[00:17:37] definitely check out this video up here
[00:17:38] where I go over how I built my executive
[00:17:40] assistant and the way that you should be
[00:17:42] thinking about it. So hopefully I'll see
[00:17:43] you guys over there, but if not, I'll
[00:17:45] see you in the next