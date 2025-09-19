# Data Visualization

Essential plotting techniques for data exploration and presentation.

## Files in this Section

- [`matplotlib_basics.py`](./matplotlib_basics.py) - Matplotlib fundamentals
- [`seaborn_examples.py`](./seaborn_examples.py) - Statistical plots with seaborn
- [`plotly_interactive.py`](./plotly_interactive.py) - Interactive visualizations
- [`visualization_best_practices.py`](./visualization_best_practices.py) - Design principles

## Quick Reference

### Matplotlib Basics
```python
import matplotlib.pyplot as plt
import numpy as np

# Basic line plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Title')
plt.legend()
plt.grid(True)
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].hist(data, bins=30)
axes[1, 1].bar(categories, values)
plt.tight_layout()
```

### Seaborn Statistical Plots
```python
import seaborn as sns

# Set style
sns.set_style("whitegrid")

# Distribution plots
sns.histplot(data, kde=True)
sns.boxplot(x='category', y='value', data=df)
sns.violinplot(x='category', y='value', data=df)

# Relationship plots
sns.scatterplot(x='x', y='y', hue='category', data=df)
sns.lineplot(x='x', y='y', hue='category', data=df)
sns.regplot(x='x', y='y', data=df)

# Categorical plots
sns.countplot(x='category', data=df)
sns.barplot(x='category', y='value', data=df)
```

### Common Plot Types

#### Distribution Analysis
```python
# Histogram
plt.hist(data, bins=30, alpha=0.7)

# Box plot
sns.boxplot(y=data)

# Density plot
sns.kdeplot(data)

# Q-Q plot
from scipy import stats
stats.probplot(data, dist="norm", plot=plt)
```

#### Correlation and Relationships
```python
# Correlation heatmap
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')

# Pair plot
sns.pairplot(df, hue='target')

# Scatter plot with regression line
sns.regplot(x='x', y='y', data=df)
```

#### Time Series
```python
# Time series plot
plt.plot(dates, values)
plt.xticks(rotation=45)

# Multiple time series
for column in df.columns:
    plt.plot(df.index, df[column], label=column)
plt.legend()
```

### Customization Tips
```python
# Color palettes
sns.color_palette("husl", 8)
sns.color_palette("Set2")

# Figure size and DPI
plt.figure(figsize=(12, 8), dpi=300)

# Save plots
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```