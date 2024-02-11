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
        # Keep track highest score
        self.high_score = 0
        # Don't show turtle instance
        self.hideturtle()
        self.penup()
        # Set width and height as attributes
        self.width = WIDTH
        self.height = HEIGHT
        # Write score
        self.color("white")
        # Read previous highest score if exist
        self.filename = "high_score.txt"
        with open(self.filename, 'r') as file:
            self.high_score = int(file.read())

        self.update_score()

    def update_score(self):
        self.goto(-5, self.height//2 - 25)
        self.write(f"Score: {self.score} Highest score: {self.high_score}", True, ALIGNEMENT, (FONT, SIZE, FONTYPE))

    # Increase score
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()


    # Reset the highest score if bigger score
    def reset(self) -> None:
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        # Reset the score
        self.score = 0
        self.update_score()
        # Write high score
        with open(self.filename, 'w') as score_tracker:
            score_tracker.write(f"{self.high_score}")
