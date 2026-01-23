# Machine Learning Scalers – Practical Cheat Sheet

## What is Scaling and Why It Matters

**Scaling** is the process of transforming numerical features so that they lie on comparable scales.

Many machine learning algorithms are **scale-sensitive**, meaning that features with larger magnitudes can dominate others and bias the learning process.

Scaling directly impacts:

* Optimization speed
* Model convergence
* Distance computations
* Numerical stability

> ⚠️ Tree-based models (Decision Trees, Random Forests, Gradient Boosting) generally **do not require scaling**.

---

## Key Dimensions to Understand

Before choosing a scaler, always reason along these axes:

* **Feature-wise vs Row-wise**: Are features normalized independently, or are entire observations normalized?
* **Outlier Sensitivity**: Does the scaler rely on mean/min/max statistics?
* **Distribution Shape**: Is the scaler trying to make data Gaussian?
* **Distance Preservation**: Does it preserve Euclidean distances?
* **Sparsity Preservation**: Can it be used safely on sparse matrices?

---

## 1. StandardScaler (Z-score normalization)

### Principle

Each feature is centered and scaled using its mean and standard deviation:

x' = (x − μ) / σ

This results in:

* Mean = 0
* Standard deviation = 1

Scaling is performed **feature-wise**.

### When to Use

* Data approximately Gaussian
* Linear and logistic regression
* Support Vector Machines
* Principal Component Analysis (mandatory)
* Neural networks

### Advantages

* Very common and well understood
* Preserves relative distances
* Works well with gradient-based optimization

### Drawbacks

* Highly sensitive to outliers
* Mean and variance can be distorted by extreme values

---

## 2. MinMaxScaler

### Principle

Each feature is rescaled into a fixed interval (default: [0, 1]):

x' = (x − min) / (max − min)

Scaling is **feature-wise**.

### When to Use

* Neural networks (especially with bounded activation functions)
* When feature bounds are known and meaningful
* Image and pixel-based data

### Advantages

* Easy to interpret
* Preserves original distribution shape
* Ensures bounded values

### Drawbacks

* Extremely sensitive to outliers
* New unseen values may fall outside the original range

---

## 3. RobustScaler

### Principle

Uses robust statistics:

* Centering with the median
* Scaling with the interquartile range (IQR)

x' = (x − median) / IQR

Scaling is **feature-wise**.

### When to Use

* Real-world business data
* Sensor measurements
* Financial or operational data with strong outliers

### Advantages

* Robust to extreme values
* Much more stable than StandardScaler in noisy datasets

### Drawbacks

* Less efficient when data is already well-behaved (Gaussian)
* Slightly harder to interpret

---

## 4. MaxAbsScaler

### Principle

Each feature is divided by its maximum absolute value:

x' = x / max(|x|)

Results in values within [-1, 1].
Scaling is **feature-wise**.

### When to Use

* Sparse data
* One-hot encoded features
* NLP pipelines

### Advantages

* Preserves sparsity
* Very fast and memory-efficient
* No centering (safe for sparse matrices)

### Drawbacks

* Sensitive to outliers
* No variance normalization

---

## 5. Normalizer (L1 / L2 Normalization)

### Principle

Each **row (observation)** is scaled independently so that its vector norm equals 1:

x' = x / ||x||

Common norms:

* L1 norm (sum of absolute values = 1)
* L2 norm (Euclidean norm = 1)

⚠️ This is **row-wise**, not feature-wise.

### When to Use

* Text data (TF-IDF)
* Cosine similarity
* Directional clustering
* k-NN with angular distance

### Advantages

* Makes samples comparable by direction
* Ideal when magnitude is meaningless

### Drawbacks

* Completely destroys absolute scale
* Generally unsuitable for regression tasks
* Can be disastrous for time series

---

## 6. PowerTransformer (Box-Cox / Yeo-Johnson)

### Principle

Applies a **non-linear transformation** to make data more Gaussian and stabilize variance.

Variants:

* Box-Cox: strictly positive values
* Yeo-Johnson: supports zero and negative values

Followed by standardization.

### When to Use

* Strongly skewed features
* Statistical modeling
* Linear models sensitive to normality assumptions

### Advantages

* Reduces skewness and kurtosis
* Improves linear model performance
* Often boosts interpretability

### Drawbacks

* Harder to interpret
* Requires careful inverse transformation
* Can distort original feature meaning

---

## 7. QuantileTransformer

### Principle

Maps the feature distribution to a target distribution:

* Uniform
* Gaussian

Based on empirical quantiles.

Scaling is **feature-wise**.

### When to Use

* Highly non-Gaussian data
* Extreme outliers dominate variance
* When rank information matters more than distance

### Advantages

* Very strong outlier handling
* Forces stable distributions

### Drawbacks

* Destroys metric structure
* Risk of overfitting
* Inverse transformation can be unstable

---

## Comparative Summary

| Scaler              | Feature-wise  | Outlier Robust | Preserves Sparsity | Typical Use Case      |
| ------------------- | ------------- | -------------- | ------------------ | --------------------- |
| StandardScaler      | Yes           | No             | Yes                | Regression, PCA, SVM  |
| MinMaxScaler        | Yes           | No             | Yes                | Neural Networks       |
| RobustScaler        | Yes           | Yes            | Yes                | Dirty real-world data |
| MaxAbsScaler        | Yes           | No             | Yes                | Sparse / NLP          |
| Normalizer          | No (row-wise) | N/A            | Yes                | Cosine similarity     |
| PowerTransformer    | Yes           | Partial        | No                 | Statistical modeling  |
| QuantileTransformer | Yes           | Yes            | No                 | Extreme distributions |

---

## Production & Interview Rules

* Always **fit scalers on training data only**
* Save scaling parameters for inference
* Avoid data leakage in time series
* Scaling choice is model- and data-dependent

> A good data scientist does not scale blindly — they justify the transformation.

---

