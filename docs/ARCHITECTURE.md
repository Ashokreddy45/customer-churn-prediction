# System Architecture

## 1. Overview

The Customer Churn Intelligence Platform is organized as an end-to-end machine learning workflow.

The system takes customer-level data, processes the features, benchmarks multiple machine learning models, selects a final model, generates churn probabilities, segments customers by risk, provides model explanations, and estimates potential business impact.

The primary application interface is implemented using Streamlit.

A FastAPI service is also included for API-based integration.

---

## 2. High-Level Architecture

```text
                    ┌──────────────────────┐
                    │    Customer Data     │
                    │ CSV / Demo Dataset   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Cleaning        │
                    │ & Validation         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Feature Preparation  │
                    │ Numeric + Categorical│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Train/Test Split     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Cross Validation     │
                    │ Model Benchmarking   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Best Model           │
                    │ Selection             │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
         ┌────────────┐ ┌────────────┐ ┌──────────────┐
         │ Prediction │ │ Explain-   │ │ Business     │
         │ & Risk     │ │ ability    │ │ Impact       │
         │ Scoring    │ │ SHAP       │ │ Simulation   │
         └─────┬──────┘ └─────┬──────┘ └──────┬───────┘
               │              │               │
               └──────────────┼───────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────────────────┘
```

---

# 3. Application Layers

## Data Layer

Responsible for loading and cleaning customer data.

Main module:

```text
src/churn/data.py
```

Responsibilities include:

- Loading datasets
- Creating demonstration data
- Cleaning column names
- Converting numeric values
- Encoding the churn target
- Removing duplicate rows

---

## Feature Engineering Layer

Main module:

```text
src/churn/features.py
```

The feature preparation layer separates numeric and categorical variables.

### Numeric pipeline

```text
Numeric Features
      ↓
Median Imputation
      ↓
StandardScaler
```

### Categorical pipeline

```text
Categorical Features
      ↓
Most-Frequent Imputation
      ↓
One-Hot Encoding
```

The categorical encoder uses:

```python
OneHotEncoder(handle_unknown="ignore")
```

This allows the pipeline to handle categories that were not observed during model training.

---

# 4. Model Layer

Main module:

```text
src/churn/models.py
```

The project benchmarks:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

The models are evaluated using cross-validation on the training data.

The highest-performing benchmark model is then fitted on the training dataset.

---

# 5. Evaluation Layer

Main module:

```text
src/churn/evaluation.py
```

The evaluation layer calculates:

- ROC-AUC
- F1
- Precision
- Recall
- Confusion-matrix related outputs

The project also calculates a decision threshold rather than assuming that `0.50` is always the optimal classification threshold.

---

# 6. Explainability Layer

Main module:

```text
src/churn/explainability.py
```

SHAP is used to provide feature contribution information for individual predictions.

The purpose is to make the model output easier to inspect.

The system treats SHAP as an explanation of model behavior rather than proof of causality.

---

# 7. Business Layer

Main module:

```text
src/churn/business.py
```

This layer converts model outputs into simplified retention economics.

Inputs include:

- Number of targeted customers
- Monthly revenue per customer
- Expected retention/save rate
- Intervention cost

The output estimates the potential business impact of intervention.

---

# 8. Application Layer

Main application:

```text
app.py
```

The Streamlit application provides five main sections:

```text
Overview
Model Benchmark
Customer Risk
Explainability
Business Impact
```

The application also supports an optional CSV upload.

When no file is uploaded, the built-in demonstration dataset is used.

---

# 9. API Layer

API entry point:

```text
api.py
```

The project includes a FastAPI service for API-oriented integration.

The development server can be started using:

```bash
uvicorn api:app --reload
```

Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

The exact API request and response behavior should be verified against the current `api.py` implementation before production integration.

---

# 10. Testing Layer

Tests are located in:

```text
tests/
```

The project uses Pytest.

Run:

```bash
python -m pytest -q
```

Current local status:

```text
3 passed
```

---

# 11. Deployment

The Streamlit application is deployed using Streamlit Community Cloud.

Deployment flow:

```text
GitHub Repository
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

# 12. Design Principles

The project follows several practical ML engineering principles:

### Reproducibility

The project structure separates data processing, features, models, evaluation, explainability, and business logic.

### Leakage Awareness

Preprocessing is performed through a pipeline so transformations are learned from the appropriate training data.

### Model Comparison

Multiple algorithms are benchmarked rather than assuming one model is automatically optimal.

### Explainability

Predictions can be investigated through SHAP-based explanations.

### Business Relevance

The application connects predictions to customer risk and simplified retention economics.

### Testability

Core functionality is covered by automated tests.

---

# 13. Future Architecture Improvements

For a production system, the architecture could be extended with:

```text
Data Warehouse
      ↓
Feature Store
      ↓
Training Pipeline
      ↓
Experiment Tracking
      ↓
Model Registry
      ↓
Model Serving
      ↓
Monitoring
      ↓
Business Application
```

Potential technologies could include managed cloud databases, experiment tracking systems, model registries, containerized inference, and model monitoring.

These components are not currently required for the demonstration application.