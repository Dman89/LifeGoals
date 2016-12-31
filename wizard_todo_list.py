import os
import time
import json
from functions import clear
goal = {"name": "", "subject": {"name": "", "rank": 0}, "rank": "", "impact": "", "progression": "", "completed": "False", "id": time.time(), "value": 0}
subject = {"name": "", "rank": 0}
completed_arr = []
data = []
check = ""
def check_input(i, o):
    if "" in i:
        if len(i) == 0:
            print("\n", o, "\n\n")
            return o
        else:
            return i
def top_goals():
    global data
    sort_data()
    list_top = data
    list_top.reverse()
    clear()
    print("\n\n\n")
    z=0
    for info in list_top:
        if z < 3:
            if info["completed"] == "False":
                print(info["name"], "\n", (int(info["value"])/10000), "\n\n")
                z+=1
def search(term):
    global data
    z = 1
    x = 0
    for info in data:
        if term in info["name"]:
            print("\n\n___---***^^#"+str(z)+"^^***---___\n\n")
            print("Name:", info["name"], "\n", "Subject:", info["subject"]["name"], "\n", "Value:", (int(info["value"]) / 10000), "\n", "Index:", x)
            print("\n\n___---***^^#"+str(z)+"^^***---___\n\n")
            z+=1
        x+=1
    if z == 1:
        print("Not in a current goal.")
def list_completed(name):
    global completed_arr
    clear()
    try:
        with open(name+"_completed.json", "r") as DATA:
            completed_arr = json.load(DATA)
            completed_arr = completed_arr["completed"]
        print("\nCompleted Goals Found\n\n")
        print("Past Goals Complete:\n", len(completed_arr), "\n\n")
    except FileNotFoundError:
        completed_arr = []
        print("\nNone Completed, yet...\n\n")
        return
    else:
        for comp in completed_arr:
            print(comp["name"])
            print(comp["subject"]["name"])
            print((int(comp["value"])/ 10000))
            print("\n\n\n")
def clear_completed(name, data):
    global completed_arr
    z=0
    for info in data:
        if info["completed"] == "True":
            try:
                with open("{}_completed.json".format(name), "r") as DATA:
                    completed_arr = json.load(DATA)
                    completed_arr = completed_arr["completed"]
                    print("\nCompleted Goals Found\n\n")
                    print("Past Goals Complete:\n", len(completed_arr), "\n\n")
            except FileNotFoundError:
                completed_arr = []
                print("\nCompleted Goals Created\n\n")
            complete_a_goal = data[z]
            completed_arr.append(complete_a_goal)
            del data[z]
        z+=1
    try:
        with open("{}_completed.json".format(name), "w", encoding="UTF-8") as text_file:
            json.dump({"completed": completed_arr}, text_file)
    except TypeError:
        print("\n\n\n","Didnt Save File", "\n\n\n\n")
    save_file(name, data)
def compute_goal(subrank, rank, impact, progression):
    return ((int(rank) * int(subrank)) * (int(impact) * int(progression)))
def recompute_data():
    global data
    x=0
    for info in data:
        data[x]["value"] = compute_goal(info["subject"]["rank"], info["rank"], info["impact"], info["progression"])
        x+=1
