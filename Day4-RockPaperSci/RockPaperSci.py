import random 

#Graphical content for the game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Graphics in list to print given the choice of player
# Ordered list so player choice corresponds to the drawing index
graphics = [rock, paper, scissors]


# Display Rock, Paper and Scissors choice
# Attribute a number to each choice to facilitate implamantion
# Change str to int
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

# Check for wrong inputs
if player >= 3 or player < 0:
    print("You have an invalid value choice!\n---")
    exit(1)

# Print drawing of choice
print(graphics[player])

# Computer random choice
computer = random.randint(0,2)

# Print drawing of compute choice
print(f"Computer choice:\n{graphics[computer]}")

# Check win condition based on the numbers attributed to each choice
# Cheeck for draw
if computer == player:
    print("This is a draw!\n---")
# Rock beats Scissors
elif player == 0 and computer == 2:
    print("You win!\n---")
# Paper beats Rock
elif player == 1 and computer == 0:
    print("You win!\n---")
# Scissors beats Paper
elif player == 2 and computer == 1:
    print("You win!\n---")
# Loosing condition
else:
    print("You lost!\n---")