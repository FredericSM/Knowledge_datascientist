query = """
SELECT * 
FROM detailed_order
LEFT JOIN df_store_products
USING (store_id)
"""

duckdb.query(query)
