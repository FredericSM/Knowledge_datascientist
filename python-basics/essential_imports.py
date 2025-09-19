"""
Essential imports for data science projects.
Standard imports that should be at the beginning of most data science notebooks/scripts.
"""

# Data manipulation and analysis
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Machine Learning
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression

# Statistical analysis
from scipy import stats
from scipy.stats import chi2_contingency, ttest_ind

# System and utilities
import os
import sys
import warnings
from pathlib import Path

# Jupyter notebook specific
try:
    from IPython.display import display, HTML
    get_ipython().run_line_magic('matplotlib', 'inline')
    print("Jupyter environment detected")
except:
    print("Running in standard Python environment")

# Configuration
warnings.filterwarnings('ignore')
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("All essential libraries imported successfully!")
print(f"Python version: {sys.version}")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"Scikit-learn version: {__import__('sklearn').__version__}")