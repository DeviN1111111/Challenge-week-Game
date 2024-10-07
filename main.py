import time, random
from config import *

#alternative prints
def typewriter(str):
    for letter in str: 
        time.sleep(random.uniform(time_sleep[0], time_sleep[1]))
        print(letter, end='', flush = True)
    print()


def game_print(text: str)-> str:
    print(f"{print_highlight(text)}")


def inv_add_print(item: str, colour: str)-> str:
    if colour == 'Yellow':
        print(f"\033[1;37mAdded \033[33m{item}\033[1;37m to your inventory\033[0m")
    elif colour == 'Purple':
        print(f"\033[1;37mAdded \033[35m{item}\033[1;37m to your inventory\033[0m")

#validators
def is_number_valid(prompt: str, total_choices: int)-> str:
    user_input = input(prompt)
    if user_input.startswith("/"):
        input_commands(user_input)
        return is_number_valid(prompt, total_choices)
    elif user_input.isdigit():
        choice = int(user_input)
        if 1 <= choice <= total_choices:
            return str(choice)
        else:
            print("ERROR: Choice out of option range.")
            return is_number_valid(prompt, total_choices)
    else:
        print("ERROR: Invalid input. Please enter a number.")
        return is_number_valid(prompt, total_choices)
    

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


def item_highlight_bold(text: str):#yellow -> white bold
    return f"\033[33m{text}\033[1;37m"


def enemy_highlight(text: str):#green
    return f"\033[32m{text}\033[0m"


def hp_highlight(text: str):#red
    return f"\033[31m{text}\033[0m"


def hp_highlight_bold(text: str):#red -> white bold
    return f"\033[31m{text}\033[1;37m"


def dmg_highlight(text: str):#bright-red
    return f"\033[91m{text}\033[0m"


def pot_highlight(text: str):#purple
    return f"\033[35m{text}\033[0m"


def pot_highlight_bold(text: str):#purple -> bold
    return f"\033[35m{text}\033[1;37m"


def print_highlight(text: str):#white-bold
    return f"\033[1;37m{text}\033[0m"

#combat stats
def give_player_weapon(weapon_name:str):
    for weapon in weapons:
        if weapon["name"] == weapon_name:
            player_stats["weapon"] = weapon["name"]
            return
    
    print(f"Weapon {weapon_name} not found.")


def upgrade_weapon(amount:int):
    current_weapon = player_stats["weapon"]
    for weapon in weapons:
        if weapon["name"] == current_weapon:
            weapon["damage"] += amount


def stealth(steps:int):
    for i in range(steps):
        if i == 0:
            yes_or_no = is_yesno_valid("Do you want to take a step closer? ")
        else:
            yes_or_no = is_yesno_valid("Do you want to take another step closer? ")
        random_number = random.randint(0, 100)
        if random_number >= 65 and yes_or_no == "Yes":
            typewriter("He heard you and wakes up!")
            combat("Crystal Golem")
            return False
        elif random_number < 65 and yes_or_no == "Yes":
            typewriter(f"You took a step he didnt hear you, step {i + 1}/{steps}")
    return True
            


def combat(enemy:str):
    if enemy in enemy_stats and player_stats["health"] > 0:
        enemy_name = enemy
        enemy = enemy_stats[enemy]
        current_weapon = player_stats["weapon"]
        enemy_hp_reset = enemy["health"]
        value_of_damage_potion = check_inventory_value("Damage potion")
        amount_of_damage_potions = check_inventory_amount("Damage potion")
        
        for weapon in weapons:
            if weapon["name"] == current_weapon:
                player_weapon = weapon
        
        typewriter(f"You encountered a {enemy_highlight(enemy_name)}! He has {hp_highlight(enemy['health'])} {hp_highlight('health')} and you have {hp_highlight(player_stats['health'])} {hp_highlight('health')}!")

        while player_stats["health"] > 0 and enemy["health"] > 0:
            enemy["health"] -= player_weapon["damage"]
            typewriter(f"{player_stats['name']} hit the {enemy_highlight(enemy_name)} for {dmg_highlight(player_weapon['damage'])} {dmg_highlight('damage')}.")
                
            if enemy["health"] > 0:
                typewriter(f"{enemy_highlight(enemy_name)} {hp_highlight('health')} is now {hp_highlight(enemy['health'])}.")
            else:
                typewriter(f"{enemy_highlight(enemy_name)} has {hp_highlight('0 health')} it died.")
                typewriter(f"Your {hp_highlight('health')} is {hp_highlight(player_stats['health'])}.")
                enemy["health"] = enemy_hp_reset
                return
            if enemy["health"] > 0:    
                player_stats["health"] -= enemy["damage"]
                typewriter(f"The {enemy_highlight(enemy_name)} hits you for {dmg_highlight(enemy['damage'])} {dmg_highlight('damage')}.")
                if(player_stats["health"] > 0 ):
                    typewriter(f"Your {hp_highlight('health')} is now {hp_highlight(player_stats['health'])}.")
                else:
                    typewriter(f"Your {hp_highlight('health')} is now {hp_highlight('0.')}")
                    typewriter(f"{hp_highlight('YOU DIED! RESETTING GAME')}")
                    time.sleep(3)
                    game_loop()
                    break
                amount_of_damage_potions = check_inventory_amount("Damage potion")
                if amount_of_damage_potions >= 1:
                    user_input = is_yesno_valid(f"Do you want to use a {pot_highlight('damage potion')}? You have {pot_highlight(amount_of_damage_potions)} {pot_highlight('damage potions')} left! ")
                    if user_input.lower() == "yes":
                        for item in player_inventory:
                            if item["name"] == "Damage potion":
                                item["amount"] -= 1
                        if enemy["health"] <= value_of_damage_potion:
                            enemy["health"] -=  value_of_damage_potion
                            typewriter(f"Your {pot_highlight('damage potion')} hit the {enemy_highlight(enemy_name)} right on! it did {dmg_highlight(value_of_damage_potion)} {dmg_highlight('damage')}!")
                            typewriter(f"{enemy_highlight(enemy_name)} {hp_highlight('health')} is now {hp_highlight('0')}.")
                            typewriter(f"{enemy_highlight(enemy_name)} has {hp_highlight('died')}.")
                            enemy["health"] = enemy_hp_reset
                            typewriter(f"Your {hp_highlight('health')} is {hp_highlight(player_stats['health'])}.")
                            return
                        else:
                            enemy["health"] -=  value_of_damage_potion
                            typewriter(f"Your {pot_highlight('damage potion')} hit the {enemy_highlight(enemy_name)} right on! it did {dmg_highlight(value_of_damage_potion)} {dmg_highlight('damage')}")
                            typewriter(f"{enemy_highlight(enemy_name)} {hp_highlight('health')} is now {hp_highlight(enemy['health'])}.")
                    else:
                        typewriter(f"You decided not to use a {pot_highlight('damage potion')}.")

    else:
        typewriter(f"ERROR Enemy typo of je begint je gevecht met 0 of minder HP")
        
    
    
def damage_pot_combat(enemy:str):
    enemy_name = enemy
    enemy = enemy_stats[enemy]
    player_weapon = player_stats["weapon"]
    enemy_hp_reset = enemy["health"]
    enemy["health"] -= player_weapon["damage"]
    
        
def player_reset():
    player_stats["health"] = 100
    give_player_weapon("Fist")

def enemy_reset(enemy_name, new_health):
    if enemy_name in enemy_stats:
        enemy_stats[enemy_name]['health'] = new_health
    else:
        print(f"Enemy '{enemy_name}' not found.")
        
def set_inventory_amounts_to_zero(inventory):
    for item in inventory:
        item['amount'] = 0  

        
def reset_game():
    player_reset()
    set_inventory_amounts_to_zero(player_inventory)
    enemy_reset("Skeleton", 60)
    enemy_reset("Wife", 500)
    enemy_reset("Zombie", 50)
    enemy_reset("Crystal Golem", 175)
    ingredient_order.clear()
    
def use_healing_potion():
        item = player_inventory[0]
        old_hp = player_stats["health"]
        if item["name"] == "Healing potion":
            if item["amount"] >= 1:
                if player_stats["health"] <= 50: #Healing does 50 this makes sure u dont heal over 100 health
                    item["amount"] -= 1
                    player_stats["health"] += item["value"]
                    typewriter(f"You healed from {hp_highlight(old_hp)} to {hp_highlight(player_stats['health'])} health, and you have {item['amount']} healing potions left.")
                elif player_stats["health"] >= 50 and player_stats['health'] < 100:
                    item["amount"] -= 1
                    player_stats["health"] = 100 #If you are over 50 hp you would heal to over 100 hp this makes sure u only heal to 100 
                    typewriter(f"You healed from {hp_highlight(old_hp)} to {hp_highlight(player_stats['health'])} health, and you have {item['amount']} healing potions left.")
                else:
                    typewriter(f"You are already full health! you have {item['amount']} {pot_highlight('healing potion')} left.")
            else:
                typewriter("You don't have any healing potions.")

#'/' commands                
def input_commands(command): 
    if command.lower() == "/heal":
        use_healing_potion()
    elif command.lower() == "/help":
        show_help()
    elif command.lower() == "/inventory":
        print_inventory()
    elif command.lower() == "/logbook":
        print_logbook()
    elif command.lower() == "/quit":
        quit_game()
    else:
        typewriter("Invalid command type /help for help.")
        return
    
    
def show_help():
    help_text = """
    Available Commands:

    /heal          - Use a healing potion to restore health.
    
    /inventory     - Display your current inventory items.
    
    /help          - Show this help message with the list of commands.

    /logbook       - Show the description in your logbook

    /quit          - To quit the game :(

    Type a command to execute it. Have fun exploring!
    """
    typewriter(help_text)
    
#inventory things
def print_inventory():
    current_weapon = player_stats["weapon"]
    for weapon in weapons:
        if weapon["name"] == current_weapon:
            current_weapon = weapon
            
    for item in player_inventory:
        if item["amount"] > 0:
            print(f"- {item['name']}, Amount: {item['amount']}")
    print(f"- Melee: {player_stats['weapon']}, Damage: {current_weapon['damage']}")
    print("") 
    
    
    
def check_inventory_amount(item_name:str): #you can use this function to see how many of asked item you have left
    for item in player_inventory:
        if item["name"] == item_name:
            return item["amount"]
    return False
        
def check_inventory_value(item_name:str): #you can use this function to see the value of an item
    for item in player_inventory:
        if item["name"] == item_name:
            return item["value"]
    return False
        
def add_inventory_value(item_name:str, item_amount:int):#you can use this function to add an item to a player eg add_inventory_value("Healing potion", 3) adds 3 healing potions
    for item in player_inventory:
        if item["name"] == item_name:
            item["amount"] += item_amount


def add_item_to_inventory(name: str, amount: int, value: int): #Name is the name of the item Amount is how many of the item you get, and value is the value the item does for damage or other things (Value could be 0 for keys or other items without damage)
    player_inventory.append({"name": name, "amount": amount, "value": value})


def print_logbook():
    print(player_logbook['Logbook']['description'])
    print("")


def add_desc_to_logbook(description:str):
    player_logbook["Logbook"]['description'] = str(description)


def quit_game():
    typewriter("Game shutting down...")
    time.sleep(1)
    exit()
    

import time, random, os
from main import *
from config import *


def main_menu()->str:
    print('''
====================================================================================='
                        Welcome to The Alchemist's Quest!
                            made by Devin & Lucio
====================================================================================='
In a world overrun by plague and creatures of darkness, your wife lies gravely ill. 
As a skilled alchemist, you alone have the knowledge to craft a cure,
but the rare ingredients you need are scattered across a dying, perilous land.
Armed with potions and desperation, you must venture beyond the safety of your lab
into forgotten ruins, haunted forests, and crumbling villages.
Time is running out. Will you find the cure before it's too late?
Or will the horrors of this shattered world consume you?
====================================================================================='
    Enter '1' to start the game.
    Enter '2' to quit.
=====================================================================================''')


def level_one():
    print('''    Making Choices:
    Throughout the game, you'll face decisions and challenges where you must choose an option:
    
    Numbered choices: Some situations will ask you to choose between options. Simply type the number of your choice (eg., 1, 2 or 3).
    
    Yes or No: Other situations will ask you to do something and you can answer using "Yes" or "No".
          
    Available Commands:
    Type these commands during the game to perform specific actions.
    /heal          - Use a healing potion to restore health.
    
    /inventory     - Display your current inventory items.
    
    /help          - Show this help message with the list of commands.

    /logbook       - Show the description in your logbook

    /quit          - To quit the game :(

    Type a command to execute it. Have fun exploring!
          ''')
    start_game = is_number_valid("Enter '1' to continue.", 1)
    if start_game == '1':
        time.sleep(1)
        typewriter('''
As you step out of your lab, the air is thick with decay, and the once-familiar village now feels like a stranger.
The sky, a bleak gray, hangs over crumbling houses and the echo of distant groans.
With your satchel of alchemical supplies strapped tight, you head towards the town square, knowing the first ingredient is found somewhere within the village.
But you don't make it far before a chilling sound stops you in your tracks.
A shambling figure emerges from behind a broken cart—its skin gray, eyes lifeless. It stumbles toward you, hunger in its eyes.

You've read about these creatures, but now you face one, alone.
Your hands shake as you ready your weapon. It's time to fight. Will your alchemy save you?''')
        time.sleep(3)
        print()
        combat('Zombie')
        print()
        typewriter(f'''With the {enemy_highlight('zombie')} defeated, a grim realization settles in—there are more dangers ahead,
to prepare, you grab {pot_highlight('3 Damage potions')} from your pouch and attach them to your belt for easy access.
With your wife's illness in your mind, you push forward.''')
        print()
        add_inventory_value("Damage potion", 3)
        inv_add_print("3 damage potions", "Purple")
        time.sleep(1)

    
def level_two():
    print()
    time.sleep(1)
    typewriter('''As you look around, two buildings catch your eye.
1. The Bakery, Its door hangs loosely on the hinges, and the smell of stale flour still lingers in the air.
   Could there be ingredients or other supplies left behind?
2. The Smithy, could there be some useful equipment or weaponry left behind?''')
    print()
    level_choice = is_number_valid("Which building do you enter?  ", 2)
    if level_choice == '1':
        bakery()
    if level_choice == '2':
        smithy()


def bakery():#a key and potential encounter
    typewriter(f'''Inside the bakery, shelves are bare, and dust covers everything.
Searching deeper, you find a {item_highlight('rusted key')} hidden under a pile of old sacks.
In the storage room there isn't much of anything. However a large wooden crate sits in the corner, untouched.''')
    print()
    add_item_to_inventory("Rusted Key", 1, 0)
    inv_add_print("Rusted key", "Yellow")
    print()
    answer = is_yesno_valid("Do you open the crate? ")
    if answer == 'Yes':
        typewriter('''As you pry open the crate, the wood creaks loudly. 
Suddenly, with a burst of dust and decay, the lid flies open and a bony hand shoots out!
A skeleton, long entombed, rises from the crate, its empty eye sockets glowing with malevolent energy.''')
        combat('Skeleton')
        typewriter(f'''
With a final strike, the {enemy_highlight('skeleton')} collapses into dust. 
You grab the {item_highlight('rusted key')} and quickly exit the bakery, feeling the weight of danger still lurking in the village.
''')
    elif answer == 'No':
        typewriter(f"There isn't really anything else of use, you leave the bakery with the {item_highlight('rusted key')}.")


def smithy():#a new weapon and an encounter
    typewriter(f'''The smithy is eerily quiet, filled with the scent of rust and decay. Broken tools scatter the floor, and the once roaring forge now stands cold. 
Among the debris, a glint catches your eye—a {item_highlight('Dagger')} clutched by a skeletal hand, still lying near the anvil.''')
    answer = is_yesno_valid("Do you pick up the dagger from the skeleton? ")
    if answer == 'Yes':
        give_player_weapon("Dagger")
        print()
        inv_add_print("Dagger", "Yellow")
        print()
        typewriter("As you pick up the weapon, the body starts moving...")
        time.sleep(1)
        typewriter("The skeleton starts attacking!\n")
        combat("Skeleton")
        typewriter("After fending off the skeleton, you head back outside")
        print(end='')
    if answer == 'No':
        typewriter('After looking around some more, you find nothing of note and head back outside')



def level_three():#you find, ingredient 1
    typewriter('''
You recall the old apothecary near the village well and walk to the ruined building. 
The path is eerie, lined with crumbling homes and empty streets. 
You arrive at the overgrown building, its door creaking open to reveal dusty shelves of herbs and remedies. 
There must be some ingredients you can use inside.''')
    print()
    time.sleep(1)
    typewriter('''As you enter the old ruined apothecary you have a look around. 
Two plants catch your eye, but which one do you need?
You decide to search for clues.''')
    print('''
Where do you want to look?
1. The closet
2. The chest
3. The drawers
''')
    room_check = True
    while room_check:
        room_choice = is_number_valid("Enter your choice: ", 3)
        if room_choice == '1':#closet
            typewriter('You open the creaky closet door to find dusty old cloaks and broken bottles, but nothing of use.')
        if room_choice == '2':#chest
            typewriter('The chest opens with a groan, revealing only crumbling parchment and useless trinkets long forgotten')
        if room_choice == '3':#drawers
            room_check = False
            typewriter("You pull the drawers open, one after another, each filled with dust and debris until... something catches your eye,\nyour fingers brush against a worn notebook, its pages yellowed with age,\nrevealing the secrets of healing and the dangers lurking within the herbs.\n")
            add_desc_to_logbook('''The plant with soft, vibrant leaves emits a faint glow when touched,
hinting at its life-giving properties.

The one with twisted stems and brittle leaves, though alluring,
is often used in poisons and dark rituals, dangerous to the unskilled.''')
    typewriter('''You return to the room where you first spotted the plants.

1. The first plant stands tall with thick, waxy leaves and green petals. It has a strong, earthy scent.

2. The second plant sprawls low, its thin, brittle stems bearing dark purple flowers. The air around it feels strangely cool.

With the apothecary's logbook in hand, you weigh your choices carefully.\n(Type /logbook to read)''')
    flower_choice = is_number_valid("Enter your choice: ", 2)
    if flower_choice == '1':
        add_item_to_inventory("Sylvan Heartflower", 1, 1)
        typewriter("You have picked up the first plant and stashed it away.\n")
        inv_add_print("Sylvan Heartflower", "Yellow")
        print()
    if flower_choice == '2':
        add_item_to_inventory("Shadowbane Blossom", 1, 0)
        typewriter("You have picked up the second plant and stashed it away.\n")
        inv_add_print("Shadowbane Blossom", "Yellow")
        print()


def level_four():#town hall, resting point, chest for the key, find shortsword
    typewriter('''After finding your first ingredient, you leave the apothecary and travel onwards to the Town Hall.\nOnce inside you sense a moment of calm, peace and quiet. The walls are standing steady and the windows are still barged.\nThe only way in or out is through the entrance.''')
  
    townh_choice = is_yesno_valid('Do you take this moment to rest up? ')

    if townh_choice == 'Yes':
        print('You decide to take a moment to rest up.\n')
        player_stats["health"] += 35
        time.sleep(1)
        game_print(f"You have restored {hp_highlight_bold('35 health')}. (If you want to heal using a {pot_highlight_bold('healing potion')}, use /heal)")
        print("\nAfter resting for a moment, you look around and,", end='')
        if player_stats["health"] >= 100:
            player_stats["health"] = 100

    if townh_choice == 'No':
        print('You decide not to rest and look around.\n')
        time.sleep(1)
        print(f"While looking around, you find a {pot_highlight('healing potion')} hidden behind a shelf!\n")
        add_inventory_value("Healing potion", 1)
        inv_add_print("Healing potion", "Purple")
        print()
        time.sleep(1)
        print("Whilst exploring further,", end='')
    typewriter(" in the corner, you notice an unopened chest and approach it.")
    chest_choice = is_yesno_valid('Do you try opening the chest? ')
    
    if chest_choice == 'No':
        print("You do not try opening the chest.\n ")
        print("You take a step back, only for the ground beneath you to emit an ominous creak")
    if chest_choice == 'Yes':
        typewriter("You try to lift the lid, but it remains firmly locked.\nThe faint glint of a keyhole suggests there's a way to open it—if only you had the right key.")
        if check_inventory_amount("Rusted Key"):
            key_confirm = is_yesno_valid("You have a key, do you want try opening the chest with it? ")
            time.sleep(1)
        
            if key_confirm == 'Yes':
                print(f"You succesfully open the chest and find a {item_highlight('Shortsword')} inside!\n")
                give_player_weapon("Shortsword")
                inv_add_print("Shortsword", "Yellow")
                typewriter("\nYou secure the weapon from the chest and take a moment to catch your breath.\nBut as you step back, the ground beneath you begins to creak ominously.\n")
            else:
                print("You decide not to open the chest after all.\n")
                typewriter("You take a step back, only for the ground beneath you to emit an ominous creak.\n")
        else:
            typewriter("But as you step back, the ground beneath you begins to creak ominously.\n")

def level_five():
    #enter dungeon, check surroundings, find more healing potions or upgrade dmg with new gloves, merge at golem, either fight or stealth it. 
    print("Without warning, the floor collapses under your feet.\nWith a gasp, you fall into the darkness below, landing with a hard thud in a cold, damp chamber.\nYou're in a dungeon... and there's no going back.")
    typewriter('''
You dust yourselff off and find yourself at a crossroads,
two hallways stand right before you.
1. The left passageway seems slightly more open, its walls marked with faint scratches and worn stone.             
2. The right passageway is narrower, with jagged stones lining the floor and an eerie silence hanging in the air.
''')
    hallway_choice = is_number_valid('Which hallway do you enter? ', 2)
    if hallway_choice == '1':
        typewriter("The corridor twists and turns, leading you to a small alcove.\nThere, tucked behind an old tapestry, you find a vial shimmering faintly,\nyou recognise this as another healing potion.\n")
        add_inventory_value("Healing potion", 1)
        inv_add_print("Healing potion", "Purple")
        print(f"\nAfter picking up the {pot_highlight('Healing Potion')} you continue down the hallway.")

    if hallway_choice == '2':
        typewriter("As you move down this darker passage, the sound of your footsteps echoes ominously. Eventually, you stumble upon an old display case.\nInside, you see a pair of leather gloves, worn but sturdy, faintly glowing with a magical aura that hints at their enhanced abilities.")
        glove_pickup = is_yesno_valid("Do you pick up the gloves? ")
        if glove_pickup == 'Yes':
            print(f"You pick up the {item_highlight('Enchanted Gloves')}, as you put them on you feel yourself getting stronger.\n")
            add_item_to_inventory("Enchanted Gloves", 1, 0)
            inv_add_print("Enchanted Gloves", "Yellow")
            upgrade_weapon(5)
        if glove_pickup == 'No':
            print("You leave the gloves on the ground and continue down the hallway.")
    typewriter("The hallways merge into a vast open chamber, the air thick with ancient dust. In the center stands a massive golem,\nits body shimmering with the same crystalline glow as the shard you seek.\nThis... thing guards your next ingredient.\n")
    time.sleep(1)
    typewriter('''As you approach the chamber, you notice that the creature has not spotted you yet. 
1. You can either attempt to quietly slip past it and seize the shard from behind or,
2. Prepare for a direct confrontation with this formidable guardian. 
The choice is yours.''')
    golem_choice = is_number_valid("Enter your choice here: ", 2)
    if golem_choice == '1': #stealth
        sneak = stealth(3)
        if sneak:
            typewriter('''You move slowly, each step carefully placed to avoid making noise. 
With your heart pounding in your chest, you get closer, the Glimmering Shard within reach. 

Holding your breath, you make your move, swiftly grabbing the shard from its back. 
The golem freezes for a moment, then crumbles into lifeless stone as the crystal leaves its body.''')
            print(f"You succesfully grab the {item_highlight('Glimmering Shard')}!")
            add_item_to_inventory('Glimmering Shard', 1, 1)
            inv_add_print("Glimmering Shard", 'Yellow')
        elif not sneak:
            print(f"You succesfully grab the {item_highlight('Glimmering Shard')}!")
            add_item_to_inventory("Glimmering Shard", 1, 1)
            inv_add_print("Glimmering Shard", 'Yellow')
    if golem_choice == '2': #combat
        print(f"You decide to fight the {enemy_highlight('Crystal Golem')} head on.")
        combat("Crystal Golem")
        print(f"You succesfully grab the {item_highlight('Glimmering Shard')}!")
        add_item_to_inventory("Glimmering Shard", 1, 1)
        inv_add_print("Glimmering Shard", 'Yellow')
    typewriter("As you leave the dungeon, a chill fills the air, and you step into the shadowy forest,\nthe thick canopy above blocking out most of the light, leaving you to navigate through the gloom.")


def level_six():#walk through forest, find zombie, run or fight, end up at herbalists hut, find 3rd ingredient, start the travel back to lab
    typewriter(f'''As you press on with the second ingredient in hand, determination drives you forward; the thought of curing your wife fuels your urgency.
But in your haste, you fail to notice a shuffling figure emerging from the shadows.

A {enemy_highlight('zombie')} lurches toward you, its hollow eyes fixed on your movement, a low growl escaping its rotting lips. 
The creature's presence sends a jolt of fear through you, reminding you that danger lurks even in your moment of hope.
''')
    print('1. Do you fight the zombie? or\n2. Do you run away?')
    fight_or_flight = is_number_valid("Enter your choice here: ", 2)
    if fight_or_flight == '1':#combat
        print(f'You decide to face the {enemy_highlight("zombie")} head on.')
        combat('Zombie')
    if fight_or_flight == '2':#run away
        print(f'You decide to run away from the {enemy_highlight("zombie")}.')
    typewriter("You make your way to the herbalist's hut, the path winding through the dense underbrush.\nThe air grows thick with the scent of damp earth and moss, and the atmosphere feels charged with anticipation.")
    #npc interaction
    print("You enter the hut, and the herbalist greets you with a knowing smile.")
    typewriter(f"Ah, an alchemist! I have the ingredient you seek, but first, you must prove your wisdom by solving my riddle.\nAnswer it correctly, and the {item_highlight('Mysterious Essence')} will be yours.")
    time.sleep(1)
    typewriter(f"What can you make with leaves and a bit of heat, that can lift your spirits and make your day sweet?")
    print('1. A potion\n2. A tea.\n3. A soup.\n')
    while True:
        riddle_choice = is_number_valid("Enter your choice here: ", 3)
        if riddle_choice == '1':
            typewriter(f"The herbalist shakes their head, saying, 'Wrong answer {player_stats['name']}. Give it another try.'")
        if riddle_choice == '3':
            typewriter(f"The herbalist shakes their head, saying, 'Wrong answer {player_stats['name']}. Give it another try.'")
        if riddle_choice == '2':
            typewriter(f"The herbalist smiles and says, 'Correct! You have proven your wisdom. Here is the {item_highlight('Mysterious Essence')} you seek.'")
            add_item_to_inventory("Mysterious Essence", 1, 1)
            print()
            inv_add_print("Mysterious Essence", 'Yellow')
            break
    typewriter(f"\nWith the {item_highlight('Mysterious Essence')} in hand, you thank the herbalist and step out of the hut.\nYou make your way back through the forest, determination guiding your steps as you return to the lab to create the cure.")


def level_seven():#return to lab, try to make cure, if failed; wife == boss, if success; you win game
    typewriter("You return to the lab, feeling the weight of the ingredients in your bag. As you set them on the workbench, your eyes fall upon a note left behind:\n")
    print('''
In the dance of life, let nature weave,
Start with whispers of green that believe.
Next, the heart of stone, a glimmering glow,
To anchor your hopes where the shadows grow.
Last comes the mystery, hidden from light,
Combine them with care, or face endless night.
''')
    #sylvan heartflower -> glimmering shard -> mysterious essence
    typewriter("You start brewing the potion, but you must decide the order in which to enter the ingredients.")
    print(f'1. {item_highlight("Sylvan Heartflower")}.\n2. {item_highlight("Glimmering Shard")}.\n3. {item_highlight("Mysterious Essence")}.')
    choices = 0
    while choices < 3:
      ingredient_choice = is_number_valid("Enter your choice here: ", 3)
      if ingredient_choice == '1':
          print("You gently place the Sylvan Heartflower into the cauldron, watching as its vibrant essence swirls and mixes with the base.")
          choices += 1
          ingredient_order.append("Sylvan Heartflower")
      if ingredient_choice == '2':
          choices += 1
          print("You carefully add the Glimmering Shard, its radiant light illuminating the mixture, casting shimmering reflections around the room.")
          ingredient_order.append("Glimmering Shard")
      if ingredient_choice == '3':
          choices += 1
          print("Finally, you pour in the Mysterious Essence, the liquid swirling ominously before it begins to stabilize into a vibrant concoction.")
          ingredient_order.append("Mysterious Essence")

    if ingredient_order[0] == "Sylvan Heartflower" and ingredient_order[1] == "Glimmering Shard" and ingredient_order[2] == "Mysterious Essence":
        typewriter('''As the final ingredient melds perfectly into the cauldron, a radiant light fills the room, illuminating every corner with a warm glow. 
You carefully pour the shimmering potion into a vial, your heart racing with hope. 
With trembling hands, you rush back to your wife, the cure in hand. As you administer the potion, a soft glow envelops her, and slowly, her color returns.
Her eyes flutter open, and a smile breaks across her face, the darkness of illness lifting.
You have done it! The cure is successful, and your wife is saved! In this moment, all your trials and tribulations fade away, replaced by joy and relief.
Congratulations, you have completed your quest!''')
        time.sleep(5)

    else:
        typewriter('''As you complete the brewing process, an unsettling silence fills the room. 
You pour the potion into a delicate vial and hand it to your wife, your heart racing with hope. 
But as she drinks, her eyes widen in horror, and a low growl escapes her lips. 
The transformation is swift and brutal; your beloved is no longer the woman you cherished. 
She has become a mindless zombie, the cure instead sealing her fate. 
With tears streaming down your face, you realize you must make the hardest decision of all. 
You draw your weapon, knowing it's the only way to free her from her torment.''')
        time.sleep(3)
        combat("Wife")


def game_loop():

    while True:
        reset_game()
        main_menu()
        menu_choice = is_number_valid("Enter your choice here: ", 2)
        if menu_choice == '2':
            typewriter("Game shutting down...")
            break
        elif menu_choice == '1':
            typewriter('The game begins...')
            time.sleep(1)
            #typewriter('Loading......')
            #time.sleep(3)
            name = is_name_valid("Enter your name: ")
            typewriter(f"Welcome {name}.")
            time.sleep(1)
            typewriter
            level_one()
            time.sleep(1)
            level_two()
            time.sleep(1)
            level_three()
            time.sleep(1)
            level_four()
            time.sleep(1)
            level_five()
            time.sleep(1)
            level_six()
            time.sleep(1)
            level_seven()
            

game_loop()