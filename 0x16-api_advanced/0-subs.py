#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    # Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set the user-agent header
    headers = {'User-Agent': 'YOUR_USER_AGENT'}

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
