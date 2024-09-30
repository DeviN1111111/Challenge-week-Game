from functions import *

def gameloop():
    print(main_menu())
    picked_choice = input()
    is_choice_valid(picked_choice,2)
    input_error(is_choice_valid)


gameloop()