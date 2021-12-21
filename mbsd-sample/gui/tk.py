# -*- coding: utf8 -*-
#pip install beautifulsoup4

import sys
import tkinter as tk
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getLinks(site_url):
    html = urlopen(site_url)
    bsObj = BeautifulSoup(html, "html.parser")

    urls = []

    for link in bsObj.findAll("a"):
        url = link.get('href')
        if( '/' in url ):
            if( 'http://' in url or 'https://' in url ):
                urls.append(url)
            else:
                urls.append("." + url)

    temps = []

    for u in sorted(set(urls)):
        temps.append(u)

    return temps

root = tk.Tk()
root.title(u'サイト内リンクの検索')

# ここでウインドウサイズを変更できる
root.geometry('500x300')
root.resizable(width=False, height=False)

# ボタンが押されたらリストボックスに、Entryの中身を追加
def addList(site_url):
    url_ListBox.delete(0,tk.END)
    urls = getLinks(site_url)
    for url in urls:
        url_ListBox.insert(tk.END, url)

# ラベル
url_label = tk.Label(text=u'対象サイトのURL')
url_label.place(x=5, y=10)

#URL入力欄
EditBox = tk.Entry(width=30)
EditBox.place(x=10, y=40)

#検索ボタン
Button = tk.Button(text=u'検索', width=5, command=lambda: addList(EditBox.get())) 
Button.place(x=200, y=35)

# リストボックスを設置してみる
url_ListBox = tk.Listbox(width=75, height=13)
url_ListBox.place(x=10, y=70)

root.mainloop()