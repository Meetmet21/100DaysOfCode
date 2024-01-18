### Definition
# In this project, I implemented a simple coffe machine.
# The coffe machine has resources and can not produce coffe if any ressource is mssing.
# Ther are three type of hot drink and the machine only accepts cash money (Swiss Francs: CHF)
# There some hiden keys that allows to contact with the machine when we are administrator.

### Modules
from art import LOGO, COFFE
from data import resources, MENU
from copy import deepcopy
import time

### Variables
# Money earned by the machine
profits = 0
# State of machine
On = True
# Copy of resources
machine_resources = deepcopy(resources)

### Functions
# Check if enough resources for command
def check_resources(type_coffe):
    # Check if enough milk, coffe, water
    for type, value in MENU[type_coffe]["ingredients"].items():
        if machine_resources[type] < value:
            return False
    # Enough resources    
    return True

# Remove recipe ingredientns values from resource
def update_resource(type_coffe):
    # Deduce recipe ingredients for hot drink from resources
    for type, value in MENU[type_coffe]["ingredients"].items():
        machine_resources[type] -= value

# Display current available resources in machine
def display_resources():
    print("----------------------".center(40))
    for type, value in machine_resources.items():
        unit = ('g' if type == 'coffee' else 'ml')
        print(f"{type.capitalize()}: {value}{unit}".center(40))
    print("----------------------".center(40))

# Display the manu of the machine
def display_menu():
    print("----------------------".center(40))
    for drink, price in MENU.items():
        print(f"{drink.capitalize()}: {price['cost']} CHF.".center(40))
    print("----------------------".center(40))

# Count given money by cash
def count_money():
    print("Please insert coins")
    cent5 = int(input("How many 5 cents? "))
    cent50 = int(input("How many 50 cents? "))
    onefranc = int(input("How many 1 CHf? "))
    twofranc = int(input("How many 2 CHF? "))

    return (cent5 * 0.05) + (cent50 * 0.5) + (onefranc) + (twofranc * 2)

# Reload machine with resources
def reload_machine():
    print("Reloading machine with resources..")
    time.sleep(3)
    for res in resources:
        print(f"Reloading {res}..")
        time.sleep(2)
    print("Process finished with success!")
    return deepcopy(resources)

### Main program
# Print the menu when first use
print(LOGO)
display_menu()

while On:
    # Ask user
    answer = input("What would you like? (espresso/latte/cappuccion) ").lower()
    # Display resources
    if answer == "report":
        display_resources()
    # Turn off machine
    elif answer == "off":
        On = False
    # Reload machine
    elif answer == 'reload':
        machine_resources = reload_machine()
    # Treat selected hot drink
    elif answer in ['latte','cappuccino','espresso']:
        given_cash = count_money()
        # Enough cash for hot drink and resource
        if given_cash >= MENU[answer]['cost'] and check_resources(answer):
            # Return change
            print(f"Here is {given_cash - MENU[answer]['cost']} CHF in change.")
            # Give hot drink
            print(f"Here is your {answer}, enjoy. {COFFE}")
            # Update resource
            update_resource(answer)
            # Increase profits
            profits += MENU[answer]['cost']
        else:
            print("The process has not work, either not enough cash or enough resources. Give enough cash or reload machine.")
    elif answer == "profits":
        print(f"{profits} CHF.")
    # No matching answers
    else:
        print("The command is not valid.")

