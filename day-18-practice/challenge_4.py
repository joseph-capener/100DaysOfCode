import turtle
from turtle import Turtle, colormode, exitonclick, bye
from random import choice, randint


def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def quit_figure():
    bye()


timmy_the_turtle = Turtle()
timmy_the_turtle.speed('fastest')
timmy_the_turtle.shape('blank')
colormode(255)
timmy_the_turtle.pensize(10)

timmy_the_turtle.screen.onkey(quit_figure, "q")
timmy_the_turtle.screen.listen()

for _ in range(300):
    timmy_the_turtle.forward(20)
    timmy_the_turtle.right(choice([0, 90, 180, 270]))
    timmy_the_turtle.pencolor(change_color())
    
exitonclick()
