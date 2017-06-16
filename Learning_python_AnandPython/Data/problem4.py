#Problem 4: Implement a function product, to compute product of a list of numbers.

def lipro(arr):
    res = 1
    for i in arr:
        res*=i
        
    return res
    
    
print lipro([1,2,3])
