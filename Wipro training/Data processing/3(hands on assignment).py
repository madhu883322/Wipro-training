import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('melb_data.csv')

# 1. Overview
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

# 2. Drop columns with excessive missing data
df.drop(columns=['BuildingArea', 'YearBuilt', 'CouncilArea'], inplace=True)

# 3. Fill missing values
df['Car'].fillna(df['Car'].median(), inplace=True)
df['Bathroom'].fillna(df['Bathroom'].median(), inplace=True)

# 4. Descriptive statistics
print("\nDescriptive Stats:\n", df.describe())

# 5. Outlier detection using IQR
def detect_outliers(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
    return len(outliers)

numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    print(f"{col}: {detect_outliers(col)} outliers")

# 6. Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
