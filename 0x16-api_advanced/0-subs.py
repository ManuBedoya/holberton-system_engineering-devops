#!/usr/bin/python3
"""Module to get the suscriberf of an specific subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Method to get suscribers
    """
    if (len(sys.argv) == 2):
        user_ag = {'User-Agent': 'Hoberton'}
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

        response = requests.get(url, headers=user_ag)
        data = response.json()
        try:
            return data['data']['subscribers']
        except KeyError:
            return 0
    return 0
