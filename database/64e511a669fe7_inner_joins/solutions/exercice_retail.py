(
    ventes_df
    .merge(categorie_produit, on="produit_id", how="inner")
    .merge(univers_categorie, on="categorie_id", how="inner")
)
