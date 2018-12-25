# -*- coding:utf-8 -*-
from flask import jsonify
from flask import current_app as app
import json
def retJsonData(repcd, msg, param={}):
    resp = {
        'repcd': repcd,
        'msg': msg
    }
    resp['data'] = param
    app.logger.info('response (%s)' % json.dumps(resp))
    return jsonify(resp)
