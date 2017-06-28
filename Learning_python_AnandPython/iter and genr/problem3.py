#Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os

def findfiles(f):
    for root, dirs, files in os.walk(f):
        tab = root.count(os.sep)
        print ' '*tab, os.path.abspath(root)
        for k in files:
            
            print ' '*(tab+3),k

    



findfiles('c:/pycodes')
