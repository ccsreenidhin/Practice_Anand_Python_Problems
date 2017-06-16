#Problem 25: Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.


def maplistcom(f,val):
    ls =[f(i) for i in val]

    return ls

def square(no):
    return no**2




print(maplistcom(square, range(5)))
