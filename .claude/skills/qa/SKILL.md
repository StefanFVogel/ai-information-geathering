---
name: qa
description: "Test implementation against acceptance criteria, run security audit, classify bugs by severity. TRIGGER when implementation is complete and needs testing, or user asks for quality check."
user-invocable: true
context: fork
argument-hint: "[feature-spec-path]"
---

# QA

## When to Use

- Implementation is complete and needs validation against acceptance criteria
- User asks for a quality check or security audit
- Before handing off to `/deploy`

## Workflow

### Phase 1 — Load Context

1. Read the feature spec (argument or ask user for path)
2. Collect all acceptance criteria from the spec
3. Run `git diff main...HEAD --name-only` to identify changed files
4. Check current Ampel status:
   ```bash
   PYTHONIOENCODING=utf-8 python standards/scripts/maintain_tools.py --mode branch
   ```
   Ampel must be GREEN before declaring READY. If not GREEN, stop and report findings.

### Phase 2 — Run Tests

Run the relevant test suite for the changed area:

```bash
# Specific test file (preferred)
pytest tests/test_<feature>.py -v

# Full suite with coverage
pytest --cov=stock_buddy

# API endpoint tests via FastAPI TestClient
pytest tests/ -v -k "<feature_name>"
```

Verify that **existing tests still pass** (regression check). Any new failures in unrelated tests must be noted.

### Phase 3 — Test Against Acceptance Criteria

For each acceptance criterion in the feature spec:

1. Design a test case (manual or automated)
2. Execute it and record the actual result
3. Mark PASS or FAIL with concrete evidence (test output, log line, HTTP response)

Use the `qa-grader` sub-agent to evaluate results (see `agents/grader.md`).

**Edge cases to cover** (in addition to documented AC):
- Empty/null inputs
- Boundary values (0, max, negative)
- Concurrent requests (if async endpoint)
- Large payloads
- Missing optional fields

### Phase 4 — Security Audit

Check the changed code from a red-team perspective:

| Area | What to Check |
|---|---|
| Auth | Fief middleware present on all new endpoints; no unauthenticated routes |
| Authorization | User can only access own data (portfolios, alerts, watchlists) |
| SQL Injection | All DB queries use parameterized SQL (never f-strings in raw SQL) |
| XSS | `Utils.escapeHtml()` used on all user/API data injected into HTML |
| Secrets | No API keys, passwords, or tokens in source code or logs |
| Rate Limiting | High-cost endpoints (LLM calls, bulk operations) protected |
| Input Validation | Pydantic models used for all request bodies; no raw `dict` access |

### Phase 5 — Bug Classification

Classify each finding:

| Severity | Definition | Example |
|---|---|---|
| Critical | Security breach, data loss, data corruption | Auth bypass, SQL injection, exposed secret |
| High | Feature completely broken, incorrect data shown | AC fails end-to-end, wrong user data returned |
| Medium | Feature partially broken, workaround exists | Edge case failure, degraded UX |
| Low | Cosmetic, minor inconvenience | Wrong label text, minor layout issue |

### Phase 6 — Write QA Results

Append a `## QA Results` section to the feature spec:

```markdown
## QA Results

**Date:** YYYY-MM-DD
**Tester:** Claude QA
**Ampel:** GREEN / YELLOW / RED

### Acceptance Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | ... | PASS/FAIL | ... |

### Security Audit

| Area | Status | Notes |
|---|---|---|
| Auth | PASS/FAIL | ... |

### Bugs Found

| # | Severity | Description | File/Line |
|---|----------|-------------|-----------|
| 1 | High | ... | ... |

### Verdict

**READY** / **NOT READY**
Reason: ...
```

### Phase 7 — Verdict

- **READY**: All Critical and High bugs are absent AND Ampel is GREEN
- **NOT READY**: Any Critical or High bug exists, OR Ampel is RED/YELLOW

## DO

- Run actual tests — never assume a test passes
- Require concrete evidence (test output, log line) for each PASS
- Check regression: existing tests must still pass
- Treat auth and authorization as Critical severity
- Check `Utils.escapeHtml()` for every frontend feature that displays user data
- Check parameterized queries for every backend change that touches SQL

## DON'T

- Don't fix bugs — document and classify only
- Don't skip the Ampel check — it is a mandatory gate
- Don't mark PASS without evidence
- Don't invent test results — run the actual commands

## Handoff

- **READY** → `/deploy`
- **NOT READY** → `/backend` or `/frontend` with the bug list
