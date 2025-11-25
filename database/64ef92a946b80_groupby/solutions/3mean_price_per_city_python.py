(
    appt_nord
    .groupby("Commune")
    ["valeur_fonciere"].mean()
    .astype(int)
)
