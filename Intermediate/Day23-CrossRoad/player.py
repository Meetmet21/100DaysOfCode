# MODULES
from turtle import Turtle

# Class
class Player(Turtle):

    def __init__(self, screen_w, screen_h):
        super().__init__()
        self.color("blue")
        self.penup()
        self.shape("turtle")
        # Starting position
        self.starting_pos = (0, screen_h//2 * -1 + 40)
        self.goto(self.starting_pos)
        # Heading towards up
        self.setheading(90)

    # Movement towards upside
    def up(self):
        self.forward(15)

    # Movement towards downside
    def down(self):
        self.backward(15)

    # Reset initial position
    def reset(self):
        self.goto(self.starting_pos)