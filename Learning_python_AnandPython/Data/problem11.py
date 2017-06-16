#Problem 11: Write a function dups to find all duplicates in the list.


def dup(arr):
    rl=[]
    for i in arr:
        count =0;
        for j in arr[::-1]:
            if i == j:
                count+=1
        if count>1 and (i not in rl):
            
            rl.append(i)

    return rl
        
print (dup([1,2,3,2,4,5,1]))
