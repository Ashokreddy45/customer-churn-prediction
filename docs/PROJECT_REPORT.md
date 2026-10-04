# Customer Churn Intelligence Platform
## Technical Project Report

---

# 1. Project Overview

The Customer Churn Intelligence Platform is an end-to-end machine learning project designed to predict customer churn and convert model predictions into actionable customer risk and business insights.

The system combines:

- Data preprocessing
- Machine learning
- Model benchmarking
- Probability prediction
- Threshold optimization
- Risk segmentation
- Explainable AI
- Business impact simulation
- Interactive visualization
- API support
- Automated testing

The primary user interface is implemented using Streamlit.

---

# 2. Problem Statement

Customer churn can negatively affect recurring revenue and customer lifetime value.

A churn prediction system can help identify customers who are more likely to leave.

However, a useful business-facing solution should provide more than a binary classification.

The project therefore focuses on three main questions:

```text
Who is likely to churn?
        ↓
Why is the customer considered risky?
        ↓
What could the business gain from intervention?
```

---

# 3. Project Objectives

The main objectives are:

1. Build a reproducible churn prediction pipeline.
2. Compare multiple classification models.
3. Evaluate models using appropriate metrics.
4. Generate customer-level churn probabilities.
5. Optimize the classification threshold.
6. Segment customers according to predicted risk.
7. Provide model explanations.
8. Connect predictions with simplified business impact analysis.
9. Provide an interactive dashboard.
10. Include automated testing and technical documentation.

---

# 4. Dataset

The project includes a synthetic Telco-style dataset.

Current demonstration dataset:

```text
Rows: 5,000
Columns: 16
```

The dataset contains:

- Customer identifiers
- Demographic information
- Customer relationship information
- Service information
- Contract information
- Billing information
- Churn target

Main target:

```text
Churn
```

Target encoding:

```text
Yes → 1
No  → 0
```

---

# 5. Data Preprocessing

The data cleaning workflow includes:

1. Column name normalization.
2. Numeric conversion of `TotalCharges`.
3. Churn target conversion.
4. Customer ID conversion to string.
5. Duplicate removal.
6. Index reset.

---

# 6. Feature Engineering

The feature preparation pipeline separates numerical and categorical variables.

## Numeric Features

Numeric features use:

```text
Median Imputation
       ↓
Standard Scaling
```

## Categorical Features

Categorical features use:

```text
Most-Frequent Imputation
       ↓
One-Hot Encoding
```

The encoder uses:

```python
OneHotEncoder(handle_unknown="ignore")
```

This allows unseen categories to be handled during inference.

---

# 7. Train/Test Strategy

The project separates the dataset into training and test subsets.

The split uses stratification so that the target distribution is represented in both subsets.

The project uses a fixed random state to improve reproducibility.

Conceptually:

```text
Full Dataset
     │
     ├───────────────┐
     ▼               ▼
Training Set      Test Set
     │               │
     ▼               │
Cross-Validation     │
     │               │
     ▼               │
Model Selection      │
     │               │
     └───────┬───────┘
             ▼
       Final Evaluation
```

---

# 8. Machine Learning Models

The project benchmarks four classification approaches.

## Logistic Regression

A linear classification model that provides a strong baseline and interpretable coefficients.

## Random Forest

An ensemble of decision trees capable of modeling nonlinear relationships.

## Gradient Boosting

A boosting-based tree model that sequentially improves prediction performance.

## XGBoost

A gradient boosting implementation designed for high-performance tabular machine learning.

---

# 9. Model Benchmarking

Models are benchmarked using cross-validation.

The purpose is to compare algorithms under the same training conditions.

The current demonstration selects:

```text
Logistic Regression
```

as the best-performing benchmark model.

---

# 10. Model Evaluation

The project evaluates classification performance using:

- ROC-AUC
- Precision
- Recall
- F1 Score
- Confusion Matrix

ROC-AUC is particularly useful for evaluating the ranking quality of churn probabilities.

---

# 11. Current Results

Current demonstration results:

| Metric | Result |
|---|---:|
| Customers | 5,000 |
| Churn Rate | 42.0% |
| Best Model | Logistic Regression |
| Test ROC-AUC | 0.769 |
| Decision Threshold | 0.42 |

These results are specific to the demonstration dataset.

---

# 12. Decision Threshold Optimization

The default binary classification threshold is often:

```text
0.50
```

However, this project calculates a threshold based on the evaluation process.

Current threshold:

```text
0.42
```

A lower threshold can increase the number of customers identified as potential churners, which can affect recall and precision.

In a production environment, threshold selection should incorporate the actual costs associated with:

- False positives
- False negatives
- Retention campaigns
- Lost customers

---

# 13. Customer Risk Segmentation

The system generates a probability for each customer.

Example conceptual output:

```text
Customer
    ↓
0.82 churn probability
    ↓
High-risk customer
```

The dashboard allows users to sort customers according to churn probability.

This makes it possible to prioritize customers for further analysis or potential retention action.

---

# 14. Explainable AI

The platform includes SHAP-based explainability.

SHAP provides feature contribution information for individual model predictions.

The objective is to provide transparency around the model's output.

For example:

```text
Prediction
    ↓
Feature Contributions
    ↓
Interpretation
```

SHAP explanations should be interpreted as explanations of model behavior and not as causal evidence.

---

# 15. Business Impact Simulation

A machine learning model is more useful when its predictions can be connected to business decisions.

The platform includes a retention economics simulation.

Users can specify:

```text
Number of customers targeted
Monthly revenue/customer
Expected save rate
Intervention cost/customer
```

The application then estimates potential retention economics.

The simulation is intended to demonstrate how churn predictions could support business decision-making.

It is not a financial forecasting model.

---

# 16. Streamlit Application

The main application is:

```text
app.py
```

The interface contains five major sections.

## Overview

Provides portfolio-level churn insights.

## Model Benchmark

Displays model comparison and evaluation results.

## Customer Risk

Displays customer-level churn probabilities and risk bands.

## Explainability

Allows investigation of individual customer predictions.

## Business Impact

Provides retention economics simulation.

---

# 17. FastAPI Service

The project also includes:

```text
api.py
```

The FastAPI service provides an API-oriented layer for future integrations.

Run locally:

```bash
uvicorn api:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 18. Testing

Automated testing is implemented using Pytest.

Run:

```bash
python -m pytest -q
```

Current result:

```text
3 passed
```

The test suite provides a basic regression check for the project's core functionality.

---

# 19. Deployment

The Streamlit application is deployed using Streamlit Community Cloud.

Deployment architecture:

```text
GitHub
   ↓
Streamlit Community Cloud
   ↓
Python Environment
   ↓
requirements.txt
   ↓
Streamlit Application
```

Live application:

```text
https://customer-churn-prediction-akvxzgjsjcfaqchilwzygz.streamlit.app/
```

---

# 20. Technology Stack

### Programming

Python 3.12

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- XGBoost
- SciPy
- Joblib

### Explainability

- SHAP

### Visualization

- Plotly

### Application

- Streamlit

### API

- FastAPI
- Uvicorn

### Testing

- Pytest

### Deployment

- Streamlit Community Cloud

---

# 21. Project Structure

```text
customer-churn-intelligence-platform/
│
├── app.py
├── api.py
├── requirements.txt
├── runtime.txt
├── Makefile
├── README.md
├── run.sh
├── train.sh
├── api.sh
│
├── data/
│   └── demo_telco_churn.csv
│
├── src/
│   └── churn/
│       ├── data.py
│       ├── features.py
│       ├── models.py
│       ├── evaluation.py
│       ├── explainability.py
│       └── business.py
│
├── tests/
│
├── scripts/
│
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── DATA_DICTIONARY.md
│   ├── MODEL_CARD.md
│   └── PROJECT_REPORT.md
│
├── screenshots/
│   ├── overview.png
│   ├── model-benchmark.png
│   ├── customer-risk.png
│   ├── explainability.png
│   └── business-impact.png
│
└── .github/
    └── workflows/
```

---

# 22. Limitations

The current project has several limitations.

## Synthetic Data

The demonstration dataset is synthetic and does not represent a specific real-world company.

## Production Performance

The reported ROC-AUC should not be interpreted as production performance.

## Business Assumptions

The business impact simulation depends on assumptions entered by the user.

## Model Generalization

Performance may change when the model is applied to a different customer population.

## Explainability

SHAP explanations describe model behavior and do not establish causal relationships.

---

# 23. Future Improvements

Future versions could include:

- Real customer data integration
- Automated retraining
- Model drift detection
- Feature drift monitoring
- Model registry
- Experiment tracking
- Hyperparameter optimization
- Production database integration
- Real-time inference
- Customer-specific retention recommendations
- Authentication
- Role-based access control
- Containerized deployment
- Monitoring dashboards
- Automated reporting

---

# 24. Conclusion

The Customer Churn Intelligence Platform demonstrates a complete machine learning workflow rather than only a model-training notebook.

The project combines:

```text
Data
 ↓
Preprocessing
 ↓
Model Benchmarking
 ↓
Prediction
 ↓
Risk Segmentation
 ↓
Explainability
 ↓
Business Impact
 ↓
Interactive Application
```

This structure demonstrates how a machine learning model can be developed into a practical analytical application.

The current implementation is intentionally positioned as a portfolio and demonstration project, while the architecture leaves room for future production-oriented improvements.