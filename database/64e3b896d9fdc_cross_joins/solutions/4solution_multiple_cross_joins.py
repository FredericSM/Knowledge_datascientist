multiple_cross = """
SELECT * 
FROM stores
CROSS JOIN markets
CROSS JOIN months
CROSS JOIN dows
CROSS JOIN quarters
"""

duckdb.sql(multiple_cross)
