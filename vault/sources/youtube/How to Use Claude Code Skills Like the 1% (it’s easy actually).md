---
author: '[[Simon Scrapes]]'
channel_id: UCdCR4-uYOg5ju-IUuDnfnQA
created: 2026-04-07
date: '2026-03-04'
description: "\U0001F680 Build agentic systems that run your business: https://skool.com/scrapesDon't
  miss the next build - https://www.youtube.com/@simonscrapes?sub_confirmation=1Tired
  of using Claude Code Skills the s"
duration: 993
language: en
published: 2026-03-04
source: https://www.youtube.com/watch?v=6-D3fg3JUL4
status: processed
tags:
- skills
- ai
- clippings
- framework
- best-practices
- claude-code
title: How to Use Claude Code Skills Like the 1% (it’s easy actually)
topics:
- '[[Claude Code Skills]]'
- '[[Progressive Disclosure]]'
- '[[Skill Framework]]'
---

## Summary

[[Simon Scrapes]] breaks down the framework the top 1% use for [[Claude Code]] skills -- fewer, better-built skills instead of installing hundreds from marketplaces.

### Key Takeaways

- **Less Is More**: The 1% don't use more skills, they use fewer and build them properly. Installing hundreds makes agents slower and less predictable.
- **Skills Are SOPs for AI**: A skill.md is a Standard Operating Procedure -- step-by-step instructions with supporting scripts, references, and assets.
- **Progressive Disclosure**: Claude only loads YAML front matter (name + description) initially. Full skill instructions load only when triggered. This keeps context windows efficient.
- **Six-Step Framework**: (1) Name it (kebab-case), (2) Trigger (description Claude reads to decide relevance), (3) Outcome (define "done" before writing), (4) Dependencies (tools, connectors, references), (5) Step-by-step instructions, (6) Edge cases (handle vague/missing input).
- **Activation Problem**: Community testing found skill activation as low as 20% with vague descriptions. The YAML description is critical.
- **Skill Creator Skill**: Anthropic's built-in skill for building and testing skills, with activation testing and output evaluation.
- **Test Before Trusting**: Use binary assertions to validate skill outputs, not subjective "is it good?" checks.

![](https://www.youtube.com/watch?v=6-D3fg3JUL4)

🚀 Build agentic systems that run your business: https://skool.com/scrapes  
Don't miss the next build - https://www.youtube.com/@simonscrapes?sub\_confirmation=1  
  
Tired of using Claude Code Skills the same way as everyone else? Most people overcomplicate it by installing hundreds of skills, but the top 1% know that less is more. In this video, you'll learn the simple but powerful framework they use to build a small, curated set of skills that delivers professional-grade results every time.  
  
Skill builder Skill shown - https://github.com/glittercowboy/taches-cc-resources/blob/main/commands/create-agent-skill.md  
  
Six step skill building framework (full module in my Skool community):  
Name it – A short kebab-case label that describes exactly what the skill does  
Trigger – The description Claude reads to decide whether to load your skill; get this wrong and it won't activate  
Outcome – Define what "done" looks like before writing a single instruction  
Dependencies – Every tool, connector, reference file, or asset the skill needs to deliver that outcome  
Step-by-step – The exact instructions Claude follows, in order, with clear human-in-the-loop moments  
Edge cases – What happens when input is vague, missing, or unexpected; robust skills handle failure gracefully  
  
#claudecodetutorial #claudeskills #claudecodeskills

## Transcript

**0:00** · I see this trend where people are installing hundreds or sometimes even thousands of clawed code marketplace skills. They think that more equals better. And that's exactly what the 99% are doing. But it's the same reason why their agents are getting slower, less predictable, and harder to scale. So over the last few months, I've been reverse engineering what actually works, building skills from scratch, testing out community builds, and crawling through the official docs to see what's most important. And here's what I found.

**0:25** · The 1% don't use more skills, they use fewer, and they build them properly. So, in this video, I'll show you exactly what skills really are, why they're so powerful, and the simple framework I use to build a small curated set that consistently produce professional grade outputs. So, let's get straight into it.

**0:40** · So, before we get into the how, let's make sure we're on the same page about what skills actually are. So, I keep seeing skills being described as good system prompts, but truly that's only part of it. And understanding the difference there is what's going to separate you from getting average results to somebody who gets genuinely impressive results when you use those skills. A skill is just a folder with step-by-step instructions on how to create something valuable. And if we look at the complete guide to building skills in claw code, the folder is just made up of a skill.md file. And you can think of this as the step-by-step or process instructions for exactly what a clause should do with that skill. And then we have a bunch of optional supporting files. The scripts can actually be executed. The references might be things like examples, assets which show exactly how the output should look potentially. So you can think of the scripts, references, and assets as just telling Claude exactly how to do the specific task. So these are the knowledge bits behind the process. So the skill.md file is effectively a standard operating procedure or SOP for an AI agent. It tells Claude, here's what to do. Here's the order to do it in. Here's what good looks like and here's what to avoid. And then it's going to point to the scripts, the references, or the assets if they're relevant and included. And here's the really clever bit about Claude code skills and how Claude uses them. They work on a system called progressive disclosure which basically means we only give it the right information at the right time. So inside every skill.md file the only thing that's loaded into the initial prompt for claude what's called a YAML front matter. Think of it as a name and description of exactly what that skill is going to do and you can remember us this as the summary. So if we were to load up an actual skill like marketing Ideas by Cory Haynes, we've got the skill.md file here and then we've got this YAML front matter which has a name and description. You can also include metadata, but it's an optional field. So, the name is marketing ideas. That's the skill name.

**2:28** · And then the description tells us exactly or tells Claude exactly when to use it. So, when the user needs marketing ideas, inspiration or strategies for their SAS or software product. Also used when the user asks for marketing ideas, growth ideas, how to market, marketing strategies, marketing tactics, ways to promote or ideas to grow. This skill provides 139 proven marketing approaches organized by category. So, we can install this locally by copying this command inside here. And what we're going to add to it is dash for the specific skill marketing ideas. So it's from this marketing skills directory of skills. Cory Haynes has multiple marketing skills. D-skll marketing ideas. And then we're going to install it locally. So we can see the file inside our skills folder. Next we have the skill.md body. So this is where we have the full process instructions.

**3:13** · And always think of this as the process.

**3:15** · So Claude isn't going to load the skill.md file into this until it knows it's going to use that skill from reading the description. And the skill.md file is effectively giving Claude code the process on how to use this skill. So check for product marketing context first. So all these marketing skills refer to a docord/roduct marketing context file which will effectively reference that file and use that context. So it has information about the product, the audience, the current stage. So we would build out that file if we were going to use this skill. And then what it's going to do is suggest three to five most relevant ideas based on that context.

**3:48** · Provide details on implementation for chosen ideas and consider their resources, time, budget, and team size.

**3:54** · And then this is where this becomes really powerful because actually we're using this in the same way we build a claude.md file. We're using the trick called point don't dump. So what we're saying is actually we're not going to load up the skill with information about all of these different categories. You can see we've got 139 different categories in here that we've listed in detail. We're not going to put that in the skill. MD file because that will be loaded in right away as soon as we know we're going to use the skill. It's just got the key information about task specific questions, output format, some top ideas by use case that actually will then help it point to the reference files, which is where the knowledge comes in. So, YAML front matter is the summary. The skill.md body is the process or our step-by-step instructions on how to use the reference files. And then the linked files like references, scripts, and assets are only loaded into context when skill.mmd says to load them. So in our marketing ideas knowledge base, you can see this is a huge document detailing all of the different marketing ideas by category.

**4:50** · And this is like the level of detail that we need to go to in the reference files and not the skill.md file. Now, one of the reason that skills are so powerful in cycllo code is that actually you don't just need one reference file.

**5:02** · You can load in certain reference files only when you need them. So we're not bloating context. So, for example, in this skill that's an SEO content writer, we've got two reference files. So, the skill.md tells you actually if you're ideulating titles, then we're going to use only the title formulas.mmd. But actually, if you're creating content structure, then we've got a bunch of content structure templates in there.

**5:22** · So, think of this as your best practice and the knowledge base that your instruction guide or your skill.md your process is going to only introduce when relevant. We can also have scripts. So, we can actually execute code through this. So, for example, if we wanted the skill that generates Nano Banana Pro images or edits them, it just basically says if you're going to edit images as a single image, you're going to need to run this script with this prompt. And if you're going to compose multiple images together, then you need to run this script with this prompt. So, this is an extremely simple skill.md because actually it's just saying this is how you process and use the script which is generate image pi. And then inside that script, we've got an executable script which takes arguments from the skill.md when Claude starts to use it. But that is not loaded into context. The skilled MD which is super simple and concise is loaded into context and it knows when to use it because it's generate or edit images via Gemini 3 image pro Nano Banana Pro. So this is why skills can actually scale because you're not overloading Claude's context window every time even if you install thousands of these because all we're loading in is the summary which is the name and the description of each skill. So you're effectively giving Claude code a toolkit it can reach for when it needs it. But more isn't necessarily better, though, and we'll come back to that later. So, that's what skills are. They're folders that organize expertise that have a summary, the process steps, and then reference knowledge base that you build on. And you can think of them as plug-and-play SOPs for Claude. The same way in which you provide long context prompts and feed in examples for either Claude projects or your custom GPTs. So, now you understand what they are. Here's why you should actually care about this right now, because what's happening with skills is way bigger than just a simple nice claude code feature. So, here's where this gets really interesting because people aren't just comparing skills to prompts or templates anymore.

**7:03** · They're comparing them to entire software products. And when you look at what's happening in the market right now, you can start to see why. So, in early 2026, when Anthropic launched co-work and they launched their new plugins feature, which are basically just bundles of skills, agents, hooks, and commands, it triggered a massive sell-off in software stocks. We're talking 285 billion wiped off huge companies like Intu IT, Adobe, Salesforce, and investors literally panicked because they realized if an AI agent with the right skills can do what a $50 a month subscription does, then why would companies keep paying for all these separate tools? Now, I'm definitely not saying that SAS is dead.

**7:38** · That's a total exaggeration. The price of SAS stocks was overvalued because it was based on the old model of SAS. But here's what is happening and is important. Skills are basically becoming a new layer of software. So, think about this. a well-built skill with the right reference files, the right scripts, the right assets, can do what used to require a dedicated SAS tool with its own UI. And we can make it completely custom to our own business by just using a few prompts. So, it's like building bespoke software very, very quickly. So, a lead generation skill can replace parts of your outreach stack. A content creation skill can replace your copywriting tool. An SEO skill can replace chunks of what you pay ah refs or surfer to do. And we're already seeing marketplaces of these skills blow up. So skillsmpp has over 280,000 skills indexed from GitHub and we can search through any of the skills they've got available. Search by categories and then we've got other marketplaces like skill hub which has 7,000 plus AI evaluated skills and then even companies like Stripe, Cloudfare, Vel Century are launching their own skills that can interact with their platform. So for example, here we have the Stripe best practices skill which effectively gives you the ability to reference external documentation that Claude can go and read about interacting with Stripe and the web hooks etc API calls with Stripe.

**8:53** · So, it's becoming a total ecosystem. And in my opinion, the people who get really, really good at building and customizing skills are going to have a massive advantage because anyone can go and install one of those 280,000 generic skills. But building one that's tailored to your specific business with your years worth of knowledge and context for your specific processes and your brand, that's where the real value is. And if you're building an agency, skills become totally productizable, too. So you can build a skill once and you can deploy it for multiple clients, customize it slightly, and probably charge much higher rates for it. So skills aren't just a claw code feature. They're potentially the building blocks of how we'll work with AI agents going forwards. And getting good at building them now puts you months ahead of everyone else. And by the way, if you want a deep dive into skills, we're building out an entire section in our Aentic community linked in the description below. So up until now, we've talked about what they are and why they matter. But you're probably thinking, "Okay, where do I actually get these? Do I build them or do I download them? Well, let me show you the three different places where you can get each of them. And each has its pros and cons.

**9:54** · And this is where I'm going to share with you something that goes against what most people online are telling you now. So, the first one is Anthropic's official skills. So, this is a really good way to see how good skills are built out. And they have effectively a bunch of different skills at that link mainly to do with doc transformation.

**10:10** · So, it might be creating a DOCX file, creating PDFs and editing those. And you can see they've got various scripts in here. Here they've got the skill.md. Use the skill whenever the user wants to do anything with PDF files. This includes reading or extracting text, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, etc., etc. And it gives it the process instructions on how to do that and the scripts to execute as well. And we can install these simply by running npx skills add and then the directory. So, anthropics/skills dash the skill we want skill pdf and run that. and that will install that into our global folder. So if we want to use this across all our projects like we might do with PDF manipulation, we'd install it globally. And then if we wanted to actually install that globally, we'd hit-lo on the end of that command and we could see that skills folder inside of our docord folder here.

**11:00** · Then you've got community marketplaces as the second resource which we've already seen. So we've got skillsmpp.com which was one of the most popular and skillhub.comcl club as well. And you can search by different categories, different use cases. You can search by the role that you are to find relevant skills for you too. Basically everything you could want. But here's where you have to be careful with that. And this is the thing nobody's really talking about. There's a trend right now where people are saying just install all the skills I've got my system or install plugins with, you know, hundreds of different skills in. And I've seen posts telling you to load 500 a,000 skills into your claw code setup. And it sounds great in theory because it's giving your agent access to all of these capabilities. But in reality, remember what I said earlier about progressive disclosure. So Claude is going to scan the name and description of every skill to decide which one to use. So the more skills you have, the noisier the menu that it's picking from gets. And Anthropic's own documentation as well says there's a 15,000 character limit for the entire available skills list that gets loaded. So load in a th000 skills, you're not only taking up that valuable context, but you'll likely have crossover skills that start to cannibalize each other. Say we have two skills that are based around SEO, then which one is Claude Code going to pick?

**12:10** · And then if you look at how most people or LLMs are building them on their behalfs, it's not at all using the architecture we mentioned earlier. So everything is included in one skill.md file. It has no references, which means when you have quality issues, you can't work out whether it's a process issue, i.e. it's the skill.md file, or if it's a knowledge issue, like should you update the reference files? So, this becomes a big problem if you install other people's skills without understanding truly what you're installing. And by the way, somebody did a test on activation of skills. I.e., how often does Claude actually recognize that it should activate a skill and then activate it? And they found that skill activation with a basic setup and a poor description was as low as 20%. Meaning, if you're trying to do a job, Claude will only pick it up or pick up the skill one out of five times every time you try and do it. And even with proper hooks and optimized descriptions, the best you're able to get is around 84% in picking that up. So still, one out of five times it will not run the correct skill. And that's just with like four or five well-built skills. So imagine what happens when you've got 500 generic ones with vague descriptions fighting for Claude's attention. The quality of the outputs will vary significantly. It might pick one SEO skill one time and another SEO skill another time. So the takeaway is really simple. A small number of properly built skills with specific trigger descriptions will massively outperform a huge library of generic ones. So if you load a thousand generic skills with average descriptions, Claude is going to miss the right one more than half the time.

**13:38** · But if you have a library of just 20 to 30 really well-built, isolated, properly described skills that are specific to your workflows and have your reference context, then Claude is going to nail it more often than not. And that brings us to the third source, which is actually building your own. And this is where the real magic happens because no marketplace skill is going to know your business as well as you do. And that's your domain expertise, your brand voice, your process, all in your skills. So the secret isn't having the most skills.

**14:04** · It's having the right skills built properly. So now you know where to find them. Why not learn how to build ones that actually outperform 99% of what's out there? Now we can absolutely write these skills from scratch and give you a framework. And I'll leave a framework down below on how to do that. However, let's just use a skill to create a skill. Tash, who created the really popular framework GST or get done, has created an agent skill that creates skills. So, this is a really useful way to effectively tell Claude when you're prompting it to create a skill, create it in this format, and it follows the conventions that we talked about today where we're putting actual instructions inside the skill.md. So, it's a routter plus the principles of the step-by-step procedures. And then what we're doing is actually putting any references in separate files and linking to those from the skill.md. So I'll leave that down below and all you need to do is run the command npx skills add glitter cowboy.

**14:57** · And then we're using the skill create agent skills. And I'm installing this just locally so that I can show you that the skill installs here. But just take away the d-local if you want to continue to create skills just by prompting them.

**15:09** · But follow this specific anthropic framework to do so. And the reason these things are so important, right? The convention on how you build it is it helps you debug, iterate, and troubleshoot. So if your skill isn't following the process correctly, you know that that's an issue in the skill.md our process file only. If the skill needs more information is getting the context wrong, then actually we need to potentially add a reference file or update the information in our reference file. So start simple. Put the process in the skill.md. Use the front matter as if it was a summary that's being fed into Claude because it is. And then put your expertise, your brand voice, etc.

**15:44** · in the reference files. Iterate every time you use the skill and add scripts only when you need execution power. So there you have it. Skills are organized expertise that plug into claw code and they're being called a completely new business mode for good reason because they're actually replacing chunks of what you normally need separate SAS tools for. And the secret here, the real secret, the one takeaway is stop loading thousands of generic skills in and actually build a curated set of really well-crafted ones. Even if you install somebody else's skill that looks promising, put it into the right format and actually build on the reference context to make it relevant to your business and your brand. Now, if you want to go deeper on claw code and actually start building out productionready systems, whether that's for you, whether that's for your own business, or to sell it as a service, I've got a full claw code course inside my agentic community link below. And if you want to see more claw code content, then check out the video right here.

**16:31** · I'll see you in the next one.

---

## Transcript

[00:00:00] I see this trend where people are
[00:00:01] installing hundreds or sometimes even
[00:00:03] thousands of clawed code marketplace
[00:00:05] skills. They think that more equals
[00:00:07] better. And that's exactly what the 99%
[00:00:09] are doing. But it's the same reason why
[00:00:11] their agents are getting slower, less
[00:00:13] predictable, and harder to scale. So
[00:00:14] over the last few months, I've been
[00:00:16] reverse engineering what actually works,
[00:00:18] building skills from scratch, testing
[00:00:20] out community builds, and crawling
[00:00:21] through the official docs to see what's
[00:00:23] most important. And here's what I found.
[00:00:25] The 1% don't use more skills, they use
[00:00:28] fewer, and they build them properly. So,
[00:00:29] in this video, I'll show you exactly
[00:00:31] what skills really are, why they're so
[00:00:33] powerful, and the simple framework I use
[00:00:35] to build a small curated set that
[00:00:37] consistently produce professional grade
[00:00:38] outputs. So, let's get straight into it.
[00:00:40] So, before we get into the how, let's
[00:00:42] make sure we're on the same page about
[00:00:43] what skills actually are. So, I keep
[00:00:45] seeing skills being described as good
[00:00:48] system prompts, but truly that's only
[00:00:50] part of it. And understanding the
[00:00:51] difference there is what's going to
[00:00:53] separate you from getting average
[00:00:54] results to somebody who gets genuinely
[00:00:56] impressive results when you use those
[00:00:58] skills. A skill is just a folder with
[00:01:00] step-by-step instructions on how to
[00:01:02] create something valuable. And if we
[00:01:03] look at the complete guide to building
[00:01:05] skills in claw code, the folder is just
[00:01:08] made up of a skill.md file. And you can
[00:01:10] think of this as the step-by-step or
[00:01:12] process instructions for exactly what a
[00:01:14] clause should do with that skill. And
[00:01:15] then we have a bunch of optional
[00:01:16] supporting files. The scripts can
[00:01:18] actually be executed. The references
[00:01:20] might be things like examples, assets
[00:01:22] which show exactly how the output should
[00:01:24] look potentially. So you can think of
[00:01:25] the scripts, references, and assets as
[00:01:27] just telling Claude exactly how to do
[00:01:29] the specific task. So these are the
[00:01:31] knowledge bits behind the process. So
[00:01:34] the skill.md file is effectively a
[00:01:36] standard operating procedure or SOP for
[00:01:38] an AI agent. It tells Claude, here's
[00:01:41] what to do. Here's the order to do it
[00:01:42] in. Here's what good looks like and
[00:01:44] here's what to avoid. And then it's
[00:01:45] going to point to the scripts, the
[00:01:47] references, or the assets if they're
[00:01:49] relevant and included. And here's the
[00:01:50] really clever bit about Claude code
[00:01:52] skills and how Claude uses them. They
[00:01:54] work on a system called progressive
[00:01:56] disclosure which basically means we only
[00:01:58] give it the right information at the
[00:02:00] right time. So inside every skill.md
[00:02:02] file the only thing that's loaded into
[00:02:04] the initial prompt for claude what's
[00:02:06] called a YAML front matter. Think of it
[00:02:08] as a name and description of exactly
[00:02:10] what that skill is going to do and you
[00:02:12] can remember us this as the summary. So
[00:02:14] if we were to load up an actual skill
[00:02:16] like marketing Ideas by Cory Haynes,
[00:02:18] we've got the skill.md file here and
[00:02:20] then we've got this YAML front matter
[00:02:21] which has a name and description. You
[00:02:23] can also include metadata, but it's an
[00:02:25] optional field. So, the name is
[00:02:26] marketing ideas. That's the skill name.
[00:02:28] And then the description tells us
[00:02:29] exactly or tells Claude exactly when to
[00:02:31] use it. So, when the user needs
[00:02:32] marketing ideas, inspiration or
[00:02:34] strategies for their SAS or software
[00:02:36] product. Also used when the user asks
[00:02:37] for marketing ideas, growth ideas, how
[00:02:39] to market, marketing strategies,
[00:02:40] marketing tactics, ways to promote or
[00:02:42] ideas to grow. This skill provides 139
[00:02:45] proven marketing approaches organized by
[00:02:47] category. So, we can install this
[00:02:49] locally by copying this command inside
[00:02:51] here. And what we're going to add to it
[00:02:53] is dash for the specific skill marketing
[00:02:56] ideas. So it's from this marketing
[00:02:58] skills directory of skills. Cory Haynes
[00:03:01] has multiple marketing skills. D-skll
[00:03:04] marketing ideas. And then we're going to
[00:03:05] install it locally. So we can see the
[00:03:07] file inside our skills folder. Next we
[00:03:09] have the skill.md body. So this is where
[00:03:11] we have the full process instructions.
[00:03:13] And always think of this as the process.
[00:03:15] So Claude isn't going to load the
[00:03:17] skill.md file into this until it knows
[00:03:20] it's going to use that skill from
[00:03:21] reading the description. And the
[00:03:23] skill.md file is effectively giving
[00:03:25] Claude code the process on how to use
[00:03:27] this skill. So check for product
[00:03:28] marketing context first. So all these
[00:03:30] marketing skills refer to a
[00:03:32] docord/roduct marketing context file
[00:03:34] which will effectively reference that
[00:03:36] file and use that context. So it has
[00:03:38] information about the product, the
[00:03:40] audience, the current stage. So we would
[00:03:42] build out that file if we were going to
[00:03:43] use this skill. And then what it's going
[00:03:45] to do is suggest three to five most
[00:03:46] relevant ideas based on that context.
[00:03:48] Provide details on implementation for
[00:03:50] chosen ideas and consider their
[00:03:52] resources, time, budget, and team size.
[00:03:54] And then this is where this becomes
[00:03:56] really powerful because actually we're
[00:03:58] using this in the same way we build a
[00:03:59] claude.md file. We're using the trick
[00:04:01] called point don't dump. So what we're
[00:04:03] saying is actually we're not going to
[00:04:05] load up the skill with information about
[00:04:07] all of these different categories. You
[00:04:09] can see we've got 139 different
[00:04:11] categories in here that we've listed in
[00:04:13] detail. We're not going to put that in
[00:04:14] the skill. MD file because that will be
[00:04:16] loaded in right away as soon as we know
[00:04:19] we're going to use the skill. It's just
[00:04:20] got the key information about task
[00:04:22] specific questions, output format, some
[00:04:25] top ideas by use case that actually will
[00:04:27] then help it point to the reference
[00:04:28] files, which is where the knowledge
[00:04:30] comes in. So, YAML front matter is the
[00:04:32] summary. The skill.md body is the
[00:04:34] process or our step-by-step instructions
[00:04:36] on how to use the reference files. And
[00:04:38] then the linked files like references,
[00:04:39] scripts, and assets are only loaded into
[00:04:41] context when skill.mmd says to load
[00:04:43] them. So in our marketing ideas
[00:04:45] knowledge base, you can see this is a
[00:04:47] huge document detailing all of the
[00:04:49] different marketing ideas by category.
[00:04:50] And this is like the level of detail
[00:04:52] that we need to go to in the reference
[00:04:54] files and not the skill.md file. Now,
[00:04:56] one of the reason that skills are so
[00:04:58] powerful in cycllo code is that actually
[00:05:00] you don't just need one reference file.
[00:05:02] You can load in certain reference files
[00:05:04] only when you need them. So we're not
[00:05:05] bloating context. So, for example, in
[00:05:07] this skill that's an SEO content writer,
[00:05:09] we've got two reference files. So, the
[00:05:11] skill.md tells you actually if you're
[00:05:13] ideulating titles, then we're going to
[00:05:15] use only the title formulas.mmd. But
[00:05:17] actually, if you're creating content
[00:05:19] structure, then we've got a bunch of
[00:05:20] content structure templates in there.
[00:05:22] So, think of this as your best practice
[00:05:24] and the knowledge base that your
[00:05:26] instruction guide or your skill.md your
[00:05:28] process is going to only introduce when
[00:05:30] relevant. We can also have scripts. So,
[00:05:32] we can actually execute code through
[00:05:34] this. So, for example, if we wanted the
[00:05:36] skill that generates Nano Banana Pro
[00:05:37] images or edits them, it just basically
[00:05:40] says if you're going to edit images as a
[00:05:42] single image, you're going to need to
[00:05:43] run this script with this prompt. And if
[00:05:45] you're going to compose multiple images
[00:05:46] together, then you need to run this
[00:05:48] script with this prompt. So, this is an
[00:05:50] extremely simple skill.md because
[00:05:52] actually it's just saying this is how
[00:05:53] you process and use the script which is
[00:05:56] generate image pi. And then inside that
[00:05:58] script, we've got an executable script
[00:06:00] which takes arguments from the skill.md
[00:06:02] when Claude starts to use it. But that
[00:06:04] is not loaded into context. The skilled
[00:06:06] MD which is super simple and concise is
[00:06:08] loaded into context and it knows when to
[00:06:10] use it because it's generate or edit
[00:06:12] images via Gemini 3 image pro Nano
[00:06:14] Banana Pro. So this is why skills can
[00:06:16] actually scale because you're not
[00:06:18] overloading Claude's context window
[00:06:20] every time even if you install thousands
[00:06:21] of these because all we're loading in is
[00:06:23] the summary which is the name and the
[00:06:25] description of each skill. So you're
[00:06:26] effectively giving Claude code a toolkit
[00:06:28] it can reach for when it needs it. But
[00:06:30] more isn't necessarily better, though,
[00:06:32] and we'll come back to that later. So,
[00:06:34] that's what skills are. They're folders
[00:06:35] that organize expertise that have a
[00:06:37] summary, the process steps, and then
[00:06:39] reference knowledge base that you build
[00:06:40] on. And you can think of them as
[00:06:41] plug-and-play SOPs for Claude. The same
[00:06:43] way in which you provide long context
[00:06:45] prompts and feed in examples for either
[00:06:47] Claude projects or your custom GPTs. So,
[00:06:49] now you understand what they are. Here's
[00:06:51] why you should actually care about this
[00:06:52] right now, because what's happening with
[00:06:54] skills is way bigger than just a simple
[00:06:57] nice claude code feature. So, here's
[00:06:58] where this gets really interesting
[00:07:00] because people aren't just comparing
[00:07:01] skills to prompts or templates anymore.
[00:07:03] They're comparing them to entire
[00:07:05] software products. And when you look at
[00:07:06] what's happening in the market right
[00:07:07] now, you can start to see why. So, in
[00:07:09] early 2026, when Anthropic launched
[00:07:12] co-work and they launched their new
[00:07:13] plugins feature, which are basically
[00:07:15] just bundles of skills, agents, hooks,
[00:07:17] and commands, it triggered a massive
[00:07:19] sell-off in software stocks. We're
[00:07:21] talking 285 billion wiped off huge
[00:07:24] companies like Intu IT, Adobe,
[00:07:25] Salesforce, and investors literally
[00:07:27] panicked because they realized if an AI
[00:07:29] agent with the right skills can do what
[00:07:31] a $50 a month subscription does, then
[00:07:33] why would companies keep paying for all
[00:07:35] these separate tools? Now, I'm
[00:07:36] definitely not saying that SAS is dead.
[00:07:38] That's a total exaggeration. The price
[00:07:40] of SAS stocks was overvalued because it
[00:07:42] was based on the old model of SAS. But
[00:07:44] here's what is happening and is
[00:07:46] important. Skills are basically becoming
[00:07:47] a new layer of software. So, think about
[00:07:49] this. a well-built skill with the right
[00:07:52] reference files, the right scripts, the
[00:07:53] right assets, can do what used to
[00:07:55] require a dedicated SAS tool with its
[00:07:58] own UI. And we can make it completely
[00:07:59] custom to our own business by just using
[00:08:01] a few prompts. So, it's like building
[00:08:03] bespoke software very, very quickly. So,
[00:08:05] a lead generation skill can replace
[00:08:07] parts of your outreach stack. A content
[00:08:09] creation skill can replace your
[00:08:10] copywriting tool. An SEO skill can
[00:08:12] replace chunks of what you pay ah refs
[00:08:15] or surfer to do. And we're already
[00:08:16] seeing marketplaces of these skills blow
[00:08:19] up. So skillsmpp has over 280,000 skills
[00:08:23] indexed from GitHub and we can search
[00:08:24] through any of the skills they've got
[00:08:26] available. Search by categories and then
[00:08:28] we've got other marketplaces like skill
[00:08:30] hub which has 7,000 plus AI evaluated
[00:08:33] skills and then even companies like
[00:08:35] Stripe, Cloudfare, Vel Century are
[00:08:38] launching their own skills that can
[00:08:40] interact with their platform. So for
[00:08:41] example, here we have the Stripe best
[00:08:43] practices skill which effectively gives
[00:08:44] you the ability to reference external
[00:08:47] documentation that Claude can go and
[00:08:48] read about interacting with Stripe and
[00:08:51] the web hooks etc API calls with Stripe.
[00:08:53] So, it's becoming a total ecosystem. And
[00:08:56] in my opinion, the people who get
[00:08:57] really, really good at building and
[00:08:58] customizing skills are going to have a
[00:09:00] massive advantage because anyone can go
[00:09:02] and install one of those 280,000 generic
[00:09:05] skills. But building one that's tailored
[00:09:07] to your specific business with your
[00:09:09] years worth of knowledge and context for
[00:09:11] your specific processes and your brand,
[00:09:13] that's where the real value is. And if
[00:09:15] you're building an agency, skills become
[00:09:17] totally productizable, too. So you can
[00:09:19] build a skill once and you can deploy it
[00:09:20] for multiple clients, customize it
[00:09:22] slightly, and probably charge much
[00:09:24] higher rates for it. So skills aren't
[00:09:26] just a claw code feature. They're
[00:09:27] potentially the building blocks of how
[00:09:29] we'll work with AI agents going
[00:09:31] forwards. And getting good at building
[00:09:32] them now puts you months ahead of
[00:09:34] everyone else. And by the way, if you
[00:09:35] want a deep dive into skills, we're
[00:09:37] building out an entire section in our
[00:09:39] Aentic community linked in the
[00:09:40] description below. So up until now,
[00:09:42] we've talked about what they are and why
[00:09:44] they matter. But you're probably
[00:09:45] thinking, "Okay, where do I actually get
[00:09:47] these? Do I build them or do I download
[00:09:49] them? Well, let me show you the three
[00:09:50] different places where you can get each
[00:09:52] of them. And each has its pros and cons.
[00:09:54] And this is where I'm going to share
[00:09:55] with you something that goes against
[00:09:56] what most people online are telling you
[00:09:58] now. So, the first one is Anthropic's
[00:10:00] official skills. So, this is a really
[00:10:02] good way to see how good skills are
[00:10:04] built out. And they have effectively a
[00:10:06] bunch of different skills at that link
[00:10:08] mainly to do with doc transformation.
[00:10:10] So, it might be creating a DOCX file,
[00:10:12] creating PDFs and editing those. And you
[00:10:14] can see they've got various scripts in
[00:10:16] here. Here they've got the skill.md. Use
[00:10:17] the skill whenever the user wants to do
[00:10:19] anything with PDF files. This includes
[00:10:21] reading or extracting text, combining or
[00:10:23] merging multiple PDFs into one,
[00:10:25] splitting PDFs apart, rotating pages,
[00:10:27] etc., etc. And it gives it the process
[00:10:30] instructions on how to do that and the
[00:10:31] scripts to execute as well. And we can
[00:10:33] install these simply by running npx
[00:10:35] skills add and then the directory. So,
[00:10:38] anthropics/skills
[00:10:40] dash the skill we want skill pdf and run
[00:10:44] that. and that will install that into
[00:10:46] our global folder. So if we want to use
[00:10:48] this across all our projects like we
[00:10:49] might do with PDF manipulation, we'd
[00:10:51] install it globally. And then if we
[00:10:52] wanted to actually install that
[00:10:54] globally, we'd hit-lo on the end of that
[00:10:56] command and we could see that skills
[00:10:57] folder inside of our docord folder here.
[00:11:00] Then you've got community marketplaces
[00:11:02] as the second resource which we've
[00:11:03] already seen. So we've got skillsmpp.com
[00:11:05] which was one of the most popular and
[00:11:07] skillhub.comcl club as well. And you can
[00:11:09] search by different categories,
[00:11:11] different use cases. You can search by
[00:11:13] the role that you are to find relevant
[00:11:15] skills for you too. Basically everything
[00:11:17] you could want. But here's where you
[00:11:19] have to be careful with that. And this
[00:11:21] is the thing nobody's really talking
[00:11:22] about. There's a trend right now where
[00:11:23] people are saying just install all the
[00:11:25] skills I've got my system or install
[00:11:27] plugins with, you know, hundreds of
[00:11:29] different skills in. And I've seen posts
[00:11:31] telling you to load 500 a,000 skills
[00:11:33] into your claw code setup. And it sounds
[00:11:35] great in theory because it's giving your
[00:11:37] agent access to all of these
[00:11:38] capabilities. But in reality, remember
[00:11:41] what I said earlier about progressive
[00:11:42] disclosure. So Claude is going to scan
[00:11:44] the name and description of every skill
[00:11:46] to decide which one to use. So the more
[00:11:48] skills you have, the noisier the menu
[00:11:50] that it's picking from gets. And
[00:11:51] Anthropic's own documentation as well
[00:11:53] says there's a 15,000 character limit
[00:11:55] for the entire available skills list
[00:11:57] that gets loaded. So load in a th000
[00:11:59] skills, you're not only taking up that
[00:12:01] valuable context, but you'll likely have
[00:12:03] crossover skills that start to
[00:12:04] cannibalize each other. Say we have two
[00:12:07] skills that are based around SEO, then
[00:12:09] which one is Claude Code going to pick?
[00:12:10] And then if you look at how most people
[00:12:12] or LLMs are building them on their
[00:12:15] behalfs, it's not at all using the
[00:12:17] architecture we mentioned earlier. So
[00:12:18] everything is included in one skill.md
[00:12:21] file. It has no references, which means
[00:12:22] when you have quality issues, you can't
[00:12:24] work out whether it's a process issue,
[00:12:27] i.e. it's the skill.md file, or if it's
[00:12:29] a knowledge issue, like should you
[00:12:30] update the reference files? So, this
[00:12:32] becomes a big problem if you install
[00:12:34] other people's skills without
[00:12:36] understanding truly what you're
[00:12:37] installing. And by the way, somebody did
[00:12:39] a test on activation of skills. I.e.,
[00:12:42] how often does Claude actually recognize
[00:12:44] that it should activate a skill and then
[00:12:45] activate it? And they found that skill
[00:12:47] activation with a basic setup and a poor
[00:12:50] description was as low as 20%. Meaning,
[00:12:52] if you're trying to do a job, Claude
[00:12:55] will only pick it up or pick up the
[00:12:56] skill one out of five times every time
[00:12:58] you try and do it. And even with proper
[00:13:00] hooks and optimized descriptions, the
[00:13:02] best you're able to get is around 84% in
[00:13:05] picking that up. So still, one out of
[00:13:07] five times it will not run the correct
[00:13:09] skill. And that's just with like four or
[00:13:11] five well-built skills. So imagine what
[00:13:13] happens when you've got 500 generic ones
[00:13:15] with vague descriptions fighting for
[00:13:17] Claude's attention. The quality of the
[00:13:19] outputs will vary significantly. It
[00:13:20] might pick one SEO skill one time and
[00:13:23] another SEO skill another time. So the
[00:13:25] takeaway is really simple. A small
[00:13:26] number of properly built skills with
[00:13:28] specific trigger descriptions will
[00:13:30] massively outperform a huge library of
[00:13:32] generic ones. So if you load a thousand
[00:13:34] generic skills with average
[00:13:35] descriptions, Claude is going to miss
[00:13:36] the right one more than half the time.
[00:13:38] But if you have a library of just 20 to
[00:13:40] 30 really well-built, isolated, properly
[00:13:42] described skills that are specific to
[00:13:44] your workflows and have your reference
[00:13:46] context, then Claude is going to nail it
[00:13:48] more often than not. And that brings us
[00:13:49] to the third source, which is actually
[00:13:51] building your own. And this is where the
[00:13:52] real magic happens because no
[00:13:54] marketplace skill is going to know your
[00:13:55] business as well as you do. And that's
[00:13:57] your domain expertise, your brand voice,
[00:14:00] your process, all in your skills. So the
[00:14:02] secret isn't having the most skills.
[00:14:04] It's having the right skills built
[00:14:05] properly. So now you know where to find
[00:14:07] them. Why not learn how to build ones
[00:14:08] that actually outperform 99% of what's
[00:14:11] out there? Now we can absolutely write
[00:14:13] these skills from scratch and give you a
[00:14:15] framework. And I'll leave a framework
[00:14:16] down below on how to do that. However,
[00:14:19] let's just use a skill to create a
[00:14:21] skill. Tash, who created the really
[00:14:24] popular framework GST or get done,
[00:14:27] has created an agent skill that creates
[00:14:29] skills. So, this is a really useful way
[00:14:31] to effectively tell Claude when you're
[00:14:34] prompting it to create a skill, create
[00:14:36] it in this format, and it follows the
[00:14:37] conventions that we talked about today
[00:14:39] where we're putting actual instructions
[00:14:41] inside the skill.md. So, it's a routter
[00:14:43] plus the principles of the step-by-step
[00:14:45] procedures. And then what we're doing is
[00:14:47] actually putting any references in
[00:14:49] separate files and linking to those from
[00:14:51] the skill.md. So I'll leave that down
[00:14:53] below and all you need to do is run the
[00:14:55] command npx skills add glitter cowboy.
[00:14:57] And then we're using the skill create
[00:14:59] agent skills. And I'm installing this
[00:15:01] just locally so that I can show you that
[00:15:02] the skill installs here. But just take
[00:15:04] away the d-local if you want to continue
[00:15:06] to create skills just by prompting them.
[00:15:09] But follow this specific anthropic
[00:15:11] framework to do so. And the reason these
[00:15:12] things are so important, right? The
[00:15:14] convention on how you build it is it
[00:15:16] helps you debug, iterate, and
[00:15:18] troubleshoot. So if your skill isn't
[00:15:20] following the process correctly, you
[00:15:22] know that that's an issue in the
[00:15:23] skill.md our process file only. If the
[00:15:27] skill needs more information is getting
[00:15:29] the context wrong, then actually we need
[00:15:30] to potentially add a reference file or
[00:15:32] update the information in our reference
[00:15:34] file. So start simple. Put the process
[00:15:36] in the skill.md. Use the front matter as
[00:15:38] if it was a summary that's being fed
[00:15:40] into Claude because it is. And then put
[00:15:41] your expertise, your brand voice, etc.
[00:15:44] in the reference files. Iterate every
[00:15:46] time you use the skill and add scripts
[00:15:48] only when you need execution power. So
[00:15:50] there you have it. Skills are organized
[00:15:51] expertise that plug into claw code and
[00:15:54] they're being called a completely new
[00:15:55] business mode for good reason because
[00:15:57] they're actually replacing chunks of
[00:15:58] what you normally need separate SAS
[00:16:00] tools for. And the secret here, the real
[00:16:02] secret, the one takeaway is stop loading
[00:16:04] thousands of generic skills in and
[00:16:06] actually build a curated set of really
[00:16:08] well-crafted ones. Even if you install
[00:16:10] somebody else's skill that looks
[00:16:11] promising, put it into the right format
[00:16:13] and actually build on the reference
[00:16:14] context to make it relevant to your
[00:16:16] business and your brand. Now, if you
[00:16:17] want to go deeper on claw code and
[00:16:18] actually start building out
[00:16:19] productionready systems, whether that's
[00:16:21] for you, whether that's for your own
[00:16:23] business, or to sell it as a service,
[00:16:24] I've got a full claw code course inside
[00:16:26] my agentic community link below. And if
[00:16:28] you want to see more claw code content,
[00:16:30] then check out the video right here.
[00:16:31] I'll see you in the next one.