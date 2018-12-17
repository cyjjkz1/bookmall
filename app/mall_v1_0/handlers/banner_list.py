# -*- coding:utf-8 -*-

from flask_restful import Resource
from flask import jsonify


class BannerList(Resource):

    def get(self):
        return jsonify({'list': 'list'})

