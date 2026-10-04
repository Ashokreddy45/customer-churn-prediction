# Model Card

## Model Overview

The Customer Churn Intelligence Platform predicts the probability that
a customer will churn.

The model is designed as a decision-support component for customer
retention analysis.

The application combines prediction with risk segmentation,
explainability, and business impact analysis.

---

## Intended Use

The model can be used to:

- Identify customers with higher predicted churn risk.
- Rank customers by churn probability.
- Support retention prioritization.
- Explain individual customer predictions.
- Estimate the potential impact of retention strategies.

The model should be treated as a decision-support tool rather than an
automated decision-making system.

---

## Models Evaluated

The project benchmarks four classification algorithms:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting
4. XGBoost

Models are compared using cross-validation before selecting the final
model.

---

## Data Processing

The model pipeline includes:

- Numerical imputation
- Categorical imputation
- Numerical scaling
- One-hot encoding
- Stratified train/test splitting

Preprocessing is implemented using scikit-learn pipelines to reduce the
risk of data leakage.

---

## Evaluation

The model is evaluated using:

- ROC-AUC
- PR-AUC
- F1 Score
- Precision
- Recall
- Accuracy

The classification decision threshold is optimized instead of assuming
that 0.50 is always the best threshold.

---

## Explainability

SHAP is used to provide local explanations for individual predictions.

The explainability component helps users understand which input features
contributed to a customer's predicted churn probability.

---

## Current Demonstration Results

The currently deployed demonstration application reports:

| Metric | Result |
|---|---:|
| Customers | 5,000 |
| Churn Rate | 42.0% |
| Best Model | Logistic Regression |
| Test ROC-AUC | 0.769 |
| Decision Threshold | 0.42 |

These results correspond to the included demonstration dataset.

---

## Limitations

### Demonstration Dataset

The included dataset is intended for reproducible demonstration and
portfolio purposes.

Performance on a real production dataset may differ substantially.

### Distribution Changes

Customer behavior can change over time. Model performance should
therefore be monitored when used with new data.

### Business Assumptions

The business impact simulation depends on assumptions such as:

- Number of customers targeted
- Monthly revenue per customer
- Expected retention rate
- Intervention cost

These assumptions should be replaced with validated business values
before production use.

### Model Interpretation

SHAP explanations describe model behavior and should not automatically
be interpreted as causal relationships.

---

## Responsible Use

The model should not be used as the sole basis for decisions that could
negatively affect individual customers.

Predictions should be reviewed alongside business context and appropriate
human judgment.