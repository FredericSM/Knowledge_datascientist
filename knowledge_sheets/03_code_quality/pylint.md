# Pylint — Static Code Analysis Cheat Sheet

Pylint analyzes Python code to detect errors, bad practices,
and deviations from coding standards.

It focuses on **code quality and correctness**, not formatting.

---

## Install Pylint (dev dependency)

```bash
uv add --group dev pylint
```

---

## Run Pylint on the project

```bash
pylint .
```

Analyzes all Python files recursively.

---

## Run Pylint on a single file

```bash
pylint my_script.py
```

---

## Understand the Score

At the end of execution, Pylint outputs a score:

```text
Your code has been rated at 8.75/10
```

- 10.0 → excellent
- ≥ 8.0 → good for data projects
- < 7.0 → needs cleanup

Do **not** aim blindly for 10/10.

---

## Most Common Warnings (Data Science)

- `unused-import`
- `unused-variable`
- `invalid-name`
- `too-many-locals`
- `too-many-arguments`

Many are acceptable in notebooks or experiments.

---

## Disable a Warning (Inline)

```python
# pylint: disable=unused-variable
```

Disable for a single line or block.

---

## Disable a Warning (Globally)

Create or update `.pylintrc`:

```bash
pylint --generate-rcfile > .pylintrc
```

Then edit:

```ini
[MESSAGES CONTROL]
disable=
    C0114,  # missing-module-docstring
    C0115,  # missing-class-docstring
    C0116   # missing-function-docstring
```

---

## Recommended Minimal Configuration (pyproject.toml)

```toml
[tool.pylint.messages_control]
disable = [
  "missing-module-docstring",
  "missing-class-docstring",
  "missing-function-docstring",
]
```

---

## Typical Workflow

```bash
isort .
black .
pylint .
```

Pylint always runs **after formatting**.

---

## Why Use Pylint

- Catches bugs early
- Enforces consistency
- Improves maintainability
- Common in production codebases

---

## Notes

- Slower than Black or isort
- Very strict by default
- Tune rules for data science workflows
