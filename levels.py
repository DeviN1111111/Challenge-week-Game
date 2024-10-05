import time, random, os
from main import *
from config import *


def main_menu()->str:
    print('''
====================================================================================='
                            Welcome to placeholder
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
    start_game = is_number_valid("Enter '1' to continue." , 1)
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
        game_print(f"You have restored {hp_highlight_bold("35 health")}. (If you want to heal using a {pot_highlight_bold('healing potion')}, use /heal)")
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
                print("\nYou secure the weapon from the chest and take a moment to catch your breath.\nBut as you step back, the ground beneath you begins to creak ominously.\n")
            else:
                print("You decide not to open the chest after all.\n")
                print("You take a step back, only for the ground beneath you to emit an ominous creak.\n")
        else:
            print("But as you step back, the ground beneath you begins to creak ominously.\n")

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
            print(f"You succesfully grab the {item_highlight("Glimmering Shard")}!")
            add_item_to_inventory("Glimmering Shard", 1, 1)
            inv_add_print("Glimmering Shard", 'Yellow')
        elif not sneak:
            print(f"You succesfully grab the {item_highlight("Glimmering Shard")}!")
            add_item_to_inventory("Glimmering Shard", 1, 1)
            inv_add_print("Glimmering Shard", 'Yellow')
    if golem_choice == '2': #combat
        print(f"You decide to fight the {enemy_highlight("Crystal Golem")} head on.")
        combat("Crystal Golem")
        print(f"You succesfully grab the {item_highlight("Glimmering Shard")}!")
        add_item_to_inventory("Glimmering Shard", 1, 1)
        inv_add_print("Glimmering Shard", 'Yellow')
    print("you find back exit, you enter the forest")


def level_six():#walk through forest, find zombie, run or fight, end up at herbalists hut, find 3rd ingredient, start the travel back to lab
    typewriter("with 2nd ingredient in hand you keep pushing, knowing youre close to making the cure for your wife. in your haste you do not notice a zombie approaching you")
    print('1. Do you fight the zombie? or\n2. Do you run away?')
    fight_or_flight = is_number_valid("Enter your choice here: ", 2)
    if fight_or_flight == '1':#combat
        print('You decide to fight the zombie')
        combat('Zombie')
    if fight_or_flight == '2':#run away
        print('You decide to run away')
    print('you make your way to the herbalists hut')
    #npc interaction
    print("you enter the hut and the herbalist says;")
    typewriter(f"Ah, an alchemist! I have the ingredient you seek, but first, you must prove your wisdom by solving my riddle.\nAnswer it correctly, and the {item_highlight('Mysterious Essence')} will be yours.")
    time.sleep(1)
    typewriter(f"What can you make with leaves and a bit of heat, that can lift your spirits and make your day sweet?")
    print('1. A potion\n2. A tea.\n3. A soup.\n')
    while True:
        riddle_choice = is_number_valid("Enter your choice here: ", 3)
        if riddle_choice == '1':
            print("wrong answer, try again")
        if riddle_choice == '2':
            print("wrong answer, try again")
        if riddle_choice == '3':
            print("correct!")
            add_item_to_inventory("Mysterious Essence", 1, 1)
            inv_add_print("Mysterious Essence", 'Yellow')
            break
    print("yo u leave with the last ingredient congrats")


def level_seven():#return to lab, try to make cure, if failed; wife == boss, if success; you win game
    print('return to the lab')
    print('''your note says the following;
In the dance of life, let nature weave,
Start with whispers of green that believe.
Next, the heart of stone, a glimmering glow,
To anchor your hopes where the shadows grow.
Last comes the mystery, hidden from light,
Combine them with care, or face endless night.''')
    #sylvan heartflower -> glimmering shard -> mysterious essence
    print('you start brewing, but in what order to you enter the ingredients')
    print(f'1. {item_highlight('Sylvan Heartflower')}.\n2. {item_highlight("Glimmering Shard")}.\n3. {item_highlight("Mysterious Essence")}.')
    choices = 0
    while choices < 3:
      ingredient_choice = is_number_valid("Enter your choice here: ", 3)
      if ingredient_choice == '1':
          print("you enter the flower")
          choices += 1
          ingredient_order.append("Sylvan Heartflower")
      if ingredient_choice == '2':
          choices += 1
          print("you enter the shard")
          ingredient_order.append("Glimmering Shard")
      if ingredient_choice == '3':
          choices += 1
          print("you enter the essence")
          ingredient_order.append("Mysterious Essence")
    print(ingredient_order)

    if ingredient_order[0] == "Sylvan Heartflower" and ingredient_order[1] == "Glimmering Shard" and ingredient_order[2] == "Mysterious Essence":
        print('you win!!!!')
    else:
        print('your potion failed')#DOESNT WORK
    print(ingredient_order)

    