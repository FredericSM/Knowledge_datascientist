# mouhahahahaha
# *evil laugh*

query = """
______ * 
____ commande_client cc
____ ____ df_products products
__ cc.product_id = products.product_id
"""

duckdb.query(query).df()
