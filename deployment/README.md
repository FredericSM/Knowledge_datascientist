# Model Deployment and MLOps

Deploying machine learning models to production and managing ML workflows.

## Files in this Section

- [`model_serialization.py`](./model_serialization.py) - Saving and loading models
- [`flask_api_example.py`](./flask_api_example.py) - Creating REST APIs with Flask
- [`docker_deployment.md`](./docker_deployment.md) - Containerization with Docker
- [`model_monitoring.py`](./model_monitoring.py) - Model performance monitoring

## Quick Reference

### Model Serialization
```python
import joblib
import pickle
from sklearn.ensemble import RandomForestClassifier

# Train a model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save with joblib (recommended for sklearn)
joblib.dump(model, 'model.joblib')
loaded_model = joblib.load('model.joblib')

# Save with pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
```

### Flask API Example
```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
```

### Docker Deployment
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

### Model Monitoring
```python
import numpy as np
from scipy import stats
import pandas as pd

def detect_data_drift(reference_data, current_data, threshold=0.05):
    """Detect data drift using statistical tests."""
    drift_detected = {}
    
    for column in reference_data.columns:
        if reference_data[column].dtype in ['int64', 'float64']:
            # KS test for numerical features
            statistic, p_value = stats.ks_2samp(
                reference_data[column], 
                current_data[column]
            )
        else:
            # Chi-square test for categorical features
            ref_counts = reference_data[column].value_counts()
            curr_counts = current_data[column].value_counts()
            
            # Align categories
            all_categories = set(ref_counts.index) | set(curr_counts.index)
            ref_aligned = [ref_counts.get(cat, 0) for cat in all_categories]
            curr_aligned = [curr_counts.get(cat, 0) for cat in all_categories]
            
            statistic, p_value = stats.chisquare(curr_aligned, ref_aligned)
        
        drift_detected[column] = p_value < threshold
    
    return drift_detected

def monitor_model_performance(y_true, y_pred, y_pred_proba=None):
    """Monitor model performance metrics."""
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    from sklearn.metrics import roc_auc_score, f1_score
    
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1': f1_score(y_true, y_pred, average='weighted')
    }
    
    if y_pred_proba is not None:
        metrics['auc'] = roc_auc_score(y_true, y_pred_proba, multi_class='ovr')
    
    return metrics
```

### Cloud Deployment

#### AWS SageMaker
```python
import boto3
import sagemaker
from sagemaker.sklearn.estimator import SKLearn

# Deploy to SageMaker
sklearn_estimator = SKLearn(
    entry_point='train.py',
    role=sagemaker.get_execution_role(),
    instance_type='ml.m5.large',
    framework_version='0.23-1',
    py_version='py3'
)

sklearn_estimator.fit({'train': 's3://bucket/train.csv'})
predictor = sklearn_estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)
```

#### Google Cloud Platform
```python
from google.cloud import aiplatform

# Deploy to Vertex AI
model = aiplatform.Model.upload(
    display_name="my-model",
    artifact_uri="gs://bucket/model",
    serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/sklearn-cpu.1-0:latest"
)

endpoint = model.deploy(
    machine_type="n1-standard-4",
    min_replica_count=1,
    max_replica_count=5
)
```

### CI/CD Pipeline Example
```yaml
# .github/workflows/ml-pipeline.yml
name: ML Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest
    
    - name: Run tests
      run: pytest tests/
    
    - name: Train model
      run: python train_model.py
    
    - name: Validate model
      run: python validate_model.py
    
    - name: Deploy model
      if: github.ref == 'refs/heads/main'
      run: python deploy_model.py
```