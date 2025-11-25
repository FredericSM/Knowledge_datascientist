# Essayez de déconstruire ce snippet ligne par ligne
# puis essayez de l'effacer et de le réécrire
(
    ventes_immo
    .groupby("neighborhood")
    ["price"].mean()
    .reset_index()
    .set_index("neighborhood")
    .T
)
