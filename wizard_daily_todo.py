from functions import clear
import os
import json
content = ""
todos = ""
run_mode = 1
username = ""


def daily_todo_start(usrnam):
    global content
    global todos
    global run_mode
    global username
    username = usrnam
    try:
        with open("{}_subjects.json".format(username), "r") as fi:
            content = json.load(fi)
            content = content["subjects"]
    except FileNotFoundError:
        print("No Subjects Available")
        return None
    try:
        with open("{}_daily.json".format(username), 'r') as f:
            todos = json.load(f)
            todos = todos["daily"]
    except FileNotFoundError:
        todos = start_todos()
        save_todos(username, todos)
    while (run_mode == 1):
        function_selector()
    return todos
