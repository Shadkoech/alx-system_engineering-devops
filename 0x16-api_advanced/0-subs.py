#!/usr/bin/python3
"""Python module that queries the Reddit API and returns the
number of sunscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Obtains number of subscribers in a parsed
    subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Setting up a custom User-Agent to avoid too many Request errors
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    output = response.json()

    if response.status_code != 200:
        return 0
    if 'data' not in output:
        return 0
    if 'subscribers' not in output.get('data'):
        return 0

    subscribers_count = output['data']['subscribers']
    return (subscribers_count)
