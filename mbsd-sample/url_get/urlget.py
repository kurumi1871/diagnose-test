#https://yukituna.com/1684/
#urlの変更

from urllib.request import urlopen
from bs4 import BeautifulSoup

site_url = "https://www.google.com"

def getLinks():
    html = urlopen(site_url)
    bsObj = BeautifulSoup(html, "html.parser")

    urls = []

    for link in bsObj.findAll("a"):
        url = link.get('href')
        if( '/' in url ):
            if( 'http://' in url or 'https://' in url ):
                urls.append(url)
            else:
                urls.append('.' + url)

    return set(urls)

urls = getLinks()

for u in urls:
    print(u)