# -*- coding:utf-8 -*-

from app import db

func_age = db.Table('func_age',
                    db.Column('func_id', db.Integer, db.ForeignKey('function.id'), primary_key=True),
                    db.Column('age_id', db.Integer, db.ForeignKey('age_group.id'), primary_key=True)
                    )


class AgeGroup(db.Model):
    __tablename__ = 'age_group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    functions = db.relationship('Function',
                                secondary=func_age,
                                backref=db.backref('age_group', lazy='dynamic'),
                                lazy='dynamic')
    
    def __init__(self, name):
        self.name = name

    def model_to_dict(self):
        mt_dict = {
            'id': self.id,
            'name': self.name
        }
        funcArr = [];
        if self.functions is not None and len(self.functions) != 0:
            for func in self.functions:
                funcArr.append(func.model_to_dict())
        mt_dict['functions'] = func
        return mt_dict


class Function(db.Model):
    __tablename__ = 'function'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)

    def __init__(self, name):
        self.name = name

    def model_to_dict(self):
        mt_dict = {
            'id': self.id,
            'name': self.name
        }
        return mt_dict