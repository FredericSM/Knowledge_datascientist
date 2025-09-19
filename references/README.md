# Quick References and Cheat Sheets

Fast lookup guides for common data science tasks.

## Python Data Science Cheat Sheet

### Essential Imports
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
```

### Pandas Quick Reference
```python
# DataFrame creation
df = pd.DataFrame(data)
df = pd.read_csv('file.csv')

# Selection
df['col']                    # Single column
df[['col1', 'col2']]        # Multiple columns
df.loc[row_indexer]         # Label-based selection
df.iloc[row_indexer]        # Integer-based selection

# Filtering
df[df['col'] > 5]           # Conditional filtering
df[df['col'].isin(['A','B'])] # Filter by values
df.query('col1 > 5 & col2 == "A"') # Query syntax

# Grouping and aggregation
df.groupby('col').mean()    # Group by and aggregate
df.groupby('col').agg({'col2': 'sum', 'col3': 'mean'})

# Missing data
df.isna()                   # Check for missing values
df.dropna()                 # Drop missing values
df.fillna(value)            # Fill missing values

# Data types
df.dtypes                   # Check data types
df.astype({'col': 'int64'}) # Convert data types
```

### NumPy Quick Reference
```python
# Array creation
np.array([1, 2, 3])         # From list
np.zeros(shape)             # Array of zeros
np.ones(shape)              # Array of ones
np.random.randn(n)          # Random normal distribution

# Array operations
arr.shape                   # Shape of array
arr.reshape(new_shape)      # Reshape array
arr.mean()                  # Mean
arr.std()                   # Standard deviation
arr.sum()                   # Sum
np.concatenate([arr1, arr2]) # Concatenate arrays
```

### Matplotlib Quick Reference
```python
# Basic plotting
plt.figure(figsize=(10, 6)) # Set figure size
plt.plot(x, y)              # Line plot
plt.scatter(x, y)           # Scatter plot
plt.hist(data, bins=30)     # Histogram
plt.bar(categories, values) # Bar plot

# Customization
plt.xlabel('X Label')       # X-axis label
plt.ylabel('Y Label')       # Y-axis label
plt.title('Title')          # Plot title
plt.legend()                # Show legend
plt.grid(True)              # Show grid
plt.show()                  # Display plot
```

### Scikit-learn Quick Reference
```python
# Data splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Classification
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

# Regression
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)
predictions = reg.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_true, y_pred)
report = classification_report(y_true, y_pred)
```

## Common Data Science Tasks

### Data Loading and Saving
```python
# Reading files
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')
df = pd.read_parquet('data.parquet')

# Writing files
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json')
df.to_parquet('output.parquet')
```

### Data Exploration
```python
df.info()                   # Dataset info
df.describe()               # Statistical summary
df.shape                    # Dimensions
df.columns                  # Column names
df.head()                   # First 5 rows
df.tail()                   # Last 5 rows
df['col'].value_counts()    # Value counts
df.corr()                   # Correlation matrix
```

### Data Cleaning
```python
# Remove duplicates
df.drop_duplicates()

# Handle missing values
df.dropna()                 # Remove missing values
df.fillna(0)                # Fill with zero
df.fillna(method='ffill')   # Forward fill
df.fillna(df.mean())        # Fill with mean

# String operations
df['col'].str.lower()       # Lowercase
df['col'].str.replace('old', 'new') # Replace text
df['col'].str.contains('pattern') # Pattern matching
```

## Statistical Tests Cheat Sheet

### Descriptive Statistics
```python
import scipy.stats as stats

# Central tendency
np.mean(data)               # Mean
np.median(data)             # Median
stats.mode(data)            # Mode

# Spread
np.std(data)                # Standard deviation
np.var(data)                # Variance
np.percentile(data, [25, 75]) # Quartiles
```

### Hypothesis Testing
```python
# T-test
stats.ttest_1samp(data, popmean) # One-sample t-test
stats.ttest_ind(group1, group2)  # Independent t-test
stats.ttest_rel(before, after)   # Paired t-test

# Chi-square test
stats.chi2_contingency(crosstab) # Chi-square test

# ANOVA
stats.f_oneway(group1, group2, group3) # One-way ANOVA
```

## Git Cheat Sheet

```bash
# Repository setup
git init                    # Initialize repository
git clone <url>             # Clone repository
git remote add origin <url> # Add remote

# Basic workflow
git status                  # Check status
git add <file>              # Stage file
git add .                   # Stage all files
git commit -m "message"     # Commit changes
git push                    # Push to remote
git pull                    # Pull from remote

# Branching
git branch                  # List branches
git branch <name>           # Create branch
git checkout <branch>       # Switch branch
git checkout -b <branch>    # Create and switch
git merge <branch>          # Merge branch
git branch -d <branch>      # Delete branch

# History
git log                     # View commit history
git diff                    # View changes
git show <commit>           # Show commit details
```

## Troubleshooting Guide

### Common Error Solutions

#### ModuleNotFoundError
```bash
# Solution 1: Install the module
pip install module_name

# Solution 2: Check Python path
import sys
print(sys.path)

# Solution 3: Virtual environment
conda activate your_env
```

#### Memory Errors
```python
# Solution 1: Read in chunks
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)

# Solution 2: Optimize data types
df = df.astype({'int_col': 'int32', 'float_col': 'float32'})

# Solution 3: Use efficient formats
df.to_parquet('file.parquet')  # More efficient than CSV
```

#### Slow Performance
```python
# Solution 1: Vectorize operations
df['new_col'] = df['col1'] * df['col2']  # Instead of loops

# Solution 2: Use built-in functions
df.groupby('col').sum()  # Instead of manual aggregation

# Solution 3: Index optimization
df.set_index('col')  # For frequent lookups
```

### Best Practices

1. **Always use version control (Git)**
2. **Create virtual environments for projects**
3. **Document your code and analysis**
4. **Validate data before analysis**
5. **Use meaningful variable names**
6. **Save intermediate results**
7. **Test your code with small datasets first**
8. **Keep raw data separate from processed data**