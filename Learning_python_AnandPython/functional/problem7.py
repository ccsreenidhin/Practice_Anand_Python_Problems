#Problem 7: Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.



import os

def dirtree(f):

    for root, dirs, files in os.walk(f):
        tab = root.count(os.sep)
        print ' '*tab, os.path.basename(root)
        for k in files:
            
            print ' '*(tab+3),k




dirtree('c:/pycodes')
