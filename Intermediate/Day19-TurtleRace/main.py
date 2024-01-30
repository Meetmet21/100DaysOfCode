# Description

# Modules
import turtle as T
from random import randint

# Turtle and Screen instances
pen = T.Turtle()
screen = T.Screen()
# Set up the GUI window
screen.setup(width=500, height=400)

# List to contain turtle instances
turtles = []
# 6 turtles racing
for color in ["red", "blue", "yellow", "brown", "black", "pink"]:
    turtles.append(T.Turtle("turtle"))
    # Color the last instance
    turtles[-1].color(color)

# Ask user for bet
answer = screen.textinput(title="Who will win the race?", prompt="Red, Yellow, Brown, Black or Pink?")

# Move turtles to the starting line
dist = 0
for turtle in turtles:
    # Do not draw
    turtle.penup()
    # Move to starting line
    turtle.goto(x=-250, y=-75 + dist)
    # Distance between turtles
    dist += 25

# Tell if race not finished
race_state = True
# Random forward steps for each turtle until reach end
while race_state:
    for turtle in turtles:
        # Random distance to go
        dist = randint(0,15)
        turtle.forward(dist)

        # When turtle xcor reaches the end (-20 because turtle size
        if turtle.xcor() >= 250 - 20:
            print(f"The {turtle.color()[0]} turtle has won the race!")
            race_state = False





# Keep screen while not click
screen.exitonclick()
