# ==========================================================
# AI-Based Network Intrusion Detection System (NIDS)
# train_model.py
# Train Random Forest using all CSV files
# ==========================================================

import os
import glob
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("AI-Based Network Intrusion Detection System")
print("Random Forest Model Training")
print("=" * 60)

# ==========================================================
# Find all CSV files
# ==========================================================

csv_files = glob.glob("datasets/*.csv")

if len(csv_files) == 0:
    print("\nNo CSV files found inside 'datasets' folder.")
    exit()

print(f"\nFound {len(csv_files)} CSV files.\n")

# ==========================================================
# Load and Merge all CSV files
# ==========================================================

dataframes = []

for file in csv_files:

    print("Loading :", os.path.basename(file))

    df = pd.read_csv(file)

    dataframes.append(df)

dataset = pd.concat(dataframes, ignore_index=True)

print("\nDataset merged successfully.")
print("Shape :", dataset.shape)

# ==========================================================
# Remove Missing Values
# ==========================================================

dataset = dataset.dropna()

print("Shape after cleaning :", dataset.shape)

# ==========================================================
# Check Label Column
# ==========================================================

if "Label" not in dataset.columns:
    print("\nERROR: 'Label' column not found.")
    exit()

# ==========================================================
# Features and Labels
# ==========================================================

X = dataset.drop("Label", axis=1)
y = dataset["Label"]

# ==========================================================
# Convert Categorical Columns
# ==========================================================

X = pd.get_dummies(X)

# Save feature names
feature_names = X.columns.tolist()

# ==========================================================
# Split Dataset
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================================
# Train Random Forest
# ==========================================================

print("\nTraining Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Training Completed.")

# ==========================================================
# Evaluate Model
# ==========================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy : {:.2f}%".format(accuracy * 100))

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# ==========================================================
# Save Model
# ==========================================================

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/model.pkl")
joblib.dump(feature_names, "model/features.pkl")
joblib.dump(accuracy, "model/accuracy.pkl")

print("\nModel saved successfully.")
print("model/model.pkl")
print("model/features.pkl")
print("model/accuracy.pkl")

print("\nTraining Finished Successfully.")