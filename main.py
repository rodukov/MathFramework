import math
from os import system
# MathFramework
from src.MathFramework import MathFramework
# File Explorer
from os import listdir
from os.path import isfile, join

files = [f.replace('.py', '') for f in listdir('src/mathframework') if isfile(join('src/mathframework', f))]
for _import in files:
    im = __import__('src.mathframework.'+_import, globals(), locals(), ['*'], 0) # get imported module and import all
    func = getattr(im, _import) # find executable class
    globals()[_import] = func # save it

def do(_input: str, MF_SCRIPT_ITEMS: list = ['var', 'use', 'run', 'sh']):
    _topics = _input.split()
    if _topics[0] in MF_SCRIPT_ITEMS:
        if (_topics[0] == 'var'): globals()[_topics[1]] = eval(_topics[3]) # create var
        if (_topics[0] == 'sh'): system(_topics[1]) # use bash(system shell)
        elif (_topics[0] == 'run'): locals()[_topics[1]]() # run function
    else: # call eval()
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