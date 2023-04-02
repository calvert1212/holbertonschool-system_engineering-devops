#!/usr/bin/python3
"""
Retrieves TODO list progress of a given employee ID from a REST
API and exports data to a CSV file.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    EMPLOYEE_ID = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        EMPLOYEE_ID)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        exit(1)

    todos = response.json()
    employee_name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        EMPLOYEE_ID)
    response_name = requests.get(employee_name_url)

    if response_name.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_name.status_code))
        exit(1)

    employee_name = response_name.json().get("username")
    filename = "{}.csv".format(EMPLOYEE_ID)

    with open(filename, mode="w", newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for todo in todos:
            completed_status = "True" if todo["completed"] else "False"
            writer.writerow({
                'USER_ID': EMPLOYEE_ID,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': completed_status,
                'TASK_TITLE': todo["title"]
            })
