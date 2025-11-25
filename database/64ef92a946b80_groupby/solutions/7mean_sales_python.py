# Avec une subquery
query = f"""
SELECT client, 
MEAN(montant) as mean_sales
FROM ventes
GROUP BY CLIENT
HAVING mean_sales > 
(SELECT MEAN(montant) FROM ventes)
"""

duckdb.sql(query)
