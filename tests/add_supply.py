# coding:utf-8
import json
import requests

url = 'http://192.168.0.218:9090/bookmall/v1.0/supply/add'

headers = {
    'Content-Type': 'application/json',
    'charset': 'utf-8'
}

data = {
    'name': '儿童绘本旗舰店',
    'mobile': '13541134276',
    'fast_mail': '中通快递',
    'address': '深圳市宝钢市君安先南区'
}

resp = requests.post(url=url, headers=headers, data=json.dumps(data))


