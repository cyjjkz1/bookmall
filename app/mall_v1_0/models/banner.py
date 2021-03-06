# -*-  coding:utf-8 -*-

from app import db


class Banner(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    validate = db.Column(db.Integer, nullable=False)  # 0 无效 1 有效
    create_time = db.Column(db.Date, nullable=False)

    def __init__(self, title, img_id, validate):
        self.title = title
        self.img_id = img_id
        self.validate = validate



