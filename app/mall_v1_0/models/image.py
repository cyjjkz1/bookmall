# -*- coding:utf-8 -*-

from app import db


class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __init__(self, name, book_id):
        self.name = name
        self.book_id = book_id

    def model_to_dict(self):
        img_dict = {
            'id': self.id,
            'name': self.name,
        }
        return img_dict

