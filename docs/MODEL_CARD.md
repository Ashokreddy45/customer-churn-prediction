# Model Card

## 1. Model Overview

The Customer Churn Intelligence Platform uses supervised machine learning to estimate the probability that a customer will churn.

Multiple classification models are benchmarked before selecting the final model.

Current evaluated models:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

The current demonstration selects:

```text
Logistic Regression
```

as the best model according to the benchmarked ROC-AUC result.

---

# 2. Intended Use

The model is intended for:

- Educational demonstrations
- Machine learning portfolio development
- Customer churn analysis
- Risk segmentation demonstrations
- Model explainability demonstrations
- Business impact analysis demonstrations

The model can be used to demonstrate how customer-level churn probabilities could support retention prioritization.

---

# 3. Out-of-Scope Use

The model should not be used directly for:

- Automated high-stakes customer decisions
- Customer denial of essential services
- Financial decisions without additional validation
- Production retention campaigns without proper business validation
- Individual customer decisions based solely on model output

The demonstration dataset and model have not been validated for production use.

---

# 4. Training Data

The repository includes a synthetic Telco-style demonstration dataset.

Current demonstration dataset:

```text
5,000 records
16 columns
```

Target:

```text
Churn
```

The target is represented internally as:

```text
1 = churn
0 = no churn
```

---

# 5. Features

The dataset includes customer-level attributes such as:

- Demographic information
- Partner/dependent information
- Tenure
- Phone service
- Internet service
- Online security
- Technical support
- Contract type
- Billing preferences
- Payment method
- Monthly charges
- Total charges

---

# 6. Preprocessing

The preprocessing pipeline contains separate numeric and categorical transformations.

### Numeric

```text
Median Imputation
        ↓
StandardScaler
```

### Categorical

```text
Most-Frequent Imputation
        ↓
OneHotEncoder
```

The categorical encoder uses:

```python
OneHotEncoder(handle_unknown="ignore")
```

This helps handle unseen categorical values during prediction.

---

# 7. Model Selection

The system benchmarks several classification algorithms.

```text
Training Data
     ↓
Cross-Validation
     ↓
Model Benchmarking
     ↓
ROC-AUC Comparison
     ↓
Best Model
```

The current demonstration selects Logistic Regression as the best benchmarked model.

---

# 8. Evaluation Metrics

The project evaluates models using:

- ROC-AUC
- Precision
- Recall
- F1 Score
- Confusion Matrix

ROC-AUC is used as an important ranking metric because the application generates churn probabilities rather than only binary classifications.

---

# 9. Current Demonstration Results

Current demonstration results:

| Metric | Result |
|---|---:|
| Dataset Size | 5,000 |
| Churn Rate | 42.0% |
| Selected Model | Logistic Regression |
| Test ROC-AUC | 0.769 |
| Decision Threshold | 0.42 |

These results are specific to the included demonstration dataset.

They should not be interpreted as expected production performance.

---

# 10. Decision Threshold

The application does not assume that the default threshold of `0.50` is always appropriate.

A threshold is calculated using prediction behavior and the project's evaluation process.

Current demonstration:

```text
Threshold = 0.42
```

Changing the threshold can affect:

- Precision
- Recall
- F1 Score
- Number of customers classified as high risk

The appropriate production threshold would depend on the business cost of false positives and false negatives.

---

# 11. Explainability

The project uses SHAP-based explainability.

The purpose is to provide information about which model features contribute to an individual prediction.

Important distinction:

> A model explanation describes how the model arrived at a prediction; it does not establish a causal relationship.

---

# 12. Risk Segmentation

Predicted churn probabilities are mapped to customer risk bands.

This allows users to prioritize customers based on predicted risk.

Risk segmentation is intended as a decision-support mechanism rather than an automatic business decision system.

---

# 13. Business Impact

The application provides a simplified retention economics simulation.

Inputs include:

- Target customer count
- Monthly revenue per customer
- Expected save rate
- Intervention cost

The output estimates potential retention economics.

These values are scenario assumptions rather than observed financial outcomes.

---

# 14. Fairness Considerations

The demonstration dataset contains demographic variables such as gender and senior-citizen status.

Before production deployment, these variables should be evaluated carefully for:

- Disparate impact
- Performance differences across groups
- Data quality issues
- Potential proxy relationships
- Business and regulatory requirements

A production model should undergo an appropriate fairness and governance review.

---

# 15. Limitations

Major limitations include:

### Synthetic Data

The included dataset is synthetic.

### Distribution Shift

A model trained on one customer population may perform differently on another.

### Probability Calibration

Predicted probabilities should be evaluated and calibrated before being interpreted as reliable real-world probabilities.

### Business Assumptions

The business impact simulator depends on assumptions supplied by the user.

### Causality

Model explanations do not prove that changing a feature would cause a customer to behave differently.

---

# 16. Monitoring Requirements for Production

A production implementation should monitor:

- ROC-AUC
- Precision
- Recall
- F1
- Calibration
- Prediction distribution
- Feature distribution
- Data quality
- Missing-value rates
- Population drift
- Model drift
- Business retention outcomes

---

# 17. Responsible Use

The model should be treated as a decision-support system.

Human review and business context should be incorporated before acting on predictions.

The model should not be treated as a guarantee that a customer will churn.

---

# 18. Versioning

This model card documents the current portfolio implementation.

For production use, model versions should additionally record:

- Training dataset version
- Feature version
- Model version
- Hyperparameters
- Evaluation dataset
- Evaluation metrics
- Training timestamp
- Deployment version