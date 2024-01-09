### Project description
# In this project, I'll implement a encoder based on Ceaser historical 
# encrypt method. It consits on taking for each char of a string the n step further
# char in the alphabet. For example, 'a' with n = 6 becomes 'g'. The user
# has also the possibility to decode the message by giving n.

### Modules
import string # ascii letters
import CeasarCipher_art # logo

### Functions
# Encode or decode a char given its type and the state
def letterEncodeDecode(letter, shift, string_char, state):
    # List ascii string
    list_char = list(string_char)
    # Find letter index 
    index = list_char.index(letter)

    # COmpute the total index with shift
    total_index = (shift + index)
    # Total is longer than len, so look how many times len fits in total
    # Keep the remainw which is the current index after shift
    if total_index > len(list_char):
        # Here, shift is subscribed because I center (begin the list of character) to
        # letter, so it's normalized in a sort of way
        real_index = shift - ((total_index // len(list_char)) * len(list_char))
    # Total lower than len, so new index is shift if list begins with letter
    else:
        real_index = shift

    # To encode
    if state == "encode":
        # Return the encode by centering the list to letter index at beginning
        centered_list = list_char[index:] + list_char[:index]
        return centered_list[real_index]
    # To decode
    else:
        # Center the list but in the other sense as we decode we go back
        reverse_1 = list_char[:index + 1][::-1]
        reverse_2 = list_char[index + 1:][::-1]
        centered_list = reverse_1 + reverse_2
        return centered_list[real_index]

# Encode a string given an integer to shift alphabet
def encodeDecode(message, shift, state):
    # Different list of character
    punctuation = string.punctuation
    alphabet = string.ascii_lowercase
    digits = string.digits

    # Resulting message store
    result = ""
    
    # First cut string by space to encode the different words
    split_message = message.split()

    # Encode each word in splitted message
    # Go through each word in message
    for word in split_message:
        # Go through each letters in word
        for letter in word:
            # Check if special character
            if letter in punctuation:
                #shifted ponctuation
                result += letterEncodeDecode(letter, shift, punctuation, state)
            elif letter in alphabet:
                #shifted alphabet
                result += letterEncodeDecode(letter, shift, alphabet, state)
            else:
                result += letterEncodeDecode(letter, shift, digits, state)     
        # Add the space removed from split method
        result += " "

    # Remove the last space at right position
    return result.rstrip()

### Main application
# Display logo
print(CeasarCipher_art.logo)

while True:
    # Ask for which utility user is here
    state = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Wrong input
    if state not in ['encode', 'decode']:
        print("You should answer by 'encode' or 'decode'!")
        break

    # Ask for the message
    message = input("Type your message:\n").lower()

    # Ask for shift key to encrypt or decrypt
    try:
        shift = int(input("Type the shift number:\n"))
    # Wrong input
    except ValueError:
        print("The shift should be a digit!")
        break

    # Work on message depending on state
    result = encodeDecode(message, shift, state)

    # Display the message depnding on state
    print(f"Here's the {state}d result: {result}")

    # Ask for stop or continue
    answer = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
    if answer == "no":
        break
    elif answer == 'yes':
        continue
    # If wrong input from user
    else:
        print("You should answer by 'yes' or 'non'!")
        break
