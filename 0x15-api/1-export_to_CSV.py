#!/usr/bin/python3
"""Module to export csv
"""
if __name__ == '__main__':
    import csv
    from sys import argv
    import requests

    if len(sys.argv) == 2:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
        res = requests.get(url)
        name = res.json()['username']
        todo = requests.get("https://jsonplaceholder.typicode.com/todos")
        with open(sys.argv[1] + '.csv', "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)

            for item in todo.json():
                if item['userId'] == int(sys.argv[1]):
                    csv_writer.writerow([sys.argv[1], name, item['completed'],
                                         item['title']])
