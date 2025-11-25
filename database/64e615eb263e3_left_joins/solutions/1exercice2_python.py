order_client = pd.merge(
    df_customers,
    detailed_order,
    on='customer_id',
    how='left'
)
order_client
