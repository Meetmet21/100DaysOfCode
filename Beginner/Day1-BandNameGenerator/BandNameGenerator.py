#The purpose of this script is to build a band name from user input

# Great the user
print("Welcome to the Band Name Generator.")

# Questions to build band name for stdin
city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

# Generate band name
print("Your band name could be", city, pet, sep=" ", end="\n")