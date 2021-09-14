#!/usr/bin/python3
"""Module to export json
"""
if __name__ == '__main__':
    import sys
    from json import dump
    from requests import get

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    name = get(url).json()['username']

    todo = get('https://jsonplaceholder.typicode.com/todos').json()

    task_dict = {}
    task_dict[sys.argv[1]] = []

    for task in todo:
        if task['userId'] == int(av[1]):
            tmp_dict = {}
            tmp_dict['task'] = task['title']
            tmp_dict['completed'] = task['completed']
            tmp_dict['username'] = name
            task_dict[sys.argv[1]].append(tmp_dict)

    with open('{}.json'.format(av[1]), 'w') as F:
        dump(task_dict, F)
