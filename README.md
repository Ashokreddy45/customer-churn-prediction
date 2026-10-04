# Customer Churn Intelligence Platform

A machine learning application for predicting customer churn, understanding customer risk, and evaluating potential retention actions.

## Features

- End-to-end customer churn prediction
- Data cleaning and preprocessing
- Leakage-safe machine learning pipelines
- Cross-validation and held-out testing
- Model benchmarking:
  - Logistic Regression
  - Random Forest
  - Gradient Boosting
  - XGBoost
- Model evaluation using:
  - ROC-AUC
  - PR-AUC
  - F1 Score
  - Precision
  - Recall
  - Accuracy
- Probability threshold optimization
- Customer risk segmentation
- SHAP-based local explanations
- Business impact and retention analysis
- Interactive Streamlit dashboard
- FastAPI prediction endpoint
- Automated tests

## Project Structure

```text
customer_churn_intelligence_platform/
│
├── app.py
├── api.py
├── requirements.txt
├── README.md
│
├── data/
│   └── demo_telco_churn.csv
│
├── src/
│   └── churn/
│       ├── business.py
│       ├── data.py
│       ├── evaluation.py
│       ├── explainability.py
│       ├── features.py
│       └── models.py
│
├── scripts/
│   └── train.py
│
├── tests/
│   ├── test_business.py
│   └── test_data.py
│
├── artifacts/
├── docs/
│   └── PROJECT_REPORT.md
│
├── run.sh
├── train.sh
└── Makefile