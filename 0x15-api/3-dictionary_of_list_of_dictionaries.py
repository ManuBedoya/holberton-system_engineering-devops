#!/usr/bin/python3
"""module to dictionary of list dictionaries
"""
if __name__ == '__main__':
    from json import dump
    from requests import get

    name_path = 'https://jsonplaceholder.typicode.com/users/'
    users = get(name_path).json()

    todo = get('https://jsonplaceholder.typicode.com/todos').json()

    name_list = []
    task_dict = {}

    for user in users:
        task_dict[user['id']] = []
        name_list.append(user['username'])

    for task in todo:
        tmp_dict = {}
        tmp_dict['username'] = name_list[task['userId'] - 1]
        tmp_dict['task'] = task['title']
        tmp_dict['completed'] = task['completed']
        task_dict[task['userId']].append(tmp_dict)

    with open('todo_all_employees.json', 'w') as F:
        dump(task_dict, F)
