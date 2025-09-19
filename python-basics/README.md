# Python Basics for Data Science

Essential Python knowledge every data scientist needs.

## Environment Setup

### Virtual Environment Creation
```bash
# Using venv
python -m venv datascience_env
source datascience_env/bin/activate  # Linux/Mac
datascience_env\Scripts\activate     # Windows

# Using conda
conda create -n datascience python=3.9
conda activate datascience
```

### Essential Libraries Installation
```bash
pip install numpy pandas scikit-learn matplotlib seaborn jupyter plotly
# Or using conda
conda install numpy pandas scikit-learn matplotlib seaborn jupyter plotly
```

## Files in this Section

- [`essential_imports.py`](./essential_imports.py) - Standard imports for data science
- [`environment_setup.py`](./environment_setup.py) - Environment configuration examples
- [`common_patterns.py`](./common_patterns.py) - Useful Python patterns for data science
- [`performance_tips.py`](./performance_tips.py) - Performance optimization techniques

## Key Concepts

### 1. Import Conventions
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
```

### 2. Jupyter Notebook Magic Commands
```python
%matplotlib inline
%load_ext autoreload
%autoreload 2
```

### 3. Environment Information
```python
import sys
print(f"Python version: {sys.version}")
print(f"Numpy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
```