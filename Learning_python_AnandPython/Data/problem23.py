#Problem 23: Write a program center_align.py to center align all lines in the given file.

def centerali(f):
    fil = open(f)
    lin = fil.readlines()
    fil.close()
    max =len(lin[0])
    rl = ' '
    
    for i in lin:
        if len(i)> max:
            max = len(i)

    #print max

    for i in range(len(lin)):
        rl = ' '
        #print len(lin[i])
        if len(lin[i])<max:
            d=(max-len(lin[i]))/2
            #print d
            
            for j in range(d):
                rl += ' '
            #print len(rl)
            lin[i]=rl + lin[i]
            lin[i] = lin[i]+ rl
            
            


    print '\n'.join(lin)
    
centerali('test.txt')
