import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
# screen.screensize()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(key="Up",fun= player.move_up)

carmanager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Move cars
    for i in carmanager.car_list:
        i.forward(carmanager.move_speed)
    loop += 1
    if loop == 6:
        carmanager.create_car()
        loop = 0

    #Detect collision with cars
    for i in carmanager.car_list:
        if i.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect if reach the top edge
    if player.ycor() > 280:
        player.finish_line()
        carmanager.speed_up()
        scoreboard.update_scoreboard()

screen.exitonclick()