#!/usr/bin/python3
"""Returns a to do list information for a given employee ID."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    user_name = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), 'w') as jfile:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
        }for task in todos]}, jfile)
