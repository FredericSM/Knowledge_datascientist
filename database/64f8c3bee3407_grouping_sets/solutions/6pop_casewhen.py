query = """
SELECT 
year,
SUM(
    CASE 
    WHEN region = 'IDF' THEN population 
    END
) AS 'IDF', 
SUM(population) AS total_pop,
IDF / total_pop,
FROM dpts_dfs
GROUP BY "year"
"""
duckdb.sql(query).df()
