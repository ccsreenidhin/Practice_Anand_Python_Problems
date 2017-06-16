#Problem 16: Write a function extsort to sort a list of files based on extension.

def extsort(arr):
    rl=[]
    arr.sort()
    print arr
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i].split('.')[1]<arr[j].split('.')[1]) :
                arr[i],arr[j] = arr[j],arr[i]
           
            if arr[i].split('.')[1] == arr[j].split('.')[1] and arr[i].split('.')[0] < arr[j].split('.')[0]:
                    arr[i],arr[j] = arr[j],arr[i]
    return arr


print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
