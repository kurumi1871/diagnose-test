#https://yukituna.com/1684/

from urllib.request import urlopen
from bs4 import BeautifulSoup

site_url = "https://www.metro-cit.ac.jp"

html = urlopen(site_url)
bsObj = BeautifulSoup(html, "html.parser")

tags = ['html', 'head', 'body', 'title', 'p', 'img', 'a', 'script', 'div', 'form']

for tag in tags:
    print(tag + " : " + str(len(bsObj.findAll(tag))))

#print(bsObj.findAll('form'))