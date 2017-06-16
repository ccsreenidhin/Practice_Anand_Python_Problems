#Problem 10: Write a function unique to find all the unique elements of a list.

def uniqli(arr):
  
    un = [arr[0]]
    for j in arr:
        if j not in un:
            un.append(j)
    return un


print(uniqli([1,2,1]))
