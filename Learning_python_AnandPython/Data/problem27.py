#Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.

def triplets(no):
    ls = [(x,y,z) for x in range(1,no) for y in range(1,no) for z in range(1,no) if x+y == z and y>=x]
    return ls 




print(triplets(8))
