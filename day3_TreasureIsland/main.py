print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

def cross_road():
    print("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\".")
    choice = input("> ").lower()
    return choice == "left"

def lake():
    print("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. "
          "Type \"swim\" to swim across.")
    choice = input("> ").lower()
    return choice == "wait"

def house():
    print("You arrive at the island unharmed. There is a house with 3 doors. "
          "One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?")
    choice = input("> ").lower()
    if choice == "red":
        print("It's a room full of fire.")
        return False
    elif choice == "blue":
        print("You enter a room of beasts.")
        return False
    elif choice == "yellow":
        print("You found the treasure!")
        return True
    else:
        print("You chose a door that doesn't exist.")
        return False

# Start the game
if cross_road():
    if lake():
        if house():
            print("You win!")
        else:
            print("Game over.")
    else:
        print("You get attacked by an angry trout.")
        print("Game over.")
else:
    print("You fell into a hole.")
    print("Game over.")
