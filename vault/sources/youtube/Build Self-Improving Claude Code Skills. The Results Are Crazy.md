---
author: '[[Simon Scrapes]]'
channel_id: UCdCR4-uYOg5ju-IUuDnfnQA
created: 2026-04-07
date: '2026-03-13'
description: "\U0001F680 Build agentic systems that run your business: https://skool.com/scrapesDon't
  miss the next build - https://www.youtube.com/@simonscrapes?sub_confirmation=1What
  if your Claude Code skills could i"
duration: 662
language: en
published: 2026-03-13
source: https://www.youtube.com/watch?v=wQ0duoTeAAU
status: processed
tags:
- skills
- ai
- clippings
- auto-research
- claude-code
- testing
title: Build Self-Improving Claude Code Skills. The Results Are Crazy.
topics:
- '[[Claude Code Skills]]'
- '[[Auto-Research]]'
- '[[Self-Improving AI]]'
- '[[Binary Assertions]]'
---

## Summary

[[Simon Scrapes]] applies [[Andrej Karpathy]]'s Auto-Research concept to [[Claude Code]] skills -- building an autonomous loop that tests, scores, and refines skills overnight without human input.

### Key Takeaways

- **The Problem**: Getting skills from v1 to reliable takes weeks of manual tweaking -- run, spot issues, edit skill.md, repeat.
- **Karpathy's Auto-Research Pattern**: Give an AI something to improve + one clear metric. It loops: make change, run test, check score, keep or revert. Repeat indefinitely.
- **Applied to Skills**: Same pattern but measuring skill output quality with binary assertions (true/false) instead of training loss.
- **Binary Assertions Are Key**: "Is it under 300 words?" (binary) vs "Is it compelling?" (subjective). Only binary assertions can be automated reliably.
- **Eval Setup**: Create an `eval.json` with 25 binary assertions across 5 test prompts. Claude checks each assertion, scores the skill, and if any fail, modifies skill.md and retests.
- **Two Layers of Self-Improvement**: (1) Anthropic's built-in description loop for skill activation/triggering. (2) This Karpathy-style loop for skill output quality.
- **Limitations**: Binary loops handle structure, format, word counts, forbidden patterns. Tone, creative quality, and context usage still need human judgment.
- **Progressive Disclosure**: Skills use YAML front matter as a summary -- Claude only loads full instructions when the skill is triggered.

### Referenced Concepts
- [[Andrej Karpathy]]'s Auto-Research
- [[Claude Code]] Skills Framework
- Binary Assertions for automated testing

![](https://www.youtube.com/watch?v=wQ0duoTeAAU)

🚀 Build agentic systems that run your business: https://skool.com/scrapes  
Don't miss the next build - https://www.youtube.com/@simonscrapes?sub\_confirmation=1  
  
What if your Claude Code skills could improve themselves overnight while you sleep? In this tutorial, we take inspiration from Andrej Karpathy's "Autoresearch" concept and apply it to Claude Code. You'll learn how to set up an autonomous loop that tests, scores, and refines your skills based on a set of binary criteria, ensuring they get more reliable with every iteration.  
  
#claudecode #claudecodetutorial #autoresearchclaude

## Transcript

**0:00** · Skills are one of the most powerful things you can build inside Claw Code for your business. But what if those skills could even improve themselves overnight? I've built over 20 so far, and getting them from version one to something reliable usually takes weeks of tweaking. So you run the skill, you spot something wrong, you open up the skill.md file and make a change, and it's pretty repetitive. It's slow and it's inconsistent. And then last week, Andre Carpathy, part of the founding team at OpenAI and former head of AI at Tesla, shared an idea called auto research. So the idea is simple. You give an AI system something to improve and one clear way to measure if it got better. Then it just loops. So it's trying a change. It's running a test.

**0:37** · It's checking the score. And if the results improves, it keeps the change.

**0:41** · If not, it rolls it back and tries something else. And the best thing about it is it keeps going all night so you get to sleep and wake up to a better system. So today we're applying that exact idea, but to Claude Code skills.

**0:53** · I'm going to show you how to set up a loop where your skills improve themselves automatically. Let's get straight into it. So let's take a quick look at what Carpathy actually built and it can pretty much be summarized by three different files here. So first we have the program.md which is just a markdown instruction file that we give to that agent telling it what we want to test. We have a fixed data file for recording all the results. And then we have a training script that the agent actually goes in and edits. And the core of the program.md file or the one that we edit is actually really summarized by about 10 lines. And that's all we need to make it our own. So we've got tune train.py Pi with an experimental idea by directly hacking the code, i.e. make a change. We've got run the experiment as it sounds. Read out the results. If the value has improved, then we're going to advance the branch and keep the commit.

**1:38** · If the value is worse, then we're going to reset to where we started. And I love this line down here, too. Never stop.

**1:44** · Once the experiment loop has begun, do not pause to ask the human if you should continue. Do not ask if I should keep going or is this a good stopping point.

**1:51** · The human might be asleep or gone from the computer and expects you to continue working indefinitely until you are manually stopped. You are autonomous.

**1:59** · I.e. just keep working until you've either improved the results indefinitely where there's no additional gains to be made or we interrupt you. So let's talk about how we apply this directly to our skills. So before we improve our skills output, we need Claude to actually use the skill. So a quick recap because we covered this in the last video. So Claude reads, "Your YAML description decide relevance of the skill and community testing found that activation was as low as 20% when you've got vague descriptions." So basically descriptions in the YAML are super important inside the skill. Now the skill creator anthropic skill, the upgrade already has a built-in loop for this. So it's effectively the same pattern as Carpathy. You give it test queries to see if a skill activates. Some are going to trigger the skill, some aren't going to trigger the skill. and it runs each multiple times, checks the trigger accuracy and proposes a better description to trigger the skill and then retests that. So you can see this directly in the improved description.py file here which is designed to improve a skill description based on evaluation results and that runs through the run loop which combines the evaluation and the improved description Python files in a loop. So i.e. it keeps running and improves the description based on the trigger accuracy. So did Claude actually activate the skill at the right time?

**3:13** · Yes or no? That's basically how it works. So, we already know by this that this is automated and built into this skills 2.0 version. So, there's no need to reinvent the wheel here with skill descriptions. We're just going to use anthropics built-in skill creator skill.

**3:26** · But, triggering reliably and producing actual great outputs from the skills are different problems. So, the skill creators eval which we covered in the last video let you test and score output quality based on your own defined metrics. So, we actually went ahead and tested this. So we had optimize my skill for making sure my copy follows the persuasive techniques listed in my persuasion toolkit reference file which was just a reference file that we had inside the marketing copywriting skill.

**3:52** · And then we said measure it on does it always use that reference file? Does it use curiosity and open loops? And how often is it using proof or founderled stories which were both metrics inside that persuasion toolkit. And then we tested it by getting it to write landing page copy for my school community five times and testing it against that criteria. And it was brilliant. It came up with qualitative feedback on the skill quality and even displayed it in a nice click-through dashboard, but it wasn't self-improving. So, what we're adding today is making that loop run autonomously Carpathy style, so it improves overnight without your inputs.

**4:24** · So, let's visualize them now side by side so you can see the exact framework and the same or similar logic that we're using between Karpathy's original loop or ours here when applied to skills. So, we've got read the train.python Python file, change a value, run a test, check the value. So this is the metric they're using, val\_bpb, keep or revert. So it's either going to if if the score is improved, get commit it and keep it and run the next loop. Or if the score is dropped, it's going to get reset and actually start again and make a different change. So ours is seriously similar. It's going to be the same logic, same infrastructure, but what we're actually doing is reading this skill.md file instead. So reading our skill instructions, process instructions, changing a value, we're going to run a test, we're going to check the pass rate, and then we're going to keep or revert. So the only difference here is the metric by which we're measuring it by. So they're using a value here. We're checking the pass rate against 25 binary assertions across five tests. So we're going to talk about uh what binary assertions are right now and why they're important. Now the word binary is everything here and this is where most people are getting it wrong when they're te executing tests on their skills. So for example we have something binary on the right hand side. It does not contain m dashes. So our text doesn't contain m dashes or it's under 300 words or the final line is a question. It's all true or false statements versus something very subjective like does it have a compelling subject line. And this is obviously not binary because two people can disagree on what compelling actually means which means we can't actually automate it. Of course, we can get the assistance from claw code to say actually based on certain frameworks, this is considered compelling, but it's not this binary true false approach. So, here's my actual setup. So, inside my skills here, we've got a marketing copywriting skill and what we need to do is set up an eval folder. So, this is something that the skill creator skill can actually do for you or you can actually create this yourself. So, we set up an eval folder and an eval.json.

**6:21** · And inside that eval.json, JSON, we've got 25 assertions or true or false binary things that we can check or the autonomous agent can actually go through and check and make sure are true or not.

**6:32** · So, for example, for the copyrightiting skill for the first test, we're going to feed in the prompt, write a LinkedIn post about why simple automations beat complex ones with an expected output of a LinkedIn post following brand structure rules. And it's grabbing those brand structure rules from our reference files. So, our contextual files inside the skill. So, we've got a tone of voice guide, we've got persuasion toolkit, we've got examples of good posts inside there. But what we're doing is actually testing things that are totally based on this skill.md and the process. So, does the first line appear as a standalone sentence and not part as paragraph? That is going to be marked true or false.

**7:05** · Does it contain at least one specific number or statistic? Is the final line not a question? I don't like questions as the final line in my posts. Is the total word count under 300? And you get the point. We have various different uh tests that we run with different prompts and different assertions that are going to come back true or false. And this enables the loop to go through each of these assertions, validate whether it's true or false, and then make a change to the skill.md if it's not hit perfect score. And of course, you don't need to go through and actually create this manually, this evals.json. You can just ask cloud code to spin up an evals.json file with assertions that can be validated by true or false questions based on your skill.md. And then what we're effectively doing is feeding in a prompt, seeing does it hit those assertions. If it doesn't, then we need to improve our skill.md so that clog code is able to follow it every single time. And then after that, all you need to do to run this autonomously is say to use the skill creator skill. We probably didn't need to say that even run a self-improvement loop on my copywriting skill. We'll point it to our evals file to evaluate each iteration. We're telling it to basically use the same principles, detect whether it passes or fails, and then return a pass fail mark.

**8:11** · If any of the assertions fail, make one change to the skilled atm. So, we're doing the exact same logic that we spoke about in that diagram. If any fail, rerun the tests and recalculate. If the score improved, keep the change and get commit. If it dropped, get reset and make a new change. It's going to log everything. And we've also given it the instruction to not ask for my permissions and keep looping until I interrupt you or you hit a perfect score. So, we can run through that. And what we've effectively got here is on the first run of this, we've scored 23 out of 24. So, as I've already mentioned, this is like the fifth version of this marketing copywriting skill. So, it's already gone through quite comprehensive iterations and changes. But you can see on the first iteration of this test, we had a 95.8% success rate. One of the assertions failed, which was end with a question rule, which was actually a rule in the tone of voice.md, but not in the skill.md. So, that we had contrasting information there. So, it added a rule to the skill.md. LinkedIn post must not end with a question, close with declarative statement, CTA, or a punchy fragment. And then on the second time it actually ran that and it got a perfect score. So obviously we're talking about an example that only need two runs to be perfect, but where you've just created a skill. This will take many runs to actually refine and improve on the skill here. So get claw code to write your assertions once, set up the loop and you can literally let it run overnight and come back to a skill the next day or multiple agents running multiple tests on these skills. They're actually structurally more sound. So there's two layers of skill self-improvement. Layer one is the skill creator's own description improvement loop to improve skill activation to get it to actually trigger a skill in the first place. And layer two is our amended carpathy loop for skill outputs that use those binary true false assertions and a score and then autonomous improvement through a simple prompt where we ask it to actually use the evals and continue to loop until we are happy it's met a certain criteria. Now a quick note on limitations. The binary loop handles structure, format, word counts, forbidden patterns, but it does not handle tone of voice, creative quality, whether your skill is actually using the context you've put in your reference files properly. Those still need a bit of human judgment. But if you watched the last video, you already know how to use the skill creator tool for that where it gives you a sideby-side dashboard to review the qualitative output, write feedback, and even AB test your reference files. Whereas this binary loop can be used for the more structural stuff. Now, if you're looking for bespoke skills to run your business, we've just launched a complete agentic operating system built on claw code that ties all of this, including all the skills into one system. So, it has your brand memory, 18 production skills across marketing, strategy, ops, and visuals, too. A self-learning loop, self-maintenance, and you can access it through your phone through Telegram, too. So, it's not a personal assistant.

**10:53** · It's entire business context packaged into a system that gets sharper every time you use it. Links down in the description if you want more info. And thanks so much for watching.

---

## Transcript

[00:00:00] Skills are one of the most powerful
[00:00:01] things you can build inside Claw Code
[00:00:03] for your business. But what if those
[00:00:04] skills could even improve themselves
[00:00:06] overnight? I've built over 20 so far,
[00:00:08] and getting them from version one to
[00:00:10] something reliable usually takes weeks
[00:00:12] of tweaking. So you run the skill, you
[00:00:13] spot something wrong, you open up the
[00:00:15] skill.md file and make a change, and
[00:00:17] it's pretty repetitive. It's slow and
[00:00:19] it's inconsistent. And then last week,
[00:00:21] Andre Carpathy, part of the founding
[00:00:23] team at OpenAI and former head of AI at
[00:00:25] Tesla, shared an idea called auto
[00:00:27] research. So the idea is simple. You
[00:00:29] give an AI system something to improve
[00:00:31] and one clear way to measure if it got
[00:00:34] better. Then it just loops. So it's
[00:00:35] trying a change. It's running a test.
[00:00:37] It's checking the score. And if the
[00:00:39] results improves, it keeps the change.
[00:00:41] If not, it rolls it back and tries
[00:00:43] something else. And the best thing about
[00:00:44] it is it keeps going all night so you
[00:00:46] get to sleep and wake up to a better
[00:00:48] system. So today we're applying that
[00:00:50] exact idea, but to Claude Code skills.
[00:00:53] I'm going to show you how to set up a
[00:00:54] loop where your skills improve
[00:00:55] themselves automatically. Let's get
[00:00:57] straight into it. So let's take a quick
[00:00:59] look at what Carpathy actually built and
[00:01:01] it can pretty much be summarized by
[00:01:02] three different files here. So first we
[00:01:04] have the program.md which is just a
[00:01:06] markdown instruction file that we give
[00:01:08] to that agent telling it what we want to
[00:01:10] test. We have a fixed data file for
[00:01:12] recording all the results. And then we
[00:01:14] have a training script that the agent
[00:01:16] actually goes in and edits. And the core
[00:01:18] of the program.md file or the one that
[00:01:20] we edit is actually really summarized by
[00:01:22] about 10 lines. And that's all we need
[00:01:24] to make it our own. So we've got tune
[00:01:26] train.py Pi with an experimental idea by
[00:01:28] directly hacking the code, i.e. make a
[00:01:30] change. We've got run the experiment as
[00:01:32] it sounds. Read out the results. If the
[00:01:35] value has improved, then we're going to
[00:01:36] advance the branch and keep the commit.
[00:01:38] If the value is worse, then we're going
[00:01:40] to reset to where we started. And I love
[00:01:42] this line down here, too. Never stop.
[00:01:44] Once the experiment loop has begun, do
[00:01:46] not pause to ask the human if you should
[00:01:48] continue. Do not ask if I should keep
[00:01:49] going or is this a good stopping point.
[00:01:51] The human might be asleep or gone from
[00:01:53] the computer and expects you to continue
[00:01:55] working indefinitely until you are
[00:01:57] manually stopped. You are autonomous.
[00:01:59] I.e. just keep working until you've
[00:02:01] either improved the results indefinitely
[00:02:03] where there's no additional gains to be
[00:02:06] made or we interrupt you. So let's talk
[00:02:08] about how we apply this directly to our
[00:02:10] skills. So before we improve our skills
[00:02:13] output, we need Claude to actually use
[00:02:15] the skill. So a quick recap because we
[00:02:17] covered this in the last video. So
[00:02:18] Claude reads, "Your YAML description
[00:02:20] decide relevance of the skill and
[00:02:22] community testing found that activation
[00:02:24] was as low as 20% when you've got vague
[00:02:27] descriptions." So basically descriptions
[00:02:28] in the YAML are super important inside
[00:02:30] the skill. Now the skill creator
[00:02:32] anthropic skill, the upgrade already has
[00:02:35] a built-in loop for this. So it's
[00:02:36] effectively the same pattern as
[00:02:38] Carpathy. You give it test queries to
[00:02:40] see if a skill activates. Some are going
[00:02:41] to trigger the skill, some aren't going
[00:02:43] to trigger the skill. and it runs each
[00:02:45] multiple times, checks the trigger
[00:02:47] accuracy and proposes a better
[00:02:49] description to trigger the skill and
[00:02:51] then retests that. So you can see this
[00:02:52] directly in the improved description.py
[00:02:55] file here which is designed to improve a
[00:02:57] skill description based on evaluation
[00:02:59] results and that runs through the run
[00:03:01] loop which combines the evaluation and
[00:03:02] the improved description Python files in
[00:03:04] a loop. So i.e. it keeps running and
[00:03:07] improves the description based on the
[00:03:09] trigger accuracy. So did Claude actually
[00:03:11] activate the skill at the right time?
[00:03:13] Yes or no? That's basically how it
[00:03:15] works. So, we already know by this that
[00:03:17] this is automated and built into this
[00:03:19] skills 2.0 version. So, there's no need
[00:03:21] to reinvent the wheel here with skill
[00:03:23] descriptions. We're just going to use
[00:03:24] anthropics built-in skill creator skill.
[00:03:26] But, triggering reliably and producing
[00:03:28] actual great outputs from the skills are
[00:03:30] different problems. So, the skill
[00:03:31] creators eval which we covered in the
[00:03:34] last video let you test and score output
[00:03:36] quality based on your own defined
[00:03:38] metrics. So, we actually went ahead and
[00:03:40] tested this. So we had optimize my skill
[00:03:42] for making sure my copy follows the
[00:03:44] persuasive techniques listed in my
[00:03:46] persuasion toolkit reference file which
[00:03:48] was just a reference file that we had
[00:03:50] inside the marketing copywriting skill.
[00:03:52] And then we said measure it on does it
[00:03:54] always use that reference file? Does it
[00:03:56] use curiosity and open loops? And how
[00:03:58] often is it using proof or founderled
[00:04:00] stories which were both metrics inside
[00:04:01] that persuasion toolkit. And then we
[00:04:03] tested it by getting it to write landing
[00:04:04] page copy for my school community five
[00:04:06] times and testing it against that
[00:04:08] criteria. And it was brilliant. It came
[00:04:10] up with qualitative feedback on the
[00:04:12] skill quality and even displayed it in a
[00:04:14] nice click-through dashboard, but it
[00:04:16] wasn't self-improving. So, what we're
[00:04:18] adding today is making that loop run
[00:04:19] autonomously Carpathy style, so it
[00:04:22] improves overnight without your inputs.
[00:04:24] So, let's visualize them now side by
[00:04:26] side so you can see the exact framework
[00:04:29] and the same or similar logic that we're
[00:04:31] using between Karpathy's original loop
[00:04:33] or ours here when applied to skills. So,
[00:04:35] we've got read the train.python Python
[00:04:38] file, change a value, run a test, check
[00:04:41] the value. So this is the metric they're
[00:04:42] using, val_bpb,
[00:04:45] keep or revert. So it's either going to
[00:04:47] if if the score is improved, get commit
[00:04:49] it and keep it and run the next loop. Or
[00:04:51] if the score is dropped, it's going to
[00:04:53] get reset and actually start again and
[00:04:54] make a different change. So ours is
[00:04:56] seriously similar. It's going to be the
[00:04:58] same logic, same infrastructure, but
[00:05:00] what we're actually doing is reading
[00:05:01] this skill.md file instead. So reading
[00:05:03] our skill instructions, process
[00:05:05] instructions, changing a value, we're
[00:05:07] going to run a test, we're going to
[00:05:09] check the pass rate, and then we're
[00:05:10] going to keep or revert. So the only
[00:05:12] difference here is the metric by which
[00:05:13] we're measuring it by. So they're using
[00:05:15] a value here. We're checking the pass
[00:05:18] rate against 25 binary assertions across
[00:05:22] five tests. So we're going to talk about
[00:05:24] uh what binary assertions are right now
[00:05:25] and why they're important. Now the word
[00:05:27] binary is everything here and this is
[00:05:29] where most people are getting it wrong
[00:05:30] when they're te executing tests on their
[00:05:32] skills. So for example we have something
[00:05:35] binary on the right hand side. It does
[00:05:37] not contain m dashes. So our text
[00:05:39] doesn't contain m dashes or it's under
[00:05:41] 300 words or the final line is a
[00:05:43] question. It's all true or false
[00:05:44] statements versus something very
[00:05:46] subjective like does it have a
[00:05:48] compelling subject line. And this is
[00:05:50] obviously not binary because two people
[00:05:51] can disagree on what compelling actually
[00:05:53] means which means we can't actually
[00:05:55] automate it. Of course, we can get the
[00:05:56] assistance from claw code to say
[00:05:58] actually based on certain frameworks,
[00:06:00] this is considered compelling, but it's
[00:06:02] not this binary true false approach. So,
[00:06:04] here's my actual setup. So, inside my
[00:06:06] skills here, we've got a marketing
[00:06:08] copywriting skill and what we need to do
[00:06:10] is set up an eval folder. So, this is
[00:06:13] something that the skill creator skill
[00:06:15] can actually do for you or you can
[00:06:17] actually create this yourself. So, we
[00:06:18] set up an eval folder and an eval.json.
[00:06:21] And inside that eval.json, JSON, we've
[00:06:23] got 25 assertions or true or false
[00:06:26] binary things that we can check or the
[00:06:28] autonomous agent can actually go through
[00:06:30] and check and make sure are true or not.
[00:06:32] So, for example, for the copyrightiting
[00:06:34] skill for the first test, we're going to
[00:06:35] feed in the prompt, write a LinkedIn
[00:06:37] post about why simple automations beat
[00:06:39] complex ones with an expected output of
[00:06:41] a LinkedIn post following brand
[00:06:43] structure rules. And it's grabbing those
[00:06:44] brand structure rules from our reference
[00:06:46] files. So, our contextual files inside
[00:06:48] the skill. So, we've got a tone of voice
[00:06:50] guide, we've got persuasion toolkit,
[00:06:52] we've got examples of good posts inside
[00:06:54] there. But what we're doing is actually
[00:06:55] testing things that are totally based on
[00:06:57] this skill.md and the process. So, does
[00:06:59] the first line appear as a standalone
[00:07:01] sentence and not part as paragraph? That
[00:07:03] is going to be marked true or false.
[00:07:05] Does it contain at least one specific
[00:07:06] number or statistic? Is the final line
[00:07:09] not a question? I don't like questions
[00:07:11] as the final line in my posts. Is the
[00:07:13] total word count under 300? And you get
[00:07:15] the point. We have various different uh
[00:07:17] tests that we run with different prompts
[00:07:18] and different assertions that are going
[00:07:20] to come back true or false. And this
[00:07:21] enables the loop to go through each of
[00:07:23] these assertions, validate whether it's
[00:07:26] true or false, and then make a change to
[00:07:27] the skill.md if it's not hit perfect
[00:07:30] score. And of course, you don't need to
[00:07:31] go through and actually create this
[00:07:32] manually, this evals.json. You can just
[00:07:34] ask cloud code to spin up an evals.json
[00:07:37] file with assertions that can be
[00:07:39] validated by true or false questions
[00:07:41] based on your skill.md. And then what
[00:07:43] we're effectively doing is feeding in a
[00:07:44] prompt, seeing does it hit those
[00:07:46] assertions. If it doesn't, then we need
[00:07:48] to improve our skill.md so that clog
[00:07:50] code is able to follow it every single
[00:07:51] time. And then after that, all you need
[00:07:53] to do to run this autonomously is say to
[00:07:55] use the skill creator skill. We probably
[00:07:57] didn't need to say that even run a
[00:07:59] self-improvement loop on my copywriting
[00:08:01] skill. We'll point it to our evals file
[00:08:03] to evaluate each iteration. We're
[00:08:05] telling it to basically use the same
[00:08:07] principles, detect whether it passes or
[00:08:09] fails, and then return a pass fail mark.
[00:08:11] If any of the assertions fail, make one
[00:08:13] change to the skilled atm. So, we're
[00:08:14] doing the exact same logic that we spoke
[00:08:16] about in that diagram. If any fail,
[00:08:18] rerun the tests and recalculate. If the
[00:08:20] score improved, keep the change and get
[00:08:22] commit. If it dropped, get reset and
[00:08:25] make a new change. It's going to log
[00:08:26] everything. And we've also given it the
[00:08:28] instruction to not ask for my
[00:08:29] permissions and keep looping until I
[00:08:31] interrupt you or you hit a perfect
[00:08:33] score. So, we can run through that. And
[00:08:35] what we've effectively got here is on
[00:08:37] the first run of this, we've scored 23
[00:08:40] out of 24. So, as I've already
[00:08:41] mentioned, this is like the fifth
[00:08:42] version of this marketing copywriting
[00:08:44] skill. So, it's already gone through
[00:08:45] quite comprehensive iterations and
[00:08:47] changes. But you can see on the first
[00:08:49] iteration of this test, we had a 95.8%
[00:08:52] success rate. One of the assertions
[00:08:54] failed, which was end with a question
[00:08:56] rule, which was actually a rule in the
[00:08:58] tone of voice.md, but not in the
[00:09:00] skill.md. So, that we had contrasting
[00:09:02] information there. So, it added a rule
[00:09:03] to the skill.md. LinkedIn post must not
[00:09:06] end with a question, close with
[00:09:07] declarative statement, CTA, or a punchy
[00:09:09] fragment. And then on the second time it
[00:09:11] actually ran that and it got a perfect
[00:09:13] score. So obviously we're talking about
[00:09:15] an example that only need two runs to be
[00:09:17] perfect, but where you've just created a
[00:09:19] skill. This will take many runs to
[00:09:20] actually refine and improve on the skill
[00:09:22] here. So get claw code to write your
[00:09:24] assertions once, set up the loop and you
[00:09:27] can literally let it run overnight and
[00:09:29] come back to a skill the next day or
[00:09:30] multiple agents running multiple tests
[00:09:32] on these skills. They're actually
[00:09:34] structurally more sound. So there's two
[00:09:36] layers of skill self-improvement. Layer
[00:09:38] one is the skill creator's own
[00:09:40] description improvement loop to improve
[00:09:42] skill activation to get it to actually
[00:09:44] trigger a skill in the first place. And
[00:09:46] layer two is our amended carpathy loop
[00:09:49] for skill outputs that use those binary
[00:09:51] true false assertions and a score and
[00:09:54] then autonomous improvement through a
[00:09:57] simple prompt where we ask it to
[00:09:58] actually use the evals and continue to
[00:10:00] loop until we are happy it's met a
[00:10:02] certain criteria. Now a quick note on
[00:10:04] limitations. The binary loop handles
[00:10:07] structure, format, word counts,
[00:10:08] forbidden patterns, but it does not
[00:10:10] handle tone of voice, creative quality,
[00:10:12] whether your skill is actually using the
[00:10:14] context you've put in your reference
[00:10:15] files properly. Those still need a bit
[00:10:17] of human judgment. But if you watched
[00:10:18] the last video, you already know how to
[00:10:20] use the skill creator tool for that
[00:10:22] where it gives you a sideby-side
[00:10:23] dashboard to review the qualitative
[00:10:25] output, write feedback, and even AB test
[00:10:27] your reference files. Whereas this
[00:10:29] binary loop can be used for the more
[00:10:30] structural stuff. Now, if you're looking
[00:10:32] for bespoke skills to run your business,
[00:10:34] we've just launched a complete agentic
[00:10:36] operating system built on claw code that
[00:10:38] ties all of this, including all the
[00:10:40] skills into one system. So, it has your
[00:10:42] brand memory, 18 production skills
[00:10:44] across marketing, strategy, ops, and
[00:10:46] visuals, too. A self-learning loop,
[00:10:48] self-maintenance, and you can access it
[00:10:50] through your phone through Telegram,
[00:10:52] too. So, it's not a personal assistant.
[00:10:53] It's entire business context packaged
[00:10:55] into a system that gets sharper every
[00:10:57] time you use it. Links down in the
[00:10:59] description if you want more info. And
[00:11:00] thanks so much for watching.