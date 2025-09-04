import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Sample dataset
data = pd.DataFrame({
    'Name': ['Tom', 'Jerry', np.nan, 'Spike', 'Tyke'],
    'Age': [20, np.nan, 25, 30, 18],
    'Gender': ['Male', 'Male', 'Female', np.nan, 'Male']
})

# Handling missing values
data_filled = data.fillna({
    'Name': 'Unknown',
    'Age': data['Age'].mean(),
    'Gender': 'Not Specified'
})

# Encoding categorical data
X = data_filled[['Name', 'Age', 'Gender']]
ct = ColumnTransformer(transformers=[
    ('encoder', OneHotEncoder(), ['Name', 'Gender'])
], remainder='passthrough')
X_encoded = ct.fit_transform(X)

# Simulated target variable
y = np.array(['Yes', 'No', 'Yes', 'No', 'Yes'])
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=1)

# Feature scaling
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

# Final output
print("X_train:\n", X_train_scaled)
print("X_test:\n", X_test_scaled)
print("y_train:", y_train)
print("y_test:", y_test)
