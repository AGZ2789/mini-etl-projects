import pandas as pd

# 1. Extract: make a small dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "Dana"],
    "Score": [85, 90, 78, 92]
}
df = pd.DataFrame(data)

# 2. Transform: add a "Passed" column
df["Passed"] = df["Score"] >= 80

df["Failed"] = df["Score"] <= 80

# 3. Load: save to a CSV file
df.to_csv("results.csv", index=False)

print("Done! Check results.csv for the output.")
