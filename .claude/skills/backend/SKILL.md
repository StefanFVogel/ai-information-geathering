---
name: backend
description: "Implement backend code: APIs, database schemas, business logic with FastAPI, SQLModel, and Repository Pattern. Automatically loads Python-Style, SQL-Style, and FastAPI-Patterns specialists. Runs Ampel quality gate after each code step. TRIGGER when user wants to build backend functionality."
user-invocable: true
context: fork
argument-hint: "[feature-spec-path]"
---

## When to Use

- User says: "implement the API", "build the backend for X", "add this endpoint"
- After `/architecture` — tech design exists, ready to code
- Status.yaml shows phase: `planning` or `implementation`

## Pre-Work

Load style specialists before writing a single line:

```bash
# Python coding standards
cat standards/skills/styles/python/SKILL.md 2>/dev/null

# SQL patterns (Azure SQL Server / T-SQL)
cat standards/skills/styles/sql/SKILL.md 2>/dev/null

# FastAPI patterns
cat standards/skills/styles/fastapi/SKILL.md 2>/dev/null

# Project-specific overrides (if present)
cat .claude/skills/projekt/python-style.md 2>/dev/null
```

Read context:

```bash
# Feature spec + tech design
cat docs/superpowers/specs/*.md 2>/dev/null | head -150

# Existing routers — avoid duplicating endpoints
git ls-files stock_buddy/routers/

# Existing repositories — reuse before creating new
git ls-files stock_buddy/repositories/

# Existing models
git ls-files stock_buddy/models/

# Recent branch changes
git log --oneline -10
git branch --show-current
```

## Clarifying Questions

Ask these **before** writing code if the spec does not answer them:

1. **Permissions** — Is this endpoint user-scoped (Fief auth) or admin-only?
2. **Concurrent edits** — Can two users modify the same record simultaneously? Optimistic locking needed?
3. **Rate limiting** — Does this endpoint need throttling (e.g. external API calls)?
4. **Validation** — What are the field constraints (min/max, allowed values, required vs optional)?
5. **Soft delete vs hard delete** — Should records be archived or permanently removed?

Skip questions that are clearly answered in the spec.

## Workflow

### Step 1 — DB Schema

- Add/alter tables in `stock_buddy/models/` using SQLModel
- Migration script in `stock_buddy/migrations/` (plain T-SQL, named `YYYYMMDD_description.sql`)
- Run Ampel after this step

### Step 2 — Repository

- Create or extend in `stock_buddy/repositories/`
- Async methods only; use `run_in_executor` / `asyncio.to_thread` for blocking pyodbc calls
- No raw SQL in routes — all queries belong in the repository
- Run Ampel after this step

### Step 3 — API Routes

- New router file in `stock_buddy/routers/`
- Register in `stock_buddy/routing.py`
- Fief auth middleware on all user-facing endpoints
- Pydantic models for request/response bodies (separate from SQLModel table models)
- Result pattern for expected errors; raise `HTTPException` only for HTTP-level failures
- Run Ampel after this step

### Step 4 — Integration Check

```bash
# Verify route is registered
grep -n "include_router" stock_buddy/routing.py

# Verify no circular imports
python -c "import stock_buddy.main"

# Final Ampel
PYTHONIOENCODING=utf-8 python standards/scripts/maintain_tools.py --mode commit
```

## Ampel Gate

After **every code step**, run:

```bash
PYTHONIOENCODING=utf-8 python standards/scripts/maintain_tools.py --mode commit
```

See `references/ampel-integration.md` for thresholds and remediation.

- GREEN → continue to next step
- YELLOW → note warning, continue
- RED → stop, fix, re-run before continuing

## Code Standards (non-negotiable)

| Rule | Value |
|------|-------|
| Line length | 120 chars |
| Naming | `snake_case` |
| Type hints | mandatory — no `Any` |
| Docstrings | Google-style on all public functions/classes |
| CC per function | ≤ 6 (use early returns, extract helpers) |
| Dead code | 0% — remove immediately |
| Blocking I/O in async | `run_in_executor` or `asyncio.to_thread` |
| Expected errors | Result pattern |
| Panics | Exceptions only |

## File Locations

| Artifact | Location |
|----------|----------|
| Router | `stock_buddy/routers/<feature>.py` |
| Repository | `stock_buddy/repositories/<feature>_repository.py` |
| SQLModel table | `stock_buddy/models/<feature>.py` |
| Pydantic schema | `stock_buddy/models/<feature>.py` (same file, separate class) |
| Migration | `stock_buddy/migrations/YYYYMMDD_<description>.sql` |
| Tests | `tests/test_<feature>.py` |

## DO

- Read style specialists before writing code
- Ask clarifying questions before the first implementation step
- One repository method per query — no fat methods
- Reuse existing repositories if the feature overlaps
- Validate at the API boundary (Pydantic), not deep in business logic
- Keep router thin: delegate to repository, return Pydantic response
- Commit after each step that passes Ampel GREEN

## DON'T

- Don't write SQL directly in routes or business logic
- Don't use synchronous pyodbc calls inside `async def` without `run_in_executor`
- Don't return SQLModel table objects directly from endpoints — use Pydantic response models
- Don't skip Ampel — a RED result blocks the next step
- Don't implement frontend changes — hand off to `/frontend`
- Don't use `Any` type — annotate everything explicitly

## Context Recovery

If called with no context (fresh session):

```bash
# Find active spec
ls docs/superpowers/specs/ 2>/dev/null

# Find plan
ls docs/superpowers/plans/ 2>/dev/null

# Check recent implementation work
git log --oneline -10
git branch --show-current

# Check what already exists on this branch
git diff main --name-only
```

Use the branch name (e.g. `SBMVP-733-alerts`) to infer the active Jira ticket.
If no spec exists, prompt: "No spec found — run /requirements then /architecture first."

## Handoff

After all steps pass Ampel GREEN:

- Frontend changes needed → `/frontend`
- Tests needed → `/qa`
- Both → `/frontend` first (uses the new API contract), then `/qa`

Update `docs/superpowers/specs/*.status.yaml` → phase: `review` before handing off.

Commit message pattern:
```
feat(SBMVP-X): implement [feature name] API and repository
```
