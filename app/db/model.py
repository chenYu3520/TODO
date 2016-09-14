# -*- coding: utf-8 -*-
'''
Created on 2016年6月15日

@author: hustcc
'''
from sqlalchemy import Column, DateTime, Integer, String

from app import SQLAlchemyDB as db
from app.utils import DateUtil
from sqlalchemy import func


# common method
class BaseMethod(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model, BaseMethod):
    '''用户表'''
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    last_login = db.Column(db.DateTime)

    todos = db.relationship('Todo', backref='user', lazy='dynamic')


class Todo(db.Model, BaseMethod):
    '''用户表'''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1024))
    add_time = db.Column(db.DateTime)
    completed = db.Column(db.Boolean)
    
    user_id = db.Column(db.String(64), db.ForeignKey('user.id'))
