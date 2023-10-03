from turtle import Turtle, colormode
from random import randint

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
timmy_the_turtle.speed('fastest')
colormode(255)

for num_side in range(3, 11):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy_the_turtle.pencolor(r,g,b)
    for _ in range(num_side):
        timmy_the_turtle.forward(75)
        timmy_the_turtle.right(360/num_side)


