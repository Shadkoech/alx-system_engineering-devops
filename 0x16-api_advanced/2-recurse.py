#!/usr/bin/python3
"""
Module that queries the Reddit API and returns a list
of all hot articles for a given subreddit.
Args:
    subreddit, hot_list=[]
Returns:
    A list of titles or None otherwose
    """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Function that recursively querries the reddit API and
    returns a list of all hot articles """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {
        "limit": 100,
        "after": after
    }
    headers = {
            "User-Agent": "Google Chrome Version 120.0.6099.217"
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        output = response.json()
        hot_posts = output['data']['children']
        after = output['data']['after']
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
