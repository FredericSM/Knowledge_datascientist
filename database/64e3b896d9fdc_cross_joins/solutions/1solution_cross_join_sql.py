cross_join_query = """
SELECT * FROM size
CROSS JOIN trademark
"""
duckdb.sql(cross_join_query)
