from turtle import Turtle


class Snake:

    MOVE_DISTANCE = 10

    def __init__(self):
        self.__turtles = []
        self.__positions = [(-40, 0), (-20, 0), (0, 0)]
        self.__create_snake()
        self.head = self.__turtles[-1]
        self.tail = self.__turtles[0]
        self.direction = "right"

    @property
    def turtles(self):
        """Returns all segments except the head (for collision checks)."""
        return self.__turtles[:-1]

    def __create_snake(self):
        for i in range(len(self.__positions)):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(self.__positions[i])
            self.__turtles.append(new_turtle)

    def move_snake(self):
        for i in range(len(self.__turtles) - 1):
            self.__turtles[i].goto(self.__turtles[i + 1].pos())
        self.head.forward(Snake.MOVE_DISTANCE)

    def go_up(self):  # Prevent reverse direction
        if self.direction != "dowm":
            self.direction = "up"
            self.head.setheading(90)

    def go_down(self):  # Prevent reverse direction
        if self.direction != "up":
            self.direction = "down"
            self.head.setheading(270)

    def go_right(self):  # Prevent reverse direction
        if self.direction != "left":
            self.direction = "right"
            self.head.setheading(0)

    def go_left(self):
        if self.direction != "right":  # Prevent reverse direction
            self.direction = "left"
            self.head.setheading(180)

    def grow_snake(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.tail.pos())
        self.__turtles.insert(0, new_segment)
