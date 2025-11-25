query = """
SELECT *,
ROW_NUMBER() OVER(
    PARTITION BY department
    ORDER BY wage DESC
    ) AS index
FROM wages
LIMIT 10
"""
duckdb.sql(query).df()
