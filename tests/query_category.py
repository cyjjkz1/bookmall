# -*- coding:utf-8 -*-
import json
import requests

url = 'http://192.168.0.218:9090/bookmall/v1.0/category/query?type=1&key=~'
headers = {
    'Content-Type': 'application/json',
    'charset': 'utf-8'
}

res = requests.get(url=url, headers=headers)

