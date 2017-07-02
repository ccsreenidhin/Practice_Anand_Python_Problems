#Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

import os


def extcount(f):
    fr = {}
    arr = next(os.walk(f))[2]
    for i in arr:
        fr[i.split('.')[1]] = fr.get(i.split('.')[1],0) + 1

    for k,v in fr.items():
        print (k,v)
        










extcount('c:/anand python')
