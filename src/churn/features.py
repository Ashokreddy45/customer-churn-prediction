from __future__ import annotations
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TARGET = "Churn"
ID_COL = "customerID"

def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    numeric = X.select_dtypes(include="number").columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    num_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    cat_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))])
    return ColumnTransformer([("num", num_pipe, numeric), ("cat", cat_pipe, categorical)], remainder="drop")

def prepare_xy(df):
    y = df[TARGET].copy()

    # Support both numeric targets (0/1) and Telco-style Yes/No targets.
    if y.dtype == "object" or str(y.dtype).startswith("string"):
        y = (
            y.astype(str)
            .str.strip()
            .str.lower()
            .map({
                "yes": 1,
                "no": 0,
                "true": 1,
                "false": 0,
                "1": 1,
                "0": 0
            })
        )

    y = y.astype(int)

    X = df.drop(columns=[TARGET])

    return X, y
