"""Implementing the tac shell command in python."""
"""
Imports sys library so that we can use functions in it
"""
import sys
"""
From lib.helper class imports tac and readfile functions
"""
from lib.helper import tac, readfile
"""
Value None is assigned to the variable TEXT of NoneType
"""
TEXT = None
"""
Number of command line arguments in the list is decremented by 1 and the value is
assigned to ARG_CNT variable
"""
ARG_CNT = len(sys.argv) - 1
"""
sys.stdin.read function reads lines from the console and assignes
them to TEXT variable if ARG_CNT = 0
"""
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
"""
Second argument on the command line is assigned to filename variable,
readfile function takes filename as argument and return value is
assigned to TEXT variable if ARG_CNT = 1
"""
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
"""
Prints name of the current Python script followed by string if ARG_CNT > 1
"""
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")
"""
Calls the tac function with TEXT variable as argument and prints the return value of tac function
"""
print(tac(TEXT))
