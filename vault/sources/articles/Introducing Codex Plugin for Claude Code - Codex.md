---
author: vb (OpenAI Community)
created: 2026-04-07
description: 'If you already use Claude Code, this Codex plugin is a simple way to
  bring Codex into the same workflow. It is useful in three cases: a standard Codex
  review, a more skeptical adversarial review, and handing work off to…'
published: 2026-03-30
source: https://community.openai.com/t/introducing-codex-plugin-for-claude-code/1378186
source_type: articles
status: processed
tags:
- claude-code
- openai
- clippings
- ai
- codex
- plugin
title: Introducing Codex Plugin for Claude Code - Codex
topics:
- '[[Codex]]'
- '[[Claude Code]]'
- '[[Code Review]]'
---

## Summary

Official announcement of the [[Codex]] plugin for [[Claude Code]] on the OpenAI community forum. The plugin lets Claude Code users invoke Codex directly via slash commands for code reviews, adversarial reviews, and task delegation.

### Key Points

- **Lightweight integration**: The plugin delegates through the local Codex CLI and app server -- same auth, config, environment, and [[MCP]] setup. Not a separate runtime.
- **Three use cases**: Standard code review, adversarial (skeptical) review, and handing work off to Codex for a second pass.
- **Requirements**: ChatGPT subscription (including Free tier) or OpenAI API key, plus Node.js 18.18+
- **Source**: [GitHub - openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

### Context

This article complements the video [[Codex Just 10x'd Claude Code Projects.md]] by [[Nate Herk]] which demonstrates the plugin in practice.

## Introducing Codex Plugin for Claude Code

[Codex](https://community.openai.com/c/codex/37)

[2](https://community.openai.com/u/vb "vb")

## post by vb on Mar 30

If you already use Claude Code, this Codex plugin is a simple way to bring Codex into the same workflow.

It is useful in three cases: a standard Codex review, a more skeptical adversarial review, and handing work off to Codex when you want a second pass from a different agent.

Check out the plugin here: [GitHub - openai/codex-plugin-cc: Use Codex from Claude Code to review code or delegate tasks. · GitHub](https://github.com/openai/codex-plugin-cc)

You need a ChatGPT subscription, including Free, or an OpenAI API key, plus Node.js 18.18 or later.

How it works:  
The plugin delegates through the local Codex CLI and Codex app server. So it uses the same local auth, config, environment, and MCP setup you already have with Codex.  
That is why it feels lightweight. It is not a separate runtime. It is Codex, just invoked from inside Claude Code.

Learn more about this release here

[2](https://community.openai.com/u/vb "vb")

## post by Bruno\_F on Apr 1

[Bruno\_F](https://community.openai.com/u/bruno_f)

[6d](https://community.openai.com/t/introducing-codex-plugin-for-claude-code/1378186/4 "Post date")

This post was flagged by the community and is temporarily hidden.