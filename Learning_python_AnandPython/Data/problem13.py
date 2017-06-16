#Problem 13: Write a function lensort to sort a list of strings based on length.


def lens(arr):
    rl=[]
    i=0
    
    while i<len(arr)-1:
        j=0
        while j<len(arr)-1:
            if len(arr[j])>len(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            j+=1
        i+=1
        
        
    return arr

print(lens(['python','perl','java', 'c', 'haskell', 'ruby']))
