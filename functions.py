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
In a world overrun by plague and creatures of darkness, your wife lies gravely ill. 
As a skilled alchemist, you alone have the knowledge to craft a cure,
but the rare ingredients you need are scattered across a dying, perilous land.
Armed with potions and desperation, you must venture beyond the safety of your lab
into forgotten ruins, haunted forests, and crumbling villages.
Time is running out. Will you find the cure before it's too late?
Or will the horrors of this shattered world consume you?
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
        print("ERROR: Invalid input. Please enter letters only.")
        return is_name_valid(prompt)
    

def level_one():
    typewriter('''
As you step out of your lab, the air is thick with decay, and the once-familiar village now feels like a stranger.
The sky, a bleak gray, hangs over crumbling houses and the echo of distant groans.
With your satchel of alchemical supplies strapped tight, you head towards the town square, knowing the first ingredient lies somewhere within the village.
But you don't make it far before a chilling sound stops you in your tracks.
A shambling figure emerges from behind a broken cart—its skin gray, eyes lifeless. It stumbles toward you, hunger in its eyes. 
You've read about these creatures, but now you face one, alone.
Your hands shake as you ready your weapon. It's time to fight. Will your alchemy save you?''')