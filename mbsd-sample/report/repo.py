from urllib.request import *

url = 'https://yahoo.co.jp/'

# HTTP レスポンスのヘッダ情報を取得
req = Request(url)

with urlopen(req) as res:
    headers = res.headers

    print('[URL]')
    print(res.url)

    print('[パラメータ]')
    parameter=''
    print(parameter)

    print('[脆弱性名]')
    vulnerability = ''
    print(vulnerability)

    print('[リクエスト]')
    print(req.full_url)
    print(req.type)
    print(req.host)
    print(req.origin_req_host)
    print(req.data)
    print(req.get_method())

    print('[レスポンス]')
    print(headers)
    text = res.read().decode('utf-8')
    #print(text)