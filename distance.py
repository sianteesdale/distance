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
    
def compute_minimum_distance(points):
    """
    Compute the minimum distance between several points.
    
    Given a list of points, compute the distance between all pairs of points 
    and return the minimum of these distances.
    """
    result = None
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            distance = compute_distance(points[i], 
                                        points[j])
            if result == None:
                result = distance
            elif distance < result:
                result = distance
    return result

point1 = (0,0)
point2 = (1,1)
print(compute_distance(point1, point2))

point3 = (1,0)
list_of_points = [point1, point2, point3]
print(compute_minimum_distance(list_of_points))
