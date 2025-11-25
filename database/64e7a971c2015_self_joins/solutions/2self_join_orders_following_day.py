query = """
SELECT customer_id,
ls.order_id as first_order, 
ls.date as date_first_order,
rs.order_id as second_order, 
rs.date as date_next_order,
FROM df_sales ls
INNER JOIN df_sales rs
USING (customer_id)
WHERE ls.order_id != rs.order_id 
AND date_next_order - date_first_order = 1
"""
duckdb.sql(query)
