#Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


def factr(i):
    am = 1;
    for x in range(1,i+1):
        am*=x
    return am;

print(factr(5))

print fact(5)
