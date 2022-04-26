from ast import arg
from os import system
import sys

print(sys.argv) # list of argument as string

try:
    arg =  sys.argv.index('print')
    if sys.argv.__len__() > arg:
        print('\nHello World' * int(sys.argv[arg+1]))
except:
    print("command not found!")
