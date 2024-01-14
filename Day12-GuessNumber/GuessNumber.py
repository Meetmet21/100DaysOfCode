### Description
# In this project, I implement an easy guess my number game.
# There is two mods: easy or hard:
    # Easy = 10 attempts
    # Hard = 5 attempts
# The guess range is fixed between 1 to random number between 100-9999.
# Clues are given to player depending on the guess he did.

### Modules
import random
import art 
import os

### Variables
# depends on mode
attempts = 0
min_range = 1
max_range = random.randint(100,9999)
# Number to find by player
secret_number = random.randint(min_range, max_range)
print(secret_number)
# Game state
start = True
# Guess state
guessed = False

### Functions
# Remove one attempt
def removeAttempt():
    return attempts - 1

# Check if guess over or below
# remove attempts if wrong
def checkGuess(guess):
    # Overestimating
    if guess > secret_number:
        print("Too high")
        # Not guessed
        return False
    # Underestimating
    elif guess < secret_number:
        print("Too low")
        # Not guessed
        return False
    else:
        # Guessed
        return True

# Track for user the remaining attempts
def showAttempt():
    print(f"You have {attempts} remaining to guess the number.")

### Main program
# Display logo
print(art.logo)
# Great the user
print("Welcome to the Number Guessing Game!")

while start:
    # Display the range of possibilities
    print(f"I'm thinking of a number between {min_range} and {max_range}")

    # Choose difficulty
    answer = input("Choose a difficulty: type 'easy' or 'hard': ").lower()
    # Check if answer good
    if answer == 'easy':
        attempts = 10
        showAttempt()
    elif answer == 'hard':
        attempts = 5
        showAttempt()
    else:
        print("You didn't answered to the question! You shall begin in hard mode.")
        attempts = 5
        showAttempt()

    # Continue while not guessed or no more attempts
    while attempts > 0 and not guessed:
        # Check if good input format
        try:
            number_input = int(input("Make a guess (Only whole numbers): "))
        except ValueError:
            print("You didn't give a whole number, you loose one attempt.")
            attempts = removeAttempt()
            showAttempt()
            # Skip to the next iteration
            continue
        # Wrong guess
        if checkGuess(number_input) is False:
            attempts = removeAttempt()
            showAttempt()
        # Good guess
        else:
            guessed = checkGuess(number_input)
            print(f"You got it! The answer was {secret_number}.")

    # Check fi win or loose:
    if guessed == False:
        print(f"You've run out of guesses, you lost. The secret number was {secret_number}")
        # End the game
        start = False
    else:
        answer = input("Do you want to play again? (y) or (n): ").lower()
        if answer == 'n':
            start = False
        elif answer == 'y':
            # Clean the screen
            os.system('cls' if os.name == 'nr' else 'clear')
        else:
            start = False






