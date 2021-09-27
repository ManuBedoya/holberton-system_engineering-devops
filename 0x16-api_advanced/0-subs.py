#!/usr/bin/python3
import requests
import user_agent
import sys

def number_of_subscribers(subreddit):
    if (len(sys.argv) == 2):
        user_ag = {'User-Agent': user_agent.generate_user_agent()}
        url = 'https://www.reddit.com/r/{}/about.json'.format(sys.argv[1])

        response = requests.get(url, headers=user_ag)
        data = response.json()
        try:
            return data['data']['subscribers']
        except KeyError:
            return 0
    return 0
