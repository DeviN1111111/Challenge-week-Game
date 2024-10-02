import time
import random
from config import *
from functions import *


def main_menu()->str:
    print('''
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
========================================''')
    reset_game()


def level_one():
    typewriter('''
As you step out of your lab, the air is thick with decay, and the once-familiar village now feels like a stranger.
The sky, a bleak gray, hangs over crumbling houses and the echo of distant groans.
With your satchel of alchemical supplies strapped tight, you head towards the town square, knowing the first ingredient is found somewhere within the village.

But you don't make it far before a chilling sound stops you in your tracks.
A shambling figure emerges from behind a broken cart—its skin gray, eyes lifeless. It stumbles toward you, hunger in its eyes.
 
You've read about these creatures, but now you face one, alone.
Your hands shake as you ready your weapon. It's time to fight. Will your alchemy save you?''')
    print()
    combat('Zombie')
    print()
    typewriter(f'''With the {enemy_highlight('zombie')} defeated, a grim realization settles in—there are more dangers ahead,
to prepare, you grab {pot_highlight('3 Damage potions')} from your pouch and attach them to your belt for easy access.
With your wife's illness in your mind, you push forward.''')
    print()
    add_inventory_value("Damage potion", 3)
    game_print(f"Added {pot_highlight_bold('3 damage potions')} to your inventory")

    
def level_two():
    print()
    time.sleep(1)
    typewriter('''As you look around, two buildings catch your eye.
1. The Bakery, Its door hangs loosely on the hinges, and the smell of stale flour still lingers in the air.
   Could there be ingredients or other supplies left behind?
2. The Smithy, could there be some useful equipment or weaponry left behind?''')
    print()
    level_choice = valid_input("Which way do you go?  ", 2)
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
    game_print(f"Added {item_highlight('Rusted key')}\033[1;37m to your inventory.")
    print()
    answer = is_yesno_valid("Do you open the crate? ")
    if answer == 'Yes':
        print('placeholder')
        combat('Skeleton')
    elif answer == 'No':
        typewriter(f"There isn't really anything else of use, you leave the bakery with the {item_highlight('rusted key')}.")


def smithy():#a new weapon and an encounter
    typewriter("smithy story dead skeleton new dagger etc")
    answer = is_yesno_valid("Do you pick up the dagger from the Skeleton? ")
    if answer == 'Yes':
        give_player_weapon("Dagger")
        game_print(f"Added {item_highlight_bold('Dagger')} to your inventory.")
        typewriter("As you pick up the weapon, the body starts moving... The skeleton starts attacking!")
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
    print('''Where do you want to look?
1. The closet
2. The chest
3. The drawers''')
    room_check = True
    while room_check:
        room_choice = valid_input("Enter your choice: ", 3)
        if room_choice == '1':#closet
            print('You find nothing')
        if room_choice == '2':#chest
            print('You find nothing')
        if room_choice == '3':#drawers
            room_check = False
            typewriter("As you sift through the clutter in the dim light of the apothecary's hut,\nyour fingers brush against a worn notebook, its pages yellowed with age,\nrevealing the secrets of healing and the dangers lurking within the herbs.\n")
            add_desc_to_logbook('''The plant with soft, vibrant leaves emits a faint, warm glow in the sunlight,
hinting at its restorative properties.
In contrast, the one with dark, twisted stems and jagged edges thrives in the shadows;
its appearance is alluring but deceptive, bringing misfortune to the unwary.''')
    typewriter('''You return to the room where you first spotted the plants.
               
1. The first plant stands tall with vibrant green leaves and soft blue petals,\nemanating a sweet aroma that hints at its healing properties.

2. The second plant sprawls low to the ground,\nits twisted gray leaves and dark flowers exuding an unsettling energy.

With the apothecary's logbook in hand, you weigh your choices carefully.\n(Type /logbook to read)''')
    flower_choice = valid_input("Enter your choice: ", 2)
    if flower_choice == '1':
        add_item_to_inventory("Sylvan Heartflower", 1, 1)
        typewriter("You have picked up the first plant and stashed it away.\n")
        game_print(f"Added {item_highlight_bold('Sylvan Heartflower')} to your inventory")
        print()
    if flower_choice == '2':
        add_item_to_inventory("Shadowbane Blossom", 1, 0)
        typewriter("You have picked up the second plant and stashed it away.\n")
        game_print(f"Added {item_highlight_bold('Shadowbane Blossom')} to your inventory")
        print()


def level_four():#town hall, resting point, chest for the key, find shortsword
    typewriter('''After finding your first ingredient, you leave the apothecary and travel onwards to the Town Hall.\nOnce inside you sense a moment of calm, peace and quiet. The walls are standing steady and the windows are still barged.\nThe only way in or out is through the entrance.''')
  
    townh_choice = is_yesno_valid('Do you take this moment to rest up? ')

    if townh_choice == 'Yes':
        print('You decide to take a moment to rest up.\n')
        player_stats["health"] += 25
        time.sleep(1)
        game_print(f"You have restored 25 health. (If you want to heal using a {pot_highlight_bold('healing potion')}, use /heal)")
        print("\nAfter resting for a moment, you look around and", end='')

    if townh_choice == 'No':
        print('You decide not to rest and look around.\n')
        time.sleep(1)
        print(f"While looking around, you find a {pot_highlight('healing potion')} hidden behind a shelf!\n")
        add_item_to_inventory("Healing Potion", 1, 0)
        game_print(f"Added {pot_highlight_bold('Healing potion')} to your inventory.")
        print()
        time.sleep(1)
        print("Whilst exploring further,", end='')
    typewriter(" in the corner, you noticed an unopened chest.")
    chest_choice = is_yesno_valid('Do you try opening the chest? ')
    
    if chest_choice == 'No':
        print("You do not try opening the chest.\n ")
    if chest_choice == 'Yes':
        typewriter("You try to lift the lid, but it remains firmly locked.\nThe faint glint of a keyhole suggests there's a way to open it—if only you had the right key.")
        if check_inventory_amount("Rusted Key"):
            key_confirm = is_yesno_valid("You have a key, do you want try opening the chest with it? ")
            time.sleep(1)
            if key_confirm == 'Yes':
                print(f"You succesfully open the chest and find a {item_highlight('Shortsword')} inside!\n")
                give_player_weapon("Shortsword")
                game_print(f"Added {item_highlight_bold('Shortsword')} to your inventory.")
            else:
                print("You decide not to open the chest after all.\n")
