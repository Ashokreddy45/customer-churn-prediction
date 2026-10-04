import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import json, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from churn.data import load_dataset
from churn.features import prepare_xy
from churn.models import benchmark_cv, fit_final_model, predict_proba
from churn.evaluation import metrics, best_f1_threshold

ROOT=Path(__file__).resolve().parents[1]
ART=ROOT/"artifacts"; ART.mkdir(exist_ok=True)
df=load_dataset(str(ROOT/"data"/"demo_telco_churn.csv"))
X,y=prepare_xy(df)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
rows=benchmark_cv(Xtr,ytr)
cv=pd.DataFrame(rows).sort_values("CV ROC_AUC",ascending=False)
best=str(cv.iloc[0]["Model"])
model=fit_final_model(Xtr,ytr,best)
prob=predict_proba(model,Xte)
threshold=best_f1_threshold(yte,prob)
result=metrics(yte,prob,threshold); result.update({"selected_model":best,"threshold":threshold,"test_rows":len(yte)})
joblib.dump(model,ART/"churn_pipeline.joblib")
cv.to_csv(ART/"cv_benchmark.csv",index=False)
(ART/"model_metadata.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
