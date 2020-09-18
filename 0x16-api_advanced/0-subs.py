#!/usr/bin/python3
"""
Queries Reddit API, returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    try:
        subscribers = requests.get('https://www.reddit.com/r/{}/about.json'.
                                   format(subreddit), allow_redirects=False,
                                   headers={'User-Agent': 'custom'})
        return subscribers.json().get('data').get('subscribers')
    except:
        return 0
