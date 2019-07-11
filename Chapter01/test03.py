from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, あるいは他のプランを実行
else:
    # プログラムを継続 (例外の補足でreturnかbreakした際にはesleは不要)
