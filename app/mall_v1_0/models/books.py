# -*- coding:utf-8 -*-

from app import db


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False)
    price = db.Column(db.String(16), nullable=False)
    postage = db.Column(db.Integer, nullable=False)
    details = db.Column(db.String(200), nullable=True)
    choicest = db.Column(db.Integer, default=1)
    has_goods = db.Column(db.Integer, default=1)

