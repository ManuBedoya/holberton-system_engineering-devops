#!/usr/bin/python3
"""Module for api reddit
"""
import requests


def count_words(subreddit, word_list):
    """Method recursive that counts words
    """
    headers = {'User-Agent': 'Manu'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if after is None:
        return word_list

    params = {'limit': 100, 'count': count}
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        catch = response.json()
        data = catch.get('data')
        after = catch.get('after')

        for item in data.get('children'):
            word_list.append(item.get('data').get('title'))
    except:
        return None
    return recurse(subreddit, word_list)
