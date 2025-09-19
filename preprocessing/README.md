# Data Preprocessing Techniques

Essential data preprocessing methods for machine learning readiness.

## Files in this Section

- [`feature_scaling.py`](./feature_scaling.py) - Feature scaling and normalization techniques
- [`encoding_categorical.py`](./encoding_categorical.py) - Categorical variable encoding
- [`feature_selection.py`](./feature_selection.py) - Feature selection methods
- [`outlier_detection.py`](./outlier_detection.py) - Outlier detection and treatment

## Quick Reference

### Feature Scaling
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Standard scaling (z-score normalization)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Min-max scaling (0-1 normalization)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Robust scaling (median and IQR)
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

### Categorical Encoding
```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

# Label encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# One-hot encoding
encoder = OneHotEncoder(sparse=False)
X_encoded = encoder.fit_transform(X)

# Pandas get_dummies
X_encoded = pd.get_dummies(X, columns=['categorical_column'])
```

### Handling Missing Values
```python
from sklearn.impute import SimpleImputer, KNNImputer

# Simple imputation
imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent'
X_imputed = imputer.fit_transform(X)

# KNN imputation
imputer = KNNImputer(n_neighbors=5)
X_imputed = imputer.fit_transform(X)
```

### Outlier Detection
```python
from sklearn.ensemble import IsolationForest
from scipy import stats

# Z-score method
z_scores = np.abs(stats.zscore(data))
outliers = z_scores > 3

# IQR method
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
outliers = (data < Q1 - 1.5*IQR) | (data > Q3 + 1.5*IQR)

# Isolation Forest
iso_forest = IsolationForest(contamination=0.1)
outliers = iso_forest.fit_predict(X) == -1
```

### Feature Selection
```python
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# Univariate selection
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Recursive feature elimination
rf = RandomForestClassifier()
rfe = RFE(rf, n_features_to_select=10)
X_selected = rfe.fit_transform(X, y)

# Feature importance from tree-based models
rf.fit(X, y)
important_features = rf.feature_importances_ > 0.01
X_selected = X[:, important_features]
```