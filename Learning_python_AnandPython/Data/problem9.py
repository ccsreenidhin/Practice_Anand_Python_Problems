#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.


def cumupro(arr):
    rl = []
    for i in range(1,len(arr)+1):
        s=1
        for j in range(i):
            s*=arr[j]
        rl.append(s)

    return rl


print(cumupro([1,2,3,4]))
