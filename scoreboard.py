from logging import fatal
from turtle import Turtle

FONT = ("Courier", 24, "normal")
START_POSITION = (-260, 250)

##---- Class for Scoreboard ----##
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color("black")
        self.goto(START_POSITION)
        self.write(f"Level: {self.level}", False, "left", FONT)

    ## Function to trigger level increase
    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "left", FONT)

    ## Function to trigger gameover
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", False, "center", FONT)
