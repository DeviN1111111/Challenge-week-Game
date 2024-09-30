import time
import random
from config import time_sleep


def typewriter(str):
    for letter in str: 
        time.sleep(random.uniform(time_sleep[0], time_sleep[1]))
        print(letter, end='', flush = True)
    print()


def main_menu()->str:
    return'''
========================================
        Welcome to placeholder
        made by Devin & Lucio
========================================
    placeholder story intro
          


========================================
    Enter '1' to start the game.
    Enter '2' to quit.
========================================'''


def is_choice_valid(picked_choice:str,total_choices:int):#->bool?():
    if int(picked_choice) >= 1 and int(picked_choice) <= total_choices:
        return True
    else:
        return False
        
    

# def input_error(valid):
#     while not valid:
#         print('Input Error')
#         return False
    
    

