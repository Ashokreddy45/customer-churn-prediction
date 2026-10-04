from __future__ import annotations
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from .features import build_preprocessor, prepare_xy

SCORING = {"roc_auc":"roc_auc", "pr_auc":"average_precision", "f1":"f1", "precision":"precision", "recall":"recall", "accuracy":"accuracy"}

def model_library(seed: int = 42):
    return {
        "Logistic Regression": LogisticRegression(max_iter=2000, class_weight="balanced", random_state=seed),
        "Random Forest": RandomForestClassifier(n_estimators=350, min_samples_leaf=2, class_weight="balanced", n_jobs=-1, random_state=seed),
        "Gradient Boosting": GradientBoostingClassifier(n_estimators=250, learning_rate=.04, max_depth=3, random_state=seed),
        "XGBoost": XGBClassifier(n_estimators=300, max_depth=4, learning_rate=.04, subsample=.85, colsample_bytree=.85,
                                  eval_metric="logloss", tree_method="hist", random_state=seed, n_jobs=4)
    }

def benchmark_cv(X_train, y_train, seed=42):
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    rows=[]
    pre = build_preprocessor(X_train)
    for name, model in model_library(seed).items():
        pipe=Pipeline([("preprocess", pre), ("model", model)])
        scores=cross_validate(pipe, X_train, y_train, cv=cv, scoring=SCORING, n_jobs=1, error_score="raise")
        rows.append({"Model": name, "CV ROC_AUC": float(np.mean(scores["test_roc_auc"])), "CV PR_AUC": float(np.mean(scores["test_pr_auc"])), "CV F1": float(np.mean(scores["test_f1"])), "CV Precision": float(np.mean(scores["test_precision"])), "CV Recall": float(np.mean(scores["test_recall"])), "CV Accuracy": float(np.mean(scores["test_accuracy"]))})
    return rows

def fit_final_model(X_train, y_train, model_name: str, seed=42):
    models=model_library(seed)
    if model_name not in models: raise ValueError(f"Unknown model: {model_name}")
    pipe=Pipeline([("preprocess", build_preprocessor(X_train)), ("model", models[model_name])])
    pipe.fit(X_train, y_train)
    return pipe

def predict_proba(pipe, X):
    return pipe.predict_proba(X)[:,1]
