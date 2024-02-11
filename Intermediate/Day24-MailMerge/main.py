# DESCRIPTION
# Send formatted mails to friends by using file handler system of python

# MODULES
import re

# VARIABLES
# List containing friends names
friends_names = []
names_file_path = "Mail Merge Project Start/Input/Names/invited_names.txt"
example_lettre_path = "Mail Merge Project Start/Input/Letters/starting_letter.txt"
output_path = "Mail Merge Project Start/Output/ReadyToSend"

# MAIN PROGRAM
# Retrieves all friends names
with open(names_file_path, 'r') as names_file:
    for line in names_file:
        # Remove '\n' at the end
        friends_names.append(line.strip())

# Write formatted letter with corresponding name
for name in friends_names:
    # Open example letter and output letter
    with open(example_lettre_path, 'r') as example, open(f"{output_path}/letter_for_{name},txt", 'w') as output:
        # Read text in example letter
        text = example.read()
        # Substitute the [name] pattern with name via regular expression
        output.write(re.sub(r'\[name\]', name, text))

