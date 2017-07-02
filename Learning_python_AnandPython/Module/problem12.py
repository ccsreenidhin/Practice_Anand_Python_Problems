#Problem 12: Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.

import sys


arg = sys.argv[1]

n = __import__(arg)

print "Description: \n\n"

print n.__doc__

print "Function: \n\n"

for i in dir(arg):
    print i

