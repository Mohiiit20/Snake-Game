from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from Snake import Snake

screen = Screen()
food = Food()
scoreboard = Scoreboard()
screen.setup(height=600, width=600)
screen.tracer(0)

screen.bgcolor("#90EE90")
player = Snake()
screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")
screen.onkey(player.right, "d")
screen.onkey(player.left, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    player.move()
    # detect collision
    if player.head.distance(food) < 15:
        food.reset()
        scoreboard.increase_score()
        player.extend()


    for segment in player.snake[1:]:
        if player.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    if player.head.xcor() > 280 or player.head.ycor() > 270 or player.head.ycor() < -280 or player.head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
