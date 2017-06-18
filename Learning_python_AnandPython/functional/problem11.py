#Problem 11: Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.

def square(x):
    return x*x

def vectorize(fun):
    def mapper(li):
        res = []
        for i in li:
            res.append(fun(i))
        return res
    return mapper
    

g = vectorize(square)
print g([2,3,4])
            
