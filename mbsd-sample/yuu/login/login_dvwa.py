#webページにログイン
import time
from selenium import webdriver

#Chromeドライバの設定
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options = options)

#画面遷移
driver.get('http://192.168.56.103/dvwa/login.php')

#ログインIDを入力
login_id = driver.find_element_by_name("username")
login_id.send_keys('admin')

#パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys('password')

#「ログイン」をクリック
login_tb = driver.find_element_by_name("Login")
login_tb.click()
time.sleep(1)

#ブラウザを閉じる
driver.close()