query = """
SELECT neighborhood, MEAN(price) 
FROM ventes_immo
GROUP BY neighborhood
"""

duckdb.sql(query)
