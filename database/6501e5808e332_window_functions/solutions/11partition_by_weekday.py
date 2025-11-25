query = """
SELECT *,
AVG(visiteurs_count) OVER(
    PARTITION BY weekday 
    ROWS BETWEEN 6 PRECEDING 
    AND CURRENT ROW
    ) AS avg_last_seven_same_days,
avg_last_seven_same_days * 0.8 as threshold
FROM capteurs
"""
df = duckdb.sql(query).df()
df
