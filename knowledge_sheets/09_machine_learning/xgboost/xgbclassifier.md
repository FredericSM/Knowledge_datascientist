# XGBClassifier — Defaults & Quick Links

This section lists **all XGBClassifier parameters with their default values**.
Click on any parameter name to jump to its **detailed explanation section** below.

---

## 1. Core Task Parameters

| Parameter | Default | Link |
|---------|--------|------|
| `objective` | `binary:logistic` | [details](#objective) |
| `eval_metric` | depends on objective | [details](#eval_metric) |
| `num_class` | `None` | [details](#num_class) |
| `booster` | `gbtree` | [details](#booster) |

---

## 2. Boosting Parameters

| Parameter | Default | Link |
|---------|--------|------|
| `n_estimators` | `100` | [details](#n_estimators) |
| `learning_rate` | `0.3` | [details](#learning_rate-eta) |
| `base_score` | `0.5` | [details](#base_score) |

---

## 3. Tree Structure (Capacity)

| Parameter | Default | Link |
|---------|--------|------|
| `max_depth` | `6` | [details](#max_depth) |
| `min_child_weight` | `1` | [details](#min_child_weight) |
| `gamma` | `0` | [details](#gamma) |
| `max_delta_step` | `0` | [details](#max_delta_step) |
| `max_leaves` | `0` (unlimited) | [details](#max_leaves) |
| `grow_policy` | `depthwise` | [details](#grow_policy) |

---

## 4. Sampling (Overfitting Control)

| Parameter | Default | Link |
|---------|--------|------|
| `subsample` | `1.0` | [details](#subsample) |
| `colsample_bytree` | `1.0` | [details](#colsample_bytree) |
| `colsample_bylevel` | `1.0` | [details](#colsample_bylevel) |
| `colsample_bynode` | `1.0` | [details](#colsample_bynode) |

---

## 5. Regularization

| Parameter | Default | Link |
|---------|--------|------|
| `reg_lambda` | `1.0` | [details](#reg_lambda-l2) |
| `reg_alpha` | `0.0` | [details](#reg_alpha-l1) |

---

## 6. Class Imbalance (Binary Only)

| Parameter | Default | Link |
|---------|--------|------|
| `scale_pos_weight` | `1.0` | [details](#scale_pos_weight) |

---

## 7. Tree Construction & Performance

| Parameter | Default | Link |
|---------|--------|------|
| `tree_method` | `auto` | [details](#tree_method) |
| `max_bin` | `256` | [details](#max_bin) |
| `sampling_method` | `uniform` | [details](#sampling_method) |
| `predictor` | `auto` | [details](#predictor) |
| `n_jobs` | `None` | [details](#n_jobs) |

---

## 8. Categorical & Missing Data

| Parameter | Default | Link |
|---------|--------|------|
| `missing` | `np.nan` | [details](#missing) |
| `enable_categorical` | `False` | [details](#enable_categorical) |
| `max_cat_to_onehot` | `4` | [details](#max_cat_to_onehot) |
| `max_cat_threshold` | `64` | [details](#max_cat_threshold) |

---

## 9. Constraints (Production / Regulation)

| Parameter | Default | Link |
|---------|--------|------|
| `monotone_constraints` | `None` | [details](#monotone_constraints) |
| `interaction_constraints` | `None` | [details](#interaction_constraints) |

---

## 10. Randomness & Validation

| Parameter | Default | Link |
|---------|--------|------|
| `random_state` | `None` | [details](#random_state) |
| `seed` | `None` | [details](#seed) |
| `verbosity` | `1` | [details](#verbosity) |
| `validate_parameters` | `True` | [details](#validate_parameters) |

---

## 11. Experimental / Rare

| Parameter | Default | Link |
|---------|--------|------|
| `enable_experimental_json_serialization` | `False` | [details](#enable_experimental_json_serialization) |

---

# XGBClassifier.fit() — Defaults & Quick Links

This section lists **all parameters of `XGBClassifier.fit()` with their default values**.  
Click on any parameter name to jump to its **detailed explanation section** below.

---

## 1. Core Inputs

| Parameter | Default | Link |
|---------|--------|------|
| `X` | required | [details](#x) |
| `y` | required | [details](#y) |

---

## 2. Sample & Feature Weighting

| Parameter | Default | Link |
|---------|--------|------|
| `sample_weight` | `None` | [details](#sample_weight) |
| `feature_weights` | `None` | [details](#feature_weights) |

---

## 3. Initial Prediction Control

| Parameter | Default | Link |
|---------|--------|------|
| `base_margin` | `None` | [details](#base_margin) |

---

## 4. Validation & Evaluation

| Parameter | Default | Link |
|---------|--------|------|
| `eval_set` | `None` | [details](#eval_set) |
| `eval_metric` | constructor value | [details](#eval_metric-fit-time-override) |
| `sample_weight_eval_set` | `None` | [details](#sample_weight_eval_set) |
| `base_margin_eval_set` | `None` | [details](#base_margin_eval_set) |

---

## 5. Training Control

| Parameter | Default | Link |
|---------|--------|------|
| `early_stopping_rounds` | `None` | [details](#early_stopping_rounds) |
| `verbose` | `True` | [details](#verbose) |

---

## 6. Advanced / Power-User

| Parameter | Default | Link |
|---------|--------|------|
| `xgb_model` | `None` | [details](#xgb_model) |
| `callbacks` | `None` | [details](#callbacks) |

---

# How to Use This Section

- Use it as a **parameter index**
- Jump instantly to detailed explanations
- Check **true defaults** before overriding anything
- Combine with early stopping instead of tuning blindly

---

## Rule of Thumb

> If a parameter is not in **sections 1–5**,  
> you usually don’t need to touch it.

---

---

## `objective`

**Purpose**  
Defines the learning task and the loss function.  
This is the **single most important parameter**.

### Possible values (classification)
- `binary:logistic`  
  → Binary classification  
  → Outputs probabilities in (0, 1)

- `binary:hinge`  
  → Binary classification  
  → Outputs hard labels (0 / 1)  
  → No probabilities

- `multi:softprob`  
  → Multi-class classification  
  → Outputs probability distribution over classes  
  → **Recommended**

- `multi:softmax`  
  → Multi-class classification  
  → Outputs class index directly

### What really happens
- Defines the **loss**
- Defines the **gradient & Hessian**
- Controls how trees are trained

---

## `eval_metric`

**Purpose**  
Metric used for evaluation and early stopping.

### Common values
- Binary:
  - `logloss`
  - `auc`
  - `error`

- Multi-class:
  - `mlogloss`
  - `merror`

### Notes
- Does **not** affect training gradients
- Only affects **monitoring and early stopping**
- Can specify multiple metrics

---

## `num_class`

**Purpose**  
Number of target classes.

### Values
- Integer ≥ 2
- Required when `objective` starts with `multi:`

### Internal behavior
- XGBoost trains **one tree per class per boosting round**
- Training cost ≈ `num_class × binary model`

---

## `booster`

**Purpose**  
Defines the boosting model type.

### Possible values
- `gbtree` (default)  
  → Tree-based boosting (almost always used)

- `gblinear`  
  → Linear booster  
  → No trees, no interactions

- `dart`  
  → Dropout boosting  
  → Rare, experimental

### Recommendation
Use `gbtree` unless you know exactly why not.

---

## `n_estimators`

**Purpose**  
Maximum number of boosting rounds (trees).

### Default
`100`

### Best practice
- Set **high**
- Use `early_stopping_rounds`

### Internal behavior
Each iteration adds one (or more) trees to the ensemble.

---

## `learning_rate` (`eta`)

**Purpose**  
Controls how much each tree contributes.

### Default
`0.3`

### Typical values
- `0.05` → stable
- `0.1` → faster
- `< 0.05` → very stable, slow

### Internal meaning
Shrinkage factor applied to leaf weights.

---

## `base_score`

**Purpose**  
Initial prediction before any trees.

### Default
- Binary: `0.5`
- Multi-class: uniform

### When to change
Almost never.

---

## `max_depth`

**Purpose**  
Maximum depth of each tree.

### Default
`6`

### Typical values
- `3–4` → strong regularization
- `5–6` → more expressive

### Internal meaning
Controls **interaction order**:
- Depth 1 = linear
- Depth k = k-way interactions

---

## `min_child_weight`

**Purpose**  
Minimum Hessian (≈ sample weight) in a leaf.

### Default
`1`

### Effect
- Higher → fewer splits
- Higher → more conservative model

### Internal meaning
Prevents learning from unreliable small regions.

---

## `gamma`

**Purpose**  
Minimum loss reduction required to split.

### Default
`0`

### Typical values
`0–0.3`

### Internal meaning
Penalty for creating a new node.

---

## `max_delta_step`

**Purpose**  
Limits how much leaf weights can change.

### Default
`0` (no limit)

### Use case
Extreme class imbalance.

---

## `max_leaves`

**Purpose**  
Maximum number of leaves per tree.

### Default
`0` (unlimited)

### Used with
`grow_policy="lossguide"`

---

## `grow_policy`

**Purpose**  
Controls tree growth strategy.

### Values
- `depthwise` (default)  
  → Balanced trees

- `lossguide`  
  → Grow leaves with highest loss first  
  → Wide trees, used for huge datasets

---

## `subsample`

**Purpose**  
Row subsampling per tree.

### Default
`1.0`

### Typical values
`0.6–0.9`

### Internal meaning
Introduces stochasticity, reduces variance.

---

## `colsample_bytree`

**Purpose**  
Feature subsampling per tree.

### Default
`1.0`

### Typical values
`0.6–0.9`

---

## `colsample_bylevel`

**Purpose**  
Feature subsampling per tree level.

### Default
`1.0`

---

## `colsample_bynode`

**Purpose**  
Feature subsampling per split.

### Default
`1.0`

### Note
Rarely needed.

---

## `reg_lambda` (L2)

**Purpose**  
L2 regularization on leaf weights.

### Default
`1.0`

### Effect
Smooths predictions, reduces overfitting.

---

## `reg_alpha` (L1)

**Purpose**  
L1 regularization on leaf weights.

### Default
`0.0`

### Effect
Encourages sparse leaf weights.

---

## `scale_pos_weight`

**Purpose**  
Balances positive vs negative class.

### Default
`1.0`

### Rule of thumb
`scale_pos_weight = n_negative / n_positive``


### Binary only.

---

## `tree_method`

**Purpose**  
Tree construction algorithm.

### Values
- `auto`
- `exact`
- `hist` (recommended)
- `gpu_hist`

---

## `max_bin`

**Purpose**  
Number of bins for histogram-based splits.

### Default
`256`

---

## `sampling_method`

**Purpose**  
Sampling strategy for histogram.

### Values
- `uniform`
- `gradient_based` (large datasets)

---

## `predictor`

**Purpose**  
Prediction backend.

### Values
- `auto`
- `cpu_predictor`
- `gpu_predictor`

---

## `n_jobs`

**Purpose**  
Number of CPU threads.

### Default
All available cores.

---

## `missing`

**Purpose**  
Value treated as missing.

### Default
`np.nan`

---

## `enable_categorical`

**Purpose**  
Enable native categorical splits.

### Default
`False`

---

## `max_cat_to_onehot`

**Purpose**  
Threshold for one-hot vs partition-based split.

### Default
`4`

---

## `max_cat_threshold`

**Purpose**  
Max number of categories considered per split.

### Default
`64`

---

## `monotone_constraints`

**Purpose**  
Enforce monotonic relationships.

### Example
`(1, 0, -1)``

---

## `interaction_constraints`

**Purpose**  
Restrict which features can interact.

---

## `random_state` / `seed`

**Purpose**  
Reproducibility.

---

## `verbosity`

**Purpose**  
Logging level.

### Values
- `0` → silent
- `1` → default
- `2+` → verbose

---

## `validate_parameters`

**Purpose**  
Check parameter validity.

### Default
`True`

---

## `enable_experimental_json_serialization`

**Purpose**  
Enable experimental JSON model export.

### Default
`False`

---

## Final Mental Model

- **Objective** defines *what is optimized*
- **Tree parameters** define *what can be learned*
- **Sampling + regularization** define *how stable it is*
- Everything else is **infrastructure**

---

# Parameter Details

---

## `X`

**Purpose**  
Training feature matrix.

**Type**  
Array-like of shape `(n_samples, n_features)`

**Accepted formats**
- NumPy array
- pandas DataFrame
- SciPy sparse matrix

---

## `y`

**Purpose**  
Training labels.

**Constraints**
- Binary classification: `{0, 1}`
- Multi-class classification: `{0, …, num_class - 1}`

---

## `sample_weight`

**Purpose**  
Assigns a weight to each training sample.

**Default**  
`None`

**When to use**
- Class imbalance (especially multi-class)
- Cost-sensitive classification
- Unequal importance of observations

**Internal behavior**
- Multiplies gradients and Hessians:
  \[
  g_i \leftarrow w_i g_i,\quad h_i \leftarrow w_i h_i
  \]

---

## `feature_weights`

**Purpose**  
Applies weights to features during split selection.

**Default**  
`None`

**Use cases**
- Penalize noisy or unstable features
- Encourage trusted or physically meaningful features

⚠️ Advanced usage.

---

## `base_margin`

**Purpose**  
Initial raw prediction score (logit) per sample.

**Default**  
`None`

**When to use**
- Stacking
- Warm-starting from another model
- Injecting prior knowledge

**Note**
Overrides constructor parameter `base_score`.

---

## `eval_set`

**Purpose**  
Validation datasets used during training.

**Default**  
`None`

**Used for**
- Metric monitoring
- Early stopping
- Overfitting detection

**Example**
```python
eval_set=[(X_val, y_val)]
```

## `eval_metric` (fit-time override)

**Purpose**  
Overrides the constructor `eval_metric`.

**Default**  
Uses the value set in the constructor.

**Notes**
- Can be a string or list
- Does **NOT** affect training gradients
- Used only for monitoring / early stopping

---

## `sample_weight_eval_set`

**Purpose**  
Sample weights applied to validation datasets.

**Default**  
`None`

**Use case**  
Weighted validation metrics.

---

## `base_margin_eval_set`

**Purpose**  
Initial prediction margins for validation datasets.

**Default**  
`None`

**Advanced use**  
Stacking / warm-starting validation.

---

## `early_stopping_rounds`

**Purpose**  
Stops training if the evaluation metric does not improve.

**Default**  
`None`

**Requirements**
- `eval_set` must be provided

**Side effects**
- Sets `best_iteration`
- Sets `best_score`

---

## `verbose`

**Purpose**  
Controls training logs.

**Default**  
`True`

**Values**
- `True` → log every iteration
- `False` → silent
- `int` → log every `n` iterations

---

## `xgb_model`

**Purpose**  
Continue training from an existing model.

**Default**  
`None`

**Use cases**
- Incremental learning
- Resume interrupted runs

---

## `callbacks`

**Purpose**  
Custom hooks into the training loop.

**Default**  
`None`

**Examples**
- Custom early stopping logic
- Learning rate schedules
- Advanced logging

⚠️ Advanced usage.

---

## Mental model

> **Constructor parameters** define *what the model can learn*  
> **`.fit()` parameters** define *how training is executed*

---

