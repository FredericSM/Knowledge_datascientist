query = """
SELECT region, year, SUM(population) 
FROM dpts_dfs
GROUP BY 
GROUPING SETS ((year, region), year)
ORDER BY region, year
"""
duckdb.sql(query).df()
