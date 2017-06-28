#Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.


import os

def pylin(f):
    li = []

    for path,dirn,filen in os.walk(f):
        for i in filen:
            if '.py' in i:
                fil = open(os.path.join(path,i))
                lin = fil.readlines()
                fil.close()
                temp = [i, len(lin)]
                li.append(temp)
                
                
    print li


pylin("c:/anand python")
