# https://techacademy.jp/magazine/28392

# coding:utf-8
from selenium import webdriver
import time
from difflib import SequenceMatcher
import re
import os

def login(loginurl,name,passwd):
    try:
        options = webdriver.ChromeOptions()

        # ユーザプロファイルのフォルダ名(実行フォルダに作成されます)
        user_profile = 'UserProfile'

        options.add_argument('--user-data-dir=' + os.getcwd() + '/' + user_profile)

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.use_chromium = True

        # ブラウザを開く。
        driver = webdriver.Chrome(executable_path="/Users/yuu/Documents/GitHub/mbsd-sample-programs/yuu/login/chromedriver", options=options)

        driver.get(loginurl)
        # 2秒待機
        time.sleep(1)
        # ユーザーネームを入力
        login_id = driver.find_element_by_xpath()
        login_id.send_keys(name)
        # パスワードを入力
        password = driver.find_element_by_name("password")
        password.send_keys(passwd)
        #ログインボタンをクリック
        login_btn = driver.find_element_by_name("Login")
        login_btn.click()
        time.sleep(1)
        driver.close()
        return 'loginを行いました'

    except:
        return 'エラーが発生しました'

def sql(url,inp,sub):
    try:
        options = webdriver.ChromeOptions()

        # ユーザプロファイルのフォルダ名(実行フォルダに作成されます)
        user_profile = 'UserProfile'

        options.add_argument('--user-data-dir=' + os.getcwd() + '/' + user_profile)

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.use_chromium = True

        # ブラウザを開く。
        driver = webdriver.Chrome(executable_path="/Users/yuu/Documents/GitHub/mbsd-sample-programs/yuu/login/chromedriver", options=options)

        driver.get(url)

        # IDを入力
        text = driver.find_element_by_xpath(inp)
        text.send_keys("'")
        # 2秒待機
        time.sleep(1)
        #ボタンをクリック
        submit_btn = driver.find_element_by_xpath(sub)
        submit_btn.click()
        time.sleep(1)
        dp = driver.page_source

        driver.get(url)

        # IDを入力
        text = driver.find_element_by_xpath(inp)
        text.send_keys("1' or 'a'='a")
        # 2秒待機
        time.sleep(1)
        #ボタンをクリック
        submit_btn = driver.find_element_by_xpath(sub)
        submit_btn.click()
        time.sleep(1)
        dp1 = driver.page_source

        driver.get(url)

        # IDを入力
        text = driver.find_element_by_xpath(inp)
        text.send_keys("1")
        # 2秒待機
        time.sleep(1)
        #ボタンをクリック
        submit_btn = driver.find_element_by_xpath(sub)
        submit_btn.click()
        time.sleep(1)
        dp2 = driver.page_source

        # ブラウザを終了する。
        driver.close()

        time.sleep(2)

        #比較
        sqlpattern = re.compile(r'Oracle|Microsoft SQL Server|IBM DB2|MySQL|PostgreSQL|MariaDB')

        if bool(sqlpattern.search(dp)):
            mess = 'SQLインジェクションの危険性があります'
        else :
            mess = '脆弱性は発見されませんでした'

        #s = SequenceMatcher(None, dp1, dp2)
        return(mess)
    except:
        return 'エラーが発生しました'


def xss(url,inp,sub):
    try:
        options = webdriver.ChromeOptions()

        # ユーザプロファイルのフォルダ名(実行フォルダに作成されます)
        user_profile = 'UserProfile'

        options.add_argument('--user-data-dir=' + os.getcwd() + '/' + user_profile)

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.use_chromium = True

        # ブラウザを開く。
        driver = webdriver.Chrome(executable_path="/Users/yuu/Documents/GitHub/mbsd-sample-programs/yuu/login/chromedriver", options=options)

        driver.get(url)

        # IDを入力
        text = driver.find_element_by_xpath(inp)
        text.send_keys("<scriot>1<script>")
        # 2秒待機
        time.sleep(1)
        #ボタンをクリック
        submit_btn = driver.find_element_by_xpath(sub)
        submit_btn.click()
        time.sleep(1)

        dp = driver.page_source

        time.sleep(2)
        #ブラウザを終了
        driver.close()

        #比較
        sqlpattern = re.compile(r'<scriot>1<script>')
        if bool(sqlpattern.search(dp)):
            print('XSSの危険性があります')
    except:
        return 'エラーが発生しました'
