#!/usr/bin/python3
import requests
import sys
import user_agent


def recurse(subreddit, hot_list=[], after=None):
    user_ag = {'User-Agent': user_agent.generate_user_agent()}
    try:
        if after is None:
            url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        else:
            url = 'https://www.reddit.com/r/{}/hot.json?after={}'
            url = url.format(subreddit, after)
    except KeyError:
        return None

    response = requests.get(url, headers=user_ag)
    data = response.json()['data']['children'][0]['data']['title']
    hot_list.append(data)
    if response.json()['data']['after'] is not None:
        return recurse(subreddit, hot_list, response.json()['data']['after'])
    else:
        return hot_list
