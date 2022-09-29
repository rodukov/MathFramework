import math
from typing import Union

class pythagorean_theorem:
    class Meta:
        name = "Pythagorean Theorem"
        package = "pythagorean_theorem"
        description = "takes at least two arguments, you must specify whether it is a cathet or a hypotenuse"
        creator = "Gleb Rodukov<electroneuphoria@gmail.com>"
    def pythagorean_theorem(cathet1: Union[float, int] = None, cathet2: Union[float, int] = None, hypotenuse: Union[float, int] = None) -> float:
        "This function is working Pythagorean Theorem"
        if cathet1 == None:
            return math.sqrt(
                hypotenuse**2 - cathet2**2
            )
        elif cathet2 == None:
            return math.sqrt(
                hypotenuse**2 - cathet1**2
            )
        elif hypotenuse == None:
             return math.sqrt(
                cathet1**2 + cathet2**2
            )
        else:
            return False