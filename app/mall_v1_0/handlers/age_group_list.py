# -*- coding:utf-8 -*-

from flask_restful import Resource
from flask import jsonify


class AgeGroupList(Resource):

    def get(self):
        return jsonify({'list': 'list'})