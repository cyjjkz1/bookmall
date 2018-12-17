# -*- coding:utf-8 -*-

from app import db


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False)
    price = db.Column(db.String(16), nullable=False)
    postage = db.Column(db.Integer, nullable=False)
    details = db.Column(db.String(200), nullable=True)
    choicest = db.Column(db.Integer, default=1)
    has_goods = db.Column(db.Integer, default=1)
    supply_id = db.Column(db.Integer, db.ForeignKey('supply.id'))
    age_group_id = db.Column(db.Integer, db.ForeignKey('age_group.id'))
    function_id = db.Column(db.Integer, db.ForeignKey('function.id'))
    images = db.relationship('image', backref='image_i')

    def __init__(self, name, price, postage, details, choicest, has_goods, supply_id, age_group_id, function_category_id):
        self.name = name
        self.price = price
        self.postage = postage
        self.details = details
        self.choicest = choicest
        self.has_goods = has_goods
        self.supply_id = supply_id
        self.age_group_id = age_group_id
        self.function_category_id = function_category_id

    def __repr__(self):
        pass




