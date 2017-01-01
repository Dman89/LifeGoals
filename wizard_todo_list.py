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
def list_subjects():
    clear()
    z = 1
    for x in subjects:
        print("#"+str(z))
        print("\nName:")
        print(x["name"])
        print("\nValue:")
        print(x["rank"])
        print("\n\n\n")
        z+=1
def load_file(namE):
    global data
    global name
    name = namE
    try:
        with open(name+".json", "r") as DATA:
            data = json.load(DATA)
            data = data["goals"]
        print("\nUser Found\n\n")
        print("Goals left to Complete:\n", len(data), "\n\n")
    except FileNotFoundError:
        data = []
        print("\nUser Created\n\n")
    global subjects
    try:
        with open(name+"_subjects.json", "r") as DATA:
            subjects = json.load(DATA)
            subjects = subjects["subjects"]
        print("\nSubjects Loaded\n\n")
        print("In", len(subjects), "Subjects.\n\n")
    except FileNotFoundError:
        subjects = []
        print("\nSubjects Created\n\n")
    return data
def save_file(name, data):
    try:
        with open(str(name)+".json", "w", encoding="UTF-8") as text_file:
            json.dump({"goals": data}, text_file)
    except TypeError:
        print("\n\n\n","Didnt Save File '{}.json'".format(name), "\n\n\n\n")
    try:
        with open(str(name)+"_subjects.json", "w", encoding="UTF-8") as text_file:
            json.dump({"subjects": subjects}, text_file)
    except TypeError:
        print("\n\n\n","Didnt Save File '{}_subjects.json'".format(name), "\n\n\n\n")
def remove_goal():
    global data
    clear()
    list_data(0)
    print("\n\nNow removing a goal...")
    print("Remove #\n  >>> ")
    edit_num = check_index_vs_length(data)
    if edit_num != "False":
        check_now = input(str("Are you sure? "+data[edit_num]["name"]+" (y) >>> "))
        if check_now.lower() == "y":
            del data[edit_num]
            print("Removed Item.")
        else:
            print("Cancelled...")
            return
def remove_subjects():
    clear()
    list_subjects()
    print("\n\nNow removing a subject...")
    print("Remove #\n  >>> ")
    edit_num = check_index_vs_length(data)
    if edit_num != "False":
        check_now = input(str("Are you sure? "+subjects[edit_num]["name"]+" (y) >>> "))
        if check_now.lower() == "y":
            for info in data:
                if info["subject"]["name"] == subjects[edit_num]["name"]:
                    print("\n\nSubject is still in use, remove goal or change the goal's subject to continue with deleting the 'Subject'.\n\n\n")
                    return
            del subjects[edit_num]
            print("Removed Subject.")
        else:
            print("Cancelled...")
            return
def completed_goal():
    global data
    clear()
    list_data(0)
    print("\n\nNow marking goal completed...")
    print("Completed #\n")
    edit_num = check_index_vs_length(data)
    if edit_num != False:
        if data[edit_num]["completed"] == "True":
            data[edit_num]["completed"] = "False"
        else:
            data[edit_num]["completed"] = "True"
        print("Goal Completed.")
    else:
        print("Exiting now...")
def list_editable_goal(goal, number):
    global data
    item = input(str("Add a Goal (Old: "+goal["name"]+"): "))
    item = check_input(item, goal["name"])
    if item == "EXIT":
        return
    subject = input(str("Goal is for what Subject? (Old: "+goal["subject"]["name"]+"): "))
    subject = check_input(subject, goal["subject"]["name"])
    new_subject = search_for_subject(subject)
    print("For these next steps, the higher the number, the more important the goal.\n\n")
    if new_subject == "True":
        subrank = input(str("Rate the Subject's Value (1-100): "))
    else:
        subrank = new_subject
    rank = input(str("Rate the Goal (1-10) (Old: "+goal["rank"]+"): "))
    rank = check_input(rank, goal["rank"])
    impact = input(str("Impact Your Short Term Goals (1-10) (Old: "+goal["impact"]+"): "))
    impact = check_input(impact, goal["impact"])
    progression = input(str("What Effect Would this have on Your Development as a Person (1-100) (Old: "+goal["progression"]+"): "))
    progression = check_input(progression, goal["progression"])
    value = compute_goal(subrank, rank, impact, progression)
    goal = {"name": item, "subject": {"name": subject, "rank": subrank}, "rank": rank, "impact": impact, "progression": progression, "completed": "False", "id": goal["id"], "value": value}
    subject = {"name": subject, "rank": subrank}
    del data[number]
    data.insert(number, goal)
    if new_subject == "True":
        subjects.append(subject)
    print("Goal Edited!", "\n", goal["name"], "\n\n")
def list_editable_subject(subj, number):
    check = subjects[number]
    subject = input(str("Name for Subject? (Old: "+subj["name"]+"): "))
    subject = check_input(subject, subj["name"])
    if subject == "EXIT":
        return
    new_subject = search_for_subject(subject)
    if new_subject == "True":
        subrank = input(str("Rate the Subject's Value (1-100): "))
    else:
        subrank = input(str("Rate the Subject's Value (1-100) (Old: "+new_subject+"): "))
        subrank = check_input(subrank, new_subject)
    print("For these next steps, the higher the number, the more important the goal.\n\n")
    subject_save = {"name": subject, "rank": subrank}
    x = 0
    for info in data:
        if info["subject"]["name"] == check["name"]:
            data[x]["subject"]["name"] = subject
            data[x]["subject"]["rank"] = subrank
        x+=1
    del subjects[number]
    subjects.insert(number, subject_save)
    print("Subject Edited!", "\n", subject_save["name"], "\n\n")
    recompute_data()
    print("Data Recomputed\n\n")
def edit_goal():
    global data
    clear()
    list_data(0)
    print("\n\nNow editing a goal...")
    print("Edit #\n  >>> ")
    edit_num = check_index_vs_length(data)
    if edit_num != "False":
        goal = data[edit_num]
        list_editable_goal(goal, edit_num)
def edit_subjects():
    clear()
    list_subjects()
    print("\n\nNow editing a subject...")
    print("Edit #\n  >>> ")
    edit_num = check_index_vs_length(data)
    if edit_num != "False":
        subject = subjects[edit_num]
        list_editable_subject(subject, edit_num)
def search_for_subject(subj):
    for x in subjects:
        if subj == x["name"]:
            return x["rank"]
        else:
            continue
    return "True"
def sort_data():
    z=0
    while (z < len(data)):
        x=0
        y=1
        while (y < len(data)):
            if data[x]["value"] > data[y]["value"]:
                save_info = data[x]
                del data[x]
                data.insert(y, save_info)
            x+=1
            y+=1
        z+=1
def list_data(num):
    global data
    sort_data()
    print("\n\nListing Items...")
    z=1
    if num == 1:
        number = int(len(data))
    else:
        number = 1
    for info in data:
        print("\n\n___---***^^#"+str(number)+"^^***---___\n\n")
        print("#"+str(number))
        print("Index: #{}".format(z))
        print("Goal:")
        print(info["name"])
        print("Subject:")
        print(info["subject"]["name"])
        print("Progression:")
        print(info["progression"])
        print("Impact:")
        print(info["impact"])
        print("Rank:")
        print(info["rank"])
        print("Completed:")
        print(info["completed"])
        print("\nTotal Value:")
        print(int(info["value"]) / 10000)
        print("\n\n___---***^^#"+str(number)+"^^***---___\n\n")
        if num == 1:
            number -= 1
        else:
            number += 1
        z+=1
    print("\n")
def i_add_item():
    item = input(str("Add a Goal: "))
    if item == "EXIT":
        return
    subject = input(str("Goal is for what Subject?: "))
    if subject == "EXIT":
        return
    new_subject = search_for_subject(subject)
    print("For these next steps, the higher the number, the more important the goal.\n\n")
    if new_subject == "True":
        subrank = input(str("Rate the Subject's Value (1-100): "))
        if subrank == "EXIT":
            return
    else:
        subrank = new_subject
    rank = input(str("Rate the Goal (1-10): "))
    if rank == "EXIT":
        return
    impact = input(str("Impact Your Short Term Goals (1-10): "))
    if impact == "EXIT":
        return
    progression = input(str("What Effect Would this have on Your Development as a Person (1-100): "))
    if progression == "EXIT":
        return
    value = compute_goal(subrank, rank, impact, progression)
    goal = {"name": item, "subject": {"name": subject, "rank": subrank}, "rank": rank, "impact": impact, "progression": progression, "completed": "False", "id": time.time(), "value": value}
    subject = {"name": subject, "rank": subrank}
    data.append(goal)
    if new_subject == "True":
        subjects.append(subject)
    print("Goal Added!", "\n", goal["name"], "\n\n")
def i_order(name, data):
    order = input(str("Would you like to ADD, EDIT, EDIT SUBJECTS, REMOVE, REMOVE SUBJECTS, mark a goal COMPLETE, LIST, list SUBJECTS, list COMPLETED, view TOP goals, STORE completed goals, EXIT, SAVE, or SE (Save and Exit)?\n>>> "))
    print("{}:".format(order))
    if order == "ADD":
        print("\n\nNow adding a goal...")
        i_add_item()
    elif order == "EDIT":
        edit_goal()
    elif order == "COMPLETED":
        list_completed(name)
    elif order == "SEARCH":
        clear()
        term = input(str("Search:\n>>> "))
        search(term)
    elif order == "TOP":
        top_goals()
    elif order == "STORE":
        clear()
        clear_completed(name, data)
    elif order == "EDIT SUBJECTS":
        edit_subjects()
    elif order == "REMOVE":
        print("\n\nNow removing a goal...")
        remove_goal()
    elif order == "REMOVE SUBJECTS":
        print("\n\nNow removing a subject...")
        remove_subjects()
    elif order == "COMPLETE":
        print("\n\nNow marking a goal complete...")
        completed_goal()
    elif order == "SAVE":
        print("\n\nNow Saving...")
        save_file(name, data)
        print("\n\nSaved!\n")
    elif order == "SUBJECTS":
        print("\n\nNow Lisitng Subjects...")
        list_subjects()
    elif order == "LIST":
        clear()
        list_data(1)
    elif order == "EXIT":
        print("\n\nNow Exiting...")
        return False
    elif order == "SE":
        clear()
        print("\n\nNow Saving...")
        save_file(name, data)
        print("\n\nSaved!\n")
        print("\n\nNow Exiting...")
        return False
def check_index_vs_length(item_length):
    num = input(str("  > "))
    if num == "":
        return False
    if "EXIT" in num:
        return False
    try:
        num = int(num)
    except (TypeError, ValueError):
        return check_index_vs_length(item_length)
    else:
        if num > 0:
            if num <= len(item_length):
                num -= 1
                return num
            else:
                return check_index_vs_length(item_length)
        else:
            return check_index_vs_length(item_length)
# Main
def start_todo(namE):
    global name
    name = namE
    data = load_file(name)
    while (True):
        check = i_order(name, data)
        if check == False:
            break
