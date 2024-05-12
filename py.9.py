#wap to calculate distance of too points in python

import math

def calculate_distance(x1, y1, x2, y2):
    # Calculate the difference in x-coordinates and y-coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the square of the differences
    dx_squared = dx ** 2
    dy_squared = dy ** 2

    # Calculate the sum of the squared differences
    sum_of_squares = dx_squared + dy_squared

    # Calculate the distance by taking the square root of the sum of squares
    distance = math.sqrt(sum_of_squares)