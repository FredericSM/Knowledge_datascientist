shuffled = capteurs.sample(len(capteurs))
query = """
SELECT *,
AVG(visiteurs_count) OVER(
    PARTITION BY weekday 
    ORDER BY date
    ROWS BETWEEN 6 PRECEDING 
    AND CURRENT ROW
    ) AS avg_last_seven_same_days,
avg_last_seven_same_days * 0.8 as threshold
FROM shuffled
WHERE weekday = 7
"""
df = duckdb.sql(query).df()
df
