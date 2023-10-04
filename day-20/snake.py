import time
from turtle import Turtle, Screen

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
SNAKE_WIDTH = 1
DISTANCE = 20
ROTATION = 90

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def add_tail(color, pos) -> Turtle:
    new_tail = Turtle()
    new_tail.penup()
    new_tail.shape("square")
    new_tail.turtlesize(stretch_wid=SNAKE_WIDTH, stretch_len=SNAKE_WIDTH)
    new_tail.color(color)
    new_tail.speed('fastest')
    new_tail.setpos(pos)
    return new_tail


def north() -> None:
    if snake[0].heading() != 270.0:
        snake[0].setheading(90.0)


def south() -> None:
    if snake[0].heading() != 90.0:
        snake[0].setheading(270.0)


def east() -> None:
    if snake[0].heading() != 180.0:
        snake[0].setheading(0.0)


def west() -> None:
    if snake[0].heading() != 0.0:
        snake[0].setheading(180.0)


screen.listen()

screen.onkey(key="a", fun=west)
screen.onkey(key="d", fun=east)
screen.onkey(key="w", fun=north)
screen.onkey(key="s", fun=south)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake.append(new_segment)
    screen.update()
game_over = False
while not game_over:
    # coords = snake[0].pos()
    # snake[0].forward(DISTANCE)
    # snake[-1].setpos(coords)
    # snake.append(add_tail(color='white', pos=coords))

    for seg_num in range(len(snake)-1, 0, -1):
        coords = snake[seg_num - 1].pos()
        snake[seg_num].goto(coords)
    snake[0].forward(DISTANCE)
    if abs(snake[0].xcor()) > WINDOW_WIDTH / 2 or abs(snake[0].ycor()) > WINDOW_HEIGHT / 2:
        game_over = True
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
