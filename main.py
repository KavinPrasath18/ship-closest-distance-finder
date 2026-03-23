import random
import math
from turtle_plot import Shipmarker
from turtle import *

type ship_Dat = dict[int,tuple[int,int]]

def random_pos_generate(number_Ships: int,dim: int) -> ship_Dat:
    
    """
    Gets the number of ships and the dimension of the plane and gives each of the ships its respective random coordinates
    it also plots the ships in its respective coords with the use of turtle module 

    parameters:
    number_Ships(int) : Number of ships for which the coords are to be generated
    dim(int) : The x and y axis values defining the range of the plane
    
    return:
    ship_Data(Dict): dictionary containing each ship id as a key and its respective position as a value.
    """

    def generate_coords():
        x = random.randint(-dim,dim) # random x and y coords for each ships
        y = random.randint(-dim,dim)

        return((x,y))

    ship_Data: ship_Dat = {} # each ship and its respective coords are stored in a dictionary 
    ship_Id = 0
    for i in range(number_Ships):
        coords = generate_coords()
        while coords in ship_Data.values():
            coords = generate_coords()
        else:
            ship_Data[ship_Id] = coords
            obj = Shipmarker(coords[0],coords[1])  # The ships are then plotted through the turtle module with their x and y values
            obj.marker_coords()
            ship_Id += 1

    return ship_Data
            


def closest_distance_finder(ship_Data: ship_Dat):

    """
    gets the ship_Data from the random_pos_generator and uses it to find the closest between each ships with the euclidean distance formula, 
    after which it returns the two ships Id which are close to each other . It also plots the two closest ships with a line connecting them

    parameters:
    ship_Data(dict) : Dictionary containing ship Id along with its respective coordinates in the 2D plane

    return:
    closest_ships(tuple) : The two ships respective Id
    ship_coords(tuple) : the two ships respective Coords
    closest_distance(float) : the distance between the two ships
    """

    closest_distance = float('inf') # Used to set a reference for infinty as default so that the conditions work properly
    closest_ships = (0,0)
    closest_coords: tuple[tuple[int,int],tuple[int,int]] = ((0,0),(0,0))
    dis = 0

    for i in ship_Data.keys():
        for j in ship_Data.keys():
            if i!=j:
                dis = int(math.sqrt((ship_Data[i][0] - ship_Data[j][0])**2 + (ship_Data[i][1] - ship_Data[j][1])**2)) # The distance between each ships are calculated using the euclidean's distance formula
                if dis < closest_distance: 
                    closest_distance = dis
                    closest_ships = (i,j)
                    closest_coords = (ship_Data[i],ship_Data[j])


    marker = Shipmarker(0,0) 
    marker.closest_ship_marker(closest_coords[0],closest_coords[1])            

    return closest_ships,closest_coords,closest_distance
            

#print(closest_distance_finder(value))

screen = Screen() 
screen.setup(width = 600,height = 600) # The size of the screen is defined

number_ships = screen.numinput(title = "Number Of Ships to Be Spawned", prompt = "How Many Ships Do You Want To Generate :") # The Number of ships is obtined from the user through a window

closest_distance_finder(random_pos_generate(int(number_ships),280))  

screen.exitonclick() 