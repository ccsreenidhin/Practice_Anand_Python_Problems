#Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.

def parscsv(f):
    fil = open(f)
    lin = fil.readlines()
    fil.close()
    

    rl = [(i.split(',')) for i in lin]

    return rl




print(parscsv('a.csv'))
