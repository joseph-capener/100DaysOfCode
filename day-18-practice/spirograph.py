import turtle
from turtle import Turtle as Turt, colormode
from random import randint

# Parameters
NUM_CIRCLES = 100
CIRCLE_RADIUS = 150


def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# Begin

timmy = Turt()
timmy.hideturtle()
colormode(255)
timmy.speed('fastest')

for _ in range(NUM_CIRCLES):
    timmy.pencolor(change_color())
    timmy.circle(CIRCLE_RADIUS)
    timmy.right(360/NUM_CIRCLES)

turtle.exitonclick()
