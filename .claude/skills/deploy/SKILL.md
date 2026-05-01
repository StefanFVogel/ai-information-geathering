---
name: deploy
description: "Deploy to production with pre/post checks. Uses Docker and Azure Kubernetes Service (AKS). Loads K8s-Patterns specialist. TRIGGER when QA is complete and code is ready for deployment."
user-invocable: true
argument-hint: "[environment: dev|prod]"
---

# Deploy

## When to Use

- QA passed (READY verdict) and the branch is ready to ship
- User explicitly requests a deployment
- Environment: `dev` (default) or `prod`

Loads the K8s patterns specialist: `standards/skills/styles/k8s/SKILL.md`

## Workflow

### Phase 1 — Pre-Deployment Checks

Before touching Docker or K8s, verify the gate conditions:

1. **QA verdict** — read the feature spec; confirm `## QA Results` section shows READY
2. **No Critical/High bugs** — re-read the QA bug list; if any Critical or High bugs exist, abort and report
3. **Ampel is GREEN**:
   ```bash
   PYTHONIOENCODING=utf-8 python standards/scripts/maintain_tools.py --mode branch
   ```
4. **Tests pass**:
   ```bash
   pytest --cov=stock_buddy -q
   ```
5. **Branch is up to date with main**:
   ```bash
   git fetch origin
   git log origin/main..HEAD --oneline
   ```

If any check fails: abort, report clearly what failed, and suggest the fix.

### Phase 2 — Determine Version

Extract or derive the version for the build:

```bash
# From git tags (setuptools_scm convention)
git describe --tags --abbrev=0

# Or ask user if no tag exists: "Was ist die Versionsnummer? (z.B. 1.2.3)"
```

Set `APP_VERSION` for the Docker build.

### Phase 3 — Build Docker Image

```bash
docker build . --build-arg APP_VERSION=<version> -t stockbuddy:<version>
docker tag stockbuddy:<version> stockbuddy:latest
```

Verify the build exits with code 0. If it fails: show the last 30 lines of build output and stop.

### Phase 4 — Deploy via GitHub Actions

Deployment is triggered through GitHub Actions pipelines — do not push directly to K8s.

| Environment | Pipeline file | Trigger |
|---|---|---|
| dev | `.github/workflows/aks_mvp_dev.yaml` | Push to `dev` branch or manual dispatch |
| prod | `.github/workflows/aks_mvp_www.yaml` | Push to `main` or manual dispatch |

Steps:
1. Merge/push the branch to the target branch (confirm with user before executing)
2. Verify the Actions run starts:
   ```bash
   gh run list --limit 3
   ```
3. Monitor until completion:
   ```bash
   gh run watch
   ```

### Phase 5 — Post-Deployment Checks

After the pipeline succeeds:

**K8s pod status:**
```bash
kubectl get pods -l app=stockbuddy
# All pods should show STATUS=Running, READY=1/1
```

**Health endpoint:**
```bash
curl -s https://<base-url>/health
# Expected: {"status": "ok"}
```

**Application Insights:** Check for new exceptions or elevated error rates in the Azure portal (alert the user if Application Insights access is required manually).

**Rollback trigger** — if pods are crashlooping or health check fails:
```bash
kubectl rollout undo deployment/stockbuddy
kubectl rollout status deployment/stockbuddy
```
Then abort and report. Do NOT retry the same build.

### Phase 6 — Create Git Tag

```bash
git tag -a v<version> -m "Release v<version>"
git push origin v<version>
```

### Phase 7 — Update Feature Status

In `docs/features/INDEX.md`, update the deployed feature's status to `Deployed`:

```markdown
| PROJ-X | Feature Name | Deployed | [spec link] |
```

Also add a changelog entry to the feature spec:
```markdown
- YYYY-MM-DD: Deployed to <environment> as v<version>
```

## DO

- Always run pre-deployment checks before building
- Confirm with the user before merging to `main` (irreversible)
- Use `manifests/` directory for any manual K8s manifest changes
- Report pod status and health check result explicitly after deploy
- Create the git tag in the same session as the deploy

## DON'T

- Don't skip the QA READY check — it is a hard gate
- Don't push directly to K8s — always go through GitHub Actions pipelines
- Don't deploy if Ampel is RED
- Don't deploy `prod` without explicit user confirmation
- Don't proceed past Phase 1 if any pre-check fails

## Rollback

If post-deployment checks fail:
1. `kubectl rollout undo deployment/stockbuddy`
2. Verify rollback: `kubectl rollout status deployment/stockbuddy`
3. Report what failed and what the previous stable version is
4. Update INDEX.md status back to `QA Passed`

## Handoff

Feature complete. Update `docs/features/INDEX.md` status to **Deployed** and inform the user.
