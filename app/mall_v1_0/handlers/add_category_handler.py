# -*- coding:utf-8 -*-
from flask import request
from flask_restful import Resource
from flask import jsonify
from ..models.category import AgeGroup, Function
from app import db
from ..utils.tools import retJsonData
from flask import current_app as app


# 添加分类，包括年龄分类和功能分类
class AddCategoryHandler(Resource):
    '''
        添加分类
        cate_type 1 为年龄分类 2 为功能分类
        cate_name 分类名字
        cate_func_id 选传
    '''

    def post(self):
        cate_info = request.get_json()
        if not cate_info['cate_type']:
            return retJsonData(repcd='4001', msg='缺少参数cate_type')
        if not cate_info['cate_name']:
            retJsonData(repcd='4001', msg='缺少参数cate_name')
        app.logger.info('------------------------------')
        try:
            if str(cate_info['cate_type']) == '1':
                if cate_info['cate_name']:
                    ag = AgeGroup.query.filter_by(name=cate_info['cate_name'])
                    if not ag:
                        ag = AgeGroup(name=cate_info['cate_name'])
                    func = Function.query.filter_by(id=cate_info['cate_func_id'])
                    if func:
                        ag.functions.append(func)
                    db.session.add(ag)
                    db.session.commit()
            else:
                # 添加功能分类
                func = Function.query.filter_by(name=cate_info['cate_name'])
                app.logger.info('nothing')
                if func:
                    retJsonData('1001', msg='这个分类已经添加')
                else:
                    print 'insert a new'
                    app.logger.info('insert a new')
                    func = Function(name=cate_info['cate_name'])
                    db.session.add(func)
                    db.session.commit()
                    retJsonData('0000', msg='这个分类已经添加')
        except BaseException as e:
            app.logger.exception(e)
            db.session.rollback()

