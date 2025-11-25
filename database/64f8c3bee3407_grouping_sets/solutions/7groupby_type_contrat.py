query = """
SELECT type_contrat, SUM(montant_rembourse) 
FROM df
GROUP BY type_contrat
"""
duckdb.sql(query)
