# MODULES
from turtle import Turtle

# VARIABLES
FONT = 'serif'
SIZE = 16
TYPE = 'normal'
ALIGN = "left"
ROAD_SIZE = 40

# CLASS
class Gameboard(Turtle):

    def __init__(self, screen_w, screen_h):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.h = screen_h
        self.w = screen_w
        # Road_end
        self.road_end = (self.w//2 * -1, self.h//2 * 2/3)
        # Show level when initialized
        self.update_board()
        # Show highway edges
        self.draw_highway()

    # Update massage
    def update_board(self):
        self.clear()
        self.goto(self.w//2 * -1 + 40, self.h//2 - 40)
        self.write(f"Level: {self.level}", True, ALIGN, (FONT, SIZE, TYPE))
        self.draw_highway()

    # Game over message
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, 'center', (FONT, SIZE, "bold"))

    # Draw road edges:
    def draw_highway(self):
        road_edge = "-" * (2000//ROAD_SIZE)
        self.goto(self.road_end)
        # Upside road
        self.write(road_edge, True, ALIGN, (FONT, ROAD_SIZE, TYPE))
        # Downside road
        self.goto(self.road_end[0], self.road_end[1] * -1)
        self.write(road_edge, True, ALIGN, (FONT, ROAD_SIZE, TYPE))
