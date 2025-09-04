import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
import seaborn as sns
import matplotlib.pyplot as plt

def get_target_column(df):
    """
    Try to automatically detect the target column for cancer prediction.
    Returns the column name if found, else None.
    """
    possible_targets = ['diagnosis', 'target', 'class', 'label']
    for col in df.columns:
        if col.lower() in possible_targets:
            return col
    # Try to find a column with only two unique values (likely the label)
    for col in df.columns:
        if df[col].nunique() == 2 and df[col].dtype != 'float64':
            return col
    return None

def load_and_preprocess_data(filepath):
    """Load data, drop unnecessary columns, handle missing values, encode target."""
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully. Shape:", df.shape)
    except FileNotFoundError:
        print(f"ERROR: File '{filepath}' not found.")
        exit(1)
    except Exception as e:
        print("ERROR loading file:", e)
        exit(1)

    # Drop ID column if present
    for id_col in ['id', 'ID', 'Id']:
        if id_col in df.columns:
            df = df.drop(id_col, axis=1)

    # Drop rows with missing values
    df = df.dropna()

    # Detect target column
    target_col = get_target_column(df)
    if not target_col:
        print("ERROR: No suitable target column found in the dataset.")
        print("Columns found:", df.columns.tolist())
        exit(1)
    print(f"Target column detected: '{target_col}'")
    print("Unique values in target:", df[target_col].unique())

    # Encode target if necessary
    if df[target_col].dtype == 'object':
        if set(df[target_col].unique()) == set(['M', 'B']):
            df[target_col] = df[target_col].map({'M': 1, 'B': 0})
        else:
            df[target_col] = pd.factorize(df[target_col])[0]
    elif df[target_col].dtype == 'bool':
        df[target_col] = df[target_col].astype(int)

    if df[target_col].isnull().any():
        print("ERROR: Unmapped values found in target column after encoding.")
        print(df[target_col].unique())
        exit(1)

    X = df.drop(target_col, axis=1)
    y = df[target_col]
    return X, y

def train_models(X_train, y_train):
    """Train Logistic Regression and Random Forest models."""
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        models[name] = model
    return models

def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate model and print metrics."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"\n{model_name} Results:")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5,4))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=["Class 0", "Class 1"],
        yticklabels=["Class 0", "Class 1"]
    )
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()

def main():
    # Load and preprocess data
    X, y = load_and_preprocess_data("cancer.csv")
    print("Feature shape:", X.shape)
    print("Target distribution:\n", y.value_counts())
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    # Train models
    models = train_models(X_train_scaled, y_train)
    # Evaluate models
    for name, model in models.items():
        evaluate_model(model, X_test_scaled, y_test, name)
if __name__ == "__main__":
    main()