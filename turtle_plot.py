from turtle import *
class Shipmarker:
    
    def __init__(self,x,y):
        self.circle = Turtle(shape = "circle")
        self.x = x  
        self.y = y
        
    def marker_coords(self):

        # The objects are drawn and they are sent to their respective positions
        self.circle.color("red")
        self.circle.penup() 
        self.circle.goto(self.x,self.y)
    
    def closest_ship_marker(self,s1,s2):

        # The Attributes for the line drawn are given 
        self.circle.color("red")
        self.circle.hideturtle()
        self.circle.speed(1)
        self.circle.pensize(6)
        self.circle.shapesize(0.1,0.1,2)


        # The closes objects are drawn on their respective postions
        self.circle.penup()
        self.circle.goto(s1[0],s1[1])
        self.circle.pendown()
        self.circle.goto(s2[0],s2[1])