query = """
SELECT type_contrat, type_acte, SUM(montant_rembourse) 
FROM df
GROUP BY GROUPING SETS
(type_contrat, type_acte)
-- Notez la difference avec ((type_contrat, type_acte))
ORDER BY type_contrat, type_acte
"""
duckdb.sql(query)
