# %%timeit (514 µs ± 5.71 µs per loop)
# On peut retirer le groupby pour avoir la somme globale
query = """
WITH total_revenue AS(
SELECT discount_code, CASE
            WHEN discount_code = 'DISCOUNT10' THEN quantity * price_per_unit * 0.9
            WHEN discount_code = 'DISCOUNT20' THEN quantity * price_per_unit * 0.8
            ELSE quantity * price_per_unit
        END as total_revenue
FROM df)

SELECT SUM(total_revenue) 
FROM
    total_revenue
GROUP BY 
    discount_code
""" 
duckdb.query(query)
