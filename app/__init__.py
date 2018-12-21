#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.debug = True
    # 应用配置
    app.config.from_object(config[config_name])

    # 配置数据库
    db.init_app(app)

    # 配置蓝图
    from app.mall_v1_0.urls import api_1_0
    app.register_blueprint(api_1_0)

    return app


if __name__ == '__main__':
    kApp = create_app()
    kApp.run(host='0.0.0.0', port=9090)
