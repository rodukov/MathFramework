import math
import formatkit
class MathFramework:
    def help(): # ┠ ┗ ┣
        return f"""{formatkit.default}Welcome to MathFramework 1.5.3{formatkit.default}
        ├ distance_between_points(point1, point2) - accept 2 tuple with point coordinate
        └ sector_area(R, a) - [Radius, alpha] find sector area
✔ Use MathFramework.help() to show this message
✔ Use help() to enter python help console
✔ You can use all mathematic expressions like 1+1
✔ You can use added module math, for example math.pi
        """
    def distance_between_points(point1, point2):
        return math.sqrt( (point2[0] - point1[0] )**2 + (point2[1] - point1[1])**2 )
    def sector_area(R, a):
        return ((math.pi*R**2)/360)*a

print(MathFramework.help())