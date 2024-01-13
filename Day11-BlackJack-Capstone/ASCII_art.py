import re
logo = r'''
     _____
    |A .  | _____
    | /.\ ||A ^  |
    |(_._)|| / \ |
    |  |  || \ / |
    |____V||  .  |
           |____V|

 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                         
'''
# Cards skeleton
template = [
"┌─────────┐", 
"│{}       │",
"│         │",
"│    {}   │",
"│         │",
"│       {}│",
"└─────────┘"
]
# Cards logo
symbols = {
    'S':'♠',
    'D':'♦',
    'H':'♥',
    'C':'♣'
}

# Build ascii for a given set of card
def displayCards(cards):
    # Resulting string
    res = ""
    # Make a list if only one card
    if type(cards) != list:
        cards = [cards]
    
    # The number of cards in hand
    num_cards = len(cards)

    # Go through template lines and format with logo and num
    # Keep track of line number to know where to format
    for it, line in enumerate(template):
        if it == 1: # First logo
            for card in cards:
                logo = symbols[re.findall(r'\D', card)[0]]
                res += line.format(format(logo, ' <2'))
            res += "\n"
        elif it == 3: # Num of card
            for card in cards:
                num = re.findall(r'\d+', card)[0]
                res += line.format(format(num, ' <2'))
            res += "\n"
        elif it == 5: # Second logo
            for card in cards:
                logo = symbols[re.findall(r'\D', card)[0]]
                res += line.format(format(logo, ' <2'))
            res += "\n"
        else: # If no formating is necessary
            res += line * num_cards + "\n"
    
    return res
