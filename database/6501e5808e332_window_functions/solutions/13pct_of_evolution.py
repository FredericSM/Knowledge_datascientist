shuffled = capteurs.sample(len(capteurs))
query = """
SELECT *,
LAG(visiteurs_count) OVER(
    PARTITION BY weekday 
    ORDER BY date
    ) AS lag_visiteurs_count,
(visiteurs_count - lag_visiteurs_count) / lag_visiteurs_count as pct_change
FROM shuffled
"""
df = duckdb.sql(query).df()
df
