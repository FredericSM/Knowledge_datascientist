query = """
WITH max_salaries_per_dpt AS (
    SELECT *,
    MAX(wage) OVER(PARTITION BY department) AS max_dpt_wage,
    wage >= max_dpt_wage AS max_salary,
    FROM wages
    -- QUALIFY max_salary = False
    ORDER BY department
)


SELECT *,
MAX(wage) OVER(PARTITION BY department) AS max_dpt_wage
FROM max_salaries_per_dpt
WHERE max_salary = False
"""
duckdb.sql(query).df()
