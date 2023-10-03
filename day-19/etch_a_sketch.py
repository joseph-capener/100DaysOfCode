from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

DISTANCE = 10
ROTATION = 10

def move_forwards() -> None:
    tim.forward(distance=DISTANCE)


def counter_clockwise_turn() -> None:
    tim.left(angle=ROTATION)


def clockwise_turn() -> None:
    tim.right(angle=ROTATION)


def move_backwards() -> None:
    tim.back(distance=DISTANCE)


def clear_drawing() -> None:
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=counter_clockwise_turn)
screen.onkey(key="d", fun=clockwise_turn)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
