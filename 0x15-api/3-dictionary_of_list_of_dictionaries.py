#!/usr/bin/python3
"""Returns a to do list information for a given employee ID."""
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", 'w') as jfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "complted": t.get("completed"),
                "usrename": t.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userid": u.get("id")}).json()]
            for u in users}, jfile)
