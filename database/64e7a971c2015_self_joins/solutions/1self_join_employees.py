query = """
SELECT * FROM 
df_employees le
LEFT JOIN df_employees re
ON le.manager_id = re.employee_id
"""

duckdb.sql(query)
