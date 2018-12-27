# -*- coding:utf-8 -*-

from flask_restful import Resource
from flask import request
from ..models import Book
from ..models import Image
from app import db
from ..utils.tools import retJsonData
from flask import current_app as app


class BookHandler(Resource):

    def get(self):
        try:
            app.logger.info('params(%s)', request.args)
            query_info = request.args
        except Exception as e:
            app.logger.info('没有获取到任何参数')
            app.logger.exception(e)
        msg = ''
        if not query_info['book_id']:
            app.logger.info('params: 缺少参数 %s' % 'book_id')
            msg = '缺少参数' + msg + ' book_id'
            return retJsonData(repcd='4001', msg=msg)
        book = Book.query.filter_by(id=query_info['book_id']).first()
        if not book:
            return retJsonData(repcd='1001', msg='没有找到相关供应商')
        else:
            return retJsonData(repcd='0000', msg='请求成功', param=book.model_to_dict())

    def post(self):
        '''
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String(16), nullable=False)
        price = db.Column(db.String(16), nullable=False)
        postage = db.Column(db.Integer, nullable=False)
        details = db.Column(db.String(200), nullable=True)
        choicest = db.Column(db.Integer, default=1)
        has_goods = db.Column(db.Integer, default=1)
        supply_id = db.Column(db.Integer, db.ForeignKey('supply.id'))
        age_group_id = db.Column(db.Integer, db.ForeignKey('age_group.id'))
        function_id = db.Column(db.Integer, db.ForeignKey('function.id'))
        images = db.relationship('Image', backref='book_id', lazy='dynamic')
        :return:
        '''

        try:
            app.logger.info('params(%s)', request.data)
            book_info = request.json

            msg = ''
            if not book_info['name']:
                app.logger.info('params: 缺少参数 %s' % 'name')
                msg = '缺少参数' + msg + ' name'
            if not book_info['price']:
                app.logger.info('params: 缺少参数 %s' % 'price')
                msg = msg + ' price'
            if not book_info['postage']:
                app.logger.info('params: 缺少参数 %s' % 'postage')
                msg = msg + ' postage'
            if not book_info['details']:
                app.logger.info('params: 缺少参数 %s' % 'details')
                msg = msg + ' details'
            if not book_info['choicest']:
                app.logger.info('params: 缺少参数 %s' % 'choicest')
                msg = msg + ' choicest'
            if not book_info['has_goods']:
                app.logger.info('params: 缺少参数 %s' % 'has_goods')
                msg = msg + ' has_goods'
            if not book_info['supply_id']:
                app.logger.info('params: 缺少参数 %s' % 'supply_id')
                msg = msg + ' supply_id'
            if not book_info['age_group_id']:
                app.logger.info('params: 缺少参数 %s' % 'age_group_id')
                msg = msg + ' age_group_id'
            if not book_info['function_id']:
                app.logger.info('params: 缺少参数 %s' % 'function_id')
                msg = msg + ' function_id'
            if msg != '':
                return retJsonData(repcd='4001', msg=msg)

            book = Book(name=book_info['name'],
                        price=book_info['price'],
                        postage=book_info['postage'],
                        details=book_info['details'],
                        choicest=book_info['choicest'],
                        has_goods=book_info['has_goods'],
                        supply_id=book_info['supply_id'],
                        age_group_id=book_info['age_group_id'],
                        function_id=book_info['function_id'])
            db.session.add(book)
            db.session.flush()
            db.session.commit()
            return retJsonData(repcd='0000', msg='请求成功', param={'book_id': book.id})
        except KeyError as e:
            app.logger.info('解析参数异常')
            app.logger.exception(e)
        except BaseException as e:
            db.session.rollback()
            app.logger.exception(e)


class BookAddImageHandler(Resource):
    def post(self):
        try:
            app.logger.info('params(%s)', request.data)
            bk_img = request.json
            msg = ''
            if not bk_img['book_id']:
                app.logger.info('params: 缺少参数 %s' % 'book_id')
                msg = '缺少参数' + msg + ' book_id'
            if not bk_img['img_name']:
                app.logger.info('params: 缺少参数 %s' % 'img_name')
                msg = msg + ' img_name'

            if msg != '':
                return retJsonData(repcd='1001', msg=msg)

            book = Book.query.filter_by(id=bk_img['book_id']).first()
            img = Image(name=bk_img['img_name'])
            book.images = img
            db.session.add(img)
            db.session.add(book)
            db.session.flush()
            db.session.commit()
            return retJsonData(repcd='0000', msg='请求成功', param={'img_id': img.id})
        except KeyError as e:
            app.logger.info('解析参数异常')
            app.logger.exception(e)
        except BaseException as e:
            db.session.rollback()
            app.logger.exception(e)

