#Kiera McMurtrie
#Computer Programming
#10/20/2017
#Completely different than before

PLANET = "Earth"
GOTO = ""
CODE = ""
NAME = ""

def intro():
    global NAME
    print("""In this game, you have to go to
as many planets as possible""")
    NAME = str(input("Your Name: "))


def menu():
    global PLANET
    global NAME
    PLANET = "Earth"
    print("|---------------|  |----------------------|  |---------|")
    print("| 1. START GAME |  | 2. Enter Planet Code |  | 3. Quit |")
    print("|---------------|  |----------------------|  |---------|")
    menu = int(input(""))
    if menu == 1: #Start the game
        intro()
        p = str(PLANET)
        print("Hello, " +NAME+ " you are on " +PLANET)
    elif menu == 2: #Planet codes
        PLANET = int(input("Code: "))
        code()
    elif menu == 3:
        quit()
    else:
        print("Invalid Menu Choice")


def speed():
    global NAME
    s = input("How fast are you going?")

def weight():
    global NAME
    w = input("What is the weight of your ship, " +NAME+"?")
    speed()

def escape():
    global NAME
    global PLANET
    global GOTO
    GOTO = input("Where do you want to go, " +NAME+"?")
    weight()

        
menu()
escape()
        
        
    
