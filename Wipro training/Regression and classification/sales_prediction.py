import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, classification_report, confusion_matrix

# 1. Load the Data
df = pd.read_csv("advertising.csv")
print("\nDataset Loaded Successfully!\n")
print(df.head())

# 2. Data Preprocessing
# Convert 'Timestamp' to datetime if present
if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Hour'] = df['Timestamp'].dt.hour
    df['DayOfWeek'] = df['Timestamp'].dt.dayofweek
else:
    print("Warning: 'Timestamp' column not found. Skipping time features.")

# Drop unnecessary columns if present
drop_cols = [col for col in ["Ad Topic Line", "City", "Country", "Timestamp"] if col in df.columns]
X = df.drop(drop_cols, axis=1)

print("\nColumns after preprocessing:\n", X.columns)

# 3. Exploratory Data Analysis
plt.figure(figsize=(8,6))
sns.heatmap(X.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 4A. Regression Model (Predicting Daily Internet Usage)
if "Daily Internet Usage" in X.columns and "Clicked on Ad" in X.columns:
    X_reg = X.drop(["Daily Internet Usage", "Clicked on Ad"], axis=1)
    y_reg = X["Daily Internet Usage"]

    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

    reg_model = LinearRegression()
    reg_model.fit(X_train_reg, y_train_reg)
    y_pred_reg = reg_model.predict(X_test_reg)

    print("\n--- Regression Model Evaluation ---")
    print("R2 Score:", r2_score(y_test_reg, y_pred_reg))
    print("MAE:", mean_absolute_error(y_test_reg, y_pred_reg))
    print("RMSE:", np.sqrt(mean_squared_error(y_test_reg, y_pred_reg)))
else:
    print("Required columns for regression not found.")

# 4B. Classification Model (Predicting Clicked on Ad)
if "Clicked on Ad" in X.columns:
    X_clf = X.drop(["Clicked on Ad"], axis=1)
    y_clf = X["Clicked on Ad"]

    X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

    clf_model = LogisticRegression(max_iter=1000)
    clf_model.fit(X_train_clf, y_train_clf)
    y_pred_clf = clf_model.predict(X_test_clf)

    print("\n--- Classification Model Evaluation ---")
    print("Accuracy:", accuracy_score(y_test_clf, y_pred_clf))
    print("\nClassification Report:\n", classification_report(y_test_clf, y_pred_clf))

    # Confusion Matrix
    cm = confusion_matrix(y_test_clf, y_pred_clf)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
else:
    print("Required column for classification not found.")