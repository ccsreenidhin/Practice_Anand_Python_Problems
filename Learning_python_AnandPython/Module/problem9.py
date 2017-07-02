#Problem 9: Write a regular expression to validate a phone number.


import re

def valfon(f):
    
    no = re.findall('\d{1,10}', f)
    #print len(no[0])
    
    if len(no[0]) == 10:
        return 'your no',no[0],'is valid'
    else:
        return 'invalid'




print(valfon('9874563215'))
