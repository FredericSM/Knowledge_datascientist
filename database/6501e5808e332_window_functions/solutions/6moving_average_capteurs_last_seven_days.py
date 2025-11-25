query = """
SELECT *,
AVG(visiteurs_count) OVER(
    ORDER BY DATE 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
) AS seven_daysmoving_average
FROM capteurs
"""
duckdb.sql(query).df().head(10)
