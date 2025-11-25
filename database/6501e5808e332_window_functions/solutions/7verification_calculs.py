query = """
SELECT *,
SUM(visiteurs_count) OVER(
    ORDER BY DATE 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS seven_days_running_total,
COUNT(*) OVER(
    ORDER BY DATE 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS seven_days_moving_count,
seven_days_running_total / seven_days_moving_count AS verif,
AVG(visiteurs_count) OVER(
    ORDER BY DATE 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS seven_days_moving_average
FROM capteurs
"""
duckdb.sql(query).df().head(10)
