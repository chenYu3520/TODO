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

# DB_FILE_PATH = 'todo.db' # use sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % DB_FILE_PATH

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://omtqoikdraegrf:pHxk7z06MOIbd10EDpoHWsX2qX@ec2-54-235-108-156.compute-1.amazonaws.com:5432/d5gvcab8joo79k'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLAlchemyDB = SQLAlchemy(app)


from flask_github import GitHub
app.config['GITHUB_CLIENT_ID'] = '9bcf268e49ef12984560'
app.config['GITHUB_CLIENT_SECRET'] = '2e76b638daa4ab0430539da84cbe46444414ba78'
github = GitHub(app)

from app import views
from app import db
