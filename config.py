# -*- coding:utf-8 -*-

import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))

# 数据库配置
USERNAME = 'manager_mall'
PASSWORD = 'TianTian1121@@'
HOSTNAME = 'localhost'
DATABASE = 'bookmall'


class InfoFilter(logging.Filter):
    def filter(self, record):
        '''
        only use INFO
        筛选，只需要INFO级别的log
        :param record:
        :return:
        '''
        if logging.INFO <= record.levelno < logging.ERROR:
            return super(InfoFilter,self).filter(record)
        else:
            return 0


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

    LOG_PATH = os.path.join(basedir, 'logs')
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024

    # 轮转数量是10个
    LOG_FILE_BACKUP_COUNT = 10


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}



