# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_restful import Api
from handlers.addbook import AddBook

api_1_0 = Blueprint('api_1_0', __name__, url_prefix='/bookmall/v1.0')

api = Api(api_1_0)

# 后台mis接口
api.add_resource(AddBook, '/addbook', endpoint='addbook')

