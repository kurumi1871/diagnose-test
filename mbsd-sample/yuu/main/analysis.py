# -*- coding: utf8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from urllib.request import urlopen
from bs4 import BeautifulSoup

import cv2
import os
import time

def login(site_url):
    try:
        # ログオンURL
        url = site_url

        # ユーザプロファイルのフォルダ名(実行フォルダに作成されます)
        user_profile = 'UserProfile'
        os.makedirs(user_profile, exist_ok=True)

        # Optionでユーザプロファイルの場所を指定する
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=' + os.getcwd() + '/' + user_profile)

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.use_chromium = True

        driver = webdriver.Chrome(executable_path="/Users/yuu/Documents/GitHub/mbsd-sample-programs/yuu/login/chromedriver", options=options)
        driver.get(url)

        while True:
            ans = input("ログインは完了しましたか（y）>")
            if ans == 'y':
                break

        driver.close()
    except:
        return 'エラーが発生しました'


def capture(site_url):
    try:
        options = Options()
        options.add_argument('--headless')

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.use_chromium = True

        # プラウザ起動（Chrome）
        driver = webdriver.Chrome(executable_path="/Users/yuu/Documents/GitHub/mbsd-sample-programs/yuu/login/chromedriver", options=options)

        file_name = site_url.replace('http://','').replace('https://','').replace('.','_').replace('/','_') + '.png'

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
        cv2.imshow(file_name, resized_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

        driver.quit()

        return "\n#スクリーンショット名\n" + file_name + "\n"
    except:
        return 'エラーが発生しました'

def tag(site_url):
    try:
        html = urlopen(site_url)
        bsObj = BeautifulSoup(html, "html.parser")

        tags = ['html', 'head', 'body', 'title', 'p', 'img', 'a', 'script', 'div', 'form']

        tag_print = "#要素の解析\n"

        for tag in tags:
            tag_print += tag + " : " + str(len(bsObj.findAll(tag))) + "\n"

        return tag_print
    except:
        return 'エラーが発生しました'