query = """
SELECT *,
ROW_NUMBER() OVER(
    PARTITION BY sex
    ORDER BY wage DESC) 
AS index
FROM wages
LIMIT 10 
"""
duckdb.sql(query).df().head(11)
