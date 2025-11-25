query = """
SELECT * 
FROM stores_and_products
FULL OUTER JOIN df_products
USING (product_id)
"""

duckdb.query(query).df()
