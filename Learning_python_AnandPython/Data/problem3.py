#Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.

def summ(arr):
    if isinstance(arr[1], str):
        am = ''
    else:
        am = 0
    for i in arr:
       am+=i
    return am

        
        
print summ([2,8])    
print summ(['a','b'])    



