# -*- coding:utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 数据库配置
USERNAME = 'manager_mall'
PASSWORD = 'TianTian1121@@'
HOSTNAME = 'localhost'
DATABASE = 'bookmall'

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass





config={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}



