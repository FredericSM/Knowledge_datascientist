# isort — Import Sorting Cheat Sheet (Data Scientist)

isort automatically sorts and organizes Python imports.
It keeps imports clean, consistent, and readable.

---

## Install isort (dev dependency)

```bash
uv add --group dev isort
```

---

## Run isort on the project

```bash
isort .
```

Formats all Python files recursively.

---

## Run isort on a single file

```bash
isort my_script.py
```

---

## Check mode (CI / no changes)

```bash
isort . --check-only
```

Fails if imports are not correctly sorted.

---

## Typical Import Order (mental model)

1. Standard library  
2. Third-party libraries  
3. Local / project imports  

Example:

```python
import os
import sys

import numpy as np
import pandas as pd

from my_project.utils import helpers
```

---

## Common Options

```bash
isort . --profile black
```

Ensures compatibility with Black (recommended).

```bash
isort . --diff
```

Shows changes without applying them.

---

## Configure isort (recommended)

Add to `pyproject.toml`:

```toml
[tool.isort]
profile = "black"
line_length = 88
```

---

## Typical Workflow

```bash
isort .
black .
```

isort first, Black second.

---

## Why isort Matters

- Enforces clean import structure
- Avoids noisy diffs
- Improves readability
- Required in most professional codebases

---

## Notes

- Always use with Black
- Run before commits or in CI
- No impact on runtime behavior