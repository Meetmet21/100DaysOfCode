# DESCRIPTION
# Use the NATO alphabet to spell words.

# MODULES
import pandas as pd

# VARIABLES
# Extract from csv data to pandas df
alphabet = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

# MAIN PROGRAM
# From df to dictionary
dict_alphabet = {value.letter: value.code for index, value in alphabet.iterrows()}
# Ask user for a name or a word
text = input("Give a name or a word to transform to NATO alphabet: ").upper()
# Transform text to NATO alphabet
nato = [dict_alphabet.get(letter) for letter in text]
# Return nato code
print(nato)