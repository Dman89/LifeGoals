import os
from sys import platform
from functions import clear
from functions import username_input
from wizard_top_goal import top_3_start
from wizard_daily_todo import daily_todo_start
from wizard_todo_list import start_todo
import wizard_long_term_goals


username = username_input()
top_3_start(username)
wizard_long_term_goals.start(username)
daily_todo_start(username)
start_todo(username)
