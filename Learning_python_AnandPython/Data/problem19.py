#Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.


def head(f):
    fil =open(f)
    lin = fil.readlines()
    fil.close()
    for i in lin[:10]:
        print i






def tail(f):
    fil =open(f)
    lin = fil.readlines()
    fil.close()
    for i in lin[:-11:-1]:
        print i
    



head('test.txt')
tail('test.txt')
