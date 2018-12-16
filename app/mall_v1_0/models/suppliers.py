# -*- coding:utf-8 -*-

from app import db


class Suppliers(db.Model):
    __tablename__ = 'suppliers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    qq = db.Column(db.String(15), nullable=True)
    mobile = db.Column(db.String(11), nullable=True)
    fast_mail_id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(20), nullable=False)

    def __init__(self, name, qq, mobile, fast_mail_id, address):
        self.name = name
        self.qq = qq
        self.mobile = mobile
        self.fast_mail_id = fast_mail_id
        self.address = address


