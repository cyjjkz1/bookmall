# -*- coding:utf-8 -*-

from app import db


class Supply(db.Model):
    __tablename__ = 'supply'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    mobile = db.Column(db.String(11), nullable=True)
    address = db.Column(db.String(20), nullable=False)
    fast_mail = db.Column(db.String(20), nullable=False)
    books = db.relationship('Book', backref='supplier')

    def __init__(self, name, mobile, fast_mail, address):
        self.name = name
        self.mobile = mobile
        self.fast_mail = fast_mail
        self.address = address

    def model_to_dict(self):
        sup_dict = {
            'id': self.id,
            'name': self.name,
            'mobile': self.mobile,
            'fast_mail': self.fast_mail,
        }
        bookArr = []
        if (self.books is not None):
            for func in self.functions:
                bookArr.append(func.model_to_dict())
        sup_dict['books'] = bookArr
        return sup_dict
