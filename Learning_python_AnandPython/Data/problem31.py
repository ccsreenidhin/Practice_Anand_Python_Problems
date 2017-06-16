#Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

def parse(f,a,b):

    fil = open(f)
    lin = fil.readlines()
    fil.close()

    

    rl = [i.split('!') for i in lin if i[0] != '#']
    return rl



print (parse('a.csv', '!', '#'))
