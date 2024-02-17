# DESCRIPTION
# Quiz game build on turtle GUI.
# The main idea is to guess the 50 states of USA.
# Manipulate data with pandas and get input from player
# and check for wrong and right answer. If right answer,
# place the state name on the state location.

# MODULES
import pandas as pd
import turtle
import time

from state import State
from gameboard import Board

# VARIABLES
# read state data
df = pd.read_csv("50_states.csv")
# Initiate screen and set uo
screen = turtle.Screen()
WIDTH = 700
HEIGHT = 500
screen.setup(WIDTH, HEIGHT)
screen.bgpic("blank_states_img.gif")
screen.title("Guess USA states.")
screen.tracer(0)
# Gameboard class
gameboard = Board()
# Game state
game_on = True
# Get time at start
start = time.time()

while game_on:
    # Ask for state
    state = screen.textinput("USA State", "Give a USA state name:")
    # Check if right answer and update
    if df.state.str.contains(state).any():
        # INcrease score
        gameboard.score += 1
        # Update message
        gameboard.update_massage()
        # Get from df the matching row
        matching_row = df.loc[df.state.isin([state])]
        # Place state on screen
        State(matching_row.state.iloc[0], int(matching_row.x.iloc[0]), int(matching_row.y.iloc[0]))
    # Win condition
    if gameboard.score >= 50:
        gameboard.win_screen()
        game_on = False
    # Loose condition
    elif gameboard.max_time <= 0:
        gameboard.loose_screen()
        game_on = False
    # Let time to process
    time.sleep(1)
    # Get time of process
    end = time.time()
    # Update time
    gameboard.max_time -= int(end - start)
    gameboard.update_massage()



#screen exit on click
screen.exitonclick()