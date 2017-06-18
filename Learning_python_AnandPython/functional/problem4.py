#Problem 4: Write a function treemap to map a function over nested list.

def treemap(fn, lst, result=None):
    if result is None:
        result = []

    for x in lst:
        if isinstance(x, list):
            result.append(treemap(fn, x, None))
        else:
            result.append(fn(x))
    return result




print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
