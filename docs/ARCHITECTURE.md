# System Architecture

## 1. Overview

The Customer Churn Intelligence Platform is designed as an end-to-end
machine learning workflow that transforms customer data into churn
predictions, customer risk segments, explainable predictions, and
business impact estimates.

The system follows this flow:

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
Streamlit Dashboard