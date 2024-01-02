#!/usr/bin/python3
"""Returns a to do list information for a given employee ID."""
import sys
import requests
import csv


if __name__=="__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    user_name = user.get("username")
    todos = requests.get(url + "todos", params={"userId":user_id}).json()

    with open("{}.csv".format(user_id), 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, task.get("completed"), task.get("title")]
        ) for task in todos]
