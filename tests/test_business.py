from src.churn.business import risk_band, simulate
def test_risk_bands():
    assert risk_band(.1)=="Low" and risk_band(.8)=="Critical"
def test_simulation():
    r=simulate([.8,.6],2,100,.5,10)
    assert r["Estimated revenue saved"]==70
