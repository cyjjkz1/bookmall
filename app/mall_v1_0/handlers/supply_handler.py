# -*- coding:utf-8 -*-
from flask import request
from flask_restful import Resource
from ..models.supply import Supply
from app import db
from ..utils.tools import retJsonData
from flask import current_app as app


class SupplyHandler(Resource):
    def get(self):
        try:
            app.logger.info('params(%s)', request.data)
            query_info = request.json
        except Exception as e:
            app.logger.info('解析参数异常')
            app.logger.exception(e)
        msg = ''
        if not query_info['supply_id']:
            app.logger.info('params: 缺少参数 %s' % 'supply_id')
            msg = '缺少参数' + msg + ' supply_id'
            return retJsonData(repcd='4001', msg=msg)
        sup = Supply.query.filter_by(id=query_info['supply_id']).first()
        if not sup:
            return retJsonData(repcd='1001', msg='没有找到相关供应商')
        else:
            return retJsonData(repcd='0000', msg='请求成功', param=sup.model_to_dict())

    def post(self):
        '''
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String(30), nullable=False)
        mobile = db.Column(db.String(11), nullable=True)
        fast_mail_id = db.Column(db.Integer, nullable=False)
        address = db.Column(db.String(20), nullable=False)
        :param
        :return:
        '''
        try:
            app.logger.info('params(%s)', request.data)
            book_info = request.json
        except Exception as e:
            app.logger.info('没有获取到任何参数')
            app.logger.exception(e)
        msg = ''
        if not book_info['name']:
            app.logger.info('params: 缺少参数 %s' % 'name')
            msg = '缺少参数' + msg + ' name'
        if not book_info['mobile']:
            app.logger.info('params: 缺少参数 %s' % 'mobile')
            msg = msg + ' mobile'
        if not book_info['fast_mail_id']:
            app.logger.info('params: 缺少参数 %s' % 'fast_mail_id')
            msg = msg + ' fast_mail_id'
        if not book_info['address']:
            app.logger.info('params: 缺少参数 %s' % 'address')
            msg = msg + ' address'
        if msg != '':
            retJsonData(repcd='4001', msg=msg)

        sp = Supply(name=book_info['name'],
                    mobile=book_info['mobile'],
                    fast_mail=book_info['fast_mail'],
                    address=book_info['address'])
        db.session.add(sp)
        db.session.flush()
        db.session.commit()
        return retJsonData(repcd='0000', msg='请求成功', param={'id':sp.id})

