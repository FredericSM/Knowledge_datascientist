query = """
SELECT type_contrat AS typologie,
SUM(montant_rembourse) 
FROM df
GROUP BY type_contrat

UNION

SELECT type_acte AS typologie, 
SUM(montant_rembourse) 
FROM df
GROUP BY type_acte
"""
duckdb.sql(query)
