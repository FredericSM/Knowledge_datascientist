query = f"""
WITH mean_sale AS
    (SELECT MEAN(montant) FROM ventes)

SELECT client, 
MEAN(montant) as total_sales
FROM ventes
GROUP BY CLIENT
HAVING total_sales > (SELECT * FROM mean_sale)
"""

duckdb.sql(query)
