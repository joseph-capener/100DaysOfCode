from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            coordinates = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(coordinates)
        self.head.forward(MOVE_DISTANCE)

    def north(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def south(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def east(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def west(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
