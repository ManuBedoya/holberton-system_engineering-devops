#!/usr/bin/python3
"""Module for api reddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive method to get the all hot list
    """
    user_ag = {'User-Agent': 'Manu'}
    try:
        if after is None:
            url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        else:
            url = 'https://www.reddit.com/r/{}/hot.json?after={}'
            url = url.format(subreddit, after)
    except KeyError:
        return None

    response = requests.get(url, headers=user_ag, allow_redirects=False)
    data = response.json()['data']['children'][0]['data']['title']
    hot_list.append(data)
    if response.json()['data']['after'] is not None:
        return recurse(subreddit, hot_list, response.json()['data']['after'])
    else:
        return hot_list
