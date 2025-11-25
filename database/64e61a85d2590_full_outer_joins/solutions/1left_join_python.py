stores_and_products = pd.merge(
    detailed_order,
    df_store_products,
    on='store_id',
    how='left'
)
stores_and_products
