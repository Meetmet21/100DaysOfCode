# DESCRIPTION
    # Implementtion of a Pong game using the turtle GUI

# MODULES
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from padel import Padel
from time import sleep


# VARIABLES
# Screen instance
screen = Screen()
# Screen width and height
WIDTH = 800
HEIGHT = 600
screen.setup(WIDTH, HEIGHT)
# Background color
screen.bgcolor("black")
# Screen title
screen.title("Pong Game")
# Tracer off, manual update of the screen
screen.tracer(0)
# In game
scoreboard = Scoreboard(WIDTH, HEIGHT)
left_padel = Padel("left", WIDTH, HEIGHT)
right_padel = Padel("right", WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT)
# Keyboard input
screen.listen()
screen.onkeypress(left_padel.up, "w")
screen.onkeypress(left_padel.down, "s")
screen.onkeypress(right_padel.up, "Up")
screen.onkeypress(right_padel.down, "Down")
# Game state
game_on = True

while game_on:
    # Ball moves continuously
    ball.move()

    # Bounce if hit wall top and bottom
    if ball.ycor() > (HEIGHT//2 - 20) or ball.ycor() < (-1 * HEIGHT//2 + 20):
        ball.bounce_wall()

    # Bounce if hit paddle at the surface and ball is in the range
    if (ball.xcor() < -1 * WIDTH//2 + 60 and ball.distance(left_padel.xcor() + 20, left_padel.ycor()) < 70 or
            ball.xcor() > WIDTH//2 - 60 and ball.distance(right_padel.xcor() - 20, right_padel.ycor()) < 70):
        ball.bounce_paddle()

    # Increase score and reset game
    # If left miss
    if ball.xcor() < -1 * WIDTH//2:
        # Increase score for right
        scoreboard.right_score += 1
        scoreboard.update_scoreboard()
        # Reset ball and paddles
        ball.reset()
        left_padel.reset()
        right_padel.reset()
    # Same for right
    if ball.xcor() > WIDTH//2:
        scoreboard.left_score += 1
        scoreboard.update_scoreboard()
        ball.reset()
        left_padel.reset()
        right_padel.reset()

    # Game end
    if scoreboard.left_score == 7 or scoreboard.right_score == 7:
        scoreboard.winner()
        game_on = False

    # iPS
    sleep(0.05)
    screen.update()


screen.exitonclick()