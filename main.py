from turtle import Screen
from player import Player
import time
from car_manager import CarManager
from scoreboard import Scoreboard

#### Screen setup ####
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

#### spawn classes ####
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

#### keyboard setup ####
screen.listen()
screen.onkeypress(player.move,"w")
screen.onkey(player.respawn, "r")
screen.onkey(car_manager.spawn_car, "q")


#### Game Loop ####
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.spawn_car()

    #### Lose condition ####
    if car_manager.car_crash(player):
        scoreboard.game_over()
        game_is_on = False

    #### Level clear ####
    if player.finish_line():
        car_manager.speed_up()
        scoreboard.level_up()

    car_manager.move_cars()

screen.exitonclick()