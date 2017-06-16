#Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.


def linewrapimp(f,n):
    fil = open(f)
    lin = fil.readlines()
    fil.close()
    rl = []
    for i in lin:
        j=0
        while j<len(i):
            p=n 
            while p>1:
                if j+p <len(i):
                    if (i[j+p] == ' ') or (i[j+p] == '\n'):
                        rl.append(i[j:j+p])
                        break
                p-=1
            j+=p
                
            
    print ('\n'.join(rl))








linewrapimp('test.txt',30)
