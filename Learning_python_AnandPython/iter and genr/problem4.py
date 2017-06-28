#Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.


import os

def pyext(f):
    count =0
    for path,dirn,filen in os.walk(f):
        for i in filen:
            if '.py' in i:
                count +=1
    print count



    
pyext("c:/anand python")
