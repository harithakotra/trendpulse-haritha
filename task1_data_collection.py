import requests
import json

# Reddit API endpoint for trending posts
url = "https://www.reddit.com/r/popular.json"

# Headers (important to avoid blocking)
headers = {
    "User-Agent": "Mozilla/5.0 (TrendingDataPipeline)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    posts = []

    for post in data["data"]["children"]:
        post_data = post["data"]

        posts.append({
            "title": post_data["title"],
            "subreddit": post_data["subreddit"],
            "score": post_data["score"],
            "url": post_data["url"],
            "comments": post_data["num_comments"]
        })

    # Save to JSON file
    with open("trending_posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4)

    print("Saved trending_posts.json")

else:
    print("Error:", response.status_code)