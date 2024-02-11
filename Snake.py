from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            self.snake.append(Turtle(shape="square"))
            self.snake[i].color("orange")
            self.snake[i].penup()
            self.snake[i].setx(-20 * i)
            self.snake[i].sety(0)
        self.head = self.snake[0]

    def extend(self):
        prev_x = self.snake[-1].xcor()
        prev_y = self.snake[-1].ycor()
        self.snake.append(Turtle(shape="square"))
        self.snake[-1].color("orange")
        self.snake[-1].penup()
        self.snake[-1].goto(prev_x,prev_y)

    def move(self):
        for j in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[j - 1].xcor()
            new_y = self.snake[j - 1].ycor()
            self.snake[j].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
