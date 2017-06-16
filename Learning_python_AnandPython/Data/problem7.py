#Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?

def mini(arr):
    for i in range(len(arr)-1):
        for j in arr:
            if arr[i]>j:
                m=j
    return m

  

def maxi(arr):
    for i in range(len(arr)-1):
        for j in arr:
            if arr[i]<j:
                m=j
    return m


print(mini([1,4,6]))
print(maxi([1,4,6]))
print(maxi(['dhd','dsdnsd','dd']))
