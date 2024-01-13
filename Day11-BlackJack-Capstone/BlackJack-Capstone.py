### Description
# In this project, I implement a 24.7 blackjack game.
# The player draw two cards and plays again the computer.
# THe rules are the following:
#   - Draw two cards and calculate total amount (Q, K and V value is 10, 11 and 12)
#   - Ask if the player wants to pull another card
#   - Compute the new total amount and compare computer and player draws
#   - Winner is most close one to 21.
#   - If there is a tie, they both win. (The bid goes back)
### Modules
import random # random choice, int
import re # retrieve integer value from string
import ASCII_art # logo, template, and displayCards function
import copy # deep copy lists

# Variables
# Contains all type of cards with the associated point
cards = [str(val) + sign for val in range(1,10 + 1) for sign in ["C","S","D","H"]]
# Data for each player
money = 1000
current_cards = None
bid = 0
score = 0
computer = {
    "money": money,
    "bid": bid,
    "cards": current_cards,
    "score": score
}

player = {
    "money": money,
    "bid": bid,
    "cards": current_cards,
    "score": score
}

# FUnctions
# Select a number of cards for a given player
def chooseCards(number, cards_player = None):
    # The chosen subset for player
    chosen = []
    # Randomize the order of cards in game for each pull
    random.shuffle(cards)
    # Copy cards to shuffled otherwise only two pointers pointing
    # to same point in memory so same list
    shuffled_cards = copy.copy(cards)

    # IF second pull from total cards, remove already pulled cards
    if cards_player != None:
        for pulled in cards_player:
            shuffled_cards.remove(pulled)

    for _ in range(number):
        # Select a random card
        card = random.choice(shuffled_cards)
        # Remove card from possibilites to not pull it again
        shuffled_cards.remove(card)
        # Add to chosen
        chosen.append(card)

    return chosen

# From cards compute score
def scoreCards(cards_player):
    score = 0
    for card in cards_player:
        # Use regular expression to retrieve from string digits
        # re.findall returns a list so choose the item in list 
        # to retrieve a string and change it to integer.
        score += int(re.findall('\d+', card)[0])
    
    return score

# Add/remove bidded moyen from total cash depending on state (win, loose, or tie)
# The state depnding on the player
def bid(player, computer, state):
    # Keep track of current money
    computer_total = computer["money"]
    player_total = player["money"]

    # Loose money player
    if state == "loose":
        player_total -= player["bid"]
        computer_total += player["bid"]
    # Gain money player
    elif state == 'win':
        player_total += computer["bid"]
        computer_total -= computer["bid"]
    
    return player_total, computer_total

### Main program
# Adk start the game
answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n'; ").lower()
# Set state game
if answer == 'y':
    state_game = True
else:
    state_game = False
    print("See you soon!")

while state_game:
    # Display logo
    print(ASCII_art.logo)

    # Pull cards and show
    player["cards"] = chooseCards(2)
    print(f"Your cards are:")
    # Print ascii cards
    print(ASCII_art.displayCards(player["cards"]))

    # Pull computer cards and show first
    # Here add player cards to function because same card game for player and computer
    computer["cards"] = chooseCards(2, player["cards"])
    print(f"Computer's first card is:")
    # Display computer first card in ascii art
    print(ASCII_art.displayCards(computer["cards"][0]))

    # Ask for bids
    player["bid"] = int(input("How munch do you want to bid? (whole number only): $"))
    if player["bid"] > player["money"]:
        print(f"You're bidding more than what you have! Your total cash is ${player['money']}.")
        player["bid"] = int(input("How munch do you want to bid? (whole number only): $"))
    # Computer bid
    computer["bid"] = random.randint(5, computer["money"])
    # Display bid
    print(f"The computer bid is: ${computer['bid']} and your's is: ${player['bid']}")

    # Ask if another card for player
    answer = input("Tyoe 'y' to get another card, type 'n' to pass: ").lower()
    if answer == 'y':
        # add one more card to hand
        player["cards"] += chooseCards(1, player["cards"] + computer["cards"])
    elif answer != ['n','y']:
        print("You didn't answer to the question, so it's accepted as 'n'.")
    
    # Show winner for current party
    # Display both hands
    print(f"Your final hand:")
    print(ASCII_art.displayCards(player["cards"]))
    print(f"Computer's final hand: {computer['cards']}")
    print(ASCII_art.displayCards(computer["cards"]))
    # Compute score and select winner
    computer["score"] = scoreCards(computer["cards"])
    player["score"] = scoreCards(player["cards"])
    # Score above 21 or loose play
    if player["score"] > 21 or player["score"] < computer["score"]:
        print("You lose!")
        player["money"], computer["money"] = bid(player, computer, "loose")
        # Display remaining money
        print(f"You have now ${player['money']} and the computer has ${computer['money']}")
    # TIE
    elif player["score"] == computer["score"]:
        print("It's a tie!")
        print(f"You have now ${player['money']} and the computer has ${computer['money']}.")
    # Win player
    else:
        print("You win!")
        player["money"], computer["money"] = bid(player, computer, "win")
        print(f"You have now ${player['money']} and the computer has ${computer['money']}.")

    # Check if out of money
    if computer["money"] <= 0:
        print("You win the whole game, the computer has no money!")
        break # Stop game
    elif player["money"] <= 0:
        print("You lost, the computer took all your money!")
        break # Stop game

    # Again
    answer = input("Do you want to play again?: 'y' or 'n' ").lower()
    if answer == 'n':
        break
    else:
        # Reset scores
        player["score"] = 0
        computer["score"] = 0

