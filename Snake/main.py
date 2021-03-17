#Create a snake body
#Move the snake
#Control the snake
#Detection collision with food
#create scoreboard
#Detect collision with wall
#Detect collision with tail

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segments in snake.segment[1:]:
        if snake.segment[0].distance(segments) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

with open("data.txt", mode="w") as file:
    file.write(str(scoreboard.high_score))