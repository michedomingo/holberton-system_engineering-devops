#!/usr/bin/python3
"""
Queries Reddit API, prints titles of first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    try:
        posts = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                             format(subreddit), allow_redirects=False,
                             headers={'User-Agent': 'custom'})
        for topic in posts.json().get('data').get('children'):
            print(topic.get('data').get('title'))
    except:
        print('None')
