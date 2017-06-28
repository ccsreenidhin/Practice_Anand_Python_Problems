#Problem 9: The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.Write a function my_enumerate that works like enumerate.

def myenum(x):

    li = [(i,x[i]) for i in range(len(x))]
    return li
    


print (list(myenum(["a", "b", "c"])))
for i, c in myenum(["a", "b", "c"]):
    print i, c
