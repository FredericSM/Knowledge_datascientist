query = """
SELECT 
year,
SUM(population) FILTER(WHERE region = 'IDF') as 'IDF', 
SUM(population) AS total_pop,
IDF / total_pop,
FROM dpts_dfs
GROUP BY "year"
"""
duckdb.sql(query).df()
