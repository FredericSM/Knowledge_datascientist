# Command Line Tools for Data Science

Essential command-line utilities and workflows for data science projects.

## Git Commands for Data Science

### Repository Setup
```bash
# Initialize repository
git init
git remote add origin <repository-url>

# First commit
git add .
git commit -m "Initial commit"
git push -u origin main

# Clone repository
git clone <repository-url>
cd repository-name
```

### Branch Management
```bash
# Create and switch to new branch
git checkout -b feature/data-analysis

# Switch between branches
git checkout main
git checkout feature/data-analysis

# Merge branch
git checkout main
git merge feature/data-analysis

# Delete branch
git branch -d feature/data-analysis
```

### Working with Data Files
```bash
# Check large files before committing
git ls-files | xargs ls -l | sort -k5 -rn | head

# Track large files with Git LFS
git lfs track "*.csv"
git lfs track "*.parquet"
git add .gitattributes

# Add and commit data
git add data/dataset.csv
git commit -m "Add dataset for analysis"
```

## Package Management

### Pip Commands
```bash
# Install packages
pip install pandas numpy scikit-learn matplotlib seaborn

# Install from requirements file
pip install -r requirements.txt

# Create requirements file
pip freeze > requirements.txt

# Install specific version
pip install pandas==1.3.0

# Upgrade package
pip install --upgrade pandas

# Uninstall package
pip uninstall pandas
```

### Conda Commands
```bash
# Create environment
conda create -n datascience python=3.9

# Activate/deactivate environment
conda activate datascience
conda deactivate

# Install packages
conda install pandas numpy scikit-learn

# Install from conda-forge
conda install -c conda-forge plotly

# List environments
conda env list

# Export environment
conda env export > environment.yml

# Create from environment file
conda env create -f environment.yml

# Remove environment
conda env remove -n datascience
```

## Jupyter Notebook Commands

### Installation and Setup
```bash
# Install Jupyter
pip install jupyter

# Install JupyterLab
pip install jupyterlab

# Start Jupyter Notebook
jupyter notebook

# Start JupyterLab
jupyter lab

# Run notebook from command line
jupyter nbconvert --execute notebook.ipynb
```

### Notebook Management
```bash
# Convert notebook to Python script
jupyter nbconvert --to script notebook.ipynb

# Convert notebook to HTML
jupyter nbconvert --to html notebook.ipynb

# Convert notebook to PDF
jupyter nbconvert --to pdf notebook.ipynb

# Clear all output
jupyter nbconvert --clear-output notebook.ipynb

# Execute notebook and save
jupyter nbconvert --execute --inplace notebook.ipynb
```

## Data Processing Commands

### CSV Operations
```bash
# View first few lines
head -n 5 data.csv

# View last few lines
tail -n 5 data.csv

# Count lines
wc -l data.csv

# View specific columns (assuming comma-separated)
cut -d',' -f1,3 data.csv | head

# Sort CSV by column
sort -t',' -k2 data.csv

# Remove duplicates
sort data.csv | uniq

# Find specific pattern
grep "pattern" data.csv
```

### File Operations
```bash
# Compress files
gzip large_dataset.csv
tar -czf datasets.tar.gz data/

# Decompress files
gunzip large_dataset.csv.gz
tar -xzf datasets.tar.gz

# Find files
find . -name "*.csv" -type f
find . -name "*.py" -exec grep -l "pandas" {} \;

# Monitor file changes
watch -n 2 'ls -la data/'
```

## Environment and System Info

### Python Environment
```bash
# Check Python version
python --version

# Check installed packages
pip list

# Check package info
pip show pandas

# Check Python path
which python

# Check environment variables
echo $PYTHONPATH
```

### System Resources
```bash
# Check memory usage
free -h

# Check disk usage
df -h

# Check CPU usage
top
htop

# Check GPU usage (if NVIDIA)
nvidia-smi
```

## Automation Scripts

### Batch Processing
```bash
# Process all CSV files
for file in *.csv; do
    python process_data.py "$file"
done

# Run multiple notebooks
for notebook in *.ipynb; do
    jupyter nbconvert --execute "$notebook"
done
```

### Cron Jobs for Data Updates
```bash
# Edit crontab
crontab -e

# Run daily at 2 AM
0 2 * * * /path/to/python /path/to/script.py

# Run every hour
0 * * * * /path/to/data_update.sh
```

## Useful Aliases

Add to your `.bashrc` or `.zshrc`:
```bash
# Jupyter aliases
alias jn='jupyter notebook'
alias jl='jupyter lab'

# Python aliases
alias py='python'
alias ipy='ipython'

# Git aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'

# Data science shortcuts
alias activate-ds='conda activate datascience'
alias nb-clean='jupyter nbconvert --clear-output *.ipynb'
```