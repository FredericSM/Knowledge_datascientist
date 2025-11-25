# %%timeit (843 µs ± 14.1 µs per loop)
query = """
WITH total_sales AS (
SELECT store_id, SUM(amount) as total_sales
FROM df
GROUP BY
store_id
),

pct_sales AS (
SELECT *, amount/total_sales AS pct_sales 
FROM df
LEFT JOIN total_sales
USING (store_id)
)

SELECT store_id, sum(amount), total_sales, SUM(pct_sales) AS product_pct_of_sales
FROM pct_sales
WHERE product_name = 'redbull'
GROUP BY store_id, amount, total_sales
"""
duckdb.sql(query)
