query = """
SELECT df_customers.customer_id,
customer_name,
order_id,
product_id,
quantity
FROM df_customers
INNER JOIN detailed_order
on df_customers.customer_id = detailed_order.customer_id
"""

duckdb.query(query).df()
