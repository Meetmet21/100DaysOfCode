### Modules
from time import sleep
from copy import deepcopy

### Classes

class CoffeeMachine:
    # Static data
    MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18,},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24,},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24,},
        "cost": 3.0,}
        }
    
    RESOURCES = {"water": 300, "milk": 200, "coffee": 100,}
    
    # INherited by each objects and variable
    def __init__(self):
        # Initial resources in a machine
        self.resources = deepcopy(CoffeeMachine.RESOURCES)
        # Earned money
        self.profits = 0
        # Machine state
        self.on = True

    # Check if enough resources for command
    def check_resources(self, hot_drink):
    # Check if enough milk, coffe, water
        for type, value in CoffeeMachine.MENU[hot_drink]["ingredients"].items():
            if self.resources[type] < value:
                return False
        # Enough resources    
        return True
    
    # Remove recipe ingredientns values from resource
    def update_resource(self, hot_drink):
    # Deduce recipe ingredients for hot drink from resources
        for type, value in CoffeeMachine.MENU[hot_drink]["ingredients"].items():
            self.resources[type] -= value

    # Display current available resources in machine
    def display_resources(self):
        print("----------------------".center(40))
        for type, value in self.resources.items():
            unit = ('g' if type == 'coffee' else 'ml')
            print(f"{type.capitalize()}: {value}{unit}".center(40))
        print("----------------------".center(40))
    
    # Display the manu of the machine
    def display_menu(self):
        print("----------------------".center(40))
        for drink, price in CoffeeMachine.MENU.items():
            print(f"{drink.capitalize()}: {price['cost']} CHF.".center(40))
        print("----------------------".center(40))
    
    # Count given money by cash
    def count_money(self):
        print("Please insert coins")
        cent5 = int(input("How many 5 cents? "))
        cent50 = int(input("How many 50 cents? "))
        onefranc = int(input("How many 1 CHf? "))
        twofranc = int(input("How many 2 CHF? "))

        return (cent5 * 0.05) + (cent50 * 0.5) + (onefranc) + (twofranc * 2)
    
    # Reload machine with resources
    def reload_machine(self):
        print("Reloading machine with resources..")
        sleep(3)
        for res in self.resources:
            print(f"Reloading {res}..")
            sleep(2)
        print("Process finished with success!")
        self.resources = deepcopy(CoffeeMachine.RESOURCES)
    
