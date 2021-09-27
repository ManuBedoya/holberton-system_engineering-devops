#!/usr/bin/python3
import requests
import user_agent
import sys

def top_ten(subreddit):
    if (len(sys.argv) == 2):
        user_ag = {'User-Agent': user_agent.generate_user_agent()}
        url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(sys.argv[1])

        response = requests.get(url, headers=user_ag)
        data = response.json()
        try:
            for item in data['data']['children']:
                print(item['data']['title'])
        except KeyError:
            print('None')
