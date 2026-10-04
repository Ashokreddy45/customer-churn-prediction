# Data Dictionary

## 1. Dataset Overview

The project includes a synthetic Telco-style customer churn dataset for demonstration purposes.

Current demonstration dataset:

```text
Records: 5,000
Columns: 16
Target: Churn
```

The dataset is designed to resemble a customer subscription dataset containing demographic, service, contract, billing, and churn information.

---

# 2. Dataset Columns

| Column | Data Type | Description |
|---|---|---|
| `customerID` | String | Unique customer identifier |
| `gender` | Categorical | Customer gender |
| `SeniorCitizen` | Integer | Indicates whether the customer belongs to the senior-citizen category |
| `Partner` | Categorical | Whether the customer has a partner |
| `Dependents` | Categorical | Whether the customer has dependents |
| `tenure` | Integer | Number of months the customer has remained with the company |
| `PhoneService` | Categorical | Whether the customer has phone service |
| `InternetService` | Categorical | Type of internet service |
| `OnlineSecurity` | Categorical | Whether online security service is enabled |
| `TechSupport` | Categorical | Whether technical support is enabled |
| `Contract` | Categorical | Customer contract type |
| `PaperlessBilling` | Categorical | Whether paperless billing is enabled |
| `PaymentMethod` | Categorical | Customer payment method |
| `MonthlyCharges` | Float | Customer's monthly charge |
| `TotalCharges` | Float | Customer's accumulated charges |
| `Churn` | Binary / Categorical | Target variable indicating whether the customer churned |

---

# 3. Target Variable

The target variable is:

```text
Churn
```

The source representation can use:

```text
Yes
No
```

During preprocessing, the target is converted into a binary representation:

```text
Yes → 1
No  → 0
```

Therefore:

```text
1 = Customer churned
0 = Customer did not churn
```

---

# 4. Identifier Column

The column:

```text
customerID
```

is treated as an identifier.

It is not intended to provide meaningful predictive information about customer churn.

The project therefore separates the identifier from the modeling target and feature preparation workflow where appropriate.

---

# 5. Numeric Features

The main numeric variables are:

```text
SeniorCitizen
tenure
MonthlyCharges
TotalCharges
```

Numeric preprocessing includes:

```text
Missing-value handling
        ↓
Median imputation
        ↓
Standard scaling
```

---

# 6. Categorical Features

Categorical variables include:

```text
gender
Partner
Dependents
PhoneService
InternetService
OnlineSecurity
TechSupport
Contract
PaperlessBilling
PaymentMethod
```

Categorical preprocessing includes:

```text
Missing-value handling
        ↓
Most-frequent imputation
        ↓
One-hot encoding
```

The encoder uses:

```python
OneHotEncoder(handle_unknown="ignore")
```

---

# 7. Data Cleaning

The data cleaning workflow includes:

1. Copying the input DataFrame.
2. Normalizing column names.
3. Converting `TotalCharges` into numeric format.
4. Converting the churn target into a binary representation.
5. Converting `customerID` to string.
6. Removing duplicate rows.
7. Resetting the DataFrame index.

---

# 8. Missing Values

The modeling pipeline handles missing values separately for numeric and categorical variables.

### Numeric

```text
Median
```

is used for imputation.

### Categorical

```text
Most frequent value
```

is used for imputation.

---

# 9. Feature Preparation

The feature preparation process separates:

```text
X = Customer Features
y = Churn Target
```

Conceptually:

```text
Raw Dataset
     │
     ├──────────────► Churn → y
     │
     ▼
Customer Features → X
```

---

# 10. Data Leakage Considerations

Preprocessing transformations are incorporated into the machine learning pipeline.

This helps prevent information from the evaluation data from being used to learn preprocessing parameters during training.

This is particularly important for:

- Imputation
- Scaling
- One-hot encoding
- Model evaluation

---

# 11. Demonstration Dataset

The repository includes:

```text
data/demo_telco_churn.csv
```

The included dataset is synthetic and should not be interpreted as real customer data.

The purpose of the dataset is to make the application reproducible without requiring private customer information.

---

# 12. Data Limitations

The demonstration dataset has several limitations:

- It is synthetic.
- It does not represent a specific real company's customer population.
- Its churn relationships may not match real-world behavior.
- Its class distribution is not a benchmark for any particular industry.
- Model performance on this dataset should not be generalized to production environments.

For production deployment, the dataset should be replaced with a properly governed and representative customer dataset.