from turtle import Turtle

# Fond parameters
SIZE = 40
FONT = "arial"
ALLIGNEMENT = "center"
FONTYPE = "bold"

class Scoreboard(Turtle):
    def __init__(self, screen_width, screen_height):
        # Inheritance from turtle
        super().__init__()
        self.height = screen_height
        self.width = screen_width
        # Score
        self.left_score = 0
        self.right_score = 0
        # Build turtle
        self.hideturtle()
        self.penup()
        self.color("cyan")
        # Initial score
        self.update_scoreboard()

    def update_scoreboard(self):
        # Clear previous writing
        self.clear()
        # Write left score
        self.goto(-50, self.height//2 - 80)
        self.write(f"{self.left_score}", True, ALLIGNEMENT, (FONT, SIZE, FONTYPE))
        # Write right score
        self.goto(50, self.height//2 - 80)
        self.write(f"{self.right_score}", True, ALLIGNEMENT, (FONT, SIZE, FONTYPE))

    def winner(self):
        if self.right_score == 7:
            self.goto(0, 0)
            self.write(f"The winner is right side!", True, ALLIGNEMENT, (FONT, SIZE, FONTYPE))
        else:
            self.goto(0, 0)
            self.write(f"The winner is left side!", True, ALLIGNEMENT, (FONT, SIZE, FONTYPE))
