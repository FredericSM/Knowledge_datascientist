query = """
SELECT date, daily_sales,
AVG(daily_sales) OVER(
    ORDER BY date 
    ROWS BETWEEN 2 PRECEDING and 2 FOLLOWING)
    AS moving_average,
from df
"""
duckdb.sql(query).df().head(7)
