#Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.


import urllib
import os

f = 'http://docs.python.org/tutorial/interpreter.html'
response = urllib.urlopen(f)
html = response.read()
if f.endswith('/'):
    fname = 'index.html'
else:
    fname = os.path.basename(f)
fil=open(fname+'.html','w')
for data in html:
    fil.write(data)

fil.close()

