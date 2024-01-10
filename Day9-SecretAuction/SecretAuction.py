# In this project, I implement a hidden auction game
# in which players defines their name and their bid, but
# the other players can't see the bid of one player. At
# the end, the biggest bid is returned with the name of the bidder.

# Module
import os # to clear the screen
import SecretAuction_art # Logo

# Global variable
# dictionnary of bids by player
dict_bids = {}

# Function
# Append a bid to a key in the main bid dictionnary called dict_bids
def addBid(name, bid, dict_bids):
    # Add or replace bid for name (player)
    dict_bids[name] = bid

# Select the highest bid with the player name
def highestBid(dict_bids):
    best_bid = 0
    best_player = ""
    for name,bid in dict_bids.items():
        if bid > best_bid:
            best_bid = bid
            best_player = name
    
    # Return both values
    return best_player, best_bid


### Main program
# Display logo
print(SecretAuction_art.logo)

# Great the user
print("Welcome to the secret auction program.")

while True:
    # Ask for the player name
    name = input("What is your name?: ")
    # Ask for bid amount and int it
    bid = int(input("What's your bid?: $"))
    # Add input to dict
    addBid(name, bid, dict_bids)

    # Other player?
    answer = input("Are they any other bidders? Type 'yes' or 'no'.\n").lower()
    if answer == "no":
        # Display the best bid and player
        best_player, best_bid = highestBid(dict_bids)
        print(f"The winner is {best_player} with a bid of {best_bid}$.")
        break
    elif answer == "yes":
        # Clear the screen
        os.system('cls' if os.name == "nt" else 'clear')
    else:
        print("You don't anser to the question or spell it wrong!")
        break

