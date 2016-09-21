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
    redirect_uri = url_for('authorized',  _external=True)
    # More scopes http://developer.github.com/v3/oauth/#scopes
    params = {'redirect_uri': redirect_uri, 'scope': 'user:email'}
    
    return redirect(github.get_authorize_url(**params))


@app.route('/logout', methods=['GET'])
@app.route('/logout.html', methods=['GET'])
def logout():
    RequestUtil.logout(session)
    resp = redirect(url_for('login'))
    resp.set_cookie('sessionID', '', expires=0)
    return resp

@app.route('/github/callback')
def authorized():
    # check to make sure the user authorized the request
    code = RequestUtil.get_parameter(request, 'code', None)
    if not code:
        flash('You did not authorize the request')
        return redirect(url_for('index'))

    # make a request for the access token credentials using code
    redirect_uri = url_for('authorized', _external=True)

    data = dict(code=code,
        redirect_uri=redirect_uri,
        scope='user:email')

    auth = github.get_auth_session(data=data)

    # the "me" response
    me = auth.get('user').json()
    user_id = me['login']
    RequestUtil.login(session, user_id)
    
    # add in to db
    user = User.query.filter_by(id=user_id).first()
    if not user:
        # not exist, insert
        user = User(id=user_id, uid=user_id, name=me['name'], source='github')
    user.last_login=DateUtil.now_datetime()
    # save to db
    user.save()

    flash('Logged in as ' + me['name'])
    return redirect(url_for('index'))
