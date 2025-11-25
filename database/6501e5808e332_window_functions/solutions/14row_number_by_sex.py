query = """
SELECT *,
ROW_NUMBER() OVER(
    PARTITION BY sex
    ) AS index
FROM wages
"""
duckdb.sql(query).df().head(11)
