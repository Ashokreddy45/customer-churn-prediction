def simulate(probabilities, customers, monthly_revenue=75.0, retention_rate=.35, intervention_cost=12.0):
    expected_loss=float(sum(probabilities)*monthly_revenue)
    retained=expected_loss*retention_rate
    cost=customers*intervention_cost
    return {"Expected monthly revenue at risk":expected_loss,"Estimated revenue saved":retained,"Intervention cost":cost,"Net expected value":retained-cost}

def risk_band(p):
    if p>=.75:return "Critical"
    if p>=.50:return "High"
    if p>=.25:return "Medium"
    return "Low"
