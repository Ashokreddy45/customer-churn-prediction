from __future__ import annotations
import numpy as np
from sklearn.metrics import accuracy_score, average_precision_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score

def metrics(y_true, prob, threshold=.5):
    pred=(prob>=threshold).astype(int)
    return {"ROC-AUC":roc_auc_score(y_true,prob),"PR-AUC":average_precision_score(y_true,prob),"Accuracy":accuracy_score(y_true,pred),
            "Precision":precision_score(y_true,pred,zero_division=0),"Recall":recall_score(y_true,pred,zero_division=0),"F1":f1_score(y_true,pred,zero_division=0)}

def best_f1_threshold(y_true, prob):
    thresholds=np.linspace(.05,.95,181); scores=[f1_score(y_true,(prob>=t).astype(int),zero_division=0) for t in thresholds]
    return float(thresholds[int(np.argmax(scores))])

def confusion(y_true, prob, threshold):
    return confusion_matrix(y_true,(prob>=threshold).astype(int))
