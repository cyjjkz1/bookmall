# -*- coding:utf-8 -*-

from app import db


class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    c_time = db.Column(db.Date, nullable=False)

    def __init__(self, name, book_id,c_time):
        self.name = name
        self.book_id = book_id
        self.c_time = c_time


