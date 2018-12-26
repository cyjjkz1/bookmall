# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_restful import Api
from handlers.book_handler import BookHandler, BookAddImageHandler
from handlers.category_handler import AddCategoryHandler, CategoryList
from handlers.supply_handler import SupplyHandler

api_1_0 = Blueprint('api_1_0', __name__, url_prefix='/bookmall/v1.0')

api = Api(api_1_0)


api.add_resource(BookHandler, '/book/add', endpoint='add_book')
api.add_resource(BookAddImageHandler, '/book/img_add', endpoint='img_add')
api.add_resource(SupplyHandler, '/supply/add', endpoint='supply_add')
api.add_resource(AddCategoryHandler, '/category/add', endpoint='add_category')
api.add_resource(CategoryList, '/category/query', endpoint='category_query')

# api.add_resource(RemoveBook, '/removebook', endpoint='removebook')
# api.add_resource(BookDetail, '/querybook', endpoint='querybook')
# api.add_resource(ManageBook, 'managebook', endpoint='managebook')
# api.add_resource(QueryBook, '/querybook', endpoint='querybook')
# api.add_resource(AddAgeGroup, '/add_age_group', endpoint='addagegroup')
# api.add_resource(AddFunction, '/add_function', endpoint='addfunction')
# api.add_resource(AddSupply, 'addsupply', endpoint='addsupply')
