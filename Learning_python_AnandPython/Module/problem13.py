#Problem 13: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.

import tablib


def xlsx(csv, xlsx):
    with open(csv) as c:
        lines = c.readlines()
    
    data = tablib.Dataset()
    for line in lines:
            for i in line.split(','):
                data.append([i.strip('\n\r')])
      
    with open(xlsx, 'wb') as x:
        x.write(data.xls)
        
        

xlsx('a.csv','test.xls')



