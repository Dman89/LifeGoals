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

def list_todos():
    clear()
    print("""
    Listing Daily Todos:
    """)
    list_todos_function()

def list_todos_function():
    global todos
    x=0
    data = []
    for items in todos:
        x+=1
        print("""
        #{} - {}
        """.format(x, items))
        data.append(items)
        for item in todos[items]:
            print("""
            Name: {}
            Value: {}""".format(item['name'], item['rank']))
        print("\n")
    return data

def function_selector():
    global todos
    global username
    global run_mode
    print("""
ADD, EDIT, REMOVE, SAVE, or LIST Daily Todos
    To Exit: Type EXIT or SE to Save and Exit""")
    selector = input(str("""
> """))
    if "ADD" in selector:
        add_todos()
    elif "EDIT" in selector:
        edit_todos()
    elif "SAVE" in selector:
        save_todos(username, todos)
    elif "REMOVE" in selector:
        remove_todos()
    elif "LIST" in selector:
        list_todos()
    elif "EXIT" in selector:
        run_mode = 0
    elif "SE" in selector:
        save_todos(username, todos)
        run_mode = 0

def save_todos(username, todos):
    with open("{}_daily.json".format(username), mode="w") as file:
        json.dump({"daily": todos}, file)
        print("""
        Saved File...
        """)
