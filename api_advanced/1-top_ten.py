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
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful and not redirected
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            # Print the titles of the first 10 posts
            count = 0
            for post in posts:
                if count >= 10:
                    break
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
                    count += 1
        else:
            # Invalid subreddit or redirected
            print(None)
    except Exception:
        print(None)
