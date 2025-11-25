# %%timeit (455 µs ± 8.74 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each))
query = """
WITH salary_range AS (
  SELECT 
    department, 
    wage, 
    CASE 
    WHEN wage <= 50000 THEN 'Low' 
    WHEN wage < 90000 THEN 'Medium' 
    ELSE 'High' 
    END AS salary_range, 
  FROM 
    wages
) 

SELECT 
  department, 
  salary_range, 
  AVG(wage) AS average_salary,
FROM 
  salary_range 
group by 
  department, 
  salary_range

"""
duckdb.sql(query)
