#Problem 8: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.


import urllib
import re


def links(a):

    response = urllib.urlopen(a)
    html = response.read()
    
    add = re.findall('http://[\w\d\s\.-]+/', html)
    #add.append(re.findall('^https://', html)

    for i in add:
        print i
    


links('https://in.yahoo.com/')
