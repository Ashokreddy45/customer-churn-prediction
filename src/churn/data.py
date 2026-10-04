from __future__ import annotations
import numpy as np
import pandas as pd

TARGET = "Churn"
ID_COL = "customerID"


def _binary_target(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return series.astype(int)
    mapping = {"yes": 1, "no": 0, "true": 1, "false": 0, "1": 1, "0": 0}
    return series.astype(str).str.strip().str.lower().map(mapping).fillna(0).astype(int)


def clean_telco(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(c).strip() for c in out.columns]
    if "TotalCharges" in out.columns:
        out["TotalCharges"] = pd.to_numeric(out["TotalCharges"], errors="coerce")
    if TARGET in out.columns:
        out[TARGET] = _binary_target(out[TARGET])
    if ID_COL in out.columns:
        out[ID_COL] = out[ID_COL].astype(str)
    return out.drop_duplicates().reset_index(drop=True)


def make_demo_dataset(n: int = 5000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    contract = rng.choice(["Month-to-month", "One year", "Two year"], n, p=[.56, .23, .21])
    tenure = np.clip(rng.gamma(2.1, 18, n).astype(int), 0, 72)
    monthly = np.clip(rng.normal(72, 25, n), 20, 150).round(2)
    internet = rng.choice(["DSL", "Fiber optic", "No"], n, p=[.35, .45, .20])
    payment = rng.choice(["Electronic check", "Mailed check", "Bank transfer", "Credit card"], n, p=[.34,.18,.24,.24])
    tech = rng.choice(["Yes", "No"], n, p=[.38,.62])
    support = rng.choice(["Yes", "No"], n, p=[.28,.72])
    dependents = rng.choice(["Yes", "No"], n, p=[.30,.70])
    senior = rng.choice(["Yes", "No"], n, p=[.16,.84])
    paperless = rng.choice(["Yes", "No"], n, p=[.59,.41])
    logit = (-1.25 + 1.35*(contract=="Month-to-month") + .55*(internet=="Fiber optic") + .45*(payment=="Electronic check")
             + .55*(tenure<12) + .35*(tech=="No") + .40*(support=="No") + .30*(paperless=="Yes")
             + .35*(monthly>90) + .30*(senior=="Yes") - .035*tenure)
    p = 1/(1+np.exp(-logit))
    churn = rng.binomial(1, p)
    total = (monthly*tenure + rng.normal(0, 100, n)).clip(0).round(2)
    return pd.DataFrame({
        "customerID":[f"DEMO-{i:05d}" for i in range(n)], "gender":rng.choice(["Male","Female"],n),
        "SeniorCitizen":senior, "Partner":rng.choice(["Yes","No"],n), "Dependents":dependents,
        "tenure":tenure, "PhoneService":rng.choice(["Yes","No"],n,p=[.9,.1]),
        "InternetService":internet, "OnlineSecurity":rng.choice(["Yes","No","No internet service"],n,p=[.28,.52,.20]),
        "TechSupport":tech, "Contract":contract, "PaperlessBilling":paperless, "PaymentMethod":payment,
        "MonthlyCharges":monthly, "TotalCharges":total, TARGET:np.where(churn==1,"Yes","No")
    })


def load_dataset(path: str | None = None) -> pd.DataFrame:
    if path:
        return clean_telco(pd.read_csv(path))
    return clean_telco(make_demo_dataset())
