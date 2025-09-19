# Getting Started Guide

Welcome to your Data Science Knowledge Repository! This guide will help you get started quickly.

## Quick Setup

### 1. Install Required Packages
```bash
# Clone the repository
git clone https://github.com/FredericSM/Knowledge_datascientist.git
cd Knowledge_datascientist

# Create virtual environment
python -m venv datascience_env
source datascience_env/bin/activate  # On Windows: datascience_env\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 2. Test Your Setup
Run this in Python to verify everything is working:

```python
# Test essential imports
from python_basics.essential_imports import *

# Test data manipulation
from data_manipulation.pandas_basics import basic_operations_demo
basic_operations_demo()

# Test machine learning
from machine_learning.classification_workflow import main_classification_workflow
# Note: This will take a few minutes to run
```

## Learning Path

### Beginner Path 🟢
1. **Start with [Python Basics](./python-basics/)** - Essential imports and patterns
2. **Learn [Data Manipulation](./data-manipulation/)** - Pandas fundamentals
3. **Explore [Visualization](./visualization/)** - Creating meaningful plots
4. **Study [References](./references/)** - Quick lookup guides

### Intermediate Path 🟡
1. **Master [Data Cleaning](./data-manipulation/data_cleaning.py)** - Real-world data preparation
2. **Dive into [Statistics](./statistics/)** - Statistical analysis and testing
3. **Practice [Machine Learning](./machine-learning/)** - Complete ML workflows
4. **Learn [Preprocessing](./preprocessing/)** - Feature engineering techniques

### Advanced Path 🔴
1. **Study [Deployment](./deployment/)** - Model serving and APIs
2. **Explore [Command Line Tools](./command-line-tools/)** - Workflow automation
3. **Practice MLOps** - End-to-end ML pipelines
4. **Contribute** - Add your own examples and improvements

## Common Use Cases

### Data Analysis Project
```bash
# 1. Set up your environment
source datascience_env/bin/activate

# 2. Start Jupyter notebook
jupyter notebook

# 3. Import your toolkit
from python_basics.essential_imports import *

# 4. Load and explore your data
df = pd.read_csv('your_data.csv')
df.info()
df.describe()

# 5. Clean your data (see data-manipulation/data_cleaning.py)
# 6. Visualize your data (see visualization/)
# 7. Analyze results (see statistics/)
```

### Machine Learning Project
```bash
# 1. Follow the classification_workflow.py example
# 2. Adapt it to your specific problem
# 3. Use preprocessing techniques as needed
# 4. Evaluate your model thoroughly
# 5. Deploy using flask_api_example.py
```

### Research and Experimentation
```bash
# 1. Use Jupyter notebooks for exploration
# 2. Reference the quick guides in references/
# 3. Follow statistical analysis patterns
# 4. Document your findings
```

## Tips for Success

### 1. Practice Regularly
- Work through the examples
- Modify them for your own data
- Create your own examples

### 2. Build Projects
- Start with simple datasets
- Gradually increase complexity
- Focus on end-to-end workflows

### 3. Stay Organized
- Use version control (Git)
- Document your work
- Create reproducible environments

### 4. Keep Learning
- Follow data science blogs and papers
- Join communities (Kaggle, Stack Overflow)
- Contribute to open source projects

## Troubleshooting

### Import Errors
```bash
# Make sure you're in the right environment
which python
pip list

# Reinstall if needed
pip install -r requirements.txt
```

### Memory Issues
```python
# Read large files in chunks
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)

# Use efficient data types
df = df.astype({'int_col': 'int32'})
```

### Performance Issues
```python
# Use vectorized operations
df['new_col'] = df['col1'] * df['col2']  # Good
# df['new_col'] = df.apply(lambda x: x['col1'] * x['col2'], axis=1)  # Slow

# Use built-in pandas functions
df.groupby('col').sum()  # Good
```

## Next Steps

1. **Explore the examples** - Run the Python files and understand how they work
2. **Adapt to your needs** - Modify examples for your specific use cases
3. **Build something** - Create a complete project using multiple sections
4. **Share and learn** - Contribute improvements and learn from others

Happy learning! 🚀📊