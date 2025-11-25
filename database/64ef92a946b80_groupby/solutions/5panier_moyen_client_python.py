(
    ventes
    .groupby("client")
    ["montant"].mean()
)
