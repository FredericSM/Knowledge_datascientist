# Machine Learning Encoders – Complete Practical & Conceptual Cheat Sheet

The encoders are grouped by:

* **Encoders to master perfectly** (daily usage, interviews, production)
* **Encoders to understand conceptually**
* **Encoders to recognize by name**

---

## What Is Encoding and Why It Matters

**Encoding** is the process of transforming categorical variables into numerical representations that machine learning algorithms can process.

Unlike scaling, encoding:

* Injects *inductive bias*
* Can change distance geometry
* Can introduce **severe data leakage** if done incorrectly

Key questions before choosing an encoder:

1. Is there an intrinsic order between categories?
2. What is the cardinality?
3. Is the model distance-based, linear, tree-based, or neural?
4. What is the risk of leakage?

---

## Table of Contents

1. [Part I – Encoders to Master Perfectly](#part-i---encoders-to-master-perfectly)
   - [One-Hot Encoding (OHE)](#1-one-hot-encoding-ohe)
   - [Ordinal Encoding](#2-ordinal-encoding)
   - [Binary Encoding](#3-binary-encoding)
   - [Frequency / Count Encoding](#4-frequency--count-encoding)
   - [Target Encoding (Mean Encoding)](#5-target-encoding-mean-encoding)
   - [Leave-One-Out Encoding (LOO)](#6-leave-one-out-encoding-loo)
   - [Hashing Encoder (Feature Hashing)](#7-hashing-encoder-feature-hashing)
   - [Embeddings (Entity Embeddings)](#8-embeddings-entity-embeddings)

2. [Part II – Encoders to Know Conceptually](#part-ii---encoders-to-know-conceptually)
   - [Weight of Evidence (WoE)](#9-weight-of-evidence-woe)
   - [Helmert Encoding](#10-helmert-encoding)
   - [Sum Encoding (Deviation Encoding)](#11-sum-encoding-deviation-encoding)
   - [Polynomial / Contrast Encoding](#12-polynomial--contrast-encoding)

3. [Part III – Encoders to Recognize by Name](#part-iii---encoders-to-recognize-by-name)



---

## 1. Categorical Encoding Methods Recap

| Encoding | Supervised | Uses Target | Dimensionality | Leakage Risk | Handles High Cardinality | Interpretability | Typical Use Cases |
|--------|------------|-------------|----------------|--------------|--------------------------|------------------|------------------|
| One-Hot Encoding | ❌ No | ❌ No | High (K) | ❌ None | ❌ Poor | ✅ High | Low-cardinality categories, linear models |
| Ordinal Encoding | ❌ No | ❌ No | 1 | ❌ None | ⚠️ Limited | ⚠️ Medium | True ordinal features, tree models |
| Binary Encoding | ❌ No | ❌ No | log₂(K) | ❌ None | ✅ Good | ⚠️ Low | Large cardinality, memory-constrained setups |
| Target Encoding (Naive) | ✅ Yes | ✅ Yes | 1 | 🚨 High | ✅ Excellent | ⚠️ Medium | ❌ Should be avoided |
| Target Encoding (K-Fold) | ✅ Yes | ✅ Yes | 1 | ⚠️ Controlled | ✅ Excellent | ⚠️ Medium | XGBoost / LightGBM with care |
| Leave-One-Out Encoding (LOO) | ✅ Yes | ✅ Yes | 1 | ⚠️ Controlled | ✅ Excellent | ⚠️ Medium | Medium–large datasets |
| LOO + Smoothing | ✅ Yes | ✅ Yes | 1 | ✅ Safe | ✅ Excellent | ⚠️ Medium | **Best practice for manual target encoding** |
| Hashing Encoder | ❌ No | ❌ No | Fixed | ❌ None | ✅ Excellent | ❌ None | Streaming, IDs, very large vocabularies |
| WoE (Weight of Evidence) | ✅ Yes | ✅ Yes | 1 | ⚠️ Needs care | ⚠️ Limited | ✅ Very High | Credit scoring, logistic regression |
| Helmert Encoding | ❌ No | ❌ No | K−1 | ❌ None | ❌ Poor | ✅ High | Statistics, ANOVA, GLM |


## 2. Target Encoding Strategies (Deep Dive)

| Strategy | Leakage-Free | Variance | Complexity | Recommended |
|-------|--------------|----------|------------|------------|
| Naive Target Encoding | ❌ No | Low | Low | ❌ Never |
| K-Fold Target Encoding | ✅ Yes | Medium | Medium | ✅ Yes |
| Leave-One-Out (LOO) | ✅ Yes | High | Low | ⚠️ With smoothing |
| LOO + Smoothing | ✅ Yes | Controlled | Medium | ✅ Best manual choice |
| CatBoost Ordered Encoding | ✅ Yes | Controlled | Low | ✅ Best automatic choice |

---

## Part I - Encoders to Master Perfectly

These encoders **must be fully understood**, including their math, assumptions, and failure modes.

---

## 1. One-Hot Encoding (OHE)

### Principle

Each category is mapped to a binary vector with exactly one active component.

For a categorical variable `C` with `K` categories {$c_1$, ..., $c_K$}, we encode it as a binary vector
x ∈ {0,1}$^K$ such that:

- $x_j$ = 1  if  C = $c_j$
- $x_j$ = 0  otherwise


This encoding is **feature-wise** and produces sparse representations.

### When to Use

* Nominal (unordered) categories
* Low cardinality
* Linear models, SVMs, k-NN, neural networks

### Advantages

* No artificial ordering introduced
* Highly interpretable
* Works with most algorithms

### Drawbacks

* Dimensional explosion
* Sparse high-dimensional matrices
* Becomes unusable for high cardinality features

---

## 2. Ordinal Encoding

### Principle

Each category is mapped to an integer according to a predefined order:

c₁ < c₂ < … < c_K  →  ordinal(c_j) = j

This encoding assumes that the categories have a **meaningful and consistent ordering**.

---

### When to Use

- Categories with **true ordinal semantics**
  - education level (high school < bachelor < master < PhD)
  - ratings (poor < fair < good < excellent)
- Models that can naturally handle ordered values:
  - tree-based models
  - models with monotonic constraints

---

### Advantages

- Compact representation (single feature)
- Preserves ordering information
- Efficient for tree-based models

---

### Drawbacks

- Introduces **artificial distances** between categories
- Assumes equal spacing between successive categories
- Can severely degrade performance if the order is incorrect

---

### Important Note: Cyclic Ordinal Variables

Ordinal encoding is **not suitable** for cyclic variables such as:
- hour of the day
- day of the week
- month of the year

Although these variables have an order, they are **circular**, not linear.

For such cases, a **cyclical encoding** should be used instead:

x_sin = sin(2πx / N)  
x_cos = cos(2πx / N)

This representation preserves the circular structure and ensures that values near the boundaries (e.g., 23h and 0h) remain close in the encoded space.

---

## 3. Binary Encoding

### Principle

Categories are first mapped to integers, then integers are represented in binary form.

Let:

c → id(c) ∈ ℕ

Binary encoding maps id(c) to its binary decomposition across ⌈log₂(K)⌉ features.

### When to Use

* Medium to high cardinality
* When One-Hot is too expensive

### Advantages

* Logarithmic dimensionality
* Reduced sparsity

### Drawbacks

* Reduced interpretability
* Weak implicit ordering remains

---

## 4. Frequency / Count Encoding

### Principle

Each category is replaced by its frequency or count:

freq(c) = |{i : $X_i$ = c}| / N

or

count(c) = |{i : $X_i$ = c}|

### When to Use

* Linear or tree-based models
* Large datasets
* Location / ID-like categorical features

### Advantages

* Extremely simple
* No dimensional increase

### Drawbacks

* Loses category identity
* Can encode dataset-specific bias

---

## 5. Target Encoding (Mean Encoding)

### Principle

Each category is replaced by the conditional expectation of the target given the category.

For regression:

TE(c) = E[Y | X = c]

For binary classification:

TE(c) = (1 / |$I_c$|) · $Σ_{i∈I_c}$ yᵢ

where $I_c$ = {i : $X_i$ = c}

Often regularized using global mean μ:

$TE_λ$(c) = ($n_c$ · TE(c) + λ · μ) / ($n_c$ + λ)

### When to Use

- Very high cardinality categorical features
- Categorical variables strongly correlated with the target
- Tree-based models (GBM, XGBoost, LightGBM, CatBoost)
- Large datasets with sufficient observations per category

---

### Advantages

- Very strong predictive power
- Constant dimensionality (1 feature)
- Avoids sparse representations

---

### Drawbacks

- Extremely prone to **data leakage**
- High risk of overfitting, especially for rare categories
- Requires careful validation strategy

---

### How to Use It Correctly (Mandatory)

Target encoding must be applied in a way that **prevents leakage of the target into the features**.

#### 1. Cross-Fitting (Out-of-Fold Encoding)

Target statistics must be computed **without using the observation being encoded**.

Procedure:
1. Split the training data into K folds.
2. For each fold:
   - Compute category-wise target means using the remaining K−1 folds.
   - Encode the held-out fold using these means.
3. For the test set:
   - Encode using statistics computed on the full training set.

This ensures that each encoded value is independent of its own target.

---

## 6. Leave-One-Out Encoding (LOO)

### Principle

Leave-One-Out encoding is a variation of target encoding where the current observation is explicitly excluded from the category statistics.

For an observation \( i \) belonging to category \( c \):

$LOO(c)_i$ = ($Σ_{j ∈ I_c, j ≠ i}$ $y_j$) / (|$I_c$| − 1)

where \( $I_c$ = \{ j : $X_j$ = c \} \).

This guarantees that the encoded value for observation \( i \) does **not** depend on its own target \( $y_i$ \).

---

### When to Use

- Medium to large datasets
- Categorical variables with multiple observations per category
- Situations where strict leakage control is critical
- Tree-based models or regularized linear models

---

### Advantages

- Prevents direct target leakage by construction
- Uses nearly all available data for each encoded observation
- Often more efficient than K-fold target encoding
- Simple to implement

---

### Drawbacks

- High variance for rare categories
- Undefined when a category appears only once
- Still target-dependent, hence sensitive to noise
- Requires regularization to avoid overfitting

---

### Leave-One-Out with Smoothing (Recommended)

To stabilize the encoding for rare categories, LOO encoding is typically combined with smoothing toward the global mean \( \mu \):

$LOO_λ(c)_i$ = {$Σ_{j ∈ I_c}$ $y_j$ - $y_i$ + λ . μ} / {(|$I_c$| - 1) + λ}

where:
- \( μ \) is the global mean of the target,
- \( λ \) controls the strength of the regularization.

As \( |$I_c$| \) increases, the encoding relies more on category-specific information;  
as \( |$I_c$| \) decreases, it smoothly reverts toward the global mean.

---

### Practical Notes

- For categories with a single observation, the encoding defaults to the global mean.
- LOO encoding can be viewed as an extreme case of K-fold target encoding with \( K = n \).
- Smoothing is mandatory in practice to control variance.

---

### Practical Rule

Leave-One-Out encoding should **never** be used without smoothing.  
For small datasets or highly sparse categories, K-fold target encoding is often preferable.


---

## 7. Hashing Encoder (Feature Hashing)

### Principle

A hash function maps categories into a fixed-dimensional space:

index = hash(c) mod D

Collisions are allowed and unavoidable.

### When to Use

* NLP pipelines
* Streaming data
* Unknown or infinite cardinality

### Advantages

* Constant memory footprint
* No fitting required
* Very fast

### Drawbacks

* Hash collisions
* Not interpretable
* Not invertible

---

## 8. Embeddings (Entity Embeddings)

### Principle

Each category is mapped to a dense vector learned during model training:

c → e_c ∈ ℝ^d

Embeddings are optimized jointly with the loss function.

### When to Use

* Deep learning models
* Very high cardinality features
* When category similarity matters

### Advantages

* Captures semantic similarity
* Extremely powerful representations

### Drawbacks

* Requires large datasets
* Poor interpretability
* Model-dependent

---

## Part II - Encoders to Know Conceptually

These encoders are mostly used in **statistical modeling** or **regulated environments**.

---

## 9. Weight of Evidence (WoE)

### Principle

Used for binary classification:

WoE(c) = ln( P(X=c | Y=1) / P(X=c | Y=0) )

### Usage

* Credit scoring
* Risk and compliance models

### Properties

* Monotonic
* Highly interpretable
* Strong regulatory acceptance

---

## 10. Helmert Encoding

### Principle

Each category is contrasted against the mean of subsequent categories.

### Usage

* ANOVA
* Linear hypothesis testing

---

## 11. Sum Encoding (Deviation Encoding)

### Principle

Each category is compared to the overall mean effect.

### Usage

* Interpretable linear models

---

## 12. Polynomial / Contrast Encoding

### Principle

Encodes linear, quadratic, or higher-order trends over ordered categories.

### Usage

* Ordinal regression
* Statistical inference

---

## Part III - Encoders to Recognize by Name

These encoders are rarely required in practice but appear in advanced libraries or research.

* Bayesian Encoding
* James–Stein Encoding
* M-Estimate Encoding
* Thermometer Encoding
* Forward Difference Encoding
* Backward Difference Encoding

Knowing **what problem they address** is sufficient.

---

## Practical Selection Guidelines

| Scenario                 | Recommended Encoder  |
| ------------------------ | -------------------- |
| Low cardinality, nominal | One-Hot              |
| Ordinal categories       | Ordinal / Polynomial |
| High cardinality, trees  | Target / LOO         |
| Streaming / NLP          | Hashing              |
| Deep learning            | Embeddings           |
| Regulated risk models    | WoE                  |

---

## Final Interview Rule

> Encoding is not a preprocessing detail — it is a modeling decision that embeds assumptions, bias, and leakage risk.


