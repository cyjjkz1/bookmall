# -*- coding:utf-8 -*-

from flask_restful import Resource
from flask import jsonify


class ChoiceList(Resource):

    def get(self):
        return jsonify({'list': 'list'})