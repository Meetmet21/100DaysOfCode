# Description
    # Creat food instances for the snake game

# Module
from turtle import Turtle
from random import randint, choice
# Variables
# Food size ratio (default 20px)
RATIO = 1
# Distance exclusion around border
BORDER_EXCLUSION = 20

# Class
class Food:
    # Instance attributes
    def __init__(self, screen_width, screen_height):
        # Screen dimensions
        self.width = screen_width
        self.height = screen_height
        # Food instance tracker
        self.food = None
        # Contain all current instances of food (turtle instance)
        self.generate_food()

    def generate_food(self):
        self.food = Turtle("turtle")
        # Don't draw
        self.food.penup()
        # Food color
        self.food.color("red")
        # Set resize mode to 'user' to modify square shape: Default site is 20px so ratio = 1
        self.food.resizemode('user')
        # Now square of 10 pixel
        self.food.shapesize(stretch_wid=RATIO, stretch_len=RATIO, outline=1)
        # Set position randomly
        # Choose random x and y
        x = randint(-1 * (self.width // 2) + BORDER_EXCLUSION, self.width // 2 - BORDER_EXCLUSION)
        y = randint(-1 * (self.height // 2) + BORDER_EXCLUSION, self.height // 2 - BORDER_EXCLUSION)
        # Set coordinates to random coordinates
        self.food.goto(x, y)

    # Generate new food if food eaten
    def food_bitten(self, snake_head):
        if self.food.distance(snake_head.pos()) < RATIO * 20:
            return True

    # New food instance
    def new_food(self):
        # Set position randomly
        # Choose random x and y
        x = randint(-1 * (self.width//2) + BORDER_EXCLUSION, self.width// - BORDER_EXCLUSION)
        y = randint(-1 * (self.height//2) + BORDER_EXCLUSION, self.height//2 - BORDER_EXCLUSION)
        # Set coordinates to random coordinates
        self.food.goto(x, y)
