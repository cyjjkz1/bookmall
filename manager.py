#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from app import create_app, db
from flask_script import Manager, Command, Server
from flask_migrate import Migrate, MigrateCommand
from app.mall_v1_0 import models


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

migrate = Migrate(app, db)


class CreateDB(Command):

    def run(self):
        db.create_all()


# 自定义命令
manager.add_command('createdb', CreateDB)
manager.add_command('runserver', Server(host='0.0.0.0', port=9090))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()




