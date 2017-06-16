#Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

def array(dx,dy):

    ls = [[None]*dy for i in range(dx)]
    return ls



print(array(2,3))
