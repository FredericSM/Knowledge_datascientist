# pytest — Testing Cheat Sheet 

pytest is the most common Python testing framework.  
It lets you write small, fast tests that protect your code from regressions and make refactors safe.

This sheet focuses on what you need for **data science**, **data engineering**, and **ML pipelines**.

---

## Install pytest (dev dependency)

```bash
uv add --group dev pytest
```

Common extras you may want:

```bash
uv add --group dev pytest-cov
uv add --group dev pytest-xdist
```

- `pytest-cov` → coverage reports
- `pytest-xdist` → run tests in parallel

---

## Minimal Project Layout (recommended)

```text
my_project/
├── pyproject.toml
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── features.py
└── tests/
    ├── test_features.py
    └── conftest.py
```

Key rule: tests live in `tests/` and files start with `test_`.

---

## Run Tests

Run everything:

```bash
pytest
```

Run tests in a folder:

```bash
pytest tests/
```

Run a single file:

```bash
pytest tests/test_features.py
```

Run a single test function:

```bash
pytest -k "test_name_contains"
```

---

## Common CLI Options (the 90%)

Show more details:

```bash
pytest -v
```

Stop on first failure:

```bash
pytest -x
```

Show stdout/prints:

```bash
pytest -s
```

Re-run only failing tests:

```bash
pytest --lf
```

Run failed first then the rest:

```bash
pytest --ff
```

---

## Your First Test (simple)

`src/my_project/features.py`

```python
def add(a: float, b: float) -> float:
    return a + b
```

`tests/test_features.py`

```python
from my_project.features import add

def test_add():
    assert add(2, 3) == 5
```

---

## Assertions You Actually Use

```python
assert x == y
assert x != y
assert x > 0
assert abs(x - y) < 1e-6
assert item in collection
assert df.shape == (100, 5)
```

For floats, prefer:

```python
import pytest

def test_float():
    assert 0.1 + 0.2 == pytest.approx(0.3)
```

---

## Testing pandas (highly practical)

```python
import pandas as pd
import pandas.testing as pdt

def test_dataframe_equal():
    df1 = pd.DataFrame({"a": [1, 2]})
    df2 = pd.DataFrame({"a": [1, 2]})
    pdt.assert_frame_equal(df1, df2)
```

Common helpers:
- `pandas.testing.assert_series_equal`
- `pandas.testing.assert_frame_equal`

---

## Testing numpy arrays

```python
import numpy as np

def test_array_close():
    a = np.array([1.0, 2.0])
    b = np.array([1.0, 2.0000001])
    assert np.allclose(a, b, atol=1e-6)
```

---

## Fixtures (the most important pytest feature)

Fixtures create reusable test setup.

### Simple fixture

`tests/conftest.py`

```python
import pandas as pd
import pytest

@pytest.fixture
def sample_df():
    return pd.DataFrame({"x": [1, 2, 3]})
```

Use in test:

```python
def test_mean(sample_df):
    assert sample_df["x"].mean() == 2
```

### Fixture scopes

```python
@pytest.fixture(scope="function")  # default
def fx(): ...

@pytest.fixture(scope="session")
def fx_session(): ...
```

- `function` → new instance per test
- `session` → one instance for whole test run (useful for expensive setup)

---

## Parametrization (test many cases fast)

```python
import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (0, 0, 0), (-1, 1, 0)],
)
def test_add_many(a, b, expected):
    assert a + b == expected
```

Great for feature engineering functions.

---

## Testing Exceptions

```python
import pytest

def test_raises():
    with pytest.raises(ValueError):
        int("not-a-number")
```

Also check message:

```python
with pytest.raises(ValueError, match="invalid"):
    raise ValueError("invalid input")
```

---

## Markers: slow, integration, unit

```python
import pytest

@pytest.mark.slow
def test_big_pipeline():
    ...
```

Run fast tests only:

```bash
pytest -m "not slow"
```

Register markers in `pyproject.toml` (recommended):

```toml
[tool.pytest.ini_options]
markers = [
  "slow: long running tests",
  "integration: tests that touch external systems",
]
```

---

## Skip Tests Conditionally

```python
import pytest
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_unix_only():
    ...
```

---

## Temporary Files (clean, no manual cleanup)

Use `tmp_path` fixture:

```python
def test_write_file(tmp_path):
    p = tmp_path / "out.txt"
    p.write_text("hello")
    assert p.read_text() == "hello"
```

Perfect for data pipeline outputs.

---

## Monkeypatch (replace env vars / functions)

```python
def test_env(monkeypatch):
    monkeypatch.setenv("ENV", "test")
    assert True
```

---

## Coverage (what % of code is tested)

Install:

```bash
uv add --group dev pytest-cov
```

Run with coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

Common reports:
- `term-missing` → shows missing lines in terminal
- `xml` → for CI tools

---

## Parallel Tests (speed)

Install:

```bash
uv add --group dev pytest-xdist
```

Run in parallel:

```bash
pytest -n auto
```

---

## Configure pytest (recommended)

Add to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
addopts = "-q"
```

Notes:
- `pythonpath = ["src"]` helps imports if you use a `src/` layout.

---

## Common Pitfalls (Data Projects)

- Mixing notebooks and tests: keep real logic in `src/`, notebooks call it.
- Non-determinism: set seeds (NumPy, random) and freeze data samples.
- External dependencies: mock them (filesystems, APIs, databases).
- Slow tests: mark them `@pytest.mark.slow` and exclude by default.

---

## Typical Workflow (recommended)

Before commit / push:

```bash
isort .
black .
pytest
pylint .
```

In CI:
- run `pytest --cov=...`
- optionally run `pytest -m "not slow"`

---

## Cheat Commands (copy/paste)

```bash
pytest -v
pytest -x
pytest -s
pytest -k "keyword"
pytest --lf
pytest -m "not slow"
pytest --cov=src --cov-report=term-missing
pytest -n auto
```
