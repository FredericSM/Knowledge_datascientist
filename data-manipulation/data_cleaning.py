"""
Comprehensive data cleaning techniques and examples.
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime

def create_messy_dataset():
    """Create a messy dataset for cleaning demonstration."""
    np.random.seed(42)
    
    # Create problematic data
    data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],  # Duplicate ID
        'name': ['John Doe', 'jane smith', 'BOB JOHNSON', None, 'Alice Brown', 
                'charlie white', '', 'Diana Green', 'Eve Black', 'Frank Gray', 'John Doe'],
        'email': ['john@email.com', 'JANE@EMAIL.COM', 'bob@email', 'alice@email.com',
                 None, 'charlie.white@email.com', 'invalid-email', 'diana@email.com',
                 'eve@email.com', 'frank@email.com', 'john@email.com'],
        'age': [25, 30, 35, -5, 150, 28, 32, None, 45, 22, 25],  # Invalid ages
        'salary': [50000, 60000, 70000, 80000, None, 90000, 100000, 110000, 120000, 'not_a_number', 50000],
        'date_joined': ['2020-01-15', '2021/02/20', 'March 15, 2019', '2022-13-45',
                       None, '2020-06-10', '15-07-2021', '2019-12-01', 
                       '2021-03-30', '2022-01-15', '2020-01-15'],
        'department': ['Sales', 'sales', 'MARKETING', 'HR', 'IT', 'Sales', 
                      'Marketing', 'hr', 'it', 'Sales', 'Sales']
    }
    
    return pd.DataFrame(data)

def identify_data_quality_issues(df):
    """Identify and report data quality issues."""
    print("=== DATA QUALITY ASSESSMENT ===")
    
    print(f"Dataset shape: {df.shape}")
    print(f"\nData types:\n{df.dtypes}")
    
    # Missing values
    print(f"\nMissing values:")
    missing = df.isnull().sum()
    for col, count in missing.items():
        if count > 0:
            percentage = (count / len(df)) * 100
            print(f"  {col}: {count} ({percentage:.1f}%)")
    
    # Duplicates
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate rows: {duplicates}")
    
    # Data type issues
    print(f"\nPotential data type issues:")
    for col in df.columns:
        if df[col].dtype == 'object':
            unique_count = df[col].nunique()
            print(f"  {col}: {unique_count} unique values (text column)")
    
    return missing, duplicates

def clean_text_data(df):
    """Clean text columns."""
    print("\n=== CLEANING TEXT DATA ===")
    
    df_clean = df.copy()
    
    # Clean name column
    if 'name' in df_clean.columns:
        print("Cleaning 'name' column...")
        # Remove empty strings and None values, then normalize case
        df_clean['name'] = df_clean['name'].replace('', np.nan)
        df_clean['name'] = df_clean['name'].str.title()  # Title case
        print(f"Names after cleaning: {df_clean['name'].dropna().tolist()}")
    
    # Clean email column
    if 'email' in df_clean.columns:
        print("\nCleaning 'email' column...")
        # Convert to lowercase
        df_clean['email'] = df_clean['email'].str.lower()
        
        # Validate email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        valid_emails = df_clean['email'].str.match(email_pattern, na=False)
        invalid_emails = df_clean[~valid_emails & df_clean['email'].notna()]['email']
        
        if len(invalid_emails) > 0:
            print(f"Invalid emails found: {invalid_emails.tolist()}")
            # Set invalid emails to NaN
            df_clean.loc[~valid_emails & df_clean['email'].notna(), 'email'] = np.nan
    
    # Clean department column
    if 'department' in df_clean.columns:
        print("\nCleaning 'department' column...")
        # Standardize department names
        df_clean['department'] = df_clean['department'].str.title()
        print(f"Unique departments: {df_clean['department'].unique()}")
    
    return df_clean

def clean_numeric_data(df):
    """Clean numeric columns."""
    print("\n=== CLEANING NUMERIC DATA ===")
    
    df_clean = df.copy()
    
    # Clean age column
    if 'age' in df_clean.columns:
        print("Cleaning 'age' column...")
        # Convert to numeric, coercing errors to NaN
        df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')
        
        # Set reasonable age bounds
        df_clean.loc[df_clean['age'] < 0, 'age'] = np.nan
        df_clean.loc[df_clean['age'] > 120, 'age'] = np.nan
        
        invalid_ages = df[~pd.to_numeric(df['age'], errors='coerce').between(0, 120, na=False)]['age']
        print(f"Invalid ages removed: {invalid_ages.dropna().tolist()}")
    
    # Clean salary column
    if 'salary' in df_clean.columns:
        print("\nCleaning 'salary' column...")
        # Convert to numeric, coercing errors to NaN
        df_clean['salary'] = pd.to_numeric(df_clean['salary'], errors='coerce')
        
        # Set reasonable salary bounds (assuming USD)
        df_clean.loc[df_clean['salary'] < 0, 'salary'] = np.nan
        df_clean.loc[df_clean['salary'] > 1000000, 'salary'] = np.nan  # Cap at $1M
        
        print(f"Salary range: ${df_clean['salary'].min():.0f} - ${df_clean['salary'].max():.0f}")
    
    return df_clean

def clean_date_data(df):
    """Clean date columns."""
    print("\n=== CLEANING DATE DATA ===")
    
    df_clean = df.copy()
    
    if 'date_joined' in df_clean.columns:
        print("Cleaning 'date_joined' column...")
        
        # Try to parse dates with different formats
        date_formats = ['%Y-%m-%d', '%Y/%m/%d', '%B %d, %Y', '%d-%m-%Y']
        
        df_clean['date_joined_parsed'] = None
        
        for i, date_str in enumerate(df_clean['date_joined']):
            if pd.isna(date_str):
                continue
                
            parsed_date = None
            for fmt in date_formats:
                try:
                    parsed_date = pd.to_datetime(date_str, format=fmt)
                    break
                except:
                    continue
            
            # If no format worked, try pandas' general parser
            if parsed_date is None:
                try:
                    parsed_date = pd.to_datetime(date_str, errors='coerce')
                except:
                    pass
            
            df_clean.loc[i, 'date_joined_parsed'] = parsed_date
        
        # Convert to datetime
        df_clean['date_joined_parsed'] = pd.to_datetime(df_clean['date_joined_parsed'])
        
        # Validate date ranges (assuming employees joined between 2010-2023)
        valid_range = (df_clean['date_joined_parsed'] >= '2010-01-01') & \
                     (df_clean['date_joined_parsed'] <= '2023-12-31')
        
        invalid_dates = df_clean[~valid_range & df_clean['date_joined_parsed'].notna()]
        if len(invalid_dates) > 0:
            print(f"Invalid dates found: {invalid_dates['date_joined'].tolist()}")
            df_clean.loc[~valid_range, 'date_joined_parsed'] = np.nan
        
        # Replace original column
        df_clean['date_joined'] = df_clean['date_joined_parsed']
        df_clean.drop('date_joined_parsed', axis=1, inplace=True)
        
        valid_dates = df_clean['date_joined'].dropna()
        if len(valid_dates) > 0:
            print(f"Date range: {valid_dates.min()} to {valid_dates.max()}")
    
    return df_clean

def handle_duplicates(df):
    """Handle duplicate records."""
    print("\n=== HANDLING DUPLICATES ===")
    
    # Check for exact duplicates
    exact_duplicates = df.duplicated().sum()
    print(f"Exact duplicate rows: {exact_duplicates}")
    
    # Check for duplicates based on key columns
    if 'id' in df.columns:
        id_duplicates = df.duplicated(subset=['id']).sum()
        print(f"Duplicate IDs: {id_duplicates}")
        
        if id_duplicates > 0:
            print("Duplicate ID records:")
            duplicate_ids = df[df.duplicated(subset=['id'], keep=False)].sort_values('id')
            print(duplicate_ids[['id', 'name', 'email']])
    
    # Remove exact duplicates
    df_clean = df.drop_duplicates()
    
    # For ID duplicates, keep the first occurrence
    if 'id' in df_clean.columns:
        df_clean = df_clean.drop_duplicates(subset=['id'], keep='first')
    
    print(f"Shape after removing duplicates: {df_clean.shape}")
    return df_clean

def handle_missing_values(df):
    """Handle missing values with different strategies."""
    print("\n=== HANDLING MISSING VALUES ===")
    
    df_clean = df.copy()
    
    # Strategy 1: Fill with appropriate defaults
    if 'age' in df_clean.columns:
        # Fill age with median
        median_age = df_clean['age'].median()
        df_clean['age'].fillna(median_age, inplace=True)
        print(f"Filled missing ages with median: {median_age}")
    
    if 'salary' in df_clean.columns:
        # Fill salary with median by department
        if 'department' in df_clean.columns:
            df_clean['salary'] = df_clean.groupby('department')['salary'].transform(
                lambda x: x.fillna(x.median())
            )
            print("Filled missing salaries with department median")
        else:
            median_salary = df_clean['salary'].median()
            df_clean['salary'].fillna(median_salary, inplace=True)
            print(f"Filled missing salaries with overall median: ${median_salary:,.0f}")
    
    # Strategy 2: Remove rows with critical missing values
    if 'name' in df_clean.columns:
        before_count = len(df_clean)
        df_clean = df_clean.dropna(subset=['name'])
        removed_count = before_count - len(df_clean)
        if removed_count > 0:
            print(f"Removed {removed_count} rows with missing names")
    
    print(f"Final missing value counts:")
    remaining_missing = df_clean.isnull().sum()
    for col, count in remaining_missing.items():
        if count > 0:
            print(f"  {col}: {count}")
    
    return df_clean

def validate_cleaned_data(df_original, df_clean):
    """Validate the cleaned dataset."""
    print("\n=== VALIDATION RESULTS ===")
    
    print(f"Original shape: {df_original.shape}")
    print(f"Cleaned shape: {df_clean.shape}")
    print(f"Rows removed: {df_original.shape[0] - df_clean.shape[0]}")
    
    # Check data types
    print(f"\nData types after cleaning:")
    print(df_clean.dtypes)
    
    # Check for remaining issues
    print(f"\nRemaining data quality issues:")
    
    # Missing values
    missing = df_clean.isnull().sum().sum()
    print(f"  Total missing values: {missing}")
    
    # Duplicates
    duplicates = df_clean.duplicated().sum()
    print(f"  Duplicate rows: {duplicates}")
    
    # Basic statistics for numeric columns
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print(f"\nNumeric column statistics:")
        print(df_clean[numeric_cols].describe())
    
    return df_clean

def complete_data_cleaning_workflow():
    """Run the complete data cleaning workflow."""
    print("=== COMPLETE DATA CLEANING WORKFLOW ===")
    
    # 1. Create messy dataset
    df_messy = create_messy_dataset()
    print(f"Created messy dataset with shape: {df_messy.shape}")
    
    # 2. Assess data quality
    missing, duplicates = identify_data_quality_issues(df_messy)
    
    # 3. Clean different types of data
    df_clean = clean_text_data(df_messy)
    df_clean = clean_numeric_data(df_clean)
    df_clean = clean_date_data(df_clean)
    
    # 4. Handle duplicates
    df_clean = handle_duplicates(df_clean)
    
    # 5. Handle missing values
    df_clean = handle_missing_values(df_clean)
    
    # 6. Validate results
    df_final = validate_cleaned_data(df_messy, df_clean)
    
    print("\n=== CLEANING COMPLETED ===")
    return df_messy, df_final

if __name__ == "__main__":
    original_df, cleaned_df = complete_data_cleaning_workflow()