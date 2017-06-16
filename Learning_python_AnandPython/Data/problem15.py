#Problem 15: Reimplement the unique function implemented in the earlier examples using sets.

def uniqli(arr):
  
    un = list(set(arr))
    return un


print(uniqli([1,2,1]))
