#!/usr/bin/python3
"""Module to geather data from API
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 2:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
        response = requests.get(url)
        txt_json = response.json()
        count_total = 0
        count_complete = 0
        todo = requests.get("https://jsonplaceholder.typicode.com/todos")
        message = "Employee {} is done with ".format(txt_json['name'])
        extra = ""

        for item in todo.json():
            if item['userId'] == int(argv[1]):
                if item['completed']:
                    count_complete += 1
                    extra += "\n\t {}".format(item['title'])
                count_total += 1
        message += "tasks({}/".format(count_complete)
        message += "{}):".format(count_total)
        print(message + extra)
