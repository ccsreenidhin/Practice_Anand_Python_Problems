#Problem 9: Write a function permute to compute all possible permutations of elements of a given list.


def permute(arr):
    if len(arr) <=1:
        yield arr
    else:
        for p in permute(arr[1:]):
            for i in range(len(arr)):
                yield p[:i] + arr[0:1] + p[i:]


for i in permute([1, 2, 3]):
    print i,
