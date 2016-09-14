# -*- coding: utf-8 -*-
'''
Created on 2015年8月21日

@author: hustcc
'''

from app import app
from flask.globals import session, request


def get_parameter(request, key, default=None):
    '''gain get / post parameter
    '''
    # post
    if request.method == 'POST':
        param = request.form.get(key, default)
    # get
    elif request.method == 'GET':
        param = request.args.get(key, default)
    else:
        return default

    return param


# 当前登陆用户的邮箱帐号（也就是user_id）
def get_login_user(session):
    return session.get(app.config['u_id'], '')


def login(session, user):
    session[app.config['u_id']] = user


def logout(session):
    session.pop(app.config['u_id'])

