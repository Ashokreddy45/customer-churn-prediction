from __future__ import annotations
import pandas as pd
import shap

def explain(pipe, X: pd.DataFrame, row_index: int):
    pre=pipe.named_steps["preprocess"]; model=pipe.named_steps["model"]
    Xt=pre.transform(X.iloc[[row_index]])
    names=pre.get_feature_names_out()
    try:
        explainer=shap.Explainer(model, pre.transform(X.iloc[:min(200,len(X))]))
        vals=explainer(Xt).values[0]
        if getattr(vals,"ndim",1)>1: vals=vals[:,1]
        s=pd.DataFrame({"Feature":names,"SHAP":vals}).sort_values("SHAP",key=lambda x:x.abs(),ascending=False).head(12)
        return s
    except Exception:
        return pd.DataFrame(columns=["Feature","SHAP"])
