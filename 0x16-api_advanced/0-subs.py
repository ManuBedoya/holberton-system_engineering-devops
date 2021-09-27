#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
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
