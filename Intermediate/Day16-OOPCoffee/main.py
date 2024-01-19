### Description
# This is the same exercise as the previous day, but
# I changes the coding paradigme with OOP (before procedral).

### Modules
from art import LOGO, COFFE
from CoffeeMachine import CoffeeMachine

### Main program
my_machine = CoffeeMachine()
print(LOGO)
my_machine.display_menu()

while my_machine.on:
    # Ask user
    answer = input("What would you like? (espresso/latte/cappuccion) ").lower()
    # Display resources
    if answer == "report":
        my_machine.display_resources()
    # Turn off machine
    elif answer == "off":
        my_machine.on = False
    # Reload machine
    elif answer == 'reload':
        my_machine.reload_machine()
    # Treat selected hot drink
    elif answer in ['latte','cappuccino','espresso']:
        given_cash = my_machine.count_money()
        # Enough cash for hot drink and resource
        if given_cash >= my_machine.MENU[answer]['cost'] and my_machine.check_resources(answer):
            # Return change
            print(f"Here is {given_cash - my_machine.MENU[answer]['cost']} CHF in change.")
            # Give hot drink
            print(f"Here is your {answer}, enjoy. {COFFE}")
            # Update resource
            my_machine.update_resource(answer)
            # Increase profits
            my_machine.profits += my_machine.MENU[answer]['cost']
        else:
            print("The process has not work, either not enough cash or enough resources. Give enough cash or reload machine.")
    elif answer == "profits":
        print(f"{my_machine.profits} CHF.")
    # No matching answers
    else:
        print("The command is not valid.")
