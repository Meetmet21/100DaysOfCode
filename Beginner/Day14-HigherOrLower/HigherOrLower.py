### Description
# In this project, I implemented a higher/lower game.
# The idea is simple, The player is awared about two personalities name or group,
# then, he has to make a choice, which celebrty/group has followers
# on Instgram? The count of guessed answers is tracked.

### Modules
import random # get random choice
import art # logo and vs text
import data # Celebrities data
import copy # copy list
import os # for system cli

### Variables
# Guess score
score = 0
# Game state
start = True
# Personality A
A = {}
# Personality B
B = {}
# Index of already selected celebrities
selected = []

### Functions
# Select random int to index in personalities data
# Select random personalities to compare
# Return 1 selected and keep track of already selected
def getPersonality():
    # Find not already selected index
    while True:
        index = random.randint(0, len(data.data) - 1)
        if index not in selected:
            break
    # Add to selected
    selected.append(index)
    # Return data to corresponding celebrity
    return data.data[index]

# Standard personality text
# Order of parameters important for good format
def presentPersonality(dictA, dictB):
    print(F"Compare A: {dictA['name']}, a {dictA['description']}, from {dictA['country']}.")
    print(art.vs)
    print(F"Against B: {dictB['name']}, a {dictB['description']}, from {dictB['country']}.")

# Check if answer right or not
def checkAnswer(answer):
    if A["follower_count"] > B["follower_count"] and answer == "A":
        return True
    elif B["follower_count"] > A["follower_count"] and answer == "B":
        return True
    else:
        return False

# Clear the screen of terminal
def clearScreen():
    os.system("cls" if os.name == "nr" else "clear")
### Main program
while start:
    # Display logo
    print(art.logo)
    # Display score if not 0
    if score > 0:
        print(f"You're right! Current score: {score}.")
        # Keep right answer celebrity, generate another one remaining slot
        if answer == 'A':
            B = getPersonality()
        else:
            A = copy.deepcopy(B)
            B = getPersonality()
    else:
        # Select random celebrities: data type is dict
        # Keys: "name", "follower_count", "description", "country"
        A = getPersonality()
        B = getPersonality()

    # Presnt to player the draws
    presentPersonality(A,B)
    # Ask which has more follower
    answer = input("Who has more folloers? Type 'A' or 'B': ").upper()
    # Check if good answer¨
    if answer not in ['A','B']:
        answer = input("Wrong input, last chance! Who has more folloers? Type 'A' or 'B': ").upper()
        if answer not in ['A','B']:
            start = False

    # Check if answer right
    if not checkAnswer(answer):
        clearScreen()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        break
    # Check if all list done
    if score == len(data.data):
        clearScreen()
        print(art.logo)
        print("You have answered right to all the questions, good job!")
        break

    # Right answer
    score += 1
    clearScreen()
