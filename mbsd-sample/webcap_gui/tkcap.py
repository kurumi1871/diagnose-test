# -*- coding: utf8 -*-
#pip install beautifulsoup4

import sys
import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen
from bs4 import BeautifulSoup

import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import cv2
import threading
import os
import shutil

main_url = ''

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

def tag_get(site_url):
    if('./' in site_url):
        site_url = site_url.replace('./',main_url)

    TagListBox.delete(0,tk.END)

    html = urlopen(site_url)
    bsObj = BeautifulSoup(html, "html.parser")

    tags = ['html', 'head', 'body', 'title', 'p', 'img', 'a', 'script', 'div', 'form']

    for tag in tags:
        TagListBox.insert(tk.END, tag + " : " + str(len(bsObj.findAll(tag))))

def capture(site_url):
    global driver

    file_name = site_url.replace('http://','').replace('https://','').replace('.','_').replace('/','_') + '.png'

    if('./' in site_url):
        site_url = site_url.replace('./',main_url)

    tag_get(site_url)

    if not (os.path.isfile("./images/" + file_name)):
        # URLを開く
        driver.get(site_url)
        # ウィンドウサイズとズームを設定
        driver.set_window_size(1250, 1036)
        driver.execute_script("document.body.style.zoom='100%'")
        # 読み込み待機時間
        time.sleep(1)
        # imagesフォルダにスクリーンショットを保存
        if not os.path.exists('images'):
            os.mkdir('images')
        driver.save_screenshot("./images/" + file_name)

    img = cv2.imread("./images/" + file_name, 1)
    # 読み込んだ画像の高さと幅を取得
    height = img.shape[0]
    width = img.shape[1]
    resized_img = cv2.resize(img,(int(width * 0.5), int(height * 0.5)))
    cv2.imshow('capture', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ボタンが押されたらリストボックスに、Entryの中身を追加
def addList(site_url):
    url_ListBox.delete(0,tk.END)
    global main_url
    if not (site_url[-1]=='/'):
        site_url += '/'
    main_url = site_url
    urls = getLinks(site_url)
    for url in urls:
        url_ListBox.insert(tk.END, url)

def ListBox_LeftDoubClick(event):
    n = url_ListBox.curselection()
    capture_thread = threading.Thread(target=capture, args=(url_ListBox.get(n),))
    capture_thread.setDaemon(True)
    capture_thread.start()

def Tag_Select():
    n = url_ListBox.curselection()
    tag_get(url_ListBox.get(n))

def on_closing():
    global driver
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        if os.path.exists('images'):
            shutil.rmtree('images/')
        driver.quit()
        root.destroy()

if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')

    # プラウザ起動（Chrome）
    driver = webdriver.Chrome(options=options)

    root = tk.Tk()
    root.title(u'サイト内リンクの検索')

    # ここでウインドウサイズを変更できる
    root.geometry('670x300')
    root.resizable(width=False, height=False)

    # ラベル
    url_label = tk.Label(text=u'対象サイトのURL')
    url_label.place(x=5, y=10)

    #URL入力欄
    EditBox = tk.Entry(width=30)
    EditBox.insert(tk.END,"https://www.metro-cit.ac.jp/")
    EditBox.place(x=10, y=40)

    #検索ボタン
    Button = tk.Button(text=u'検索', width=5, command=lambda: addList(EditBox.get())) 
    Button.place(x=200, y=35)

    # リストボックスを設置してみる
    url_ListBox = tk.Listbox(width=75, height=13)
    # url_ListBox.bind("<<ListboxSelect>>", Tag_Select)
    url_ListBox.bind("<Double-Button-1>", ListBox_LeftDoubClick)
    url_ListBox.place(x=10, y=70)

    #TAG欄
    TagListBox = tk.Listbox(width=30, height=13)
    TagListBox.place(x=470, y=70)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()