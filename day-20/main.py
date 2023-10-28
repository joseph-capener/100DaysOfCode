import time
from turtle import Screen
from snake import Snake
from food import Food

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()

screen.onkey(key="Up", fun=snake.north)
screen.onkey(key="Down", fun=snake.south)
screen.onkey(key="Right", fun=snake.east)
screen.onkey(key="Left", fun=snake.west)

game_over = False
score = 0
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        print(score)

screen.exitonclick()
