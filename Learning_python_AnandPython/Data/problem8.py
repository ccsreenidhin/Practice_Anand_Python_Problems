#Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?


def cumus(arr):
    rl = []
    for i in range(1,len(arr)+1):
        if isinstance(arr[0],str):
            s = ''
        else:
            s=0  
        for j in range(i):
            s+=arr[j]
        rl.append(s)
    return rl
  

print (cumus([1,2,3]))
print (cumus(['1','2','3']))
