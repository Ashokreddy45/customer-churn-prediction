# Customer Churn Intelligence Platform — Project Report

## Problem
Customer churn is not only a classification problem. A useful retention system must identify high-risk customers, explain drivers, prioritize intervention and estimate economic impact.

## Methodology
- Synthetic demo data for reproducibility; compatible with the common Telco Customer Churn CSV schema.
- Leakage-safe preprocessing through a scikit-learn Pipeline and ColumnTransformer.
- Stratified 80/20 train-test split.
- Five-fold stratified cross-validation on the training set for model selection.
- Logistic Regression, Random Forest, Gradient Boosting and XGBoost benchmarks.
- ROC-AUC, PR-AUC, precision, recall, F1 and accuracy.
- Threshold selection using validation performance rather than assuming 0.50 is optimal.
- SHAP-based local explanations where supported.
- Risk bands and retention economics.

## Portfolio value
This project demonstrates ML engineering, evaluation discipline, explainability, product thinking and communication of model outputs to non-technical stakeholders.
