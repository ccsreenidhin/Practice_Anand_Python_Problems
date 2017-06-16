#Problem 33: Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and b are nearly equal when a can be generated by a single mutation on b.

def nearlyeql(w,wc):

    al = 'abcdefghijklmnopqrstuvwxyz'
    alp = [i for i in al]
    rl = ['hello']
    ls = []

    #delete a single char
    for i in range(len(w)):
        temp = [k for k in w]
        temp.remove(temp[i])
        ls.append(''.join(temp))


    #replace a single char
    for i in range(len(w)):
        temp = [k for k in w]
        #print temp
        for j in alp:
            temp[i] = j
            ls.append(''.join(temp))

    #swap two char
    for i in range(len(w)):
        temp = [k for k in w]
        #print temp
        for j in range(len(w)):
            if i != j:
                temp = [k for k in w]
                temp[i],temp[j] = temp[j],temp[i]
                ls.append(''.join(temp))

    #insert a char
    for i in range(len(w)+1):
        temp = [k for k in w]
        #print temp
        for j in alp:
            temp = [k for k in w]
            temp.insert(i,j)
            ls.append(''.join(temp))

            
    #print rl
            
    if wc in ls:
        return True
    else :
        return False



print(nearlyeql('perl','python'))