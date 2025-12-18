# Black — Python Code Formatter

Black is an **opinionated code formatter**.
It reformats your Python code automatically and consistently.

You do **not configure style** — you accept it.

---

## Why Use Black

- Zero debates about formatting
- Consistent code across notebooks, scripts, and pipelines
- Works well with teams, CI/CD, and ML projects
- Lets you focus on logic, not style

---

## Install Black

```bash
uv add --group dev black
```

### Format a File
```bash
black script.py
```

### Format a Folder
``` bash
black .
```
(Common usage for projects.)

### Check Formatting (No Changes)
Useful in CI or before committing:

``` bash
black --check .
```

### Typical Project Usage
```bash
black src/
black tests/
```

You usually do not run Black on:
- data files
- virtual environments
- generated code

### Black with Jupyter Notebooks
``` bash
black notebook.ipynb
``` 
Works well for data science notebooks.

### pyproject.toml (Optional Configuration)
Black works without configuration, but you can pin basics:

```bash
[tool.black]
line-length = 88
target-version = ["py310"]
```
Do not over-configure Black.

### What Black Does Automatically

- Line wrapping
- String quotes normalization
- Function / class spacing
- Imports formatting (but not sorting)

### What Black Does NOT Do

- ❌ Linting
- ❌ Type checking
- ❌ Import sorting (use isort)
- ❌ Code optimization

### Best Practice for Data Science Projects
- Use Black on all Python files
- Run it:
    - before commits
    - or automatically in CI
- Combine with:
    - isort (imports)
    - pylint or ruff (linting)