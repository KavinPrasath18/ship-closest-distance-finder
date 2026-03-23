from turtle import *
class Shipmarker:
    
    def __init__(self,x,y):
        self.circle = Turtle(shape = "circle")
        self.x = x  
        self.y = y
        
    def marker_coords(self):
        self.circle.color("red")
        self.circle.penup() 
        self.circle.goto(self.x,self.y)
    
    def closest_ship_marker(self,s1,s2):


        self.circle.color("black")
        self.circle.pensize(8)
        self.circle.penup()
        self.circle.goto(s1[0],s1[1])
        self.circle.pendown()
        self.circle.goto(s2[0],s2[1])