# A treasure adventure waits you in this project. You have to make the good choices to reach
# your big treasure on a hostile island!

# Print a treasure ASCII art
print('''
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

# Great the hero
print("Welcome to Treasure Island.")

# First question 
answer = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')
# Wrong answer 
if answer.lower() != "left":
    print("You fell into a hole. Game Over.")
    exit(0)

# Right anser -> question 2
answer = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
# Wrong answer
if answer.lower() != "wait":
    print("You get attacked by an angry trout. Game Over.")
    exit(0)

# Right answer -> question 3
answer = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
if answer.lower() == "red":
    print("It's a room full of fire. Game Over.")
    exit(0)
elif answer.lower() == "blue":
    print("You enter a room of beasts. Game Over.")
    exit(0)
elif answer.lower() == "yellow":
    print("You found the treasure! You Win!")
else:
    print("You chose a door that doesn't exist. Game Over.")
