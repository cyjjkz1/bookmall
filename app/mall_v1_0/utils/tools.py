# -*- coding:utf-8 -*-
from flask import jsonify

def retJsonData(repcd, msg, param={}):
    resp = {
        'repcd': repcd,
        'msg': msg
    }
    resp['data'] = param
    return jsonify(resp)