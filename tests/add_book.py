# -*- coding:utf-8 -*-
import json
import requests

url = 'http://192.168.0.218:9090/bookmall/v1.0/book/add'

headers = {
    'Content-Type': 'application/json',
    'charset': 'utf-8'
}

data = {
    'name':'大卫的圣诞节',
    'price': 19.8,
    'postage': 1,
    'details': '大卫在圣诞节许愿想要一辆坦克',
    'choicest': 2,
    'has_goods': 1,
    'supply_id': 1,
    'age_group_id': 3,
    'function_id': 5
}
resp = requests.post(url=url, headers=headers, data=json.dumps(data))



