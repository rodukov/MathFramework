import math
import formatkit
from src.ElegantClear import clear as cls

class MathFramework:
    def help(show_logo: bool = False): # ┠ ┗ ┣
        cls()
        if show_logo:
            print("""                   _                                
 |\/|  _. _|_ |_  |_ ._ _. ._ _   _        _  ._ |  
 |  | (_|  |_ | | |  | (_| | | | (/_ \/\/ (_) |  |<
                  terminal mathematic framework
""")
        return f"""{formatkit.default}Welcome to MathFramework 1.5.3{formatkit.default}
        ├ distance_between_points(point1, point2) - accept 2 tuple with point coordinate
        └ sector_area(R, a) - [Radius, alpha] find sector area
✔ Use MathFramework.help() to show this message
✔ Use help() to enter python help console
✔ You can use all mathematic expressions like 1+1
✔ You can use added module math, for example math.pi
✔ You can use your system enviroment, for example sh help
        """
    def distance_between_points(point1, point2):
        return math.sqrt( (point2[0] - point1[0] )**2 + (point2[1] - point1[1])**2 )
    def sector_area(R, a):
        return ((math.pi*R**2)/360)*a


print(MathFramework.help())