import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("analyzed_posts.csv")

# -------------------------
#  1. Top Subreddits (Bar Chart)
# -------------------------
top_subreddits = df["subreddit"].value_counts().head(10)

plt.figure()
plt.bar(top_subreddits.index, top_subreddits.values)
plt.title("Top 10 Subreddits by Post Count")
plt.xlabel("Subreddit")
plt.ylabel("Number of Posts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------
#  2. Score Distribution (Histogram)
# -------------------------
plt.figure()
plt.hist(df["score"], bins=20)
plt.title("Distribution of Post Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -------------------------
#  3. Comments Distribution (Histogram)
# -------------------------
plt.figure()
plt.hist(df["comments"], bins=20)
plt.title("Distribution of Comments")
plt.xlabel("Comments")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -------------------------
#  4. Score vs Comments (Scatter Plot)
# -------------------------
plt.figure()
plt.scatter(df["score"], df["comments"])
plt.title("Score vs Comments Relationship")
plt.xlabel("Score")
plt.ylabel("Comments")
plt.tight_layout()
plt.show()

# -------------------------
#  5. Top 10 Posts by Score
# -------------------------
top_posts = df.nlargest(10, "score")

plt.figure()
plt.barh(top_posts["title"], top_posts["score"])
plt.title("Top 10 Posts by Score")
plt.xlabel("Score")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()