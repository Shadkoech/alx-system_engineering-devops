#!/usr/bin/python3
"""
Python module that exports data in CSV format
"""

import requests
import sys


if __name__ == "__main__":

    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + '/' + employeeId

    res = requests.get(url)
    username = res.json().get('username')

    todoUrl = url + '/todos'
    res = requests.get(todoUrl)
    tasks = res.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
