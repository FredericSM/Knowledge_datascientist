query = """
SELECT * FROM merged_df ldf
INNER JOIN merged_df rdf
USING (meeting_id)
WHERE ldf.person_name == 'Benjamin'
AND rdf.person_name != 'Benjamin'
"""

duckdb.sql(query)
