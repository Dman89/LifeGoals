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
