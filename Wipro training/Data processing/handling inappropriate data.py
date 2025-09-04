import pandas as pd
# 1. Load the dataset
df = pd.read_csv("melb_data.csv")
print("Original Shape:", df.shape)

# 2. Handle Inappropriate Data
# Remove unrealistic values
df = df[df['Price'] > 0]        # Price should be positive
df = df[df['Landsize'] >= 0]    # Land size should not be negative

# 3. Handle Missing Data
# Fill numeric columns with median
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# 4. Handle Categorical Data
# Convert categorical variables into numeric using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# 5. Handle Duplicates
df = df.drop_duplicates()

# Final Output
print("Final Shape:", df.shape)
df.to_csv("melb_data_cleaned.csv", index=False)
print("Data preprocessing completed. Cleaned file saved as 'melb_data_cleaned.csv'")
