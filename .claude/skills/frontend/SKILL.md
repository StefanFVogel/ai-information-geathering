---
name: frontend
description: "Implement frontend code: UI components, styling, interactivity with jQuery, Bootstrap 5, and vanilla JavaScript. Loads generic style specialists + project-specific styles from .claude/skills/projekt/. Runs Ampel quality gate after each code step. TRIGGER when user wants to build UI or frontend functionality."
user-invocable: true
context: fork
argument-hint: "[feature-spec-path]"
---

## When to Use

- User says: "build the UI for X", "implement the frontend for Y", "add a form/table/widget"
- After `/architecture` — component structure is defined, ready for implementation
- After `/backend` — API contract exists, frontend can be wired up
- Status.yaml shows phase: `planning` or `implementation` (frontend side)

## Stack

jQuery + Bootstrap 5 + vanilla JS. No React. No Tailwind. No shadcn/ui.

Style specialists loaded automatically:
- `standards/skills/styles/javascript/SKILL.md`
- `.claude/skills/projekt/js-style.md` (if exists)
- `.claude/skills/projekt/html-style.md` (if exists)
- `.claude/skills/projekt/css-style.md` (if exists)

## Pre-Work

Read context before writing any code:

```bash
# Active spec and tech design
cat docs/superpowers/specs/*.md 2>/dev/null | head -120

# Existing JS components — avoid duplicating
git ls-files resources/js/

# Existing CSS customizations
grep -n "module\|section" resources/css/custom.css 2>/dev/null | head -30

# Recent branch changes
git diff main --name-only
git log --oneline -10
```

Load the style specialists before implementing anything.

## Workflow

**Step 1 — Spec Review**
Load the feature spec (passed as argument or found in `docs/superpowers/specs/`).
Extract: UI components needed, user interactions, acceptance criteria, out-of-scope items.
Map each UI element to a component type: Form / Table / Widget / Manager.

**Step 2 — Design Clarification**
If the spec is ambiguous on UI behaviour, ask one focused question before coding.
Topics that need clarification: animation, inline vs. modal, empty states, error flows.
Do NOT ask about stack choices — those are fixed.

**Step 3 — Tech Questions**
Check for existing components that can be extended:
- Is there already a form for this entity? Can it be reused?
- Is there an existing table or widget pattern to follow?
- Which endpoints does the frontend call? (confirm with `/backend` output or spec)

If API contract is missing, stop and flag: "API not defined — run `/backend` first."

**Step 4 — Component Implementation**
Implement one component at a time. After each component:

```bash
# Ampel check — JS only
PYTHONIOENCODING=utf-8 python standards/scripts/maintain_tools.py --mode commit
```

Fix all RED findings before moving to the next component.
YELLOW findings must be resolved before Step 6.

**Step 5 — Integration**
Wire components into the page:
- Add `<div data-*-host></div>` placeholder to `index.html` (no HTML in JS files)
- Register manager in the page bootstrap / `DOMContentLoaded` handler
- Verify HTTP call pattern matches project style (check projekt/js-style.md)
- Verify no optimistic UI — all mutations followed by re-fetch

**Step 6 — User Review**
Present a summary of what was built and ask:
"Does this match your intent? Anything to adjust before handoff to `/qa`?"
Do NOT mark as done until user confirms.

## Component Rules

### File Organisation
- One class per file, named in kebab-case: `alert-form.js` → `AlertForm`
- Every file starts with `'use strict';` and a class-level JSDoc block
- Manager/orchestrator is a separate file; it only coordinates, never holds domain logic

### Form Components (TransactionForm pattern)
```js
'use strict';
/** @class AlertForm — create/edit an alert */
class AlertForm {
    get template() { /* returns HTML string — no <form> tag */ }

    // jQuery getters — CSS class selectors
    get $instrumentName() { return this.$form.find('.instrument'); }
    get $alertLimit()     { return this.$form.find('.alertLimit'); }

    open({ onCancel, onSave, showMode }) { /* callback pattern */ }
    bindFromView() { /* returns plain object with field values */ }
    _resetForm()   { /* clears all fields */ }

    render($container) { /* injects template, attaches events */ }
    show()  { this.$form.show('slide'); }
    hide()  { this.$form.hide('slide'); }
    destroy() { /* unbind events, remove DOM */ }
}
```
- No `<form>` tag — save via `$saveButton.click()`, cancel via `$cancelButton.click()`
- Validation helpers only: `validateField()`, `validateRequiredField()`,
  `validatePositiveValueField()`, `markAsValid()`, `markAsInvalid()`, `markFieldsAsValid()`
- Server errors via `_reportErrorViaTooltip()` — never `alert()` / `confirm()`

### Table / Widget / Manager Components
```js
static get SEL_ROW()        { return '[data-alert-row]'; }
static get SEL_DELETE_BTN() { return '[data-alert-delete]'; }
```
- `data-*` attributes for all JS hooks (not CSS classes, not IDs unless Bootstrap requires)
- Delegated `.on()` events on the container, not direct bindings on rows

### Visibility & Spinners
- `d-none` for show/hide — never `.show()`/`.hide()` except slide animations in forms
- Spinner pattern:
  ```html
  <div class="d-none alert-form-spinner">...</div>
  ```
  Toggled via `addClass('d-none')` / `removeClass('d-none')` in `_onBeginSave` / `_onFinishSave`
- Slide animation transition: `removeClass('d-none').hide()` then `.slideDown()`

### HTTP Calls
- No optimistic UI — always re-fetch after create / update / delete
- Follow the project-specific HTTP pattern (see `projekt/js-style.md`)

### Security
- `Utils.escapeHtml()` on ALL user or API data injected into HTML
- Magic strings → `Object.freeze({...})` constants

### CSS
- Custom styles only in `resources/css/custom.css` — never touch `style.css`
- Module-specific CSS grouped by module comment in `custom.css`
- No inline `style` attributes for JS-controlled behaviour

## Ampel Thresholds (JS)

After each component, run Biome + jscpd:

```bash
PYTHONIOENCODING=utf-8 python standards/scripts/maintain_tools.py --mode commit
```

- **GREEN:** No Biome errors, duplication < 5%
- **YELLOW:** Biome warnings, or complexity warnings
- **RED:** Biome errors, duplication ≥ 5%, dead code (Knip)

Do not proceed to the next component while RED.

## Completion Checklist

Before handing off to `/qa`:

- [ ] All components implemented and Ampel GREEN
- [ ] HTTP calls follow project-specific pattern (see projekt/js-style.md)
- [ ] No optimistic UI — all mutations followed by re-fetch
- [ ] All user/API data escaped with `Utils.escapeHtml()`
- [ ] All magic strings in `Object.freeze({...})` constants
- [ ] CSS in `custom.css` only — `style.css` untouched
- [ ] `index.html` has only `<div data-*-host>` placeholders — no inline form HTML
- [ ] `'use strict';` + JSDoc on every new file
- [ ] User has reviewed and confirmed the UI

## Context Recovery

If called with no arguments (fresh session):

```bash
# Find active spec
ls docs/superpowers/specs/ 2>/dev/null

# Find existing JS components
git ls-files resources/js/

# Check recent branch changes
git log --oneline -10
git diff main --name-only
git branch --show-current
```

Use the branch name (e.g. `SBMVP-733-alerts`) to infer the active Jira ticket and feature.
If no tech design exists, prompt: "No architecture found — run `/architecture` first."

## Handoff

After user confirms the UI:

- Tests needed → `/qa`
- Backend API still missing → `/backend`

Commit before handing off:
```
feat(SBMVP-X): Implement [component name] frontend
```
