#Problem 17: Write a program reverse.py to print lines of a file in reverse order.


def readrev(f):
    fil=open(f)
    lin = fil.readlines()
    fil.close()
    print len(lin)
    for i in lin[::-1]:
        print i
           



#revread('test.txt')
readrev('test.txt')
