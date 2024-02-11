import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.reset()

    def reset(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 240)
        self.goto(x=x, y=y)
