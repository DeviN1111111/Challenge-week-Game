from main import *
from levels import *


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