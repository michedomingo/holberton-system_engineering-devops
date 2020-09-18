#!/usr/bin/python3
"""
Queries Reddit API, returns a list containing titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], next_topic=''):
    try:
        posts = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                             format(subreddit, next_topic),
                             allow_redirects=False,
                             headers={'User-Agent': 'custom'})
        if next_topic is None:
            return hot_list
        for topic in posts.json().get('data').get('children'):
            hot_list += [topic.get('data').get('title')]
        next_topic = posts.json().get('data').get('after')
        recurse(subreddit, hot_list, next_topic)
        return hot_list
    except:
        return None
