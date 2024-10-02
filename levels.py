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
With your satchel of alchemical supplies strapped tight, you head towards the town square, knowing the first ingredient lies somewhere within the village.
But you don't make it far before a chilling sound stops you in your tracks.
A shambling figure emerges from behind a broken cart—its skin gray, eyes lifeless. It stumbles toward you, hunger in its eyes. 
You've read about these creatures, but now you face one, alone.
Your hands shake as you ready your weapon. It's time to fight. Will your alchemy save you?''')
    combat('Zombie')

    
def level_two():
    print()
    typewriter("Since you defeated the zombie I will grant you with 3 health potions! use /heal to use them!")
    add_inventory_value("Damage potion", 3)
    typewriter('''With the zombie defeated, a grim realization settles in—there are more dangers ahead.
But your wife's illness pushes you forward, into the unknown.''')
    print()
    time.sleep(1)
    typewriter('''As you look around, two buildings catch your eye.
1. The Bakery, Its door hangs loosely on the hinges, and the smell of stale flour still lingers in the air.
Could there be food or supplies left behind?
2. The Smithy, there could be some useful equipment of use laying around''')
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
    add_item_to_inventory("Rusted Key", 1, 0)
    print()
    answer = is_yesno_valid("Do you open the crate? ")
    if answer == 'Yes':
        print('placeholder')
        combat('Skeleton')
        level_three()
    elif answer == 'No':
        typewriter('You leave the bakery empty handed')
        level_three()


def smithy():#a new weapon and an encounter
    typewriter("smithy story dead skeleton new dagger etc")
    answer = is_yesno_valid("Do you pick up the dagger from the Skeleton? ")
    if answer == 'Yes':
        give_player_weapon("Dagger")
        typewriter("As you pick up the weapon, the body starts moving... The skeleton starts attacking!")
        combat("Skeleton")


def level_three():
    print('placeholder level three')