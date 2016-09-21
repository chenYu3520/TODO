# -*- coding: utf-8 -*-
'''
Created on 2016年9月14日

@author: hustcc
'''

from app import app, github
from app.wraps import login_wrap 
from app.utils import RequestUtil, DateUtil
from werkzeug.utils import redirect

from flask.helpers import flash, url_for
from flask.globals import session, request
import flask

from app.db import User, Todo


@app.route('/', methods=['GET'])
@login_wrap.login_required()
def index():
    user_id = RequestUtil.get_login_user(session)
    user = User.query.filter_by(id=user_id).first()
    if user:
        return flask.render_template('index.html', user_id=user_id)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def login():
    return github.authorize()


@app.route('/logout', methods=['GET'])
@app.route('/logout.html', methods=['GET'])
def logout():
    RequestUtil.logout(session)
    return redirect(url_for('login'))


@github.access_token_getter
def token_getter():
    return session.get('oauth_token', None)


@app.route('/github/callback')
@github.authorized_handler
def authorized(oauth_token):
    next_url = request.args.get('next') or url_for('index')
    if oauth_token is None:
        flash("Authorization failed.")
        return redirect(next_url)
    
    session['oauth_token'] = oauth_token
    
    me = github.get('user')
    user_id = me['login']
    
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        user = User(id=user_id, uid=user_id, name=me['name'], source='github')
        
    user.last_login=DateUtil.now_datetime()
    user.save()
    
    RequestUtil.login(session, user_id)
    
    return redirect(next_url)
