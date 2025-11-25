pd.merge(
    stores_and_products,
    df_products,
    on='product_id',
    how='outer'
)


