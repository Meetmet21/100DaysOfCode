import pandas as pd
from sys import exit

# Read dataframe
df = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

# Df to dict
natoo = {record.letter:record.code for index, record in df.iterrows()}

# User defined word
try:
	word = str(input("Select a word to translate to NATOO code: "))
except:
	print("The given value should be a string containing one word.")
	exit()

# Map letters to NATOO code
code = []
for letter in word:
	code.append(natoo.get(letter.upper()))

print(code)

