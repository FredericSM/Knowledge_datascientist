hours = '''
hour
08
09
10
11
12
'''

quarters = '''
quarter
00
15
30
45
'''

hours = pd.read_csv(io.StringIO(hours))
quarters = pd.read_csv(io.StringIO(quarters))

# python
display(hours.join(quarters, how="cross"))


# sql
query = """
SELECT * FROM hours
CROSS JOIN quarters
ORDER BY HOUR, QUARTER
"""

duckdb.sql(query)
