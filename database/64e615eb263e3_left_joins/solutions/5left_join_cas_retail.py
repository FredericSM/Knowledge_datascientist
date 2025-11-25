ventes_categories_univers = (
    ventes_df
    .merge(categorie_produit, on="produit_id", how="left")
    .merge(univers_categorie, on="categorie_id", how="left")
)

mask = (ventes_categories_univers["univers_id"].isnull())
ventes_categories_univers[mask]
