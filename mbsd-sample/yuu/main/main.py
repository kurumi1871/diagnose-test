import analysis
import scanner
import time

try:
    url = input("検査対象のURLを入力>")
    inp = input("入力欄（XPath）>")
    sub = input("送信ボタン（XPath）>")

    while True:
        ans = input("ログインが必要なシステムですか（y/n）>")
        if ans == 'y':
            loginurl = input("loginのURLを入力>")
            name = input("ログイン名を入力>")
            passwd = input("ログインパスワードを入力>")
            print(scanner.login(loginurl,name,passwd))
            time.sleep(1)
            break
        elif ans == 'n':
            break

    print(analysis.capture(url))
    print(analysis.tag(url))

    while True:
        ans = input("SQLインジェクションの脆弱性診断を行いますか（y/n）>")
        if ans == 'y':
            print(scanner.sql(url,inp,sub))
            break
        elif ans == 'n':
            break

    while True:
        ans = input("XSSの脆弱性診断を行いますか（y/n）>")
        if ans == 'y':
            print(scanner.xss(url,inp,sub))
            break
        elif ans == 'n':
            break

except:
    print('\nエラーが発生しました')