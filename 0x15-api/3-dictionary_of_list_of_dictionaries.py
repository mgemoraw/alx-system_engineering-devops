#!/usr/bin/python3
"""Returns a to do list information for a given employee ID."""
import requests
import json

if __name__=="__main__":
    
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", 'w') as jfile:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "complted": task.get("completed"),
                "usrename": user.get("username")
            } for task in requests.get(url+"todos", params={"userid": user.get("id")}).json()]
            for user in users}, jfile)
