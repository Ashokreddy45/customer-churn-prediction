from __future__ import annotations
import io, json, joblib, pandas as pd, plotly.express as px, streamlit as st
from sklearn.model_selection import train_test_split
from src.churn.data import clean_telco, make_demo_dataset
from src.churn.features import prepare_xy
from src.churn.models import benchmark_cv, fit_final_model, predict_proba
from src.churn.evaluation import metrics, best_f1_threshold
from src.churn.explainability import explain
from src.churn.business import simulate, risk_band

st.set_page_config(page_title="Customer Churn Intelligence Platform",page_icon="📊",layout="wide")
st.title("Customer Churn Intelligence Platform")
st.caption("Prediction → explanation → risk segmentation → business action")

@st.cache_data
def demo(): return make_demo_dataset()

uploaded=st.sidebar.file_uploader("Optional Telco CSV",type=["csv"])
df=clean_telco(pd.read_csv(uploaded)) if uploaded else demo()
st.sidebar.success(f"Loaded {len(df):,} customers")

X,y=prepare_xy(df)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)

@st.cache_resource(show_spinner="Training and benchmarking models...")
def train_cached(Xtr,ytr):
    rows=benchmark_cv(Xtr,ytr)
    bench=pd.DataFrame(rows).sort_values("CV ROC_AUC",ascending=False).reset_index(drop=True)
    best=bench.loc[0,"Model"]
    model=fit_final_model(Xtr,ytr,best)
    prob=predict_proba(model,Xte)
    threshold=best_f1_threshold(yte,prob)
    return bench,model,threshold

bench,model,threshold=train_cached(Xtr,ytr)
prob=predict_proba(model,Xte); m=metrics(yte,prob,threshold)

c1,c2,c3,c4=st.columns(4)
c1.metric("Churn rate",f"{y.mean()*100:.1f}%")
c2.metric("Best model",bench.iloc[0]["Model"])
c3.metric("Test ROC-AUC",f"{m['ROC-AUC']:.3f}")
c4.metric("Decision threshold",f"{threshold:.2f}")

t1,t2,t3,t4,t5=st.tabs(["Overview","Model Benchmark","Customer Risk","Explainability","Business Impact"])
with t1:
    st.subheader("Portfolio-level insights")
    if "Contract" in df:
        rate=df.groupby("Contract",dropna=False)["Churn"].apply(lambda s:(s==1).mean() if s.dtype!='O' else s.str.lower().eq('yes').mean()).reset_index(name="ChurnRate")
        st.plotly_chart(px.bar(rate,x="Contract",y="ChurnRate",title="Churn rate by contract"),use_container_width=True)
    st.dataframe(df.head(20),use_container_width=True)
with t2:
    st.dataframe(bench,use_container_width=True)
    st.bar_chart(bench.set_index("Model")["CV ROC_AUC"])
    st.write({k:round(v,4) for k,v in m.items()})
with t3:
    st.subheader("Score customers")
    sample=df.copy(); sample["ChurnProbability"]=predict_proba(model,X); sample["RiskBand"]=sample["ChurnProbability"].map(risk_band)
    cols=[c for c in ["customerID","Contract","tenure","MonthlyCharges","ChurnProbability","RiskBand"] if c in sample]
    st.dataframe(sample.sort_values("ChurnProbability",ascending=False)[cols].head(100),use_container_width=True)
with t4:
    idx=st.number_input("Customer row",min_value=0,max_value=max(0,len(X)-1),value=0)
    p=float(predict_proba(model,X.iloc[[idx]])[0]); st.metric("Churn probability",f"{p*100:.1f}%",risk_band(p))
    e=explain(model,X,int(idx))
    if len(e): st.dataframe(e,use_container_width=True)
    else: st.info("SHAP could not be computed for this model/runtime; prediction remains available.")
with t5:
    st.subheader("Retention economics")
    n=st.slider("Customers targeted",10,1000,100)
    revenue=st.number_input("Monthly revenue/customer",20.0,300.0,75.0)
    retention=st.slider("Expected save rate",.05,.80,.35)
    cost=st.number_input("Intervention cost/customer",1.0,100.0,12.0)
    top=sample.sort_values("ChurnProbability",ascending=False).head(n)
    result=simulate(top["ChurnProbability"].tolist(),n,revenue,retention,cost)
    st.json({k:round(v,2) for k,v in result.items()})

st.divider(); st.caption("Built as a reproducible ML portfolio project with leakage-safe preprocessing, cross-validation, held-out evaluation, explainability and business impact analysis.")
