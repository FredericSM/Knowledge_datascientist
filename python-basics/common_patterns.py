"""
Common Python patterns and idioms for data science.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# 1. List Comprehensions for Data Processing
def list_comprehension_examples():
    """Examples of list comprehensions commonly used in data science."""
    
    # Processing numeric data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squared = [x**2 for x in numbers]
    evens = [x for x in numbers if x % 2 == 0]
    
    # Processing strings (common for text data)
    words = ["Data", "Science", "Machine", "Learning"]
    lowercase = [word.lower() for word in words]
    filtered = [word for word in words if len(word) > 4]
    
    return squared, evens, lowercase, filtered

# 2. Dictionary Comprehensions
def dict_comprehension_examples():
    """Dictionary comprehensions for data transformation."""
    
    # Creating lookup dictionaries
    categories = ['A', 'B', 'C', 'D']
    category_codes = {cat: i for i, cat in enumerate(categories)}
    
    # Processing data dictionaries
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
    column_means = {col: np.mean(values) for col, values in data.items()}
    
    return category_codes, column_means

# 3. Context Managers for File Handling
def file_handling_patterns():
    """Safe file handling patterns."""
    
    # Reading files safely
    def read_csv_safely(filepath):
        try:
            with open(filepath, 'r') as file:
                df = pd.read_csv(file)
                return df
        except FileNotFoundError:
            print(f"File {filepath} not found")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    # Using pathlib for file operations
    def process_data_files(directory_path):
        data_dir = Path(directory_path)
        csv_files = list(data_dir.glob("*.csv"))
        
        all_data = []
        for file in csv_files:
            df = pd.read_csv(file)
            df['source_file'] = file.name
            all_data.append(df)
        
        if all_data:
            return pd.concat(all_data, ignore_index=True)
        return pd.DataFrame()
    
    return read_csv_safely, process_data_files

# 4. Function Decorators for Timing and Validation
import time
from functools import wraps

def timing_decorator(func):
    """Decorator to time function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def validate_dataframe(func):
    """Decorator to validate DataFrame input."""
    @wraps(func)
    def wrapper(df, *args, **kwargs):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("First argument must be a pandas DataFrame")
        if df.empty:
            raise ValueError("DataFrame cannot be empty")
        return func(df, *args, **kwargs)
    return wrapper

# 5. Error Handling Patterns
def safe_division(a, b):
    """Safe division with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return np.nan
    except TypeError:
        print("Invalid types for division")
        return np.nan

def process_data_safely(data):
    """Process data with comprehensive error handling."""
    try:
        # Validate input
        if data is None:
            raise ValueError("Data cannot be None")
        
        if not isinstance(data, (list, np.ndarray, pd.Series)):
            raise TypeError("Data must be list, array, or Series")
        
        # Process data
        processed = np.array(data)
        
        # Check for invalid values
        if np.any(np.isnan(processed)):
            print("Warning: NaN values found")
        
        return processed.mean(), processed.std()
    
    except Exception as e:
        print(f"Error processing data: {e}")
        return None, None

# 6. Lambda Functions for Data Transformation
def lambda_examples():
    """Common lambda function patterns in data science."""
    
    # Data cleaning
    clean_text = lambda x: str(x).strip().lower() if pd.notna(x) else ""
    
    # Categorization
    categorize_age = lambda age: 'Young' if age < 30 else 'Middle' if age < 60 else 'Senior'
    
    # Mathematical transformations
    normalize = lambda x, mean, std: (x - mean) / std
    
    return clean_text, categorize_age, normalize

# Example usage
if __name__ == "__main__":
    print("=== List Comprehension Examples ===")
    squared, evens, lowercase, filtered = list_comprehension_examples()
    print(f"Squared: {squared}")
    print(f"Evens: {evens}")
    print(f"Lowercase: {lowercase}")
    print(f"Filtered: {filtered}")
    
    print("\n=== Dictionary Comprehension Examples ===")
    category_codes, column_means = dict_comprehension_examples()
    print(f"Category codes: {category_codes}")
    print(f"Column means: {column_means}")
    
    print("\n=== Error Handling Examples ===")
    print(f"Safe division 10/2: {safe_division(10, 2)}")
    print(f"Safe division 10/0: {safe_division(10, 0)}")
    
    mean, std = process_data_safely([1, 2, 3, 4, 5])
    print(f"Data processing result - Mean: {mean}, Std: {std}")