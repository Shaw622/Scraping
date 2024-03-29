import requests
from bs4 import BeautifulSoup

class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exeptions.RequesrException:
            return None
        return Beautifuloup(req.text, 'html.parser')

class Website:
    """ webサイトの構造についての情報"""
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

def safeGet(self, pageObj, selector):
    childObj = pageObj.select(selector)
    if childObj is not None and len(childObj) > 0:
        return childObj[0].get_text()
    return ""

def search(self, topic, site):
    """
    webサイトでトピックを検索して見つけたページ全てを記録する
    """
    bs = self.getPage(site.searchUrl + topic)
    searchResults = bs.select(site.resultListing)
    for result in searchResults:
        url = result.select(site.resultUrl)[0].attrs["href"]
        # Check to see whether it's relative or an absolute URL
        if(site.absoluteUrl):
            bs = self.getPage(url)
        else:
            bs = self.getPage(site.url + url)
        if bs is None:
            print("Something was wrong with that page or URL. Skipping!")
            return
        title = self.safeGet(bs, site.titleTag)
        body = self.safeGet(bs, site.bodyTag)
        if title != '' and body != '':
            content = Content(topic, title, body, url)
            content.print()

crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
     'https://sseatch.oreilly.com/?q=','article.product-result',
     'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=',
     'div.search-result-content', 'h3.search-result-title a',
     False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
     'http://www.brookings.edu/search/?s=', 'div.list-content article', 'h4.title a', True, 'h1', 'div.post-body']
    ]
sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print("GETTING INFO ABOUT: " + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
        
