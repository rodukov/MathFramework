import math

class areas:
    class Meta:
        name = "Areas of Geometric Shapes"
        package = "areas"
        description = "To get full documentation write areas.help()"
        creator = "Gleb Rodukov<electroneuphoria@gmail.com>"
    def help():
        return """
Welcome to MathFramework Areas!
    ├ areas.Meta - information about the package
    ├ areas.square(a) - square area
    ├ areas.rectangle(a, b) - rectangle area
    ├ areas.parallelogram(a, h) - parallelogram area
    ├ areas.trapezium(a, b, h) - trapezium area
    ├ areas.rhombus(d1, d2) - rhombus area
    └ areas.sector(R, a) - sector area
"""
    def square(a):
        return a**2
    def rectangle(a, b):
        return a*b
    def parallelogram(a, h):
        return a*h
    def trapezium(a, b, h):
        return ((a+b)/2)*h
    def rhombus(d1, d2):
        return (d1*d2)/2
    def sector(R, a):
        return ((math.pi*R**2)/360)*a 