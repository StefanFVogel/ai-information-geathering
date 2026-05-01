# Ampel Integration

After every code step, run:

```bash
PYTHONIOENCODING=utf-8 python standards/scripts/maintain_tools.py --mode commit
```

## Interpreting Results

- GREEN → Continue to next step
- YELLOW → Note warning, can continue
- RED → STOP! Refactoring needed before continuing

## Common RED Causes

- Cyclomatic Complexity >= 20 → Split function, use early returns
- Dead code → Remove unused imports/variables
- Duplication > 5% → Extract shared function
- Security finding (Bandit) → Fix immediately
- Type errors (Pyright) → Fix type annotations

## Thresholds

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Python CC | <= 6 | 10-19 | >= 20 |
| Dead Code | 0 | — | any |
| Duplication | < 5% | — | >= 5% |
| Docstrings | >= 80% | < 80% | — |
| Security | 0 | — | any HIGH/MEDIUM |

## Remediation Patterns

### Complexity >= 20

Extract logical branches into named helper functions:

```python
# BAD — one function doing everything
async def create_alert(data: AlertCreate, user_id: int) -> Result[Alert]:
    if data.threshold <= 0:
        ...
    if data.direction not in ("above", "below"):
        ...
    existing = await repo.find_duplicate(...)
    if existing:
        ...
    # 40 more lines

# GOOD — early returns + helpers
async def create_alert(data: AlertCreate, user_id: int) -> Result[Alert]:
    validation_error = _validate_alert_input(data)
    if validation_error:
        return Err(validation_error)
    if await _is_duplicate_alert(repo, data, user_id):
        return Err("duplicate alert")
    return await repo.insert(data, user_id)
```

### Dead Code

Run Vulture output to identify, then delete without exception:

```bash
vulture stock_buddy/ --min-confidence 80
```

### Duplication > 5%

Extract to a shared module. Common candidates:

- Repeated `run_in_executor` wrappers → shared `db_execute()` helper
- Repeated Pydantic validators → shared validator function
- Repeated auth checks → FastAPI dependency

### Blocking I/O in Async

All pyodbc calls are synchronous. Wrap them:

```python
import asyncio

async def get_alerts(user_id: int) -> list[Alert]:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _sync_get_alerts, user_id)

def _sync_get_alerts(user_id: int) -> list[Alert]:
    # pyodbc query here
    ...
```

### Bandit Security Finding

Common findings and fixes:

| Finding | Fix |
|---------|-----|
| B608 SQL injection | Use parameterized queries — never f-string SQL |
| B105 hardcoded password | Move to `application_settings.py` (env var) |
| B101 assert used | Replace with `if not x: raise ValueError(...)` |

## When to Re-run

- After every file edit during the current step
- After fixing a RED finding
- Before committing
- Before handing off to the next skill (`/frontend`, `/qa`)
