#Problem 37: Write a function valuesort to sort values of a dictionary based on the key.

def sorts(d):
    for i in range(len(d)):
        for j in range(len(d)):
            if (d[i]<d[j]) and (i!=j):
                d[i],d[j] = d[j],d[i]
            
    return d

def sortval(d):
    keys =[i for i in d.keys()]
    #l = sort(keys))
    df = {}
    for k in sort(keys):
        df[k] = d.get(k,0)

    return df
        
    






#print (sorts([2,4,3,6,5,7]))

print (sortval({'x': 1, 'y': 2, 'a': 3}))
