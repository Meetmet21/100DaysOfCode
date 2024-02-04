from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, screen_width, screen_height):
        # Inheritance from turtle
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Shape
        self.shape("circle")
        # Color
        self.color("white")
        # Size
        self.resizemode("yellow")
        self.shapesize(stretch_wid=1, stretch_len=1)
        # Pen up
        self.penup()
        # Speed for x and y axis movement
        self.x = 10
        self.y = 10
        self.speed = 1.1

    # Reset ball position
    def reset(self):
        self.home()
        # Reset speed
        self.x = 10
        self.y = 10

    # Movement
    def move(self):
        self.goto(self.x + self.xcor(), self.y + self.ycor())

    # Bounce on the wall
    def bounce_wall(self):
        # Change y coordinates sign
        self.y *= -1

    # Bounce against paddle
    def bounce_paddle(self):
        # Change x coordinate sign
        self.x *= -1
        # Increase speed
        self.x *= self.speed
        self.y *= self.speed



