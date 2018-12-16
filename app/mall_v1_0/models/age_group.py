# -*- coding:utf-8 -*-

from app import db

class AgeGroup(db.Model):
    __tablename__ = 'age_group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)

    def __init__(self, name):
        self.name = name

