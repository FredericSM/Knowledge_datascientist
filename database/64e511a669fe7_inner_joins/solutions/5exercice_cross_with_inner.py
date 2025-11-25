food_items["id"] = beverages["id"] = [1, 1, 1]
cross_join_query = """
SELECT * FROM beverages
INNER JOIN food_items
USING (id)
"""
duckdb.sql(cross_join_query).df()
