"""
repository for computing the minimal distance between points
"""

import math

def compute_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + 
                     (point1[1] - point2[1]) **2)