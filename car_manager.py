from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

car_list = []

##---- Class for managing cars ----##
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    ## function to spawn cars
    def spawn_car(self):

        random_roll = randint(1,6)
        if random_roll == 1:

            new_car = Turtle()
            car_list.append(new_car)
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.color(COLORS[randint(0, 5)])
            new_car.setheading(180)
            ycor = randint(-230, 250)
            new_car.goto (295,ycor)

    ## Function for collision detection
    def car_crash(self,target):
        for car in car_list:
            if car.distance(target) < 20:
                return True

    ## Function for car speed increase
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    ## Function to move cars
    def move_cars(self):
        for car in car_list:
            car.forward(self.car_speed)
            if car.xcor() < -310:
                car.hideturtle()
                car_list.remove(car)
                del car
