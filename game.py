from functions import *
from levels import *

give_player_weapon("Fist")

def gameloop():
    while True:
        print(main_menu())
        menu_choice = valid_input("Enter your choice here: ", 2)
        if menu_choice == '2':
            typewriter("Game shutting down...")
            break
        elif menu_choice == '1':
            typewriter('The game begins...')
            name = is_name_valid("Enter your name: ")
            typewriter(f"Welcome {name}.")
            time.sleep(1)
            typewriter('''
placeholder intro text''')
            level_one()
            time.sleep(1)
            level_two()
            
            
    
    
            
        

gameloop()