"""
Essential pandas operations for data manipulation and analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Sample data creation
def create_sample_data():
    """Create sample dataset for demonstrations."""
    np.random.seed(42)
    
    dates = pd.date_range('2020-01-01', periods=1000, freq='D')
    
    data = {
        'date': np.random.choice(dates, 1000),
        'customer_id': np.random.randint(1, 101, 1000),
        'product': np.random.choice(['A', 'B', 'C', 'D', 'E'], 1000),
        'quantity': np.random.randint(1, 11, 1000),
        'price': np.round(np.random.uniform(10, 100, 1000), 2),
        'discount': np.random.choice([0, 0.05, 0.1, 0.15, 0.2], 1000),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
        'satisfaction': np.random.randint(1, 6, 1000)  # 1-5 rating
    }
    
    df = pd.DataFrame(data)
    df['total_amount'] = df['quantity'] * df['price'] * (1 - df['discount'])
    
    # Add some missing values
    df.loc[np.random.choice(df.index, 50, replace=False), 'satisfaction'] = np.nan
    df.loc[np.random.choice(df.index, 30, replace=False), 'discount'] = np.nan
    
    return df

# Basic DataFrame operations
def basic_operations_demo():
    """Demonstrate basic DataFrame operations."""
    df = create_sample_data()
    
    print("=== BASIC DATAFRAME OPERATIONS ===")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Data types:\n{df.dtypes}")
    print(f"\nFirst 5 rows:\n{df.head()}")
    print(f"\nBasic statistics:\n{df.describe()}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    
    return df

# Selection and filtering
def selection_filtering_demo(df):
    """Demonstrate selection and filtering operations."""
    print("\n=== SELECTION AND FILTERING ===")
    
    # Column selection
    print("Single column selection:")
    print(df['product'].value_counts())
    
    # Multiple columns
    print("\nMultiple columns:")
    print(df[['product', 'quantity', 'price']].head())
    
    # Boolean indexing
    high_value_orders = df[df['total_amount'] > 500]
    print(f"\nHigh value orders (>500): {len(high_value_orders)}")
    
    # Multiple conditions
    premium_orders = df[(df['total_amount'] > 300) & (df['satisfaction'] >= 4)]
    print(f"Premium satisfied orders: {len(premium_orders)}")
    
    # String filtering
    if 'product' in df.columns:
        product_a_or_b = df[df['product'].isin(['A', 'B'])]
        print(f"Product A or B orders: {len(product_a_or_b)}")
    
    return high_value_orders

# Data transformation
def transformation_demo(df):
    """Demonstrate data transformation operations."""
    print("\n=== DATA TRANSFORMATIONS ===")
    
    # Apply function to column
    df['price_category'] = df['price'].apply(lambda x: 'Low' if x < 30 else 'Medium' if x < 70 else 'High')
    print("Price categories:")
    print(df['price_category'].value_counts())
    
    # Create new columns
    df['profit_margin'] = df['price'] * 0.3  # Assume 30% profit margin
    df['is_discounted'] = df['discount'] > 0
    
    # Date operations
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.day_name()
    
    print(f"\nYears in data: {sorted(df['year'].unique())}")
    print(f"Day of week distribution:\n{df['day_of_week'].value_counts()}")
    
    return df

# Sorting operations
def sorting_demo(df):
    """Demonstrate sorting operations."""
    print("\n=== SORTING OPERATIONS ===")
    
    # Sort by single column
    df_sorted = df.sort_values('total_amount', ascending=False)
    print("Top 5 highest value orders:")
    print(df_sorted[['customer_id', 'product', 'total_amount']].head())
    
    # Sort by multiple columns
    df_multi_sort = df.sort_values(['region', 'total_amount'], ascending=[True, False])
    print("\nTop order by region:")
    print(df_multi_sort.groupby('region').first()[['product', 'total_amount']])
    
    return df_sorted

# Handling missing values
def missing_values_demo(df):
    """Demonstrate missing value handling."""
    print("\n=== MISSING VALUES HANDLING ===")
    
    print("Missing values before handling:")
    print(df.isnull().sum())
    
    # Fill missing satisfaction with median
    median_satisfaction = df['satisfaction'].median()
    df['satisfaction_filled'] = df['satisfaction'].fillna(median_satisfaction)
    
    # Fill missing discount with 0
    df['discount_filled'] = df['discount'].fillna(0)
    
    # Drop rows with any missing values (creates a copy)
    df_no_missing = df.dropna()
    
    print(f"\nOriginal shape: {df.shape}")
    print(f"After dropping missing values: {df_no_missing.shape}")
    print(f"Missing values after filling:")
    print(df[['satisfaction_filled', 'discount_filled']].isnull().sum())
    
    return df

# Advanced selection with query
def query_demo(df):
    """Demonstrate query method for complex filtering."""
    print("\n=== QUERY METHOD ===")
    
    # Using query for complex conditions
    high_satisfaction_discounted = df.query('satisfaction >= 4 and discount > 0.1')
    print(f"High satisfaction + discounted orders: {len(high_satisfaction_discounted)}")
    
    # Query with variables
    min_amount = 200
    target_region = 'North'
    result = df.query(f'total_amount > {min_amount} and region == "{target_region}"')
    print(f"Orders > {min_amount} in {target_region}: {len(result)}")
    
    return result

if __name__ == "__main__":
    # Run all demonstrations
    df = basic_operations_demo()
    high_value = selection_filtering_demo(df)
    df_transformed = transformation_demo(df)
    df_sorted = sorting_demo(df_transformed)
    df_clean = missing_values_demo(df_transformed)
    query_result = query_demo(df_clean)
    
    print("\n=== FINAL DATASET INFO ===")
    print(f"Final shape: {df_clean.shape}")
    print(f"Final columns: {list(df_clean.columns)}")
    print("\nDemo completed successfully!")