#Problem 38: Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.


def invdict(d):
    f = {}
    for k,v in d.items():
        f[v]=k


    return f
    




print(invdict({'x': 1, 'y': 2, 'z': 3}))
