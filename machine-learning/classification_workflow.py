"""
Complete classification workflow with scikit-learn.
End-to-end pipeline from data preparation to model evaluation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
import warnings
warnings.filterwarnings('ignore')

def create_sample_classification_data():
    """Create sample classification dataset."""
    # Generate synthetic data
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=10,
        n_redundant=10,
        n_clusters_per_class=1,
        random_state=42
    )
    
    # Create feature names
    feature_names = [f'feature_{i:02d}' for i in range(X.shape[1])]
    
    # Create DataFrame
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    
    print(f"Dataset created with shape: {df.shape}")
    print(f"Target distribution:\n{df['target'].value_counts()}")
    
    return df, X, y

def data_exploration(df, X, y):
    """Explore the dataset."""
    print("\n=== DATA EXPLORATION ===")
    
    # Basic statistics
    print(f"Dataset shape: {df.shape}")
    print(f"Features: {X.shape[1]}")
    print(f"Samples: {X.shape[0]}")
    print(f"Target classes: {np.unique(y)}")
    
    # Check for missing values
    print(f"\nMissing values: {df.isnull().sum().sum()}")
    
    # Feature statistics
    print(f"\nFeature statistics:")
    print(df.describe())
    
    return df

def data_preprocessing(X, y):
    """Preprocess the data."""
    print("\n=== DATA PREPROCESSING ===")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    print(f"Training target distribution: {np.bincount(y_train)}")
    print(f"Test target distribution: {np.bincount(y_test)}")
    
    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Features scaled using StandardScaler")
    
    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler

def train_multiple_models(X_train, y_train):
    """Train multiple classification models."""
    print("\n=== MODEL TRAINING ===")
    
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(random_state=42, probability=True)
    }
    
    trained_models = {}
    
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        trained_models[name] = model
        print(f"{name} training completed")
    
    return trained_models

def evaluate_models(models, X_test, y_test):
    """Evaluate all trained models."""
    print("\n=== MODEL EVALUATION ===")
    
    results = {}
    
    for name, model in models.items():
        print(f"\nEvaluating {name}:")
        
        # Make predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # Store results
        results[name] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'predictions': y_pred
        }
        
        # Print results
        print(f"  Accuracy:  {accuracy:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall:    {recall:.4f}")
        print(f"  F1 Score:  {f1:.4f}")
        
        # Classification report
        print(f"\nClassification Report for {name}:")
        print(classification_report(y_test, y_pred))
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        print(f"\nConfusion Matrix for {name}:")
        print(cm)
    
    return results

def cross_validation_analysis(models, X, y):
    """Perform cross-validation analysis."""
    print("\n=== CROSS-VALIDATION ANALYSIS ===")
    
    cv_results = {}
    
    for name, model in models.items():
        print(f"\nCross-validating {name}...")
        
        # 5-fold cross-validation
        cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
        
        cv_results[name] = {
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'cv_scores': cv_scores
        }
        
        print(f"  CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
        print(f"  Individual scores: {cv_scores}")
    
    return cv_results

def hyperparameter_tuning_example(X_train, y_train, X_test, y_test):
    """Demonstrate hyperparameter tuning with GridSearchCV."""
    print("\n=== HYPERPARAMETER TUNING ===")
    
    # Random Forest hyperparameter tuning
    rf = RandomForestClassifier(random_state=42)
    
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7, None],
        'min_samples_split': [2, 5, 10]
    }
    
    print("Starting Grid Search for Random Forest...")
    grid_search = GridSearchCV(
        rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1
    )
    
    grid_search.fit(X_train, y_train)
    
    print(f"\nBest parameters: {grid_search.best_params_}")
    print(f"Best cross-validation score: {grid_search.best_score_:.4f}")
    
    # Evaluate best model
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Test accuracy with best model: {accuracy:.4f}")
    
    return best_model, grid_search

def feature_importance_analysis(model, feature_names):
    """Analyze feature importance."""
    print("\n=== FEATURE IMPORTANCE ANALYSIS ===")
    
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        print("Top 10 most important features:")
        for i in range(min(10, len(feature_names))):
            idx = indices[i]
            print(f"  {i+1}. {feature_names[idx]}: {importances[idx]:.4f}")
    else:
        print("Model does not support feature importance analysis")

def main_classification_workflow():
    """Run the complete classification workflow."""
    print("=== COMPLETE CLASSIFICATION WORKFLOW ===")
    
    # 1. Create or load data
    df, X, y = create_sample_classification_data()
    feature_names = [f'feature_{i:02d}' for i in range(X.shape[1])]
    
    # 2. Explore data
    data_exploration(df, X, y)
    
    # 3. Preprocess data
    X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler = data_preprocessing(X, y)
    
    # 4. Train models
    models = train_multiple_models(X_train_scaled, y_train)
    
    # 5. Evaluate models
    results = evaluate_models(models, X_test_scaled, y_test)
    
    # 6. Cross-validation
    cv_results = cross_validation_analysis(models, X, y)
    
    # 7. Hyperparameter tuning
    best_model, grid_search = hyperparameter_tuning_example(X_train_scaled, y_train, X_test_scaled, y_test)
    
    # 8. Feature importance
    feature_importance_analysis(models['Random Forest'], feature_names)
    
    print("\n=== WORKFLOW COMPLETED ===")
    return models, results, cv_results, best_model

if __name__ == "__main__":
    models, results, cv_results, best_model = main_classification_workflow()