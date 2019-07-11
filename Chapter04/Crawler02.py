import requests
from bs4 import BeautifulSoup

class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exeptions.RequesrException:
            return None
        return Beautifuloup(req.text, 'html.parser')

def safeGet(self, pageObj, selector):
    """
    Beautiful Soupオブジェクトとセレクタからコンテンツ文字列を取得するユーティリティ関数
    セレクタでオブジェクトが見つからないとから文字列を返す
    """
    selectedElems = pageObj.select(selector)
    if selectedElems is not None and len(selectedElems) > 0:
        return '\n'.join([elem.get_text() for elem in selectedElems])
    return ''

def parse(self, site, url):
    """
    ページURLからコンテンツ抽出
    """
    bs = self.getPage(url)
    if bs is not None:
        title = self.safeGet(bs, site.titleTag)
        body = self.safeGet(bs, site.bodyTag)
        if title != '' and body != '':
            content = Content(url, title, body)
            content.print()
