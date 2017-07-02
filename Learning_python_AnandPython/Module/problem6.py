#Problem 6: Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.


import urllib
import re

response = urllib.urlopen('http://docs.python.org/tutorial/interpreter.html')

html = response.read()

fil = open('webt.html','w')
for data in html:
    fil.write(data)

fil.close()


fil = open('webt.html','r')
lin = fil.read()
strings = re.findall(r'>[^<]+<', lin)
for i in strings:
   print i[1:-1]


fil.close()

