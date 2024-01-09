import random # Random choice
import string # Ponctuation, letters, numbers

# Great the user
print("Welcome to the PyPassword Generator!")

# Ask for letters amount
letters_num = int(input("How many letters would you like in your password?\n"))

# Ask for symbols amount
symbols_num = int(input("How many symbols would you like?\n"))

# Ask for numbers amount
numbers_num = int(input("How many numbers would you like?\n"))

# Initial empty password possibilities from random choices
password_options = []

# Select randomly n letters and add to possibilities
for letter in range(letters_num):
    password_options.append(
        random.choice(list(string.ascii_letters))
    )

# Select randomly n symbols and add to possibilities
for symbol in range(symbols_num):
    password_options.append(
        random.choice(list(string.punctuation))
    )

# Select randomly n digits and add to possibilities
for digit in range(numbers_num):
    password_options.append(
        random.choice(list(string.digits))
    )

# Empty password variable to concatante
password = ""

# Build password from possibilities by shuffling list in place
random.shuffle(password_options)

# Change list to string
password = "".join(char for char in password_options)

# Display result to user
print(f"Here is your password: {password}")