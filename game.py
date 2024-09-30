from functions import *

def gameloop():
    print(main_menu())
    test = input()
    is_choice_valid(test,4)
    print("correct")


gameloop()