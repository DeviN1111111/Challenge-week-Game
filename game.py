from functions import *
from levels import *


def gameloop():
    while True:
        main_menu()
        menu_choice = valid_input("Enter your choice here: ", 2)
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
            typewriter('''
placeholder intro text''')#hier moet nog n kleine intro komen die verdiept op de intro text van de main menu en de commands uit legt
            level_one()
            time.sleep(1)
            level_two()
            level_three()
            level_four()
            
            
    
    
            
        

gameloop()