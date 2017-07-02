#Problem 3: Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.



import os
import stat



def fdet(f):
    arr = next(os.walk(f))[2]
    li = []
    for i in arr:
        print i+'   ',os.stat(i).st_size,'  ',os.stat(i).st_mtime
        





fdet('c:/anand python/')
