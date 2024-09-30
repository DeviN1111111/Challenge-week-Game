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



def valid_input(prompt: str, total_choices: int)-> str:
    user_input = input(prompt)  
    if user_input.isdigit():
        choice = int(user_input)
        if 1 <= choice <= total_choices:
            return str(choice)
        else:
            print("ERROR: Choice out of option range.")
            return valid_input(prompt, total_choices)
    else:
        print("ERROR: Invalid input. Please enter a number.")
        return valid_input(prompt, total_choices)
    

def is_name_valid(prompt: str)-> str:
    name = input(prompt)
    name = name.capitalize()
    if name.isalpha() and len(name) <= 10:
        return name
    else:
        print("ERROR: Invalid input.")
        return is_name_valid(prompt)
    

def level_one():
    typewriter()