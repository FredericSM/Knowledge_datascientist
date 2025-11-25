query = """
SELECT  SUM(visiteurs_count)  AS total_visiteurs,
FROM df
"""
duckdb.sql(query).df()
