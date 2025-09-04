import pandas as pd

# -------------------------
# Q1. Load the data in DataFrame (Pandas)
# -------------------------
df = pd.read_csv("melb_data.csv")
print("Q1: First 5 rows of dataset:\n", df.head())
print("\nDataset Info:")
print(df.info())

# -------------------------
# Q2. Handle Inappropriate Data
# -------------------------
df = df.drop_duplicates()
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.drop(['Address', 'SellerG', 'CouncilArea'], axis=1)
print("\nQ2: After handling inappropriate data:")
print(df.head())

# -------------------------
# Q3. Handle Missing Data
# -------------------------
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Drop columns with more than 40% missing values
df = df.dropna(axis=1, thresh=len(df)*0.6)

# Fill numeric columns with median
num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:\n", df.isnull().sum())

# -------------------------
# Q4. Handle the Categorical Data
# -------------------------
cat_cols = df.select_dtypes(include=['object']).columns
print("\nCategorical columns:", list(cat_cols))

df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
print("\nQ4: Final dataset ready for ML:\n", df.head())

