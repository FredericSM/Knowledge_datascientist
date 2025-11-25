order_w_products = pd.merge(
    order_client,
    df_products,
    on='product_id',
    how='left'
)
order_w_products
