#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config, InfoFilter
import os

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # 应用配置
    app.config.from_object(config[config_name])

    # 配置数据库
    db.init_app(app)

    # 配置蓝图
    from app.mall_v1_0.urls import api_1_0
    app.register_blueprint(api_1_0)

    import logging
    from logging.handlers import RotatingFileHandler
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(process)d %(thread)d '
        '%(pathname)s %(lineno)s %(message)s')

    # FileHandler Info
    file_handler_info = RotatingFileHandler(filename=config[config_name].LOG_PATH_INFO)
    file_handler_info.setFormatter(formatter)
    file_handler_info.setLevel(logging.INFO)
    info_filter = InfoFilter()
    file_handler_info.addFilter(info_filter)
    app.logger.addHandler(file_handler_info)

    # FileHandler Error
    file_handler_error = RotatingFileHandler(filename=config[config_name].LOG_PATH_ERROR)
    file_handler_error.setFormatter(formatter)
    file_handler_error.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler_error)

    return app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    kApp = create_app()
    kApp.run(host='0.0.0.0', port=9090)
