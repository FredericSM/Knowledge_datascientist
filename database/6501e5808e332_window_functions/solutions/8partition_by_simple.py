query = """
SELECT *,
AVG(wage) OVER(PARTITION BY department) AS mean_dpt_wage
FROM wages
ORDER BY department
"""
duckdb.sql(query).df()
