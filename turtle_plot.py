from turtle import *

screen = Screen()
screen.setup(width = 400,height = 400)

number_ships = screen.numinput(title = "Number Of Ships to Be Spawned" prompt = "How Many Ships Do You Want To Generate :")


class Shipmarker:
    
    def __init__(self,x,y):
        self.circle = Turtle(shape = "circle")
        self.x = x
        self.y = y
        
    def marker_coords(self):
        self.circle.color("red")
        self.pos()