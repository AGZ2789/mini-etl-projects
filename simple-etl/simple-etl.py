import pandas as pd

# Extract
data = {
    "name": ["Alice", "Bob", "Charlie", None],
    "age": [25, 30, None, 22],
    "city": ["NY", "LA", "Chicago", "Miami"]
}
df = pd.DataFrame(data)

# Save a raw file
df.to_csv("raw_data.csv", index=False)

# Transform
df_clean = df.dropna()  # remove rows with missing values
df_clean["age"] = df_clean["age"].astype(int)  # convert to integer

# Load
df_clean.to_csv("clean_data.csv", index=False)

print("ETL complete. Clean data saved to clean_data.csv")
