query = """
SELECT name, department, 
CASE 
    WHEN department = 'SALES' THEN wage * 1.1
    WHEN department = 'HR' THEN wage * 1.05
    WHEN department = 'IT' THEN wage * 1.03
    ELSE wage
END as wage_with_raise
FROM wages
"""

duckdb.sql(query)
