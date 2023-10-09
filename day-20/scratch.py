SNAKE_WIDTH = 1

def add_tail(color, pos) -> Turtle:
    new_tail = Turtle()
    new_tail.penup()
    new_tail.shape("square")
    new_tail.turtlesize(stretch_wid=SNAKE_WIDTH, stretch_len=SNAKE_WIDTH)
    new_tail.color(color)
    new_tail.speed('fastest')
    new_tail.setpos(pos)
    return new_tail

snake = []

game_over = False
while not game_over:
    # coords = snake[0].pos()
    # snake[0].forward(DISTANCE)
    # snake[-1].setpos(coords)
    # snake.append(add_tail(color='white', pos=coords))

    if abs(snake[0].xcor()) > WINDOW_WIDTH / 2 or abs(snake[0].ycor()) > WINDOW_HEIGHT / 2:
        game_over = True
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
screen.update()