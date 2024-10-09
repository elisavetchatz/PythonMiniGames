from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Best Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "W")
screen.onkey(left_paddle.go_down, "S")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #detect when right paddle misses
    if ball.xcor() > 380:
        time.sleep(0.1)
        scoreboard.l_point()
        ball.reset_pos()
    #detect when left paddle misses
    if ball.xcor() < -380 :
        time.sleep(0.1)
        scoreboard.r_point()
        ball.reset_pos()









screen.exitonclick()

