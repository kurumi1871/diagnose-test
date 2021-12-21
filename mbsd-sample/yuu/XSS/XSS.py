# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
import re

# ブラウザを開く。
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="../login/chromedriver", chrome_options = options)
# Googleの検索TOP画面を開く。
driver.get("http://192.168.56.103/dvwa/login.php")
# 2秒待機
time.sleep(1)
# ユーザーネームを入力
login_id = driver.find_element_by_name("username")
login_id.send_keys("admin")
# パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys("password")
#ログインボタンをクリック
login_btn = driver.find_element_by_name("Login")
login_btn.click()
# 2秒待機
time.sleep(1)

driver.get("http://192.168.56.103/dvwa/vulnerabilities/xss_r/")

# nameを入力
text = driver.find_element_by_name("name")
text.send_keys("<scriot>1<script>")
#text.send_keys("1")

# 2秒待機
time.sleep(1)
#ボタンをクリック
submit_btn = driver.find_element_by_xpath(".//input[@value='Submit']")
submit_btn.click()
time.sleep(1)
dp1 = driver.page_source

time.sleep(2)
#ブラウザを終了
driver.close()

#比較
sqlpattern = re.compile(r'<scriot>1<script>')
if bool(sqlpattern.search(dp1)):
    print('XSS')
else :
    print('検出なし')

#print(bool(sqlpattern.search(dp1)))
