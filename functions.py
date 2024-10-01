import time
import random
from config import *


def typewriter(str):
    for letter in str: 
        time.sleep(random.uniform(time_sleep[0], time_sleep[1]))
        print(letter, end='', flush = True)
    print()


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
    
    
def give_player_weapon(weapon_name:str):
    for weapon in weapons:
        if weapon["name"] == weapon_name:
            player_stats["weapon"] = weapon
            return
    
    print(f"Wapen {weapon_name} niet gevonden.")
    
def is_yesno_valid(prompt: str)-> str:
    yesno = input(prompt)
    yesno = yesno[0].capitalize() + yesno[1:].lower()
    if yesno == 'Yes' or yesno == 'No':
        return yesno
    else:
        print("ERROR: Invalid input. Please enter 'Yes or 'No'.")
        return is_yesno_valid(prompt)


def item_highlight(text: str):
    return f"\033[91m{text}\033[0m"


def combat(enemy:str):
    if enemy in enemy_stats and player_stats["health"] > 0:
        enemy_name = enemy
        enemy = enemy_stats[enemy]
        player_weapon = player_stats["weapon"]
        enemy_hp_reset = enemy["health"]
        typewriter(f"You encountered a {enemy_name} he has {enemy["health"]} HP and you have {player_stats["health"]} hp!")
        
        while player_stats["health"] > 0 and enemy["health"] > 0:
            enemy["health"] -= player_weapon["damage"]
            typewriter(f"You hit the {enemy_name} for {player_weapon['damage']} damage.")
            if enemy["health"] > 0:
                typewriter(f"{enemy_name} health is now {enemy['health']}.")
            else:
                typewriter(f"{enemy_name} has 0 HP he died")
                enemy["health"] = enemy_hp_reset
                return
            if enemy["health"] > 0:    
                player_stats["health"] -= enemy["damage"]
                typewriter(f"The {enemy_name} hits you for {enemy['damage']} damage.")
                typewriter(f"Your health is now {player_stats['health']}.")
            if player_stats["health"] <= 0:
                typewriter("You died")
                break 
    else:
        typewriter(f"ERROR Enemy typo of je begint je gevecht met 0 of minder HP")
        
    
        