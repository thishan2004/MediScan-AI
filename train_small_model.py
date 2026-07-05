import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv("data/processed/cleaned_DDI_data.csv")

class_counts = df["interaction_type"].value_counts()
valid_classes = class_counts[class_counts >= 2].index
df = df[df["interaction_type"].isin(valid_classes)].copy()

X = df[["drug1_name", "drug2_name"]].copy()
y_text = df["interaction_type"].copy()

drug_encoder = LabelEncoder()
all_drugs = pd.concat([X["drug1_name"], X["drug2_name"]])
drug_encoder.fit(all_drugs)

X["drug1_name"] = drug_encoder.transform(X["drug1_name"])
X["drug2_name"] = drug_encoder.transform(X["drug2_name"])

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y_text)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=20,
    max_depth=18,
    min_samples_split=5,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Macro F1:", f1_score(y_test, y_pred, average="macro", zero_division=0))
print("Weighted F1:", f1_score(y_test, y_pred, average="weighted", zero_division=0))

joblib.dump(model, "models/best_model.pkl", compress=3)
joblib.dump(drug_encoder, "models/drug_encoder.pkl")
joblib.dump(target_encoder, "models/target_encoder.pkl")

print("Small deployable model saved successfully.")