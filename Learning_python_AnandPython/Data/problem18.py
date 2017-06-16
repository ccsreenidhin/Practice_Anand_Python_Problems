#Problem 18: Write a program to print each line of a file in reverse order.

def readlinre(f):
    
    fil=open(f)
    lin = fil.readlines()
    fil.close()

    for i in lin:
        print ''.join(reversed(i))






readlinre('test.txt')
