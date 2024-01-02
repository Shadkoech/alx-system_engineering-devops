#!/usr/bin/python3
"""
Python script using REST API,
For a given employee ID, returns information on his/her TODO list progress"""

import requests
import sys


if __name__ == "__main__":

    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + '/' + employeeId

    res = requests.get(url)
    employeeName = res.json().get('name')

    todoUrl = url + '/todos'
    res = requests.get(todoUrl)
    tasks = res.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
