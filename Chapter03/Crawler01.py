from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import ssl # SSLエラー回避
ssl._create_default_https_context = ssl._create_unverified_context

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org/{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 新しいページに出会った
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')
