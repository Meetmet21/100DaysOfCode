# Description
# Print snake game score on screen

# Modules
from turtle import Turtle

# Variables
ALIGNEMENT = "center"
SIZE = 12
FONT = "arial"
FONTYPE = "bold"
# Class
class Score(Turtle):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        # Score tracker
        self.score = 0
        # Don't show turtle instance
        self.hideturtle()
        self.penup()
        # Set width and height as attributes
        self.width = WIDTH
        self.height = HEIGHT
        # Write score
        self.color("white")
        self.update_score()

    def update_score(self):
        self.goto(-5, self.height//2 - 25)
        self.write(f"Score: {self.score}", True, ALIGNEMENT, (FONT, SIZE, FONTYPE))


    # Increase score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", True, ALIGNEMENT, (FONT, SIZE, FONTYPE))

