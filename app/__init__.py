# -*- coding: utf-8 -*-
'''
Created on 2016年9月14日

@author: hustcc
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rauth.service import OAuth2Service


VERSION = '1.0.0'

app = Flask(__name__)
app.secret_key = 'your_session_key_todo'

app.config['u_id'] = 'uid' # login user's session key

DB_FILE_PATH = 'todo.db' # use sqlite

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % DB_FILE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLAlchemyDB = SQLAlchemy(app)

# github setting
github = OAuth2Service(
    name='github',
    base_url='https://api.github.com/',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    client_id = '9bcf268e49ef12984560',
    client_secret = '2e76b638daa4ab0430539da84cbe46444414ba78',
)

from app import views
from app import db
