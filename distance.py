"""
File for computing the minimal distance between points
"""

import math

def compute_distance(point1, point2):
    """
    Compute the distance between two points.
    The points should be given as a tuple with x and y co-ordinates.
    The function returns the distance which is computed using Pythagoras.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + 
                     (point1[1] - point2[1]) **2)
    
point1 = (0,0)
point2 = (1,1)
print(compute_distance(point1, point2))

