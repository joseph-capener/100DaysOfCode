import turtle

import colorgram
from turtle import Turtle
from random import randint


WIDTH = 5
HEIGHT = 5
NUM_COLORS = 10

def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# Extract 20 colors from an image.
colors = colorgram.extract('resources/img.png', NUM_COLORS)
#colors.sort(key=lambda c: c.hsl.h)

color_list = []
for color in colors:
    color_scheme = (color.rgb.r, color.rgb.g, color.rgb.b)
    color_list.append(color_scheme)

timmy = Turtle()
timmy.hideturtle()
timmy.speed('fastest')
turtle.colormode(255)
turtle.penup()

for dot in range(1, NUM_COLORS):
    timmy.dot(10, color_list[dot])
    if dot % 2*WIDTH == 5:
        timmy.right(90)
        timmy.forward(30)
        timmy.right(90)
    elif dot % WIDTH == 0:
        timmy.left(90)
        timmy.forward(30)
        timmy.left(90)
    else:
        timmy.forward(30)

turtle.exitonclick()

print(color_list)
