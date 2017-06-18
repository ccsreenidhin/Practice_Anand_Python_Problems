#Problem 8: Write a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.


def count_change(amt, change):
    if amt == 0:
        return 1
    if amt<0 or len(change)==0:
        return 0
    return count_change(amt, change[1:]) + count_change(amt-change[0], change)
        
        
print count_change(10, [1, 2, 5])
