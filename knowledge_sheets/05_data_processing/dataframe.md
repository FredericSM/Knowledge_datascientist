# Pandas Cheat Sheet (Practical, Interview/Work Edition)

A compact “use-it-every-day” Pandas reference: load → inspect → clean → transform → join → group → reshape → time series → performance.

> Assumes: `import pandas as pd` and (optionally) `import numpy as np`

---

## 0) Imports & Display

```python
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 200)
pd.set_option("display.width", 120)
```

---

## 1) Create DataFrames

```python
df = pd.DataFrame({"a": [1,2], "b": [3,4]})
df = pd.DataFrame(np.random.randn(3, 2), columns=["x", "y"])
df = pd.DataFrame.from_records([{"a": 1}, {"a": 2, "b": 9}])  # list[dict]
```

---

## 2) Load / Save

### Read
```python
df = pd.read_csv("file.csv")
df = pd.read_csv("file.csv", sep=";", encoding="utf-8")
df = pd.read_csv("file.csv", parse_dates=["date_col"])
df = pd.read_excel("file.xlsx", sheet_name=0)
df = pd.read_parquet("file.parquet")
df = pd.read_json("file.json")
df = pd.read_sql(query, con)  # DB connection
```

### Write
```python
df.to_csv("out.csv", index=False)
df.to_excel("out.xlsx", index=False)
df.to_parquet("out.parquet", index=False)
df.to_json("out.json", orient="records")
df.to_sql("table", con, if_exists="replace", index=False)
```

---

## 3) Quick Inspection (first things to type)

```python
df.head(10)
df.tail(10)
df.shape
df.columns
df.dtypes
df.info()
df.describe(include="all")
df.nunique()
df.isna().sum().sort_values(ascending=False)
df.sample(5, random_state=0)
```

Value counts:
```python
df["col"].value_counts(dropna=False)
df["col"].value_counts(normalize=True)  # proportions
```

---

## 4) Column & Row Selection

### Columns
```python
df["col"]               # Series
df[["col1","col2"]]     # DataFrame
df.filter(like="temp")  # columns containing substring
df.filter(regex=r"^x_") # regex
```

### Rows (boolean masks)
```python
mask = (df["a"] > 0) & (df["b"].isin(["x","y"]))
df[mask]
df.query("a > 0 and b in ['x','y']")  # often cleaner
```

### loc / iloc (recommended)
```python
df.loc[rows, cols]      # label-based
df.iloc[rows, cols]     # position-based

df.loc[df["a"] > 0, ["a","b"]]
df.iloc[:5, :3]
```

---

## 5) Sorting & Ranking

```python
df.sort_values(["col1", "col2"], ascending=[True, False])
df.sort_index()

df["rank"] = df["score"].rank(method="dense", ascending=False)
df["pct_rank"] = df["score"].rank(pct=True)
```

---

## 6) Basic Cleaning

### Rename
```python
df = df.rename(columns={"old": "new"})
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
```

### Drop
```python
df = df.drop(columns=["col"])
df = df.drop(index=[0, 1])
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["key"], keep="last")
```

### Missing values
```python
df["x"] = df["x"].fillna(0)
df["x"] = df["x"].fillna(df["x"].median())
df = df.dropna(subset=["important_col"])
df = df.fillna({"a": 0, "b": "unknown"})
```

### Type conversions
```python
df["x"] = df["x"].astype("int64", errors="ignore")
df["x"] = pd.to_numeric(df["x"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True)
```

---

## 7) Creating / Updating Columns

### Vectorized ops (fast)
```python
df["c"] = df["a"] + df["b"]
df["flag"] = df["a"].gt(0)          # a > 0
df["bucket"] = pd.cut(df["a"], bins=[0,10,20,100], right=False)
df["qbin"] = pd.qcut(df["a"], q=4)  # quartiles
```

### Conditional logic
```python
df["label"] = np.where(df["score"] >= 0.5, "good", "bad")

conditions = [df["x"] < 0, df["x"].between(0, 10), df["x"] > 10]
choices = ["neg", "small", "big"]
df["size"] = np.select(conditions, choices, default="unknown")
```

### apply vs map (use sparingly)
```python
df["x2"] = df["x"].map(lambda v: v * 2)          # Series element-wise
df["row_sum"] = df[["a","b","c"]].sum(axis=1)
df["custom"] = df.apply(lambda r: r["a"] * r["b"], axis=1)  # slower
```

---

## 8) String Operations (`.str`)

```python
s = df["text"].astype("string")

df["lower"] = s.str.lower()
df["contains"] = s.str.contains("foo", case=False, na=False)
df["repl"] = s.str.replace(r"\s+", " ", regex=True).str.strip()
df["split0"] = s.str.split("_").str[0]
df[["first","last"]] = s.str.split(" ", n=1, expand=True)
```

Regex extract:
```python
df["id"] = s.str.extract(r"ID-(\d+)", expand=False)
```

---

## 9) Datetime / Time Series

```python
df["dt"] = pd.to_datetime(df["dt"], errors="coerce")
df["year"] = df["dt"].dt.year
df["month"] = df["dt"].dt.month
df["date"] = df["dt"].dt.date
df["dow"] = df["dt"].dt.day_name()
```

Sort + set index:
```python
df = df.sort_values("dt").set_index("dt")
```

Resample:
```python
daily = df["value"].resample("D").mean()
monthly = df["value"].resample("M").sum()
```

Rolling:
```python
df["rolling_7"] = df["value"].rolling(7, min_periods=1).mean()
```

Time zone:
```python
df.index = df.index.tz_localize("Europe/Paris", ambiguous="NaT", nonexistent="shift_forward")
df.index = df.index.tz_convert("UTC")
```

---

## 10) GroupBy (core skill)

### Aggregations
```python
g = df.groupby("key")

g.size()
g["value"].mean()
g["value"].agg(["count", "mean", "min", "max"])
g.agg(value_mean=("value","mean"), value_sum=("value","sum"))
```

Multiple keys:
```python
df.groupby(["k1","k2"]).agg(n=("id","size"), avg=("value","mean")).reset_index()
```

### Transform (return aligned to original rows)
```python
df["group_mean"] = df.groupby("key")["value"].transform("mean")
df["z"] = (df["value"] - df["group_mean"]) / df.groupby("key")["value"].transform("std")
```

### Apply (flexible, slower)
```python
df.groupby("key").apply(lambda d: d.nlargest(3, "score"))
```

---

## 11) Joins / Merges / Concats

### Merge (SQL-style)
```python
out = df1.merge(df2, on="id", how="left")                  # inner/left/right/outer
out = df1.merge(df2, left_on="id1", right_on="id2", how="inner")
out = df1.merge(df2, on=["k1","k2"], how="left", validate="m:1")
```

Common validations:
- `"1:1"` one-to-one
- `"1:m"` one-to-many
- `"m:1"` many-to-one
- `"m:m"` many-to-many

### Concat (stack)
```python
pd.concat([df_a, df_b], axis=0, ignore_index=True)  # append rows
pd.concat([df_a, df_b], axis=1)                      # add columns side-by-side
```

### Combine-first / update
```python
df["x"] = df["x"].combine_first(df_other["x"])  # fill missing from other
df.update(df_other)                              # in-place update where not-NA in df_other
```

---

## 12) Reshaping: Pivot / Melt / Stack

### Pivot table
```python
pt = df.pivot_table(index="customer", columns="month", values="revenue",
                    aggfunc="sum", fill_value=0)
```

### Melt (wide → long)
```python
long = df.melt(id_vars=["id"], value_vars=["x","y"], var_name="feature", value_name="value")
```

### Stack/Unstack (MultiIndex)
```python
wide = long.set_index(["id","feature"])["value"].unstack("feature")
stacked = wide.stack()
```

---

## 13) Filtering Patterns You Use Daily

Top N per group:
```python
top = df.sort_values("score", ascending=False).groupby("key").head(3)
```

Keep rows with duplicate keys:
```python
dups = df[df.duplicated("key", keep=False)]
```

Find rows not in another df:
```python
missing = df1[~df1["id"].isin(df2["id"])]
```

---

## 14) Handling Categories

```python
df["cat"] = df["cat"].astype("category")
df["cat"] = df["cat"].cat.add_categories(["unknown"]).fillna("unknown")
df["cat_codes"] = df["cat"].cat.codes
```

---

## 15) Outliers & Clipping

```python
q1 = df["x"].quantile(0.25)
q3 = df["x"].quantile(0.75)
iqr = q3 - q1
df["x_clipped"] = df["x"].clip(lower=q1 - 1.5*iqr, upper=q3 + 1.5*iqr)
```

---

## 16) Performance Tips (real-world)

**Prefer vectorization**:
- ✅ `df["x"] + 1`
- ✅ `np.where(...)`, `.str`, `.dt`
- ❌ `df.apply(axis=1, ...)` (use only if needed)

**Use categorical for repeated strings**:
```python
df["country"] = df["country"].astype("category")
```

**Avoid chained indexing**:
- ❌ `df[df["a"] > 0]["b"] = 1`
- ✅ `df.loc[df["a"] > 0, "b"] = 1`

**Copy warning**: if you slice then mutate, use `.copy()`:
```python
sub = df[df["a"] > 0].copy()
sub["b"] = 1
```

**Faster groupby**: pre-sort can help in some patterns:
```python
df = df.sort_values("key")
```

---

## 17) Common “Gotchas” (interview-friendly)

### SettingWithCopyWarning
Use `.loc` or `.copy()`:
```python
df.loc[mask, "col"] = value
```

### `inplace=True` is not always faster
Many methods return a new object; prefer assignment for clarity:
```python
df = df.dropna()
```

### `df.append` is deprecated
Use `pd.concat`.

### MultiIndex headaches
Reset index when it becomes awkward:
```python
df = df.reset_index()
```

---

## 18) EDA Quick Recipes

Correlations:
```python
df.select_dtypes(include="number").corr()
```

Cross-tab:
```python
pd.crosstab(df["a"], df["b"], normalize="index")
```

Simple sanity checks:
```python
assert df["id"].is_unique
assert df.notna().all().all()  # strict: no missing anywhere
```

---

## 19) Export for Reporting

```python
df.style.format(precision=2).to_excel("styled.xlsx", engine="openpyxl", index=False)
```

---

## 20) Minimal Template (copy/paste starter)

```python
def clean_and_aggregate(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)

    df["dt"] = pd.to_datetime(df["dt"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df = df.dropna(subset=["dt", "value"])

    out = (df.groupby("key", as_index=False)
             .agg(n=("value","size"), avg=("value","mean"), total=("value","sum"))
             .sort_values("total", ascending=False))

    return out
```

---

## 21) Quick Reference: `loc` vs `iloc`

- `loc`: **labels** (includes end label in slicing for index labels)
- `iloc`: **positions** (end-exclusive like Python slices)

```python
df.loc[0:3, "col"]   # if index labels are 0..n (label-based)
df.iloc[0:3, 0]      # first 3 rows, first column (position-based)
```

---

## 22) Quick Reference: `merge` vs `join`

- `merge`: join on columns (most common)
- `join`: join on index (or set index first)

```python
df1.merge(df2, on="id", how="left")

df1.set_index("id").join(df2.set_index("id"), how="left").reset_index()
```

---

## 23) Cheat Commands for Debugging

```python
df.memory_usage(deep=True).sum()
df.select_dtypes(include="object").nunique().sort_values(ascending=False)

# where do NAs come from?
df[df["col"].isna()].head()

# duplicates
df[df.duplicated(["k1","k2"], keep=False)].sort_values(["k1","k2"])

# compare two Series
(pd.Series(a).equals(pd.Series(b)))
```

---

### End
If you want, tell me the kind of work you do (analytics, ML features, time series, ETL), and I can add a *second* page with the 20 most common patterns for that exact workflow.





to do :
assign
apply
tail
pipe
transform