#!/usr/bin/python3
"""
    Uses reddit API to get 10 hot posts
"""
import requests
import sys

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header

    try:
        response = requests.get(url, headers=headers, params={"limit": 10})
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            for post in posts:
                title = post["data"]["title"]
                print(title)
        else:
            print("None")
    except requests.RequestException:
        print("None")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
