# Description
    # In this project, I will implement a simple snake game using turtle GUI.
    # The main objective, it to improve my understanding of OOP.
    # THere are 7 parts to this project:
        # 1) Create a snake body
        # 2) Move the snake forward continuously
        # 3) Get keybord direction to move snake
        # 4) Detect collision with food
        # 5) Create a scoreboard
        # 6) Detect collision with wall
        # 7) Detect collision with tail
import turtle
# Modules
from turtle import Screen
from Snake import Snake
from Food import Food
from Score import Score
import time

# Variables
# Initiate screen instance
screen = Screen()
# Screen height and width parameters
HEIGHT = 600
WIDTH = 600
screen.setup(WIDTH, HEIGHT)
# Screen background
screen.bgcolor("black")
# Screen title
screen.title("Turtle eating snake!")
# Tracer off to custom update of images on screen
screen.tracer(0)
# Game variables
score = 0
# Show score
scoreboard = Score(WIDTH, HEIGHT)
food = Food(WIDTH, HEIGHT)
# Main program
# Initiate snake instance
snake = Snake()
# Game state
state = True
# Track for key input
screen.listen()
# Move to left or right
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")
screen.onkey(snake.up, "w")

while state:
    # Move continuously snake forward
    snake.move_body()

    # Collision with walls (width or height - 20 which is the head size)
    if abs(snake.head.xcor()) > (WIDTH//2) or abs(snake.head.ycor()) > (HEIGHT//2):
        scoreboard.reset()
        snake.reset()

    # Collision with tail
    if snake.tail_bitten():
        scoreboard.reset()
        snake.reset()

    # Check collision with food and increase score
    if food.food_bitten(snake.head):
        # New food
        food.new_food()
        # Increase score
        scoreboard.increase_score()
        # New segment
        snake.segment_build()

    # Update screen each 0.1 sec
    time.sleep(0.05)
    screen.update()

# Quit screen on click
screen.exitonclick()