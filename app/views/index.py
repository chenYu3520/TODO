# -*- coding: utf-8 -*-
'''
Created on 2016年9月14日

@author: hustcc
'''

from app import app
from app.wraps import login_wrap 
from app.utils import RequestUtil, DateUtil
from werkzeug.utils import redirect

from rauth.service import OAuth2Service
from flask.helpers import flash, url_for
from flask.globals import session, request
import flask

from app.db import User, Todo


github = OAuth2Service(
    name='github',
    base_url='https://api.github.com/',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    client_id = '9bcf268e49ef12984560',
    client_secret = '2e76b638daa4ab0430539da84cbe46444414ba78',
)


@app.route('/', methods=['GET'])
@login_wrap.login_required()
def index():
    user_id = RequestUtil.get_login_user(session)
    user = User.query.get(user_id)
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
    return redirect(url_for('login'))

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
    user = User.query.get(user_id)
    if not user:
        # not exist, insert
        user = User(id=user_id, name=me['name'])
    user.last_login=DateUtil.now_datetime()
    # save to db
    user.save()

    flash('Logged in as ' + me['name'])
    return redirect(url_for('index'))
