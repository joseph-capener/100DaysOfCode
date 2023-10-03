from turtle import Turtle, Screen

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
SNAKE_WIDTH = 1
DISTANCE = 12
ROTATION = 90


snake = []
screen = Screen()
screen.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)


def add_tail(color) -> Turtle:
    new_tail = Turtle()
    new_tail.penup()
    new_tail.shape("square")
    new_tail.shapesize(SNAKE_WIDTH)
    new_tail.color(color)
    new_tail.speed(1)
    return new_tail


def counter_clockwise_turn() -> None:
    snake[0].left(angle=ROTATION)


def clockwise_turn() -> None:
    snake[0].right(angle=ROTATION)


screen.listen()
screen.onkey(key="a", fun=counter_clockwise_turn)
screen.onkey(key="d", fun=clockwise_turn)

# Create initial snake
snake.append(add_tail('black'))
snake.append(add_tail('blue'))

game_over = False
while not game_over:
    coords = snake[0].pos()
    snake[0].forward(DISTANCE)
    snake[1].setpos(coords)


    if abs(snake[0].xcor()) > WINDOW_WIDTH/2 or abs(snake[0].ycor()) > WINDOW_HEIGHT/2:
        game_over = True


screen.exitonclick()
