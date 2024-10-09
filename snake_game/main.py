from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Best Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    #detect collision with tail
    for square in snake.squares[:1:-1]:
        if snake.head.distance(square) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()