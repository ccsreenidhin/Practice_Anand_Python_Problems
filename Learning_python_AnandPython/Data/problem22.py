#Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?


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
