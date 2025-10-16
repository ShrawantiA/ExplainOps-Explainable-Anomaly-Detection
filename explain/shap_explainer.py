from sklearn.ensemble import IsolationForest
import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
X = pd.DataFrame({
    "cpu": np.random.normal(50, 10, 200),
    "memory": np.random.normal(60, 15, 200),
    "latency": np.random.normal(100, 25, 200)
})

model = IsolationForest(contamination=0.05)
model.fit(X)
X["anomaly"] = model.predict(X)

# SHAP explainability
explainer = shap.Explainer(model, X[["cpu","memory","latency"]])
shap_values = explainer(X[["cpu","memory","latency"]])
shap.summary_plot(shap_values, X[["cpu","memory","latency"]])
