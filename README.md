# Customer Churn Intelligence Platform

A production-style portfolio project that turns customer churn prediction into an interpretable retention decision system.

## What it demonstrates
- End-to-end supervised ML
- Leakage-safe preprocessing
- Cross-validation and held-out testing
- Model benchmarking: Logistic Regression, Random Forest, Gradient Boosting, XGBoost
- ROC-AUC, PR-AUC, F1, precision, recall and accuracy
- Threshold optimization
- SHAP local explanations
- Customer risk segmentation
- Business impact / retention economics
- Streamlit analytics application
- FastAPI prediction endpoint
- Automated tests

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/train.py
streamlit run app.py
```

API:
```bash
uvicorn api:app --reload
```

Tests:
```bash
pytest -q
```

## Data
The included `data/demo_telco_churn.csv` is synthetic and intended for immediate execution. To use the classic Telco Customer Churn dataset, place a compatible CSV at `data/telco_churn.csv` or upload one through the Streamlit sidebar.

## Architecture
`data → cleaning → preprocessing pipeline → CV model benchmark → final held-out evaluation → probability threshold → risk segmentation → SHAP explanation → business impact`

## Admissions / portfolio positioning
The project deliberately goes beyond “train a classifier.” It connects model quality with explainability and an actionable retention workflow. See `docs/PROJECT_REPORT.md` for a concise technical narrative.
