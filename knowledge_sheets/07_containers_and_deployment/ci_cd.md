
# CI/CD Cheat Sheet — Practical & Production-Oriented

## 1. Definitions

### CI — Continuous Integration
Goal: Ensure code quality and correctness before deployment.

CI answers:
- Does the code respect standards?
- Does it break existing behavior?
- Can it be merged safely?

CI **never deploys**.

### CD — Continuous Deployment / Delivery
Goal: Automatically deploy validated code to an environment.

CD answers:
- How do we build artifacts?
- How do we deploy infra & code?
- How do we promote versions?

CD **does deploy**.

---

## 2. Golden Rules

- If you have **CD**, you need **CI**
- CI protects the **codebase**
- CD protects the **system**
- Never deploy without automated checks
- One environment = one deployment pipeline + one infra state

---

## 3. CI vs CD Responsibilities

| Concern | CI | CD |
|------|----|----|
| Linting / Formatting | ✅ | ❌ |
| Unit tests | ✅ | ❌ |
| Build artifacts | ❌ | ✅ |
| Cloud auth | ❌ | ✅ |
| Terraform apply | ❌ | ✅ |
| Deployment | ❌ | ✅ |
| Smoke tests | ❌ | ✅ |

---

## 4. GitHub Actions — Mental Model

- Workflow = when + jobs
- Job = one VM
- Step = one action or one shell command
- Fresh VM on every run
- Fails fast

---

## 5. Workflow Structure

```yaml
name: CI

on:
  pull_request:
  push:
    branches: ["main"]

jobs:
  job-name:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install ruff
      - run: ruff check app
```

---

## 6. `uses:` vs `run:`

### `uses:`
- Runs a reusable action (module)
- Versioned (`@v4`)
- Example:
```yaml
- uses: actions/checkout@v4
```

### `run:`
- Runs a shell command
- Example:
```yaml
- run: pytest -q
```

---

## 7. Common Reusable Actions

- Checkout code: `actions/checkout`
- Setup language: `actions/setup-python`
- Terraform: `hashicorp/setup-terraform`
- AWS auth: `aws-actions/configure-aws-credentials`
- Cache: `actions/cache`
- Docker: `docker/build-push-action`

---

## 8. CI Best Practices

- Fast (<5 min)
- Deterministic
- No secrets
- No deployment
- Runs on PRs

Typical CI steps:
1. Checkout
2. Setup runtime
3. Install tools
4. Lint
5. Tests

---

## 9. CD Best Practices

- Triggered on merge, tag, or manual approval
- Builds artifacts
- Authenticates to cloud
- Applies infra
- Deploys code
- Optional smoke tests

---

## 10. Environments

An environment = isolated system instance.

Common environments:
- dev
- staging / pre-prod
- prod

Differences:
- config values
- infra size
- protections
- credentials

---

## 11. Terraform + CI/CD

### Terraform Files
- `provider.tf`: providers, backend
- `main.tf`: resources/modules
- `variables.tf`: variable definitions
- `terraform.tfvars`: variable values (per env)
- `outputs.tf`: exported values

### Rule
**One environment = one Terraform state**

---

## 12. Variables — Where to Put Them

### Terraform `.tfvars`
- Stable per environment
- Infra configuration
- Versioned

### GitHub Actions variables/secrets
- Credentials
- Deployment context
- Backend config

Terraform precedence:
1. defaults
2. tfvars
3. env vars (`TF_VAR_`)
4. CLI args

---

## 13. Typical Promotion Flow

PR → CI → Merge → CD (dev) → Promote → CD (staging) → Tag + approval → CD (prod)

---

## 14. Common Mistakes

- Mixing CI and CD
- Deploying from CI
- Sharing infra between envs
- No remote Terraform state
- Manual prod deploys

---

## 15. One-Sentence Summaries

CI:
> Ensures code quality and integration via automated checks.

CD:
> Automates the deployment of validated code and infrastructure.

Environments:
> Isolated, independently deployable instances of a system.

---

## 16. Interview-Ready Answer

> “CI ensures code consistency and correctness, while CD automates safe delivery to environments. Both together enable reliable, repeatable production deployments.”

---
