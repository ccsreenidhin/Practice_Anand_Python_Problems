#Problem 13: Write a function istrcmp to compare two strings, ignoring the case.


def istrcmp(str1, str2):
    if str1.upper() == str2.upper():
        return True
    else:
        return False
        

print istrcmp('python', 'Python')
print istrcmp('LaTeX', 'Latex')
print istrcmp('a', 'b')
