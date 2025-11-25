(
    merged_df
    .drop("duration_minutes", axis=1)
    .merge(
        merged_df,
        on="meeting_id",
        how="inner",
        suffixes=["_L", "_R"]
    )
    .query("person_name_L == 'Benjamin' and person_name_R != 'Benjamin'")
)#.groupby("person_name_R")["duration_minutes"].mean().plot(kind="bar")
