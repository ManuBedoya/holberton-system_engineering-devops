#!/usr/bin/python3
"""Module for api reddit
"""
import requests


def top_ten(subreddit):
    """display the 10 top
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Manu'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        for item in data['data']['children']:
            print(item['data']['title'])
    else:
        print(None)
