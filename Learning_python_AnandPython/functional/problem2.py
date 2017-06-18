#Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatdict(a, r=None):
    
    if r is None:
        r = {}

    for x in a:
        y = a[x]
        if isinstance(y, dict):
            new={}
            for z in y:
                new[str(x)+'.'+str(z)]=y[z]
                flatdict(new, r)
        else:
           r[x]=y 

    return r



print flatdict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
