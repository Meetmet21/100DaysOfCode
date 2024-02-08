# DESCRIPTION
#   Game idea: A turtle tries to cross the road with hurry cars.
#   He's aim is to reach the other side which is the top section of the screen.
#   Every succeed leads to the increase of car's speed!
#   Things to implement:
#       1) Player class: player, movement, attributes (start, speed, shape, color, etc..)
#       2) Cars class: N number of cars positioned randomly on the screen,
#          trying to avoid overlapping. Set attributes and movement and also set a new positions when
#          cars reaches the left corner of the screen. Increase speed function depending on level.
#       3) Game board class: Keep track of current level and show game over text.
#       4) In main file: implement collision between car and player, winning condition and so next level
#       5) All classes needs reset or update when level finished

# MODULES
from turtle import Screen
from player import Player
from gameboard import Gameboard
from cars import Cars
from time import sleep

# VARIABLES
# Set up screen
screen = Screen()
WIDTH = 600
HEIGHT = 600
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)
screen.title("Cross the road if you dare!?")
# Initiate player instance
player = Player(WIDTH, HEIGHT)
# Initiate game board
gameboard = Gameboard(WIDTH, HEIGHT)
# Initiate cars
cars = Cars(gameboard.road_end[1], WIDTH)
# Keyboard events binding
screen.listen()
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "s")
# Cunt before car creation. Each 0.5 sec
count = 5
# Game state
state = True

while state:
    count -= 1
    if count == 0:
        cars.create_car()
        count = 5
    cars.advance_cars()
    # Collision with cars
    for car in cars.cars:
        if player.distance(car) < 20:
            gameboard.game_over()
            state = False
    # Winning condition
    if player.ycor() > gameboard.road_end[1] + 20:
        # Increase level
        gameboard.level += 1
        # Increase speed at each new level
        cars.speed *= 1.5
        # Player to beginning
        player.reset()
        # Update board
        gameboard.update_board()


    # Update screen
    sleep(0.1)
    screen.update()
# Quit on click
screen.exitonclick()
