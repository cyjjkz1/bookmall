# -*-  coding:utf-8 -*-

from app import db

class Banner(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    img_id = db.Column(db.Integer, nullable=False)
    validate = db.Column(db.Integer, nullable=False) # 0 无效 1 有效

    def __init__(self, title, img_id, validate):
        self.title = title;
        self.img_id = img_id
        self.validate = validate


