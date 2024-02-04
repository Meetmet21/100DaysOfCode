# Description
    # Snake class methods and attributes
import turtle
# Modules
from turtle import Turtle

# Variables
# The segments shape ratio (20 * ratio) 20px by default
RATIO = 0.5
# Distance between segments to not overlap
DIST = 20 * RATIO
# Number of segment at beginning
N_SEG = 3
# Class
class Snake:
    # Instance attributes
    def __init__(self):
        # Contain all square instances that contains the current body
        self.body = []
        # Begin with 3 squares/snake segments
        for square in range(N_SEG):
            self.segment_build()
        # The head os the snake
        self.head = self.body[0]

    # Set up new instance of turtle to build one new segment for snake
    def segment_build(self):
        self.body.append(Turtle("square"))
        # Don't draw
        self.body[-1].penup()
        # Set square color
        self.body[-1].color("white")
        # Set resize mode to 'user' to modify square shape: Default site is 20px so ratio = 1
        self.body[-1].resizemode('user')
        # Now square of 10 pixel
        self.body[-1].shapesize(stretch_wid=RATIO, stretch_len=RATIO, outline=1)
        # Fix squares positions
        if len(self.body) > 1:
            self.add_to_end()

    # This function will add in correction direction a new segment
    def add_to_end(self):
        # The tail segment heading to know in which direction to add new segment
        tail = self.body[-2]
        if tail.heading() == 0:
            self.body[-1].goto(x=tail.xcor() - DIST,
                               y=tail.ycor())
        elif tail.heading() == 90:
            self.body[-1].goto(x=tail.xcor(),
                               y=tail.ycor() - DIST)
        elif tail.heading() == 180:
            self.body[-1].goto(x=tail.xcor() + DIST,
                               y=tail.ycor())
        else:
            self.body[-1].goto(x=tail.xcor(),
                               y=tail.ycor() + DIST)


    # Move the body to follow the head position
    def move_body(self):
        # From tail to head
        for segment in range(len(self.body) - 1, 0, -1):
            # Coordinates of the segment before
            x = self.body[segment - 1].xcor()
            y = self.body[segment - 1].ycor()
            # Move current segment to segment before
            self.body[segment].goto(x, y)
        # Move head
        self.head.forward(10)

    # Turn snake to left
    def left(self):
        # Dont turn left if heading to right otherwise bite the tail
        if self.head.heading() != 0:
            self.head.setheading(180)

    # TUrn snake to right
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    # Check if collision between body and head by looking distance between each segment
    def tail_bitten(self):
        for segment in self.body[1:]:
            if self.head.distance(segment.pos()) < 5:
                return True


