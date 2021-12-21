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

print("\n")
login_page = driver.page_source
line = re.findall(r'input type="text" .* name=.*',login_page)
#element = re.findall(r'name=".*"',line)
print("name:")
print(line)

elementa = re.findall(r'input type="password" .* name=.*',login_page)
print("password:")
print(elementa)

time.sleep(1)
driver.close()