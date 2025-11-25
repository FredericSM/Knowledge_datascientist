query = """
SELECT *,
DENSE_RANK() OVER(
    PARTITION BY sex 
    ORDER BY wage DESC) AS index
FROM wages
"""
duckdb.sql(query).df().head(13)
