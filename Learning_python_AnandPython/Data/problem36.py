#Problem 36: Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.


def anag(arr):
    fl = []
    temp = arr
    for i in arr:
        count = 0
        rl = [i]
        for j in temp:
            count = 0
            if i != j and (len(i) == len(j)):
                for k in range(len(i)):
                    if i[k] in j:
                        count+=1
                        #print (j)
                if count == len(j):
                    rl.append(j)
                    temp.remove(j)
                    #print (rl)
        fl+=[rl]               
                    
        


    return fl
              
           
 



print(anag(['eat','ate','done','tea','soap','node']))
