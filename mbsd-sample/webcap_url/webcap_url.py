#https://yukituna.com/1684/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

site_url = "https://www.metro-cit.ac.jp"

def getLinks(articleUrl):
    html = urlopen(site_url)
    bsObj = BeautifulSoup(html, "html.parser")

    urls = [] 

    for link in bsObj.findAll("a"):
        url = link.get('href')
        if( '/' in url ):
            if( 'http://' in url or 'https://' in url ):
                urls.append(url)
            else:
                urls.append(site_url + url)

    temps = []

    for u in sorted(set(urls)):
        if(site_url in u):
            temps.append(u)

    return temps

#URLのドメイン抽出パターン作成
pat = r"https?://(www.)?([\w-]+).[\w.]"

URLS = getLinks("")

for url in URLS :
    print(url)

time.sleep(5)

# プラウザ起動（Chrome）
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("c:/driver/chromedriver.exe",options=options)

# リストからURLをひとつづつ処理
for url in URLS :
    # ドメインの一部をファイル名として設定
    # site_name = re.search(pat,url)
    file_name = "{0}.png".format(url.replace(site_url, '').replace('/', '_').replace('.html', ''))
    # URLを開く
    driver.get(url)
    # ウィンドウサイズとズームを設定
    driver.set_window_size(1250, 1036)
    driver.execute_script("document.body.style.zoom='100%'")
    # 読み込み待機時間
    time.sleep(2)
    # imagesフォルダにスクリーンショットを保存
    driver.save_screenshot("./images/" + file_name)

# プラウザを閉じる
driver.quit()