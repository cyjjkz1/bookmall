# -*- coding:utf-8 -*-

from app import db

func_age = db.Table('func_age',
                    db.Column('func_id', db.Integer, db.ForeignKey('function.id')),
                    db.Column('age_id', db.Integer, db.ForeignKey('age_group.id'))
                    )


class AgeGroup(db.Model):
    __tablename__ = 'age_group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    books = db.relationship('Book', backref='age_group_i')
    functions = db.relationship('Function',
                                secondary=func_age,
                                backref=db.backref('age_group', lazy='dynamic'),
                                lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Function(db.Model):
    __tablename__ = 'function'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    books = db.relationship('Book', backref='function_i')

    def __init__(self, name):
        self.name = name
