# -*- coding:utf-8 -*-
from flask import request
from flask_restful import Resource
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
        try:
            app.logger.info('params(%s)', request.data)
            cate_info = request.json
        except Exception as e:
            app.logger.info('没有获取到任何参数')
            app.logger.exception(e)

            if not cate_info['cate_type']:
                app.logger.info('params: 缺少参数 %s' % 'cate_type')
                return retJsonData(repcd='4001', msg='缺少参数cate_type')
            if not cate_info['cate_name']:
                app.logger.info('params: 缺少参数 %s' % 'cate_name')
                return retJsonData(repcd='4001', msg='缺少参数cate_name')

            if str(cate_info['cate_type']) == '1':
                if not cate_info['cate_func_id']:
                    return retJsonData(repcd='4001', msg='缺少参数cate_id')
                if cate_info['cate_name']:
                    ag = AgeGroup.query.filter_by(name=cate_info['cate_name']).first()
                    if not ag:
                        app.logger.info('新添加一个ageGroup %s', cate_info['cate_name'])
                        ag = AgeGroup(name=cate_info['cate_name'])
                    else:
                        # 已经添加，直接添加功能分类
                        func = Function.query.filter_by(id=cate_info['cate_func_id']).first()
                        ag.functions.append(func)
                        db.session.commit()
                        return retJsonData(repcd='1001', msg='%s --> 这个年龄段已经添加' % cate_info['cate_name'])

                    func = Function.query.filter_by(id=cate_info['cate_func_id']).first()
                    if func:
                        ag.functions.append(func)
                        db.session.add(ag)
                        db.session.flush()
                        db.session.commit()
                        return retJsonData(repcd='0000', msg='添加成功',param={'age_group_id': ag.id})
                    else:
                        return retJsonData(repcd='2001', msg='没有查找到功能分类,无法添加')
            else:
                # 添加功能分类
                func = Function.query.filter_by(name=cate_info['cate_name']).first()
                if func:
                    return retJsonData('2001', msg='%s --> 功能分类已经存在' % func.name)
                else:
                    app.logger.info('---数据库中没有找到')
                    func = Function(name=cate_info['cate_name'])
                    db.session.add(func)
                    db.session.flush()
                    db.session.commit()
                    return retJsonData('0000', msg='分类添加成功', param={'func_id': func.id})
        except KeyError as e:
            app.logger.exception(e)
        except BaseException as e:
            db.session.rollback()
            app.logger.exception(e)


class CategoryList(Resource):

    '''
    分类查询,
    :type 0 查询所有 1 查询年龄分类 2 查询功能分类
    :key
    '''

    def get(self):
        try:
            app.logger.info('params(%s)', request.args)
            query_info = request.args
            qtype = str(query_info['type'])
            if not qtype:
                return retJsonData(repcd='4001', msg='缺少查询类型参数 type')
            if qtype == '0':
                # 查询所有的年龄分类和所属功能分类
                ags = AgeGroup.query.all()
                app.logger.info('type ags %s' % type(ags))
                agsArr = []
                if (ags is not None) and (len(ags) != 0):
                    for ag in ags:
                        agsArr.append(ag.model_to_dict())

                return retJsonData(repcd='0000', msg='请求成功', param=agsArr)
            elif qtype == '1':
                # 查询所有的年龄分类
                key = query_info['key']
                ags = AgeGroup.query.filter(AgeGroup.name.like("%%" + key + "%%") if key is not None else "").all()
                agsArr = []
                if ags is not None and len(ags) != 0:
                    for ag in ags:
                        agsArr.append(ag.model_to_dict())
                return retJsonData(repcd='0000', msg='请求成功', param=agsArr)
            elif qtype == '2':
                # 查询所有功能分类
                key = query_info['key']
                funcs = Function.query.filter(Function.name.like("%%" + key + "%%") if key is not None else "").all()
                funcArr = []
                if funcs is not None and len(funcs) != 0:
                    for func in funcs:
                        funcArr.append(func.model_to_dict())
                return retJsonData(repcd='0000', msg='请求成功', param=funcArr)
            else:
                pass
        except KeyError as e:
            app.logger.info('解析参数异常')
            app.logger.exception(e)
        except BaseException as e:
            app.logger.exception(e)
