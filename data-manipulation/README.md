# Data Manipulation with Pandas

Essential pandas operations for data cleaning, transformation, and analysis.

## Files in this Section

- [`pandas_basics.py`](./pandas_basics.py) - Basic pandas operations
- [`data_cleaning.py`](./data_cleaning.py) - Data cleaning techniques
- [`groupby_operations.py`](./groupby_operations.py) - GroupBy operations and aggregations
- [`merging_joining.py`](./merging_joining.py) - Merging and joining datasets
- [`time_series.py`](./time_series.py) - Time series data manipulation

## Quick Reference

### DataFrame Creation
```python
import pandas as pd
import numpy as np

# From dictionary
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': ['a', 'b', 'c', 'd']
})

# From CSV
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', index_col=0, parse_dates=['date'])
```

### Basic Operations
```python
# Info and shape
df.info()
df.shape
df.head()
df.tail()
df.describe()

# Selection
df['column']
df[['col1', 'col2']]
df.loc[df['col'] > 5]
df.iloc[0:5, 1:3]

# Filtering
df[df['column'] > 5]
df[df['column'].isin(['A', 'B'])]
df[df['column'].str.contains('pattern')]
```

### Data Cleaning
```python
# Missing values
df.isna()
df.dropna()
df.fillna(value)
df.fillna(method='ffill')

# Duplicates
df.duplicated()
df.drop_duplicates()

# Data types
df.dtypes
df.astype({'column': 'int64'})
pd.to_datetime(df['date'])
```

### Transformations
```python
# Apply functions
df['new_col'] = df['old_col'].apply(lambda x: x * 2)
df.apply(function, axis=1)

# String operations
df['col'].str.lower()
df['col'].str.replace('old', 'new')
df['col'].str.extract('(pattern)')

# Groupby
df.groupby('column').mean()
df.groupby(['col1', 'col2']).agg({'col3': 'sum', 'col4': 'mean'})
```