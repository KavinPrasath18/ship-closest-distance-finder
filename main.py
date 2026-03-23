import random
import math
from turtle_plot import Shipmarker
from turtle import *
def random_pos_generate(number_Ships,dim):
    
    """
    Gets The Number of ships for which coords are to be generated in a 2 dimension plane and 
    generates the x,y coords for each ships 

    parameters:
    number_Ships(int) : Number of ships for which the coords are to be generated
    dim(int) : The x and y axis values defining the range of the plane
    
    return:
    ship_Data(Dict): dictionary containing each ship id as a key and its respective position as a value.
    """

    def generate_coords():
        x = random.randint(-dim,dim)
        y = random.randint(-dim,dim)

        return((x,y))

    ship_Data = {}
    ship_Id = 0
    for i in range(number_Ships):
        coords = generate_coords()
        while coords in ship_Data.values():
            coords = generate_coords()
        else:
            ship_Data[ship_Id] = coords
            obj = Shipmarker(coords[0],coords[1])
            obj.marker_coords()
            ship_Id += 1
    return ship_Data
            


def closest_distance_finder(ship_Data):

    """
    gets the ship_Data from the random_pos_generator and uses it to find the closest between each ships with the euclidean distance formula, 
    after which it returns the two ships Id which are close to each other nnmmm 

    parameters:
    ship_Data(dict) : Dictionary containing ship Id along with its respective coordinates in the 2D plane

    return:
    closest_ships(tuple) : The two ships respective Id
    ship_coords(tuple) : the two ships respective Coords
    closest_distance(float) : the distance between the two ships
    """

    data = ship_Data
    print(data)

    closest_distance = float('inf')
    closest_ships,closest_coords = (),()
    dis = 0

    print(ship_Data.keys())
    for i in ship_Data.keys():
        for j in ship_Data.keys():
            if i!=j:
                dis = math.sqrt((ship_Data[i][0] - ship_Data[j][0])**2 + (ship_Data[i][1] - ship_Data[j][1])**2)
                if dis < closest_distance: 
                    closest_distance = dis
                    closest_ships = (i,j)
                    closest_coords = (ship_Data[i],ship_Data[j])


    marker = Shipmarker(closest_coords[0],closest_coords[1])
    print(closest_coords)
    marker.closest_ship_marker(closest_coords[0],closest_coords[1])            

    return closest_ships,closest_coords,closest_distance
            

#print(closest_distance_finder(value))

screen = Screen()
screen.setup(width = 400,height = 400)

number_ships = screen.numinput(title = "Number Of Ships to Be Spawned", prompt = "How Many Ships Do You Want To Generate :")

closest_distance_finder(random_pos_generate(int(number_ships),200))

screen.exitonclick() 