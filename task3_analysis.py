import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("cleaned_posts.csv")

print(" Dataset Overview")
print(df.head())
print("\nShape:", df.shape)

# -------------------------
# 🔍 Basic Statistics
# -------------------------
print("\n Score Statistics")
print(df["score"].describe())

print("\n Comments Statistics")
print(df["comments"].describe())

# -------------------------
#  NumPy Analysis
# -------------------------

scores = df["score"].values
comments = df["comments"].values

print("\n NumPy Insights")

print("Average Score:", np.mean(scores))
print("Median Score:", np.median(scores))
print("Max Score:", np.max(scores))
print("Min Score:", np.min(scores))

print("\nAverage Comments:", np.mean(comments))

# Correlation between score and comments
correlation = np.corrcoef(scores, comments)[0, 1]
print("\n Correlation (Score vs Comments):", correlation)

# -------------------------
#  Top Posts
# -------------------------
print("\n Top 5 Posts by Score")
print(df.nlargest(5, "score")[["title", "score"]])

# -------------------------
# 📌 Subreddit Analysis
# -------------------------

# Posts count per subreddit
subreddit_counts = df["subreddit"].value_counts()
print("\nTop Subreddits:")
print(subreddit_counts.head())

# Average score per subreddit
avg_score_sub = df.groupby("subreddit")["score"].mean().sort_values(ascending=False)
print("\n Avg Score per Subreddit:")
print(avg_score_sub.head())

# -------------------------
# ⚡ Engagement Metric
# -------------------------

# Engagement ratio
df["engagement"] = df["comments"] / df["score"]

print("\nTop 5 Most Engaging Posts")
print(df.nlargest(5, "engagement")[["title", "engagement"]])

# -------------------------
# 💾 Save analyzed data
# -------------------------
df.to_csv("analyzed_posts.csv", index=False)

print("\n Analysis complete. Saved as analyzed_posts.csv")