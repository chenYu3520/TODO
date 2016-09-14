# -*- coding: utf-8 -*-
'''
Created on 2016年9月14日

@author: hustcc
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


VERSION = '1.0.0'

app = Flask(__name__)
app.secret_key = 'your_session_key_todo'

app.config['u_id'] = 'uid' # login user's session key

DB_FILE_PATH = 'todo.db' # use sqlite

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % DB_FILE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLAlchemyDB = SQLAlchemy(app)


from app import views
from app import db
