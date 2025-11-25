query = """
SELECT *,
AVG(visiteurs_count) OVER(
    PARTITION BY capteur_id, weekday
    ORDER BY Date
    ) AS avg_visitors_weekday
FROM df
ORDER BY capteur_id, weekday, date
"""
duckdb.sql(query).df().query("weekday == 7")

