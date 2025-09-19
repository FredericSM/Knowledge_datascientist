# Statistical Analysis

Essential statistical methods and tests for data science.

## Files in this Section

- [`descriptive_statistics.py`](./descriptive_statistics.py) - Descriptive statistics and summaries
- [`hypothesis_testing.py`](./hypothesis_testing.py) - Statistical hypothesis tests
- [`correlation_analysis.py`](./correlation_analysis.py) - Correlation and association analysis
- [`probability_distributions.py`](./probability_distributions.py) - Working with probability distributions

## Quick Reference

### Descriptive Statistics
```python
import numpy as np
import pandas as pd
from scipy import stats

# Central tendency
np.mean(data)               # Mean
np.median(data)             # Median
stats.mode(data)            # Mode

# Spread
np.std(data)                # Standard deviation
np.var(data)                # Variance
np.ptp(data)                # Range (peak-to-peak)
stats.iqr(data)             # Interquartile range

# Shape
stats.skew(data)            # Skewness
stats.kurtosis(data)        # Kurtosis

# Percentiles
np.percentile(data, [25, 50, 75])  # Quartiles
np.quantile(data, [0.25, 0.5, 0.75])  # Quantiles
```

### Hypothesis Testing
```python
from scipy import stats

# One-sample tests
stats.ttest_1samp(data, popmean)     # One-sample t-test
stats.wilcoxon(data - popmean)       # Wilcoxon signed-rank test

# Two-sample tests
stats.ttest_ind(group1, group2)      # Independent t-test
stats.mannwhitneyu(group1, group2)   # Mann-Whitney U test
stats.ttest_rel(before, after)       # Paired t-test

# Multiple groups
stats.f_oneway(group1, group2, group3)  # One-way ANOVA
stats.kruskal(group1, group2, group3)   # Kruskal-Wallis test
```

### Correlation Analysis
```python
# Pearson correlation
r, p_value = stats.pearsonr(x, y)

# Spearman correlation
rho, p_value = stats.spearmanr(x, y)

# Kendall's tau
tau, p_value = stats.kendalltau(x, y)

# Correlation matrix
df.corr()                    # Pearson correlation matrix
df.corr(method='spearman')   # Spearman correlation matrix
```

### Chi-Square Tests
```python
# Chi-square test of independence
chi2, p, dof, expected = stats.chi2_contingency(crosstab)

# Chi-square goodness of fit
chi2, p = stats.chisquare(observed, expected)
```

### Normality Tests
```python
# Shapiro-Wilk test
stat, p = stats.shapiro(data)

# Kolmogorov-Smirnov test
stat, p = stats.kstest(data, 'norm')

# Anderson-Darling test
stat, critical_values, significance_level = stats.anderson(data)
```

### Confidence Intervals
```python
# Confidence interval for mean
mean = np.mean(data)
sem = stats.sem(data)  # Standard error of mean
ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)

# Bootstrap confidence interval
from scipy.stats import bootstrap
rng = np.random.default_rng()
bootstrap_ci = bootstrap((data,), np.mean, 
                        n_resamples=1000, 
                        confidence_level=0.95,
                        random_state=rng)
```

### Effect Size
```python
# Cohen's d (for t-tests)
def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    pooled_std = np.sqrt(((n1-1)*np.var(group1) + (n2-1)*np.var(group2)) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

# Eta-squared (for ANOVA)
def eta_squared(groups):
    # Calculate between-group and within-group variance
    # Implementation depends on specific ANOVA results
    pass
```