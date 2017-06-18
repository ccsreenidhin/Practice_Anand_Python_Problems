#Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.



def tree_reverse(lst, result=None):
    if result is None:
        result = []

    for x in lst:
        if isinstance(x, list):
            result.insert(0, tree_reverse(x, None))
        else:
            result.insert(0, x)

    return result


print tree_reverse([[1, 2], [3, [4, 5]], 6])
