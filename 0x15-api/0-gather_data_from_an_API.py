#!/usr/bin/python3
"""Returns a to do list information for a given employee ID."""
import sys
import requests


if __name__=="__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId":sys.argv[1]}).json()

    completed = [task.get("title") for task in todos if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(task)) for task in completed]
