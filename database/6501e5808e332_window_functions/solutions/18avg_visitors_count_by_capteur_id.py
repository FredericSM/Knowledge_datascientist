query = """
SELECT *,
AVG(visiteurs_count) OVER(
    PARTITION BY capteur_id 
    ORDER BY Date
    ) AS avg_visitors_weekday
FROM df
WHERE weekday = 7
ORDER BY capteur_id, date
"""
duckdb.sql(query).df()
