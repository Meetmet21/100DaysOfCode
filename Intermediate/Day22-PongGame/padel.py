from turtle import Turtle

class Padel(Turtle):
    def __init__(self, side, screen_width, screen_height):
        # Inheritance from turtle
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.side = side
        # Choose which side is paddle
        if self.side == "left":
            self.goto((-1 * self.screen_width//2 + 20), 0)
        else:
            self.goto((self.screen_width//2 - 25), 0)
        # Shape
        self.shape("square")
        # Color
        self.color("white")
        # Size
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # Pen up
        self.penup()

    # Movement function
    def up(self):
        # While on screen
        if self.ycor() <= (self.screen_height//2 - 60):
            # Current x and y
            x, y = self.pos()
            self.goto(x, y + 30)

    def down(self):
        # While in screen
        if self.ycor() >= (-1 * self.screen_height//2 + 60):
            # Current x and y
            x, y = self.pos()
            self.goto(x, y - 30)

    # Initial position of padel
    def reset(self):
        if self.side == "left":
            self.goto((-1 * self.screen_width//2 + 20), 0)
        else:
            self.goto((self.screen_width//2 - 25), 0)