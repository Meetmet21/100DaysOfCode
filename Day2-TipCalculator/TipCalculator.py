# Great the user
print("Welcome to the tip calculator.")

# Ask for the total bill
# Convert to float for calculations
total = float(input("What was the total biil? $"))

# Ask for the tip percentage applied on the total price
# Convert to integer for calculations
# Divided by hundred to get a percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100

# Ask for the number of people
num_people = int(input("How many people to split the bill? "))

# Add tip percentage to total
total_w_tip = total + (total * tip_percentage)

# Price to pay for each person
# 2 decimals
pay = round(total_w_tip / num_people, 2)

# Print to stdout the result
print(f"Each person should pay: ${pay}.")
