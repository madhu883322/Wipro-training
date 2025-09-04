# melb_data.csv - Statistical Data Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('melb_data.csv')

# Basic info
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())

# Drop columns with excessive missing data
df = df.drop(columns=['BuildingArea', 'YearBuilt', 'CouncilArea'])

# Fill missing values
df['Car'].fillna(df['Car'].median(), inplace=True)
df['Bathroom'].fillna(df['Bathroom'].median(), inplace=True)

# Statistical summary
print("\nDescriptive Statistics:\n", df.describe())

# Outlier detection using IQR
numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
    print(f"{col}: {len(outliers)} outliers")

# Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
