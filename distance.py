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
    distances = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            distance = compute_distance(points[i], 
                                        points[j])
            distances.append(distance)
    return min(distances)