#!/usr/bin/python3
"""returns info about employee's todo list"""
import requests
from sys import argv


if __name__ == "__main__":
    # get the given employees info
    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    ).json()

    # get the employees todo list
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    ).json()

    # make it an actual list object
    todo_list = [
        task.get("title") for task in todos if task.get("completed") is True
    ]

    # format and print response
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee.get("name"), len(todo_list), len(todos)
        ), *todo_list, sep="\n\t "
    )
