query = """
SELECT *, 
AVG(visiteurs_count) OVER(ORDER BY date) AS total_visiteurs,
FROM df
ORDER BY date
"""
duckdb.sql(query).df().head()
