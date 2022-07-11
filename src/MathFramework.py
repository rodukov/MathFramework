import math
class MathFramework:
    def help():
        return """Welcome to MathFramework 1.5.3
        distance_between_points(point1, point2) - accept 2 tuple with point coordinate
        """
    class parabola:
        def table(a,b,c):
            print(f"Created function {a}x²+{b}x+{c} with name parabola{a}{b}{c}")
            # globals()[parabola{a}{b}{c}] = 50
    def distance_between_points(point1, point2):
        return math.sqrt( (point2[0] - point1[0] )**2 + (point2[1] - point1[1])**2 )