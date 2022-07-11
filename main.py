import math
from src.MathFramework import MathFramework as MF


def main():
    while True:
        _input = input("MathFramework > ")
        _result = eval(_input)
        print(f'Result: {_result}')
        print('--------------')

if ( __name__ == "__main__" ): main()