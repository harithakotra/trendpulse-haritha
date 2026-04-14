import pandas as pd

# Load JSON file
df = pd.read_json("trending_posts.json")

# Preview data
print("Before Cleaning:")
print(df.head())

# -------------------------
# 🧹 Data Cleaning Steps
# -------------------------

# 1. Remove duplicate posts (based on title)
df = df.drop_duplicates(subset="title")

# 2. Handle missing values
df = df.dropna()

# 3. Convert data types (if needed)
df["score"] = df["score"].astype(int)
df["comments"] = df["comments"].astype(int)

# 4. Clean text (remove extra spaces)
df["title"] = df["title"].str.strip()

# 5. Filter low-quality posts (example: score < 100)
df = df[df["score"] >= 100]

# 6. Sort by popularity
df = df.sort_values(by="score", ascending=False)

# Reset index
df = df.reset_index(drop=True)

# Preview cleaned data
print("\nAfter Cleaning:")
print(df.head())

# -------------------------
# 💾 Save as CSV
# -------------------------
df.to_csv("cleaned_posts.csv", index=False)

print("\nCleaned data saved as cleaned_posts.csv")