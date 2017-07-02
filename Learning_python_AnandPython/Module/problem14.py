#Problem 14: Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML. Try using it to extract all HTML links from a webpage.


from bs4 import BeautifulSoup
with open('index.html') as f:
    html_doc = f.read()
    

soup = BeautifulSoup(html_doc, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))





