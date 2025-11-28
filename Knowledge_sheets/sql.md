# 🦆 SQL Cheat Sheet

## 🗄️ Database for exemple

### Table `customers`
| id | name    | region |
|----|---------|--------|
| 1  | Alice   | West   |
| 2  | Bob     | East   |
| 3  | Charlie | West   |

### Table `orders`
| id | customer_id | amount | year |
|----|-------------|--------|------|
| 1  | 1           | 120    | 2023 |
| 2  | 1           | 80     | 2024 |
| 3  | 2           | 500    | 2023 |
| 4  | 3           | 200    | 2024 |

### Table `products`
| id | product_name | price |
|----|--------------|-------|
| 1  | Pen          | 2     |
| 2  | Laptop       | 1500  |
| 3  | Desk         | 200   |

### Table `sales`
| region | amount | year |
|--------|--------|------|
| West   | 200    | 2023 |
| East   | 500    | 2023 |
| West   | 300    | 2024 |


## 🔸 1. LOGICAL EXECUTION ORDER

SQL executes clauses in this logical order (not the writing order):

1️⃣ **FROM** — Choose tables  
2️⃣ **JOIN** — Combine tables  
3️⃣ **WHERE** — Filter **before aggregation**  
4️⃣ **GROUP BY** — Group rows  
5️⃣ **HAVING** — Filter **after aggregation**  
6️⃣ **SELECT** — Compute and project columns  
7️⃣ **QUALIFY** — Filter **after window functions**  
8️⃣ **ORDER BY** — Sort the final results  

---

## 🔸 2. JOINS — With Results

### CROSS JOIN
Returns the Cartesian product of two tables (every customer × every product).

```sql
SELECT c.name, p.product_name
FROM customers c
CROSS JOIN products p;
```

**Result:**

| name    | product_name |
|---------|--------------|
| Alice   | Pen          |
| Alice   | Laptop       |
| Alice   | Desk         |
| Bob     | Pen          |
| Bob     | Laptop       |
| Bob     | Desk         |
| Charlie | Pen          |
| Charlie | Laptop       |
| Charlie | Desk         |


---

### INNER JOIN
Returns only rows where a match exists in both tables.

```sql
SELECT c.name, o.amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;
```

**Result:**

| name    | amount |
|---------|--------|
| Alice   | 120    |
| Alice   | 80     |
| Bob     | 500    |
| Charlie | 200    |


---

### LEFT JOIN
Returns all customers, even if they have no orders.

```sql
SELECT c.name, o.amount
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;
```

**Result:**

| name    | amount |
|---------|--------|
| Alice   | 120    |
| Alice   | 80     |
| Bob     | 500    |
| Charlie | 200    |


(If a customer had no orders, it would appear as `NULL` here.  
In this dataset, all customers have at least one order.)


---

### FULL OUTER JOIN
Returns all rows from both tables (customers and orders), even if not matching.

```sql
SELECT c.name, o.amount
FROM customers c
FULL OUTER JOIN orders o ON c.id = o.customer_id;
```

**Result:**

(Same as INNER JOIN + unmatched rows from both sides.  
In this dataset, all orders match a customer and all customers have orders.)

| name    | amount |
|---------|--------|
| Alice   | 120    |
| Alice   | 80     |
| Bob     | 500    |
| Charlie | 200    |


---

### SELF JOIN
Joins a table with itself (example: employees and their managers).

```sql
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.id;
```

**Example Result (hypothetical):**

| employee | manager |
|----------|---------|
| John     | Sarah   |
| Emily    | Sarah   |
| Sarah    | Robert  |



## 🔸 3. FILTERING — With Results

### WHERE  
Filters rows **before** aggregation.

```sql
SELECT *
FROM sales
WHERE region = 'West';
```

**Result:**

| region | amount | year |
|--------|--------|------|
| West   | 200    | 2023 |
| West   | 300    | 2024 |


---

### HAVING  
Filters rows **after** aggregation.  
Used with `GROUP BY`.

```sql
SELECT region, SUM(amount) AS total
FROM sales
GROUP BY region
HAVING total > 300;
```

**Step 1 — GROUP BY result:**

| region | total |
|--------|--------|
| West   | 500    |
| East   | 500    |

**Step 2 — Apply HAVING total > 300:**

| region | total |
|--------|--------|
| West   | 500    |
| East   | 500    |

(In this dataset, both regions meet the condition.)


---

### QUALIFY  
Filters rows **after** window functions.  
Works like a `WHERE` but for windowed results.

```sql
SELECT region, amount, year,
       ROW_NUMBER() OVER(
           PARTITION BY region
           ORDER BY amount DESC
       ) AS rank
FROM sales
QUALIFY rank = 1;
```

**Step 1 — Add row numbers inside each region:**

| region | amount | year | rank |
|--------|--------|------|------|
| West   | 300    | 2024 | 1    |
| West   | 200    | 2023 | 2    |
| East   | 500    | 2023 | 1    |

**Step 2 — Apply QUALIFY rank = 1:**  
(Top sale per region)

| region | amount | year | rank |
|--------|--------|------|------|
| West   | 300    | 2024 | 1    |
| East   | 500    | 2023 | 1    |


## 🔸 4. AGGREGATION & GROUPING — With Results

### GROUP BY  
Groups rows to apply aggregate functions.

```sql
SELECT region, SUM(amount) AS total
FROM sales
GROUP BY region;
```

**Result:**

| region | total |
|--------|--------|
| West   | 500    |
| East   | 500    |


---

### GROUPING SETS  
Allows multiple independent groupings in a single query.

```sql
SELECT region, year, SUM(amount) AS total
FROM sales
GROUP BY GROUPING SETS (
    (region),
    (year),
    ()
);
```

**Result:**

| region | year | total |
|--------|------|--------|
| West   | NULL | 500    |
| East   | NULL | 500    |
| NULL   | 2023 | 700    |
| NULL   | 2024 | 300    |
| NULL   | NULL | 1000   |

Interpretation:
- `(region)` → total per region  
- `(year)` → total per year  
- `()` → grand total  


---

### ROLLUP  
Generates hierarchical subtotals (like a pyramid).

```sql
SELECT year, region, SUM(amount) AS total
FROM sales
GROUP BY ROLLUP (year, region);
```

**Result:**

| year | region | total |
|------|--------|--------|
| 2023 | East   | 500    |
| 2023 | West   | 200    |
| 2023 | NULL   | 700    |
| 2024 | West   | 300    |
| 2024 | NULL   | 300    |
| NULL | NULL   | 1000   |

Interpretation:
- (year, region): detailed rows  
- (year): subtotal per year  
- (): grand total  


---

### CUBE  
Generates all possible combinations of groupings (region, year, both, none).

```sql
SELECT year, region, SUM(amount) AS total
FROM sales
GROUP BY CUBE (year, region);
```

**Result:**  
Same as ROLLUP plus **cross-dimension totals** (totals per region across all years).

| year | region | total |
|------|--------|--------|
| 2023 | East   | 500    |
| 2023 | West   | 200    |
| 2023 | NULL   | 700    |
| 2024 | East   | NULL   | ← No row in this dataset  
| 2024 | West   | 300    |
| 2024 | NULL   | 300    |
| NULL | East   | 500    |
| NULL | West   | 500    |
| NULL | NULL   | 1000   |

Interpretation:
- Per year × region  
- Totals per year  
- Totals per region  
- Grand total  

### `HAVING year IS NOT NULL`
Used to remove the “total” rows created by ROLLUP or CUBE when they’re too general.

## 🔸 5. EXPRESSIONS & UTILITY FUNCTIONS — With Results

### COALESCE  
Returns the first non-null value.

```sql
SELECT COALESCE(region, 'Unknown') AS clean_region
FROM sales;
```

**Result:**

| clean_region |
|--------------|
| West         |
| East         |
| West         |

(There are no NULL regions in this dataset, so nothing changes.)


---

### CAST  
Converts a value to another data type.

```sql
SELECT product_name, CAST(price AS DOUBLE) AS price_double
FROM products;
```

**Result:**

| product_name | price_double |
|--------------|--------------|
| Pen          | 2.0          |
| Laptop       | 1500.0       |
| Desk         | 200.0        |


---

### CASE WHEN  
Conditional logic inside SQL.

```sql
SELECT c.name,
       CASE
           WHEN o.amount > 300 THEN 'Large'
           WHEN o.amount > 100 THEN 'Medium'
           ELSE 'Small'
       END AS order_size
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

**Result:**

| name    | order_size |
|---------|------------|
| Alice   | Medium     |
| Alice   | Small      |
| Bob     | Large      |
| Charlie | Medium     |


---

### FILTER (WHERE ...)  
Adds a condition *inside* an aggregate function.

```sql
SELECT
    SUM(amount) FILTER (WHERE region = 'West') AS west_sales,
    SUM(amount) FILTER (WHERE region = 'East') AS east_sales
FROM sales;
```

**Result:**

| west_sales | east_sales |
|------------|------------|
| 500        | 500        |

(This matches our dataset totals:  
West = 200 + 300, East = 500)

---

### Alternative CASE equivalent (when FILTER is not supported)

```sql
SELECT
    SUM(CASE WHEN region = 'West' THEN amount ELSE 0 END) AS west_sales,
    SUM(CASE WHEN region = 'East' THEN amount ELSE 0 END) AS east_sales
FROM sales;
```

**Result: identical to FILTER.**


## 🔸 6. WINDOW FUNCTIONS — Concept + Examples + Results

Window functions let you compute values **across a set of rows**  
without collapsing them into a single row (unlike GROUP BY).

They use the `OVER (...)` clause to define the “window” of rows.

### 🧩 General syntax

```sql
function_name(expression) OVER (
  PARTITION BY partition_columns   -- optional
  ORDER BY sort_columns            -- optional
  ROWS BETWEEN ... AND ...         -- optional frame
)
```

- `PARTITION BY` → splits the data into independent groups (like GROUP BY, but **without** collapsing rows).
- `ORDER BY` → defines the order **inside each partition**.
- `ROWS BETWEEN ... AND ...` → defines exactly which rows around the current one are included in the calculation.

We use this sample table `sales`:

| region | amount | year |
|--------|--------|------|
| West   | 200    | 2023 |
| East   | 500    | 2023 |
| West   | 300    | 2024 |


---

### 6.1 `SUM() OVER` — Running total

```sql
SELECT region,
       amount,
       SUM(amount) OVER (ORDER BY amount) AS running_total
FROM sales;
```

**Explanation:**

- Rows are ordered by `amount` (ascending).
- `SUM` accumulates values row by row in this order.

**Result:**

| region | amount | running_total |
|--------|--------|---------------|
| West   | 200    | 200           |
| West   | 300    | 500           |
| East   | 500    | 1000          |


---

### 6.2 `AVG() OVER` — Running average

```sql
SELECT region,
       amount,
       AVG(amount) OVER (ORDER BY amount) AS running_avg
FROM sales;
```

**Result:**

| region | amount | running_avg |
|--------|--------|-------------|
| West   | 200    | 200.00      |
| West   | 300    | 250.00      |
| East   | 500    | 333.33      |


---

### 6.3 `LAG()` — Previous row value

```sql
SELECT region,
       amount,
       LAG(amount) OVER (ORDER BY amount) AS previous_amount
FROM sales;
```

**Explanation:**

- `LAG(amount)` looks at the previous row in the `ORDER BY amount` order.

**Result:**

| region | amount | previous_amount |
|--------|--------|-----------------|
| West   | 200    | NULL            |
| West   | 300    | 200             |
| East   | 500    | 300             |


---

### 6.4 `ROW_NUMBER()` — Unique index per row

```sql
SELECT region,
       amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num
FROM sales;
```

**Explanation:**

- Sort by `amount` descending.
- Assign 1, 2, 3, ... in that order.

**Result:**

| region | amount | row_num |
|--------|--------|---------|
| East   | 500    | 1       |
| West   | 300    | 2       |
| West   | 200    | 3       |


---

### 6.5 `RANK()` — Ranking with gaps

```sql
SELECT region,
       amount,
       RANK() OVER (ORDER BY amount DESC) AS rank_pos
FROM sales;
```

**Explanation:**

- Same sorting as `ROW_NUMBER()`.
- If there are ties, `RANK` gives **the same rank**, but **skips** the next number.

**Result (no ties here):**

| region | amount | rank_pos |
|--------|--------|----------|
| East   | 500    | 1        |
| West   | 300    | 2        |
| West   | 200    | 3        |


---

### 6.6 `DENSE_RANK()` — Ranking without gaps

```sql
SELECT region,
       amount,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_pos
FROM sales;
```

**Explanation:**

- Same as `RANK()`, but **does not skip** rank values when there are ties.

**Result (no ties here):**

| region | amount | dense_rank_pos |
|--------|--------|----------------|
| East   | 500    | 1              |
| West   | 300    | 2              |
| West   | 200    | 3              |


---

### 6.7 `PARTITION BY` — Restart the window per group

Example: running total **per region**.

```sql
SELECT region,
       year,
       amount,
       SUM(amount) OVER (
           PARTITION BY region
           ORDER BY year
       ) AS running_total_by_region
FROM sales;
```

**Explanation:**

- We create **one window per region**.
- Inside each region, rows are ordered by `year`.
- `SUM` restarts from zero for each region.

**Result:**

| region | year | amount | running_total_by_region |
|--------|------|--------|-------------------------|
| East   | 2023 | 500    | 500                     |
| West   | 2023 | 200    | 200                     |
| West   | 2024 | 300    | 500                     |


---

### 6.8 `ROWS BETWEEN … AND …` — Custom window frame

Define **exactly** which rows are used for each calculation  
around the current row.

Example: moving average using **previous + current + next** row.

```sql
SELECT region,
       amount,
       AVG(amount) OVER (
           ORDER BY amount
           ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
       ) AS moving_avg
FROM sales;
```

**Explanation:**

- For each row:
  - `1 PRECEDING` → include the previous row (if it exists),
  - `CURRENT ROW` → include itself,
  - `1 FOLLOWING` → include the next row (if it exists).

**Result (ordered by amount):**

| region | amount | moving_avg |
|--------|--------|------------|
| West   | 200    | 250.00     |  -- (200 + 300) / 2
| West   | 300    | 333.33     |  -- (200 + 300 + 500) / 3
| East   | 500    | 400.00     |  -- (300 + 500) / 2


---

### 6.9 Common frame keywords quick recap

- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`  
  → from the **first** row to the current row = classic running total.

- `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING`  
  → sliding window of 3 rows max (previous, current, next).

- `ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING`  
  → current row to the **end** (useful for “remaining” values).

## 🔸 7. CTE — Common Table Expressions (WITH)  
CTEs allow you to create **temporary named result sets** that you can reuse inside a query.

They make complex SQL queries:
- easier to read  
- easier to debug  
- easier to build step-by-step  

---

## 7.1 Basic CTE example

Goal: find customers with total purchases above 150.

```sql
WITH customer_totals AS (
    SELECT customer_id,
           SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT c.name,
       t.total_amount
FROM customer_totals t
JOIN customers c ON c.id = t.customer_id
WHERE total_amount > 150;
```

### Step 1 — CTE `customer_totals`
Created from `orders` table:

| customer_id | total_amount |
|-------------|--------------|
| 1           | 200          |   -- 120 + 80
| 2           | 500          |   -- only one order
| 3           | 200          |

### Step 2 — Main query joins customers + filters > 150

**Result:**

| name    | total_amount |
|---------|--------------|
| Alice   | 200          |
| Bob     | 500          |
| Charlie | 200          |


---

## 7.2 CTE with multiple steps
You can chain multiple CTEs.

```sql
WITH sales_per_year AS (
    SELECT year,
           SUM(amount) AS total_sales
    FROM sales
    GROUP BY year
),
best_year AS (
    SELECT year,
           total_sales,
           RANK() OVER (ORDER BY total_sales DESC) AS rank
    FROM sales_per_year
)
SELECT *
FROM best_year
WHERE rank = 1;
```

### Step 1 — `sales_per_year`

| year | total_sales |
|------|-------------|
| 2023 | 700         |  -- (200 + 500)
| 2024 | 300         |

### Step 2 — `best_year` (add ranking)

| year | total_sales | rank |
|------|-------------|------|
| 2023 | 700         | 1    |
| 2024 | 300         | 2    |

### Step 3 — Main query filters top rank

**Result:**

| year | total_sales | rank |
|------|-------------|------|
| 2023 | 700         | 1    |


---

## 7.3 CTE vs Subquery (Why use CTEs?)
A CTE is simply a **named subquery** that can be reused.

### Subquery version (hard to read)

```sql
SELECT *
FROM (
    SELECT year,
           SUM(amount) AS total_sales
    FROM sales
    GROUP BY year
) s
WHERE total_sales > 400;
```

### Same logic with CTE (clearer)

```sql
WITH s AS (
    SELECT year,
           SUM(amount) AS total_sales
    FROM sales
    GROUP BY year
)
SELECT *
FROM s
WHERE total_sales > 400;
```

**Result:**

| year | total_sales |
|------|-------------|
| 2023 | 700         |

---

## 7.4 Recursive CTE (optional, more advanced)
Used for:
- hierarchical data (employees, org charts)
- tree traversal
- graph algorithms
- generating sequences

Example: generate numbers from 1 to 5.

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 5
)
SELECT * FROM numbers;
```

**Result:**

| n |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |

