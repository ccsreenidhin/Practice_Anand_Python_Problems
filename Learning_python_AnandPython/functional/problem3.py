#Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.


def unflatd(a, r=None):
    if r is None:
        r = {}
        new = {}
    for x in a:
        y=a[x]
        if '.' in x:
            new[x.split('.')[1]] = y
            r[x.split('.')[0]] =new
        else:
            r[x] = y
        
    return r    
    
    



print unflatd({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
