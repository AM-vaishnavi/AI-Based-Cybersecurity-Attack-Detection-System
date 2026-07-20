# ==========================================================
# AI-Based Network Intrusion Detection System (NIDS)
# predict.py
# ==========================================================

import os
import joblib
import pandas as pd

# ==========================================================
# Model Paths
# ==========================================================

MODEL_PATH = "model/model.pkl"
FEATURE_PATH = "model/features.pkl"

# ==========================================================
# Load Trained Model
# ==========================================================

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("model/model.pkl not found.")

if not os.path.exists(FEATURE_PATH):
    raise FileNotFoundError("model/features.pkl not found.")

model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURE_PATH)

# ==========================================================
# Prediction Function
# ==========================================================

def predict_attack(csv_file):

    # ------------------------------------------
    # Read Dataset
    # ------------------------------------------

    original_data = pd.read_csv(csv_file)

    test_data = original_data.copy()

    # ------------------------------------------
    # Remove Label (if available)
    # ------------------------------------------

    if "Label" in test_data.columns:
        test_data = test_data.drop("Label", axis=1)

    # ------------------------------------------
    # Convert Categorical Columns
    # ------------------------------------------

    test_data = pd.get_dummies(test_data)

    # ------------------------------------------
    # Match Training Features
    # ------------------------------------------

    test_data = test_data.reindex(
        columns=feature_names,
        fill_value=0
    )

    # ------------------------------------------
    # Prediction
    # ------------------------------------------

    predictions = model.predict(test_data)

    # ------------------------------------------
    # Prediction Probability
    # ------------------------------------------

    probabilities = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(test_data)

    # ------------------------------------------
    # Create Result DataFrame
    # ------------------------------------------

    result = original_data.copy()

    result["Prediction"] = predictions

    # Highest confidence score

    if probabilities is not None:

        result["Confidence (%)"] = (
            probabilities.max(axis=1) * 100
        ).round(2)

    # ------------------------------------------
    # Prediction Summary
    # ------------------------------------------

    summary = (
        result["Prediction"]
        .value_counts()
        .reset_index()
    )

    summary.columns = [

        "Attack Type",

        "Count"

    ]

    return result, summary

# ==========================================================
# Test Prediction
# ==========================================================

if __name__ == "__main__":

    TEST_FILE = "test.csv"

    result, summary = predict_attack(TEST_FILE)

    print("\nPrediction Results\n")

    print(result.head())

    print("\nPrediction Summary\n")

    print(summary)

    result.to_csv(
        "prediction_result.csv",
        index=False
    )

    print("\nPrediction saved as prediction_result.csv")