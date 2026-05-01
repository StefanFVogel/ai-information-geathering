---
name: help
description: "Context-aware guide showing project status, workflow position, and recommended next steps. TRIGGER when user asks for help, orientation, what to do next, or at session start for status overview."
user-invocable: true
argument-hint: "[optional question]"
---

## When to Use

- User asks: "what should I do next?", "where are we?", "help", "status"
- Session start: user wants orientation before diving into work
- After completing a phase: user wants to know what comes next
- User is unsure which skill to invoke

## Workflow

The standard development flow:

```
1. /requirements  →  PRD + user stories defined
2. /architecture  →  Tech design + component diagram
3. /ticket        →  Jira ticket created / synced
4. /frontend      →  UI components implemented (loads style specialists)
   /backend       →  API + business logic implemented (loads style specialists)
5. /qa            →  Tests written and passing
6. /deploy        →  Deployed to environment
```

Supporting skills (usable at any phase):
- `/analyze`  — Crawl codebase → `docs/project-analysis/overview.md`
- `/help`     — This skill

## Analysis Logic

Read these sources **in order** and apply the decision tree:

### Sources to Read
1. `docs/superpowers/specs/*.status.yaml` — active workflow state
2. `docs/superpowers/specs/*.md` — latest spec files
3. `docs/superpowers/plans/*.md` — implementation plans
4. `docs/project-analysis/overview.md` — codebase analysis (if exists)
5. `features/INDEX.md` — framework improvement backlog (if exists)
6. Last Ampel run: check for `maintain_tools.py` output in conversation history

### Decision Tree

```
Has active spec with status.yaml?
  YES → read phase field:
    brainstorming    → "Spec in progress — complete /requirements output"
    design           → run /architecture
    spec-review      → review spec, then /ticket
    planning         → run /backend or /frontend (check what's missing)
    implementation   → check stock_buddy/ for completion, then /qa
    review           → run /review-fix, check Ampel status
    completed        → check if deployed → /deploy
  NO →
    No PRD / spec?   → run /requirements
    No tech design?  → run /architecture
    No implementation in stock_buddy/?  → run /backend or /frontend
    No tests?        → run /qa
    Not deployed?    → run /deploy
    All done?        → suggest framework backlog item (see below)

Ampel status?
  RED / YELLOW  → "Fix quality issues first: python standards/scripts/maintain_tools.py --mode branch"
  GREEN or unknown → proceed with workflow recommendation

features/INDEX.md exists with open items?
  5+ skills implemented → recommend next backlog item (e.g. "SKL-2 Eval Framework")
```

## Output Format

Produce exactly these four sections — keep them concise:

```
## Current Status
[One sentence: what phase are we in, based on status.yaml or file analysis]
Last updated: [date from status.yaml or file mtime]
Ampel: [GREEN / YELLOW / RED / unknown]

## Active Work
[Table or bullet list of open specs/features with their phase]
| Item | Phase | Next Step |
|------|-------|-----------|

## Recommended Next Step
[Single clear action with exact command to run]
> Run: /architecture
> Or: python standards/scripts/maintain_tools.py --mode branch

## Other Available Actions
[List remaining skills with one-line description each, only those relevant now]
- /requirements — define PRD and user stories
- /backend — implement API endpoints and business logic
- /frontend — implement JS components (stock_buddy/static/)
- /qa — write and run tests
- /deploy — deploy to AKS
- /analyze — crawl codebase → docs/project-analysis/
- /ticket — sync to Jira
```

## DO

- Read all status.yaml files before deciding — never guess the phase
- Check `docs/project-analysis/overview.md` for codebase context
- Reference specific files and paths (e.g. `stock_buddy/routers/alerts.py`)
- Show the exact command to run, not just the skill name
- If `features/INDEX.md` exists and all workflow phases are done, suggest a backlog item
- Report Ampel status if RED or YELLOW — quality issues block merging
- Keep each section under 5 lines — this is orientation, not documentation

## DON'T

- Don't implement anything — this skill only analyzes and recommends
- Don't invent status — only report what you actually find in files
- Don't list all 8 skills every time — only show relevant next options
- Don't ask clarifying questions — read the files and give a recommendation
- Don't run `maintain_tools.py` yourself — just report its last known result and suggest running it

## Context Recovery

If called with no context (fresh session):

```bash
# Check active specs
ls docs/superpowers/specs/ 2>/dev/null
# Check plans
ls docs/superpowers/plans/ 2>/dev/null
# Check project analysis
ls docs/project-analysis/ 2>/dev/null
# Check framework backlog
cat features/INDEX.md 2>/dev/null
# Check recent git activity
git log --oneline -10
# Check current branch
git branch --show-current
```

Use the branch name (e.g. `SBMVP-733-alerts`) as additional context for the active Jira ticket.
If no spec files exist, infer phase from git log and codebase contents in `stock_buddy/`.
