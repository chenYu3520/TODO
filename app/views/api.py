# -*- coding: utf-8 -*-
'''
Created on 2016年9月14日

@author: hustcc
'''

from app import app
from app.wraps import login_wrap
from app.utils import RequestUtil, ResponseUtil, DateUtil
from werkzeug.utils import redirect

from flask.helpers import flash, url_for
from flask.globals import session, request
import flask

from app.db import User, Todo



def newTodo():
    
    pass


def itemEditDone():
    
    pass


def itemRemove():
    
    pass


def itemToggle():
    
    pass


# remove all completed todo
def removeCompleted():

    pass


#
def toggleAll():
    
    pass


def for_404():
    ResponseUtil.standard_response(0, '404')


# api request handler
hanlder = {
    'newTodo': newTodo,
    'itemEditDone': itemEditDone,
    'itemRemove': itemRemove,
    'itemToggle': itemToggle,
    'removeCompleted': removeCompleted,
    'toggleAll': toggleAll,
}


@app.route('/api/<api>', methods=['POST', 'GET'])
@login_wrap.login_required('api')
def api(api):
    rst = hanlder.get('api', for_404)()
    if rst:
        return rst
    return ResponseUtil.standard_response(1, 'test')
