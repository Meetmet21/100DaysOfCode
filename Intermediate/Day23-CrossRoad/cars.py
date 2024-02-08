# MODULES
import random
from turtle import Turtle

# VARIABLES
# Number of cars to be present on the screen
COLORS = ["red", "blue", "black", "orange", "pink", "green", "brown"]
EXCLUSION = 40
# CLASS
class Cars:

    def __init__(self, edge, screen_w):
        # Default speed
        self.speed = 10
        # Default orientation
        self.heading = 180
        # Car container
        self.cars = []
        # Size ration
        self.w_ratio = 1
        self.h_ratio = 2
        # Edge for up and downside
        self.edge = edge
        self.screen_w = screen_w

    # Create cars instance
    def create_car(self):
        self.cars.append(Turtle("square"))
        self.cars[-1].penup()
        self.cars[-1].color(random.choice(COLORS))
        self.cars[-1].resizemode("user")
        self.cars[-1].shapesize(self.w_ratio, self.h_ratio)
        self.cars[-1].setheading(self.heading)
        x = self.screen_w//2
        y = random.randint(self.edge * -1 + EXCLUSION, self.edge - EXCLUSION)
        self.cars[-1].goto(x, y)

    def advance_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    # Reset all cars
    def reset(self):
        pass
