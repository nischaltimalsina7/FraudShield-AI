from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

print("Script started", flush=True)

# Select training features
features = [
    "amount",
    "hour",
    "day_of_week",
    "is_online",
    "has_error",
    "credit_limit",
    "credit_score",
    "amount_to_limit",
    "is_refund",
    "is_foreign",
    "card_expired"
]

# Load and sort transactions
df = pd.read_parquet(
    "data/transactions_clean_sample.parquet",
    columns=features + ["date", "is_fraud"]
)

df = df.sort_values("date")

# Check numerical values
assert np.isfinite(df[features].to_numpy()).all()

# Split training and testing data
split_index = int(len(df) * 0.8)

X_train = df.iloc[:split_index][features]
X_test = df.iloc[split_index:][features]

print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)

# Initialize Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination="auto",
    random_state=42,
    n_jobs=-1
)

# Train the model
print("Training Isolation Forest...", flush=True)
model.fit(X_train)

print("Model training completed successfully!")

# Predict anomalies in testing data
predictions = model.predict(X_test)

# Calculate anomaly scores
anomaly_scores = -model.score_samples(X_test)

# Count normal and anomalous transactions
normal_count = np.sum(predictions == 1)
anomaly_count = np.sum(predictions == -1)

print("\nPrediction Results:")
print("Normal transactions:", normal_count)
print("Anomalous transactions:", anomaly_count)
print("Anomaly percentage:", round(anomaly_count / len(X_test) * 100, 2))

# Extract actual fraud labels
y_test = df.iloc[split_index:]["is_fraud"]

# Convert anomaly predictions to binary labels
y_pred = (predictions == -1).astype(int)

# Evaluate model performance
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=[0, 1]))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Normal", "Fraud"],
    zero_division=0
))

# Evaluate anomaly score performance
roc_auc = roc_auc_score(y_test, anomaly_scores)
pr_auc = average_precision_score(y_test, anomaly_scores)

print("\nAnomaly Score Evaluation:")
print("ROC-AUC:", round(roc_auc, 4))
print("Average Precision:", round(pr_auc, 4))