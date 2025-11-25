query = """
SELECT type_contrat, type_acte, SUM(montant_rembourse) 
FROM df
GROUP BY CUBE
(type_contrat, type_acte)
ORDER BY type_contrat, type_acte
"""
duckdb.sql(query).df()
