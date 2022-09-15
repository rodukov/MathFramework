import math
class distance_between_points:
    def distance_between_points(point1, point2):
        return math.sqrt( (point2[0] - point1[0] )**2 + (point2[1] - point1[1])**2 )