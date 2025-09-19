"""
Simple Flask API for serving machine learning models.
Example of deploying a trained model as a REST API.
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Global variables for model and preprocessing objects
model = None
scaler = None
feature_names = None

def load_model_and_preprocessing():
    """Load the trained model and preprocessing objects."""
    global model, scaler, feature_names
    
    try:
        # Load model (assuming it's saved as joblib file)
        model_path = os.getenv('MODEL_PATH', 'model.joblib')
        model = joblib.load(model_path)
        logger.info(f"Model loaded from {model_path}")
        
        # Load scaler if it exists
        scaler_path = os.getenv('SCALER_PATH', 'scaler.joblib')
        if os.path.exists(scaler_path):
            scaler = joblib.load(scaler_path)
            logger.info(f"Scaler loaded from {scaler_path}")
        
        # Load feature names if they exist
        features_path = os.getenv('FEATURES_PATH', 'feature_names.txt')
        if os.path.exists(features_path):
            with open(features_path, 'r') as f:
                feature_names = [line.strip() for line in f.readlines()]
            logger.info(f"Feature names loaded: {len(feature_names)} features")
        
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'model_loaded': model is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Make predictions on input data."""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate input
        if 'features' not in data:
            return jsonify({'error': 'Features not provided'}), 400
        
        features = data['features']
        
        # Convert to numpy array
        if isinstance(features, list):
            if isinstance(features[0], list):
                # Multiple samples
                X = np.array(features)
            else:
                # Single sample
                X = np.array(features).reshape(1, -1)
        else:
            return jsonify({'error': 'Features should be a list or list of lists'}), 400
        
        # Validate feature dimensions
        if feature_names and X.shape[1] != len(feature_names):
            return jsonify({
                'error': f'Expected {len(feature_names)} features, got {X.shape[1]}'
            }), 400
        
        # Apply preprocessing if scaler exists
        if scaler is not None:
            X = scaler.transform(X)
        
        # Make predictions
        predictions = model.predict(X)
        
        # Get prediction probabilities if available
        probabilities = None
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(X)
        
        # Prepare response
        response = {
            'predictions': predictions.tolist(),
            'num_samples': len(predictions),
            'timestamp': datetime.now().isoformat()
        }
        
        if probabilities is not None:
            response['probabilities'] = probabilities.tolist()
        
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    """Make predictions on batch data (CSV format)."""
    try:
        # Get JSON data
        data = request.get_json()
        
        if 'data' not in data:
            return jsonify({'error': 'Data not provided'}), 400
        
        # Convert to DataFrame
        df = pd.DataFrame(data['data'])
        
        # Validate columns if feature names are available
        if feature_names:
            missing_cols = set(feature_names) - set(df.columns)
            if missing_cols:
                return jsonify({
                    'error': f'Missing columns: {list(missing_cols)}'
                }), 400
            
            # Select only the required features in the right order
            df = df[feature_names]
        
        # Convert to numpy array
        X = df.values
        
        # Apply preprocessing if scaler exists
        if scaler is not None:
            X = scaler.transform(X)
        
        # Make predictions
        predictions = model.predict(X)
        
        # Get prediction probabilities if available
        probabilities = None
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(X)
        
        # Prepare response
        response = {
            'predictions': predictions.tolist(),
            'num_samples': len(predictions),
            'timestamp': datetime.now().isoformat()
        }
        
        if probabilities is not None:
            response['probabilities'] = probabilities.tolist()
        
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error during batch prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/model_info', methods=['GET'])
def model_info():
    """Get information about the loaded model."""
    try:
        if model is None:
            return jsonify({'error': 'No model loaded'}), 500
        
        info = {
            'model_type': type(model).__name__,
            'model_module': type(model).__module__,
            'features_count': len(feature_names) if feature_names else None,
            'feature_names': feature_names,
            'has_scaler': scaler is not None,
            'has_predict_proba': hasattr(model, 'predict_proba')
        }
        
        # Add model-specific information
        if hasattr(model, 'n_features_in_'):
            info['n_features_in'] = model.n_features_in_
        
        if hasattr(model, 'classes_'):
            info['classes'] = model.classes_.tolist()
        
        if hasattr(model, 'n_estimators'):
            info['n_estimators'] = model.n_estimators
        
        return jsonify(info)
        
    except Exception as e:
        logger.error(f"Error getting model info: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

def create_sample_model():
    """Create a sample model for testing purposes."""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import make_classification
    
    logger.info("Creating sample model for testing...")
    
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    
    # Create and train model
    global model, scaler, feature_names
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    scaler = StandardScaler()
    
    X_scaled = scaler.fit_transform(X)
    model.fit(X_scaled, y)
    
    # Create feature names
    feature_names = [f'feature_{i:02d}' for i in range(X.shape[1])]
    
    # Save model for next time
    joblib.dump(model, 'model.joblib')
    joblib.dump(scaler, 'scaler.joblib')
    
    with open('feature_names.txt', 'w') as f:
        for name in feature_names:
            f.write(f"{name}\n")
    
    logger.info("Sample model created and saved")

if __name__ == '__main__':
    try:
        load_model_and_preprocessing()
    except:
        logger.warning("Could not load model, creating sample model...")
        create_sample_model()
    
    # Run the Flask app
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Flask app on port {port}, debug={debug}")
    app.run(host='0.0.0.0', port=port, debug=debug)