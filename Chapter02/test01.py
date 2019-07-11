from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://shotayamane.com/')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.body.h1)
