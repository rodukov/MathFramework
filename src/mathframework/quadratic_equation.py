import math

def quadratic_equation(a: float = 0, b: float = 0, c: float = 0) -> tuple:
    D = b**2-4*a*c
    if (D >= 0): return (-b+math.sqrt(D))/2*a, (-b-math.sqrt(D))/2*a
    return False