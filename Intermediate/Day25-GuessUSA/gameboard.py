# MODULES
from turtle import Turtle

# VARIABLES
FONT = "arial"
SIZE = 14
TYPE = "bold"
ALIGN = "center"


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.x, self.y = -100, 220
        self.penup()
        self.hideturtle()
        self.max_time = 600
        # After attributes
        self.update_massage()

    def timer(self):
        minutes = self.max_time // 60
        seconds = self.max_time % 60

        return minutes, seconds

    # Display current states to guess or guessed
    def update_massage(self):
        self.clear()
        self.goto(self.x, self.y)
        minutes, sec = self.timer()
        self.write(f"States: {self.score}/50 Time: {minutes: 2d}:{sec: 2d}",
                   True, ALIGN, (FONT, SIZE, TYPE))


    def win_screen(self):
        self.goto(0, 0)
        self.write("You guessed all the states in USA, good job!", True, ALIGN, (FONT, SIZE, TYPE))

    def loose_screen(self):
        self.goto(0, 0)
        self.write(f"Sorry, you ran out of time. But good job, you guessed {self.score - 1} states!",
                   True, ALIGN, (FONT, SIZE, TYPE))
