from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html.read(), 'lxml')


print(bs.h1)
