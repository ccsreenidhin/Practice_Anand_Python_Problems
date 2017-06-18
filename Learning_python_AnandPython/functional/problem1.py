#Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.


def prod(n,t):

    if t>1:
        return n + prod(n,t-1)
    elif (t == 0):
        return 0
    else:
        return n



print prod(6,5)
