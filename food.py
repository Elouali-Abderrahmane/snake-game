from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.appear_food()

    def appear_food(self):
        x_random = random.randint(-350, 350)
        y_random = random.randint(-350, 350)
        self.goto(x_random, y_random)
