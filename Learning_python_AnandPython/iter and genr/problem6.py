#Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.


import os

def pylin(f):
    li = []

    for path,dirn,filen in os.walk(f):
        for i in filen:
            if '.py' in i:
                count = 0
                fil = open(os.path.join(path,i))
                lin = fil.readlines()
                fil.close()
                for line in lin:
                    if line and line[0] != '#':
                        count+=1   
                    
                temp = [i, count]
                li.append(temp)
                
                
    print li


pylin("c:/anand python")
