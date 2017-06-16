#Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.


def group(arr, z):
    gp = []
    for i in range(0,len(arr),z):
        gp.append(arr[i:i+z])
    
    return gp

    
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
