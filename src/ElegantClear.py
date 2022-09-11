from os import system
from sys import platform

# The Most Elegant Recording in the Whole Earth
clear = lambda: system("cls") if platform in ["win32", "cygwin", "msys"] else system("clear")
clear()