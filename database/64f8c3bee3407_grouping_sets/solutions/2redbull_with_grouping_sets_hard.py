# %%timeit (862 µs ± 18.5 µs per loop)
query = """
WITH sales_totals AS (
    SELECT store_id, 
    COALESCE(product_name, 'tout_le_magasin') AS product_name,
    SUM(amount) as sum_amount 
    FROM df
    GROUP BY 
    GROUPING SETS ((store_id, product_name), store_id)
    ORDER BY store_id
)

SELECT ls.store_id,
ls.product_name AS l_product_name, 
rs.product_name AS r_product_name, 
ls.sum_amount as product_sum_amount,
rs.sum_amount as store_sum_amount, 
product_sum_amount / store_sum_amount as product_pct
FROM sales_totals ls 
INNER JOIN sales_totals rs
USING (store_id)
WHERE ls.product_name = 'redbull' AND rs.product_name = 'tout_le_magasin'
ORDER BY store_id, l_product_name
"""
duckdb.sql(query).df()
