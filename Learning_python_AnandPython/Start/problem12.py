#Problem 12: Write a function count_digits to find number of digits in the given number.


def countno(no):
    return len(str(no))


ip = int(raw_input("Enter the no"))

print countno(ip)
