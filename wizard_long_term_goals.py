import json
import os
import time
import functions
from functions import clear
from functions import compute_value
from functions import is_max
from functions import search_for_subject

username=""
subjects=""
master=""
long_term_goals={}
life_goals={}
file_life_goals = {}
run_list = 1
def start(u):
    global username
    global subjects
    global run_list
    username = u
    file_loaded = load_file(u)
    subjects = functions.load_subjects(u)
    load_file_life_goals(u)
    if file_loaded == True:
        while (run_list == 1):
            # Load Options
            list_options()
    else:
        select_linked()
        # Go Through Walk Through Wizard
