# Data Preprocessing using pandas
import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Name': ['Tom', 'Jerry', 'Spike', np.nan, 'Tyke'],
    'Age': [20, np.nan, 30, 25, 18],
    'Gender': ['Male', 'Male', np.nan, 'Female', 'Male'],
    'Salary': [50000, 54000, np.nan, 58000, 52000]
}

df = pd.DataFrame(data)

# 1. Inspecting missing values
print("Missing values:\n", df.isnull().sum())

# 2. Filling missing values
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# 3. Encoding categorical data
df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=True)

# 4. Feature scaling (Min-Max normalization)
df_encoded['Age'] = (df_encoded['Age'] - df_encoded['Age'].min()) / (df_encoded['Age'].max() - df_encoded['Age'].min())
df_encoded['Salary'] = (df_encoded['Salary'] - df_encoded['Salary'].min()) / (df_encoded['Salary'].max() - df_encoded['Salary'].min())

# 5. Final preprocessed data
print("\nPreprocessed Data:\n", df_encoded)
