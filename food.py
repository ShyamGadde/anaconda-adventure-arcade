from turtle import Turtle
from random import randint


def get_random_coords():
    return randint(-280, 280) // 20 * 20, randint(-280, 280) // 20 * 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(get_random_coords())
        self.refresh()

    def refresh(self):
        self.goto(get_random_coords())
