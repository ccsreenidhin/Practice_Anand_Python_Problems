#Problem 24: Provide an implementation for zip function using list comprehensions.

def zipper(arr, art):
    rl=[(arr[x],art[y]) for x in range(len(arr)) for y in range(len(art)) if x == y ]

    return rl



print(zipper([1,2,3],[4,5,6]))
