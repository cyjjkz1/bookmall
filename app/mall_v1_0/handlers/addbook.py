# -*- coding:utf-8 -*-

from flask_restful import Resource
from flask import jsonify
class AddBook(Resource):
    def get(self):
        return jsonify({'a':'b', 'c':'d'})


