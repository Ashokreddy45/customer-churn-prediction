from src.churn.data import make_demo_dataset, clean_telco
def test_demo_dataset():
    d=clean_telco(make_demo_dataset(100)); assert len(d)==100; assert set(d["Churn"].unique())<=set([0,1])
