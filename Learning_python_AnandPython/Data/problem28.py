#Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.


def enum(arr):
    
    ls = [(x,arr[x]) for x in range(len(arr))]

    return ls



print (enum(['a','b','c']))
