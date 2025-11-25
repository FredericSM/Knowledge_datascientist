order_client = pd.merge(
    df_customers,
    detailed_order,
    on='customer_id',
    how='inner'
)
order_client
