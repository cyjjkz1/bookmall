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
    images = db.relationship('Image', backref='book_id', lazy='dynamic')

    def __init__(self, name, price, postage, details, choicest, has_goods, supply_id, age_group_id, function_id):
        self.name = name
        self.price = price
        self.postage = postage
        self.details = details
        self.choicest = choicest
        self.has_goods = has_goods
        self.supply_id = supply_id
        self.age_group_id = age_group_id
        self.function_id = function_id

    def __repr__(self):
        pass

    def model_to_dict(self):
        book_dict = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'details': self.details,
            'choicest': self.choicest,
            'has_goods': self.has_goods,
            'supply_id': self.supply_id,
            'age_group_id': self.age_group_id,
            'function_id': self.function_id
        }
        imageArr = []
        if (self.images is not None):
            for image in self.images:
                imageArr.append(image.model_to_dict())
        book_dict['image'] = imageArr
        return book_dict


