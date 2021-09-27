#!/usr/bin/python3
""" Module for api reddit """
import requests


def number_of_subscribers(subreddit):
    """ get the  number of suscribers """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Holberton'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
