import turtle
from turtle import Turtle


def clear_turtle(turtle_to_delete):
    turtle_to_delete.reset()
    turtle_to_delete.hideturtle()


timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')

# Draw a square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

timmy_the_turtle.onclick(clear_turtle(timmy_the_turtle))

james_the_turtle = Turtle()
james_the_turtle.shape('turtle')
james_the_turtle.color('green')

for _ in range(15):
    james_the_turtle.pendown()
    james_the_turtle.forward(10)
    james_the_turtle.penup()
    james_the_turtle.forward(10)

turtle.Screen().exitonclick()
