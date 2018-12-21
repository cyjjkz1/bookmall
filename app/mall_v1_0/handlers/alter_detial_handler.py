# -*- coding:utf-8 -*-

from flask_restful import Resource
from flask import jsonify


class AlterDetialHandler(Resource):
    def post(self):
        return jsonify({'a': 'b'})





