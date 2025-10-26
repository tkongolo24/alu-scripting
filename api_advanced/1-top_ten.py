#!/usr/bin/python3
"""
Module to query Reddit API for hot posts.

This module contains a function to retrieve and display the titles
of the top 10 hot posts from a specified subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """Top ten subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data').get('children')
            [print(post.get('data').get('title')) for post in posts]
        else:
            print(None)
    except Exception:
        print(None)
