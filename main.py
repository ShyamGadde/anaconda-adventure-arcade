# pylint: disable=missing-docstring

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import SNAKE_IMG, Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.addshape(SNAKE_IMG)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


GAME_IS_ON = True

while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 1:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        GAME_IS_ON = False
        screen.update()
        scoreboard.game_over()

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 1:
            GAME_IS_ON = False
            scoreboard.game_over()


screen.exitonclick()
