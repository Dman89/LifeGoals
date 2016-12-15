from functions import clear
from functions import p
import json

run_priorities_on = 1
goals_arr = []
username = ""
top_one = ""
top_3 = ""
final_ans = {}
run_mode = 1


def start_goal_finding():
    clear()
    p("Enter your life goals, one by one:")
    enter_mode = 1
    x = 0
    global run_priorities_on
    global goals_arr
    while (enter_mode == 1):
        p("\n")
        goal_item = add_item()
        if "EXIT" in goal_item:
            enter_mode = 0
            run_priorities_on = 1
        elif len(goal_item) == 0:
            if len(goals_arr) > 2:
                if "" in goal_item:
                    enter_mode = 0
        else:
            goals_arr.append(goal_item)
            x+=1
    return goals_arr

def add_item():
    global goals_arr
    res = input(str("> "))
    if len(res) == 0:
        if len(goals_arr) > 2:
            return ""
        else:
            print("Must have Three Items")
            return add_item()
    else:
        return res

def selecting_priorities(req):
    clear()
    x=1
    for item in req:
        print("""
        #{} - {}
        """.format(x,item))
        x+=1
    return x

def top_3_select(req):
    p("""
    Select the Top 3 Goals:
    """)
    n1 = top_3_check("First")
    n2 = unique_check("Second", n1, top_3_check("Second"), None)
    n3 = unique_check("Third", n1, n2, top_3_check("Third"))
    clear()
    print("""
    {}
    {}
    {}
    """.format(req[n1-1], req[n2-1], req[n3-1]))
    return [req[n1-1], req[n2-1], req[n3-1]]

def unique_check(text, n1, n2, n3):
    if n3:
        if n3 != n1:
            if n3 != n2:
                return n3
            else:
                return unique_check(text, n1, n2, top_3_check("{} [NOT in use] ".format(text)))
        else:
            return unique_check(text, n1, n2, top_3_check("{} [NOT in use] ".format(text)))
    else:
        if n2 != n1:
            return n2
        else:
            return unique_check(text, n1, top_3_check("{} [NOT in use] ".format(text)), None)

def top_3_check(text):
    if "Must be a Number" in text:
        text = "{}".format(text)
    else:
        text = "{} (Must be a Number)".format(text)
    try:
        num = int(input(str("{}: ".format(text))))
    except (ValueError, TypeError):
        top_3_check(text)
    else:
        global goalsArr
        if num < 1:
            return top_3_check(text)
        elif num > len(goalsArr):
            return top_3_check(text)
        return int(num)

def check_remove():
    try:
        remove = int(input(str("> ")))
    except (TypeError, ValueError):
        return check_remove()
    else:
        if remove < 1:
            return check_remove()
        if remove > 3:
            return check_remove()
        return remove

def print_list(data):
    x=1
    for item in data:
        print("""#{} - {}""".format(x, item))
        x+=1

def pick_item():
    try:
        add = int(input(str("> ")))
    except (TypeError, ValueError):
        return pick_item()
    else:
        if add < 1:
            return pick_item()
        if add > 2:
            return pick_item()
        return add
