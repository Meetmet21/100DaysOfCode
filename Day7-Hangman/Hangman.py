import random # Random choice
import Hangman_art # hangmans ascii art 
import Hangman_word # English words

# Select a random word from a user defined language
def chooseWord():
    # User answer
    language = input("From which language do you want to select the word? (English)/(French)\n").lower()
    # List of words for two languages
    french_words = ["Papillon","Montagne", "Coccinelle","Renaissance","Tempéte",
                    "Girafe","Jardin","Cactus","Soleil","Piano"]
    english_words = Hangman_word.word_list
    # Choose a random word depending on user selection
    if language.lower() == "french":
        return random.choice(french_words).lower()
    elif language.lower() == "english":
        return random.choice(english_words).lower()
    else:
        print("You didn't select any langauge! Try again.")
        exit(0)

# Asks user for a letter in the word unit it's given
def guess():
    while True:
        letter = input("Guess a letter: ").lower()
        # Check if a letter or not
        if letter.isalpha() and len(letter) == 1:
            return letter
        else:
            # Ask again for a letter
            print("This is not one letter!")

# Checks if letter in word
def check(letter, wor, guessed_letters):
    # Not already guessed
    if letter in word and letter not in guessed_letters:
        return True
    else:
        return False

# Draw blanks in word size
def drawBlanks(word):
    # Concatante as many blanks as there is letters in word
    blanks_list = ["_"] * len(word)

    # Display blanks
    blanks_string = " ".join(blanks_list)

    return blanks_list

# Put the letter in blanks
def drawLetter(list_blanks, word, letter):
    # Find all occurence of a letter in string
    # Go through string, letter by letter
    for index in range(len(word)):
        # Check if this string[index] is equal to letter
        if word[index] == letter:
        # Replace blanks by letter
        # Put letter in right index in list
            list_blanks[index] = letter

    #Display result in string
    blanks_string = " ".join(list_blanks)
    print(blanks_string)

    # To further replacements
    return list_blanks   

#### Game ####
# Number of loose
loose = 0 

# Display ASCII art for hangman game
print(Hangman_art.first_screen)

# Great user
print("Hello, so let's play Hangman game! You have 6 try to guess the secret word.\n")

# Generate random word
word = chooseWord()

# Display blanks for first guess
blanks_list = drawBlanks(word)

# Hangman draws
hangman_pics = Hangman_art.hangman_pics

# Max try
max_try = 6

# List of already guessed letters
list_guessed_letters = []

#Game flow
while True:
    # Ask for a letter
    letter = guess()
    # Check if in word
    if check(letter, word, list_guessed_letters):
        # Add letter to guessed list
        list_guessed_letters.append(letter)

        # Draw blanks with letters
        blanks_list = drawLetter(blanks_list, word, letter)        
        # Draw hangman (current state)
        print(hangman_pics[loose])

        # Win condition: all blanks replaced by letters means word found
        if "_" not in blanks_list:
            print("You win!")
            break
    else:
        # Remove 1 life
        loose += 1
        # Display current blanks
        print("".join(blanks_list))
        # Display current state in game
        print(f"You guessed {letter}, that's not in the word. [ - 1 life ]")
        # Display next state hangman: starts from index 1 
        print(hangman_pics[loose])

        # loose conditon: max try set to 6
        if loose == max_try:
            print("You loose! Try again.")
            break