#Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.


def lin4t(fns):
    for f in fns:
        for lin in open(f):
            if len(lin)>40:
                print lin





lin4t(['test.txt','webt.txt'])
