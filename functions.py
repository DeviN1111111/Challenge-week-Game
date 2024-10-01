import time
import random
from config import *


def typewriter(str):
    for letter in str: 
        time.sleep(random.uniform(time_sleep[0], time_sleep[1]))
        print(letter, end='', flush = True)
    print()

#validators
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
        player_stats["name"] = f"\033[36m{name}\033[0m"
        return f"\033[36m{name}\033[0m"#convert the name to cyan colour
    else:
        print("ERROR: Invalid input. Please enter letters only.")
        return is_name_valid(prompt)
    
    
def is_yesno_valid(prompt: str)-> str:
    yesno = input(prompt)
    yesno = yesno[0].capitalize() + yesno[1:].lower()
    if yesno == 'Yes' or yesno == 'No':
        return yesno
    else:
        print("ERROR: Invalid input. Please enter 'Yes or 'No'.")
        return is_yesno_valid(prompt)

#letter highlights
def item_highlight(text: str):#yellow
    return f"\033[33m{text}\033[0m"


def enemy_highlight(text: str):#green
    return f"\033[32m{text}\033[0m"


def hp_highlight(text: str):#red
    return f"\033[31m{text}\033[0m"


def dmg_highlight(text: str):#bright-red
    return f"\033[91m{text}\033[0m"

#combat stats
def give_player_weapon(weapon_name:str):
    for weapon in weapons:
        if weapon["name"] == weapon_name:
            player_stats["weapon"] = weapon
            return
    
    print(f"Weapon {weapon_name} not found.")


def combat(enemy:str):
    if enemy in enemy_stats and player_stats["health"] > 0:
        enemy_name = enemy
        enemy = enemy_stats[enemy]
        player_weapon = player_stats["weapon"]
        enemy_hp_reset = enemy["health"]
        typewriter(f"You encountered a {enemy_highlight(enemy_name)} he has {hp_highlight(enemy["health"])} {hp_highlight("health")} and you have {hp_highlight(player_stats["health"])} {hp_highlight("health")}!")
        
        while player_stats["health"] > 0 and enemy["health"] > 0:
            enemy["health"] -= player_weapon["damage"]
            typewriter(f"{player_stats["name"]} hit the {enemy_highlight(enemy_name)} for {dmg_highlight(player_weapon['damage'])} {dmg_highlight("damage")}.")
            if enemy["health"] > 0:
                typewriter(f"{enemy_highlight(enemy_name)} {hp_highlight("health")} is now {hp_highlight(enemy['health'])}.")
            else:
                typewriter(f"{enemy_highlight(enemy_name)} has {hp_highlight("0 health")} he died")
                enemy["health"] = enemy_hp_reset
                return
            if enemy["health"] > 0:    
                player_stats["health"] -= enemy["damage"]
                typewriter(f"The {enemy_highlight(enemy_name)} hits you for {dmg_highlight(enemy['damage'])} {dmg_highlight("damage")}.")
                typewriter(f"Your {hp_highlight("health")} is now {hp_highlight(player_stats['health'])}.")
            if player_stats["health"] <= 0:
                typewriter("You died")
                break 
    else:
        typewriter(f"ERROR Enemy typo of je begint je gevecht met 0 of minder HP")
        
    
def player_reset():
    player_stats["health"] = 100
    give_player_weapon("Fist")