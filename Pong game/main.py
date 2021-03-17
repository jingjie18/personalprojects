from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#create screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width = 800, height = 600)

screen.listen()
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #collision with top and bottom screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    #Detect when paddle miss ball
    if ball.xcor() > 380:
        ball.home()
        ball.move_speed = 0.1
        ball.bounce_x()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.home()
        ball.move_speed = 0.1
        ball.bounce_x()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()