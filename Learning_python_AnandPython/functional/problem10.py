#Problem 10: Write a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.

import time


def square(x):
    return x*x
    
def profile(fun):
    def g(x):
        tm = time.time()
        r = fun(x)
        tm = time.time()-tm
        return tm
    return g
    
    
    
f = profile(square)
print f(5)
        
