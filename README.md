# Customer Churn Intelligence Platform

> An end-to-end machine learning platform for predicting customer churn,
> explaining individual predictions, segmenting customer risk, and
> evaluating potential retention strategies.

## 🚀 Live Demo

**[Open the Customer Churn Intelligence Platform](https://customer-churn-prediction-akvxzgjsjcfaqchilwzygz.streamlit.app/)**

---

## 📌 Overview

Customer churn prediction is more useful when it goes beyond simply
classifying customers as "churn" or "not churn".

This project builds an end-to-end customer churn intelligence platform
that connects machine learning predictions with explainability,
customer risk segmentation, and business impact analysis.

The platform follows the workflow:

**Prediction → Explanation → Risk Segmentation → Business Action**

The application includes:

- Data cleaning and preprocessing
- Leakage-safe feature preprocessing
- Multiple machine learning models
- Cross-validation
- Held-out test evaluation
- Probability threshold optimization
- Customer-level churn prediction
- Risk segmentation
- SHAP-based explainability
- Business impact simulation
- Interactive Streamlit dashboard
- FastAPI prediction service
- Automated testing
- Cloud deployment

---

# 🎯 Problem Statement

Customer churn can directly affect recurring revenue and increase the
cost of acquiring replacement customers.

A useful churn prediction system should answer more than:

> "Will this customer churn?"

It should also help answer:

1. Which customers have the highest predicted churn probability?
2. How confident is the model?
3. What factors contribute to an individual prediction?
4. Which customers should potentially be prioritized?
5. What could be the potential financial impact of retention efforts?

This project was designed around these questions.

---

# 💡 Solution

The platform combines machine learning with explainability and business
analysis.

```text
Customer Data
      ↓
Data Cleaning
      ↓
Feature Preparation
      ↓
Train/Test Split
      ↓
Cross-Validation
      ↓
Model Benchmarking
      ↓
Model Selection
      ↓
Held-Out Evaluation
      ↓
Threshold Optimization
      ↓
Churn Probability
      ↓
Risk Segmentation
      ↓
SHAP Explainability
      ↓
Business Impact Analysis
      ↓
Interactive Dashboard