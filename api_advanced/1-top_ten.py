#!/usr/bin/python3
"""
Module to query Reddit API for hot posts.

This module contains a function to retrieve and display the titles
of the top 10 hot posts from a specified subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'linux:reddit.api.project:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data').get('children')
            [print(post.get('data').get('title')) for post in posts]
        else:
            print(None)
    except Exception:
        print(None)
