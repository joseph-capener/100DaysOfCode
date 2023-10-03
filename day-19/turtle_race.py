import turtle
from turtle import Turtle, Screen
from random import randint

red_turtle = Turtle()
orange_turtle = Turtle()
yellow_turtle = Turtle()
green_turtle = Turtle()
blue_turtle = Turtle()
purple_turtle = Turtle()
turtle_tuple = (red_turtle, orange_turtle,
                yellow_turtle, green_turtle,
                blue_turtle, purple_turtle)
rainbow = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
screen = Screen()

# Parameters
MAX_STEP = 15
MIN_STEP = 5
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.listen()

def race_startup():
    position = 0
    for turt in turtle_tuple:
        turt.shape("turtle")
        turt.penup()
        turt.color(rainbow[position])
        turt.speed(0)
        turt.goto(x=-225, y=70 - position * 30)
        position += 1


def move_forwards(turt) -> None:
    turtle.speed(0)
    turt.forward(distance=randint(MIN_STEP, MAX_STEP))


user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle do you think will win? "
                                   "Choose a color: ").lower()
race_startup()
race_finish = False
while not race_finish:
    for turt in turtle_tuple:
        move_forwards(turt=turt)
        if turt.xcor() > SCREEN_WIDTH/2-40:
            race_finish = True
            winning_color = turt.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You lose! The {winning_color} turtle is the winner")
            break

screen.exitonclick()
