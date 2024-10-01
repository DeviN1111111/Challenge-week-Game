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
    if user_input.startswith("/"):
        input_commands(user_input)
        return valid_input(prompt, total_choices)
    elif user_input.isdigit():
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
    if name.startswith("/"):
        input_commands(name)
        return is_name_valid(prompt)
    elif name.isalpha() and len(name) <= 10:
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
    elif yesno.startswith("/"):
        input_commands(yesno)
        return is_yesno_valid(prompt)
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
        value_of_damage_potion = check_inventory_value("Damage potion")
        
        typewriter(f"You encountered a {enemy_highlight(enemy_name)} he has {hp_highlight(enemy["health"])} {hp_highlight("health")} and you have {hp_highlight(player_stats["health"])} {hp_highlight("health")}!")
        
        while player_stats["health"] > 0 and enemy["health"] > 0:
            amount_of_damage_potions = check_inventory_amount("Damage potion")
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
                if(player_stats["health"] > 0 ):
                    typewriter(f"Your {hp_highlight("health")} is now {hp_highlight(player_stats['health'])}.")
                else:
                    typewriter(f"Your {hp_highlight("health")} is now {hp_highlight("0.")}")
                    typewriter(f"{hp_highlight("YOU DIED!")}")
                    break 
                
            if amount_of_damage_potions > 0:
                user_input = is_yesno_valid(f"Do you want to use a damage potion? You have {amount_of_damage_potions} damage potions left!")
                if user_input.lower() == "yes":
                    for item in player_inventory:
                        if item["name"] == "Damage potion":
                            item["amount"] -= 1
                    if enemy["health"] <= value_of_damage_potion:
                        enemy["health"] -=  value_of_damage_potion
                        typewriter(f"Your damage potion hit the {enemy_name} right on! it did {value_of_damage_potion} damage")
                        typewriter(f"{enemy_highlight(enemy_name)} {hp_highlight("health")} is now 0.")
                    else:
                        enemy["health"] -=  value_of_damage_potion
                        typewriter(f"Your damage potion hit the {enemy_name} right on! it did {value_of_damage_potion} damage")
                        typewriter(f"{enemy_highlight(enemy_name)} {hp_highlight("health")} is now {hp_highlight(enemy['health'])}.")
                else:
                    typewriter("no damage pot used")

    else:
        typewriter(f"ERROR Enemy typo of je begint je gevecht met 0 of minder HP")
        
    
def player_reset():
    player_stats["health"] = 100
    give_player_weapon("Fist")
    
def use_healing_potion():
    for item in player_inventory:
        if item["name"] == "Healing potion":
            if item["amount"] > 0:
                if player_stats["health"] <= 50: #Healing does 50 this makes sure u dont heal over 100 health
                    item["amount"] -= 1
                    player_stats["health"] += item["amount_of_healing"]
                    typewriter(f"You healed for 50 health you now have {player_stats["health"]} health and have {item['amount']} healing potions left")
                elif player_stats["health"] >= 50 and player_stats["health"] < 100:
                    item["amount"] -= 1
                    player_stats["health"] = 100 #If you are over 50 hp you would heal to over 100 hp this makes sure u only heal to 100
                    typewriter(f"You healed to 100 hp. and have {item['amount']} healing potions left")
                else:
                    typewriter(f"You are already full hp! you have {item['amount']} healing potions left")
            else:
                typewriter("You have no healing potions")
                
def input_commands(command): 
    if command.lower() == "/heal":
        use_healing_potion()
    elif command.lower() == "/help":
        show_help()
    elif command.lower() == "/inventory":
        print_inventory()
    else:
        typewriter("Invalid command type /help for help.")
        return
    
    
def show_help():
    help_text = """
    Available Commands:

    /heal          - Use a healing potion to restore health.
    
    /inventory     - Display your current inventory items.
    
    /help          - Show this help message with the list of commands.

    Type a command to execute it. Have fun exploring!
    """
    typewriter(help_text)
    
    
def print_inventory():
    for item in player_inventory:
        print(f"- {item["name"]} amount: {item["amount"]}")
    print("") 
    
    
def check_inventory_amount(item_name:str): #you can use this function to see how many of asked item you have left
    for item in player_inventory:
        if item["name"] == item_name:
            return item["amount"]
        
def check_inventory_value(item_name:str): #you can use this function to see the value of an item
    for item in player_inventory:
        if item["name"] == item_name:
            return item["value"]
        
def add_inventory_value(item_name:str, item_amount:int): #you can use this function to add an item to a player eg add_inventory_value("Healing potion", 3) adds 3 healing potions
    for item in player_inventory:
        if item["name"] == item_name:
            item["value"] += item_amount
            return
    