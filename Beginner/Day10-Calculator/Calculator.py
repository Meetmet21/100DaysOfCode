### Description
# This project implements a simple idea of a calculator.
# The operations are made between two numbers and only
# one operator is accepted. But the user can continue the
# calculations with the result of the previous operation.

### Modules
import Calculator_art # logo

### Variables
# Keep track if already a previous calculation
again = 'n'

### Functions
# We could define functions to do each operations
# but instead we will use the eval() function of python
# which evaluates a string cmd.

### Main program
# Display logo
print(Calculator_art.logo)

while True:
    # Ask for the first number -> choose float instead of int because float accept both (int and float) 
    # First number not from a previous calculation -> ask for first
    if again == 'n':
        first = input("What's the first number?: ")
        # check if a digit
        if not first.isdigit():
            print("You should provide a number to a calculator.")
            break
    else:
        # Keep the previous result, result in str because eval returns a float or int
        first = str(result)
    # Ask for operator
    operator = input("+\n-\n*\n/\nPick an operation: ")
    # Check if an operator was given:
    if operator not in ['+','-','/','*']:
        print("You didn't provide the correct operators.")
        break
    
    # Ask for second number -> choose float instead of int because float accept both (int and float)
    second = input("What's the next number?: ")
    # check if a digit
    if not second.isdigit():
            print("You should provide a number to a calculator.")
            break

    # Calculate result
    operation = first + " " + operator + " " + second
    result = eval(operation)
    # Display mathematical operation
    print(f"{operation} = {result}")

    # Ask if continue with result
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if again == 'n':
        break
    elif again not in ['n','y']:
        print("You didn't answer to the question, it's interpreted as a no!")
        break