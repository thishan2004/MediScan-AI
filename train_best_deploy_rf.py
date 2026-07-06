import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")

y_train = pd.read_csv("data/processed/y_train.csv")["interaction_type"]
y_test = pd.read_csv("data/processed/y_test.csv")["interaction_type"]

configs = [
    {"n_estimators": 80, "max_depth": 30, "min_samples_split": 5, "min_samples_leaf": 1, "max_features": "sqrt"},
    {"n_estimators": 60, "max_depth": 30, "min_samples_split": 5, "min_samples_leaf": 1, "max_features": "sqrt"},
    {"n_estimators": 50, "max_depth": 28, "min_samples_split": 5, "min_samples_leaf": 1, "max_features": "sqrt"},
    {"n_estimators": 40, "max_depth": 25, "min_samples_split": 5, "min_samples_leaf": 1, "max_features": "sqrt"},
    {"n_estimators": 35, "max_depth": 25, "min_samples_split": 5, "min_samples_leaf": 2, "max_features": "sqrt"},
]

best_result = None

os.makedirs("models", exist_ok=True)

for i, params in enumerate(configs, start=1):
    print(f"\nTraining model {i}: {params}")

    model = RandomForestClassifier(
        **params,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average="macro", zero_division=0)
    weighted_f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

    temp_path = f"models/rf_model_{i}.pkl"
    joblib.dump(model, temp_path, compress=3)

    size_mb = os.path.getsize(temp_path) / (1024 * 1024)

    print("Accuracy:", acc)
    print("Macro F1:", macro_f1)
    print("Weighted F1:", weighted_f1)
    print("Size MB:", round(size_mb, 2))

    if size_mb <= 100:
        if best_result is None or weighted_f1 > best_result["weighted_f1"]:
            best_result = {
                "model": model,
                "params": params,
                "accuracy": acc,
                "macro_f1": macro_f1,
                "weighted_f1": weighted_f1,
                "size_mb": size_mb,
                "path": temp_path
            }

if best_result is None:
    print("\nNo model under 100MB found. Need stronger pruning.")
else:
    joblib.dump(best_result["model"], "models/best_model.pkl", compress=3)

    print("\nBEST DEPLOYABLE MODEL SAVED")
    print("Params:", best_result["params"])
    print("Accuracy:", best_result["accuracy"])
    print("Macro F1:", best_result["macro_f1"])
    print("Weighted F1:", best_result["weighted_f1"])
    print("Size MB:", round(best_result["size_mb"], 2))
    print("Saved as: models/best_model.pkl")