#Problem 10: Implement a function izip that works like itertools.izip.


def myzip(x,y):

    for i in range(len(x)):
            yield  y[i], x[i]




for x, y in myzip(["a", "b", "c"], [1, 2, 3]):
    print x, y

