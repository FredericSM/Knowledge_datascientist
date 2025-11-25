# 🦆 SQL Cheat Sheet

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

## 🔸 2. JOINS

### `CROSS JOIN`
Returns the Cartesian product of two tables (all possible combinations).  
```sql
SELECT *
FROM customers CROSS JOIN products;
```
### `INNER JOIN`
Returns only rows with matching values in both tables.
```sql
SELECT *
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;
```
### `LEFT JOIN`
Keeps all rows from the left table, and matches from the right (NULL if missing).
```sql
SELECT *
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;
```
### `FULL OUTER JOIN`
Returns all rows from both tables, filling NULLs where there’s no match.
```sql
SELECT *
FROM customers c
FULL OUTER JOIN orders o ON c.id = o.customer_id;
```
### `SELF JOIN`
Joins a table with itself (useful for hierarchical or comparative queries).
```sql
SELECT e1.id, e2.name AS manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.id;
```


## 🔸 3. FILTERING CLAUSES (CONDITIONS)
### `WHERE`
Filters rows before aggregation.
Used to exclude raw data before grouping.
```sql
SELECT *
FROM sales
WHERE region = 'West';
```
### `HAVING`
Filters rows after aggregation (GROUP BY).
Used with aggregate functions.
```sql
SELECT region, SUM(amount)
FROM sales
GROUP BY region
HAVING SUM(amount) > 10000;
```
### `QUALIFY`
Filters rows after window functions (OVER()),
acting like a WHERE for computed windows.
```sql
SELECT *,
       ROW_NUMBER() OVER(PARTITION BY region ORDER BY amount DESC) AS rank
FROM sales
QUALIFY rank = 1;
```
⚠️ Not supported by all SQL engines — but available in DuckDB.

## 🔸 4. AGGREGATION & GROUPING
### `GROUP BY`
Groups rows to perform aggregations.
```sql
SELECT region, SUM(amount)
FROM sales
GROUP BY region;
```
### `GROUPING SETS`
Allows multiple grouping combinations in one query.
```sql
SELECT COALESCE(region, 'Total') AS region,
       COALESCE(year, 'All') AS year,
       SUM(amount)
FROM sales
GROUP BY GROUPING SETS ((region), (year), ());
```
### `ROLLUP`
Creates hierarchical subtotals (from detailed to global).
```sql
SELECT year, region, department, SUM(amount)
FROM sales
GROUP BY ROLLUP (year, region, department);
```
### `CUBE`
Generates all combinations of grouping columns.
```sql
SELECT year, region, department, SUM(amount)
FROM sales
GROUP BY CUBE (year, region, department);
```
### `HAVING year IS NOT NULL`
Used to remove the “total” rows created by ROLLUP or CUBE when they’re too general.

## 🔸 5. EXPRESSIONS & UTILITY FUNCTIONS
### `COALESCE(column, 'value')`
Returns the first non-null value among its arguments.
```sql
SELECT COALESCE(region, 'Unknown') AS clean_region
FROM sales;
```
### `CAST(expression AS type)`
Converts a value from one data type to another.
```sql
SELECT CAST(price AS DOUBLE)
FROM products;
```
### `CASE WHEN`
Conditional expression to categorize or compute values.
```sql
SELECT
  CASE
    WHEN amount > 1000 THEN 'Large'
    WHEN amount > 100  THEN 'Medium'
    ELSE 'Small'
  END AS customer_size
FROM customers;
```
### `FILTER (WHERE …)`
Applies a condition inside an aggregate function.
```sql
SELECT
  SUM(amount) FILTER (WHERE region = 'West') AS west_sales
FROM sales;
```
➡️ If not supported, use a CASE WHEN equivalent:
```sql
SELECT
  SUM(CASE WHEN region = 'West' THEN amount ELSE 0 END) AS west_sales
FROM sales;
```

## 🔸 6. WINDOW FUNCTIONS
### Concept
Window functions compute aggregates without collapsing rows —
they act over a “window” of data defined by `OVER()`.  
Syntax:
```sql
function() OVER (PARTITION BY ... ORDER BY ...)
```
### `SUM() OVER()`
Running or moving total.
```sql
SELECT item, SUM(weight) OVER(ORDER BY item DESC) AS total_weight
FROM products;
```
### `AVG() OVER()`
Running or moving average.
```sql
SELECT item, AVG(weight) OVER(ORDER BY item DESC) AS avg_weight
FROM products;
```
### `LAG()`
Returns the previous row’s value in the same window.
```sql
SELECT item, weight, LAG(weight) OVER(ORDER BY item) AS prev_weight
FROM products;
```
### `ROW_NUMBER()`
Assigns a unique sequential number to each row.
```sql
SELECT item, ROW_NUMBER() OVER(ORDER BY sales DESC) AS row_num
FROM products;
```
### `RANK()`
Ranks with gaps for ties.
```sql
SELECT item, RANK() OVER(ORDER BY sales DESC) AS rank_pos
FROM products;
```
### `DENSE_RANK()`
Ranks without gaps for ties.
```sql
SELECT item, DENSE_RANK() OVER(ORDER BY sales DESC) AS dense_rank_pos
FROM products;
```
### `PARTITION BY`
Divides data into subgroups (independent windows).
```sql
SELECT region, item,
       SUM(amount) OVER(PARTITION BY region) AS regional_sales
FROM sales;
```
### `ROWS BETWEEN … AND …`
Defines the range of rows around the current one.
```sql
AVG(weight) OVER(
  ORDER BY item
  ROWS BETWEEN 3 PRECEDING AND 2 FOLLOWING
);
```
- 3 PRECEDING → three rows before
- 2 FOLLOWING → two rows after
- CURRENT ROW → the current row
## 🔸 7. CTE — Common Table Expressions
### `WITH`
Creates a temporary result set used within the main query.
Improves readability and modularity.
```sql
WITH top_customers AS (
  SELECT customer_id, SUM(amount) AS total
  FROM sales
  GROUP BY customer_id
)
SELECT *
FROM top_customers
WHERE total > 10000;
```
