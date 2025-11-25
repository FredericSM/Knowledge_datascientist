# %%timeit (507 µs ± 6.31 µs per loop)
# On peut retirer le groupby pour avoir la somme globale
query = """
SELECT
    SUM(
        CASE
            WHEN discount_code = 'DISCOUNT10' THEN quantity * price_per_unit * 0.9
            WHEN discount_code = 'DISCOUNT20' THEN quantity * price_per_unit * 0.8
            ELSE quantity * price_per_unit
        END
    ) AS total_revenue
FROM
    df
GROUP BY
    discount_code
""" 
duckdb.query(query)
