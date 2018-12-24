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
        app.logger.info('params(%s)', request.data)
        cate_info = request.get_json()
        if not cate_info['cate_type']:
            app.logger.info('params: 缺少参数 %s' % 'cate_type')
            return retJsonData(repcd='4001', msg='缺少参数cate_type')
        if not cate_info['cate_name']:
            app.logger.info('params: 缺少参数 %s' % 'cate_name')
            return retJsonData(repcd='4001', msg='缺少参数cate_name')
        try:
            if str(cate_info['cate_type']) == '1':
                if cate_info['cate_func_id']:
                    return retJsonData(repcd='4001', msg='缺少参数cate_id')
                if cate_info['cate_name']:
                    ag = AgeGroup.query.filter_by(name=cate_info['cate_name'])
                    if not ag:
                        app.logger.info('新添加一个ageGroup %s', cate_info['cate_name'])
                        ag = AgeGroup(name=cate_info['cate_name'])
                    func = Function.query.filter_by(id=cate_info['cate_func_id'])
                    if func:
                        ag.functions.append(func)
                        db.session.add(ag)
                        db.session.commit()
                        return retJsonData(rcpcd='0000', msg='添加成功',param={'age_group_id': ag.id})
                    else:
                        return retJsonData(repcd='2001', msg='没有查找到功能分类')
            else:
                # 添加功能分类
                func = Function.query.filter_by(name=cate_info['cate_name'])
                if func:
                    return retJsonData('2001', msg='该功能分类已经存在')
                else:
                    func = Function(name=cate_info['cate_name'])
                    db.session.add(func)
                    db.session.commit()
                    return retJsonData('0000', msg='分类添加成功')
        except BaseException as e:
            # db.session.rollback()
            app.logger.exception(e.de)
