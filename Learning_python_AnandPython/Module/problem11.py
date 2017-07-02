#Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.


import zipfile

def zipf(n,f,ft):

    zi=zipfile.ZipFile(n, mode = 'w')

    zi.write(f)
    zi.write(ft)

    zi.close()




zipf('zipped','test.txt','a.txt')
