import math
from src.MathFramework import MathFramework
from src.Parabola import Parabola
from src.quadratic_equation import quadratic_equation
from os import system

def do(_input: str, MF_SCRIPT_ITEMS: list = ['var', 'use', 'run', 'sh']):
    _topics = _input.split()
    if _topics[0] in MF_SCRIPT_ITEMS:
        if (_topics[0] == 'var'): globals()[_topics[1]] = eval(_topics[3])
        if (_topics[0] == 'sh'): system(_topics[1])
        elif (_topics[0] == 'run'): locals()[_topics[1]]()
    else:
        _result = eval(_input)
        print(f'{_input.replace("*", "×").replace("/", "÷").replace("-", "−")} is {_result}')

def main():

    while True:
        _input = input("MathFramework > ")
        try: do(_input)
        except Exception as error: print(error)
        for _ in range(15): print('-', end="")
        else: print('-')

if ( __name__ == "__main__" ): main()