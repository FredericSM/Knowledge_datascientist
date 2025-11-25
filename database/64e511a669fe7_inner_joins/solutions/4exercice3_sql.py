query = """
SELECT * 
FROM order_client cc
INNER JOIN df_products products
on cc.product_id = products.product_id
"""

duckdb.query(query).df()
