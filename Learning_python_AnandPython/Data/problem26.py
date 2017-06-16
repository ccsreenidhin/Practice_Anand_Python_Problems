#Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

def filter(f,val):
    ls = [i for i in val if f(i)]
    return ls


def even(no):
    return no%2 == 0

print(filter(even, range(10)))
