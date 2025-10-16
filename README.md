# ExplainOps — Explainable Anomaly Detection in Observability Data

### Purpose
**ExplainOps** demonstrates how explainable AI techniques (e.g., SHAP) can provide human-interpretable insights  
for anomaly detection in system observability metrics.

This work aligns with my MSc by Research proposal at the **University of Bristol**  
on *Cognitive Reliability and Human–AI Collaboration in Incident Response.*

---

### Features
- Synthetic observability dataset (CPU, memory, latency)
- IsolationForest-based anomaly detection
- Visualisation of anomalies in observability metrics
- SHAP explanations for feature contributions
- Reproducible and parameter-controlled notebook

---

### Tech Stack
- **Python 3.10+**  
- **Scikit-learn** — anomaly detection  
- **SHAP** — explainability and feature attribution  
- **Matplotlib / Seaborn** — visualisation  
- **Jupyter Lab** — experimentation environment  

---
# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch notebook
jupyter lab

### How to Run Locally
```bash
# 1. Clone repo
git clone https://github.com/ShrawantiA/ExplainOps-Explainable-Anomaly-Detection.git
cd ExplainOps-Explainable-Anomaly-Detection

# 2. Create environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch notebook
jupyter lab
