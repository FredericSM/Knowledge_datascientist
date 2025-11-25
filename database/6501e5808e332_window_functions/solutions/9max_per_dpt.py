query = """
SELECT *,
MAX(wage) OVER(PARTITION BY department) AS max_dpt_wage,
wage >= max_dpt_wage AS is_max
FROM wages
ORDER BY department
"""
duckdb.sql(query).df()
