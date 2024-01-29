### Description
# Draw a dot plot with random manner
import turtle
### Modules
import turtle as t
import random as rd
import colorgram

### Variables
# Use default rgb range between 0 to 255
t.colormode(255)
# Turtle instance
pen = t.Turtle()
pen.pensize(3)
pen.speed("fastest")
# Screen instance
screen = t.Screen()
width, height = 800, 600
screen.screensize(width, height)
# Extract 10 colors from image and format to (r,g,b)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b)
          for color in colorgram.extract("image.jpg", 10)]
# Dot size
size = 20
# distance between dots
dist = 50

### Main program
# Pen up we dont want lines to be drawn
pen.penup()
# Max ycor and xcor in our system
xmax = -275
ymax = -200
# Pen start position at screen bottom-left
pen.setposition(xmax, ymax)
# Number of lines depeding on height
for _ in range(int(height / (size + dist))):
    # Dots par line depending on width
    for _ in range(int(width / (size + dist))):
        # Draw a dot with random color
        pen.dot(size, rd.choice(colors))
        # go forward
        pen.forward(dist)

    # Draw the last sot
    pen.dot(size, rd.choice(colors))
    # Go to new line depending on pen heading
    if pen.heading() == 0:
        pen.left(90)
        pen.forward(dist)
        pen.left(90)
    else:
        pen.right(90)
        pen.forward(dist)
        pen.right(90)






# QUit screen on click
screen.exitonclick()

