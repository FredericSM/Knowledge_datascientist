query = """
SELECT year, region, SUM(population) 
FROM dfpop
GROUP BY 
GROUPING SETS ((year, region), year)
"""
duckdb.sql(query)
