print('''
*******************************************************************************
     ^  +~+~~
    ^   )`.).
      )``)``) .~~
      ).-'.-')|)
    |-).-).-'_'-/
 ~~~\ `o-o-o'  /~~~~~~~~~~~~~~~~~
  ~~~'---.____/~~~~~~~~~~~~~~~~~
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("Your ship sailed to an unknown land.You get off the ship and have two options to go. Left or Right? \n").lower()
if choice1 == "left":
    choice2 = input("After going left you have reached a lake. You can either wait for a boat to arrive or swim across. What do you choose? \n").lower()
    if choice2 == "wait":
        choice3 = input("After waiting some time a small boat arrives. You swim the river on the boat and have reached a house with three doors. Red, Yellow and Blue. Which one do you choose?\n").lower()
        if choice3 == "red":
            print("You open the red door and a giant fire flame shoots at you - You are dead. Game Over")
        elif choice3 == "yellow":
            print("You open the yellow door and see a room full of treasure. Congratulations - You Won!")
        elif choice3 == "blue":
            print("You open the blue door and the room is full of beasts that attack you and eat you - You are dead. Game Over")
        else:
            print("You have chosen a door that does not exist. Game Over")
    else:
        print("You have chosen to swim across the river but as you get into the water a big school of piranhas attacks you - You are dead. Game Over")
else:
    print("You have chosen to go right and you fall into a hole - You are dead. Game Over")
