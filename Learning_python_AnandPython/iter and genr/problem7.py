Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.



def splitpy(n, f):

    fil =open(f, 'r')
    lines = fil.readlines()
    fil.close()
    nam = 1
    count = 0
    fil = open(str(nam)+'.txt', 'w')
    for i in lines:
        
        if count<n:
            fil.write(i)
            count+=1
        else:
            count = 0
            fil.close()
            nam+=1
            fil = open(str(nam)+'.txt', 'w')
            fil.write(i)
            count+=1
        
    fil.close()
        
                




splitpy(2, 'test.txt')
