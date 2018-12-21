# -*- coding:utf-8 -*-

from flask import Blueprint
from flask_restful import Api
from handlers.add_book_handler import AddBookHandler
from handlers.alter_detial_handler import AlterDetialHandler
from handlers.add_category_handler import AddCategoryHandler


api_1_0 = Blueprint('api_1_0', __name__, url_prefix='/bookmall/v1.0')

api = Api(api_1_0)


api.add_resource(AddBookHandler, '/book/add', endpoint='addbook')
api.add_resource(AlterDetialHandler, '/book/alter', endpoint='modifybook')
api.add_resource(AddCategoryHandler, '/category/add', endpoint='addcategory')


# api.add_resource(RemoveBook, '/removebook', endpoint='removebook')
# api.add_resource(BookDetail, '/querybook', endpoint='querybook')
# api.add_resource(ManageBook, 'managebook', endpoint='managebook')
# api.add_resource(QueryBook, '/querybook', endpoint='querybook')
# api.add_resource(AddAgeGroup, '/add_age_group', endpoint='addagegroup')
# api.add_resource(AddFunction, '/add_function', endpoint='addfunction')
# api.add_resource(AddSupply, 'addsupply', endpoint='addsupply')
