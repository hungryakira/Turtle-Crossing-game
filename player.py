from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10 #10
FINISH_LINE_Y = 290

#### Class for Player (Turtle)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])
        self.setheading(90)

    #### Function to respawn player ####
    def respawn(self):
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])

    #### Function to move player ####
    def move(self):
        self.forward(MOVE_DISTANCE)

    #### Function when trigger level clear
    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
                self.respawn()
                return True

