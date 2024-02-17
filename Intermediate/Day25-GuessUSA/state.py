# MODULES
from turtle import Turtle

# VARIABLES
FONT = "arial"
SIZE = 8
TYPE = "bold"
ALIGN = "center"

class State(Turtle):

    def __init__(self, state_name: str, state_x, state_y):
        super().__init__()
        self.name = state_name
        self.x = state_x
        self.y = state_y
        self.to_my_place()

    # Create message and send it to right place
    def to_my_place(self):
        # Don't draw and don't show
        self.penup()
        self.hideturtle()
        # Go to state localisation
        self.setpos(self.x, self.y)
        # Write message
        self.write(self.name, True, ALIGN, (FONT, SIZE, TYPE))