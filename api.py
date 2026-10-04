from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from src.churn.models import fit_final_model, predict_proba
from src.churn.features import prepare_xy
from src.churn.data import clean_telco, make_demo_dataset

app=FastAPI(title="Customer Churn Intelligence API",version="1.0")
_df=clean_telco(make_demo_dataset())
_X,_y=prepare_xy(_df)
_model=fit_final_model(_X,_y,"XGBoost")
class Customer(BaseModel):
    gender:str="Male"; SeniorCitizen:str="No"; Partner:str="No"; Dependents:str="No"; tenure:int=12
    PhoneService:str="Yes"; InternetService:str="Fiber optic"; OnlineSecurity:str="No"; TechSupport:str="No"
    Contract:str="Month-to-month"; PaperlessBilling:str="Yes"; PaymentMethod:str="Electronic check"; MonthlyCharges:float=80; TotalCharges:float=960
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/predict")
def predict(c:Customer):
    x=pd.DataFrame([c.model_dump()]); p=float(predict_proba(_model,x)[0]); return {"churn_probability":p,"risk_band":"Critical" if p>=.75 else "High" if p>=.5 else "Medium" if p>=.25 else "Low"}
