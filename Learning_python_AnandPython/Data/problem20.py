#Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

def searchf(fil, string):
    li =[]
    with open(fil) as f:
        lines = f.readlines()
    for line in lines:
        if string in line.split():
            li.append(line)
    return li
        
    

print searchf('test.txt', 'ipsum')
