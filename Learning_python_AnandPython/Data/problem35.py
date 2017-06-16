#Problem 35: Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?


def cfreq(f):
    f = freqc(readc(f))
    return f

def readc(f):
    return open(f).read().split()

def freqc(w):
    fr = {}
    for i in w:
        for j in i:
            fr[j] = fr.get(j,0)+1

    if fr[';'] >(len(w))/4:
        prob = 'could be c program'
    else:
        prob = 'text/python'
    return fr,prob








print(cfreq('test.txt'))



