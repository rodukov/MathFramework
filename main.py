import math
from src.MathFramework import MathFramework
from src.Parabola import Parabola

def do(_input: str, MF_SCRIPT_ITEMS: list = ['var', 'use']):
    _topics = _input.split()
    if _topics[0] in MF_SCRIPT_ITEMS:
        if (_topics[0] == 'var'): globals()[_topics[1]] = _topics[3]
    else:
        _result = eval(_input)
        print(f'{_input.replace("*", "×").replace("/", "÷").replace("-", "−")} is {_result}')

class test:
    def run():
        print('ok')
def main():

    while True:
        _input = input("MathFramework > ")
        try: do(_input)
        except Exception as error: print(error)
        print('--------------')

if ( __name__ == "__main__" ): main()