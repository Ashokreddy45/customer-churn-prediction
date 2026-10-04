# Data Dictionary

## Dataset Overview

The Customer Churn Intelligence Platform uses a Telco-style customer
dataset containing customer demographics, services, contracts, billing
information, and churn status.

The included demonstration dataset contains 5,000 customer records.

## Features

| Feature | Type | Description |
|---|---|---|
| `customerID` | String | Unique customer identifier |
| `gender` | Categorical | Customer gender |
| `SeniorCitizen` | Categorical | Senior citizen indicator |
| `Partner` | Categorical | Whether the customer has a partner |
| `Dependents` | Categorical | Whether the customer has dependents |
| `tenure` | Numeric | Number of months the customer has been with the company |
| `PhoneService` | Categorical | Whether phone service is active |
| `InternetService` | Categorical | Type of internet service |
| `OnlineSecurity` | Categorical | Whether online security is subscribed |
| `TechSupport` | Categorical | Whether technical support is subscribed |
| `Contract` | Categorical | Customer contract type |
| `PaperlessBilling` | Categorical | Whether paperless billing is enabled |
| `PaymentMethod` | Categorical | Customer payment method |
| `MonthlyCharges` | Numeric | Monthly customer charges |
| `TotalCharges` | Numeric | Total customer charges |
| `Churn` | Binary | Target variable indicating customer churn |

## Target Variable

The target variable is:

```text
Churn