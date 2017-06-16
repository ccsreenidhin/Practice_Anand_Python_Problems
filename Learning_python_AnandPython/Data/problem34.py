#Problem 34: Improve the above program to print the words in the descending order of the number of occurrences.


def main(f):
    freq = wfreq(rfreq(f))
    pl = [[word,count] for word, count in freq.items()]
    pl = order(pl)
    for i in range(len(pl)):
        print (pl[i][0], pl[i][1])


def rfreq(f):
    return open(f).read().split()

def wfreq(w):
    freq ={}
    for j in w:
        freq[j] = freq.get(j,0)+1
    return freq


def order(pl):
    
    for i in range(len(pl)):
        for j in range(len(pl)):
            if pl[i][1] > pl[j][1]:
                pl[i][1], pl[j][1] = pl[j][1], pl[i][1]
    return pl
    
            
                
    

print (main('test.txt'))
