query = """
SELECT *, 
SUM(visiteurs_count) OVER() AS total_visiteurs,
FROM df
ORDER BY weekday
"""
duckdb.sql(query).df().head(10)
