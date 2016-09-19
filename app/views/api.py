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

from app.db import Todo



def findAll(user_id):
    todos = Todo.query.filter_by(user_id=user_id)
    todos = [todo.dict() for todo in todos]
    return ResponseUtil.standard_response(1, todos)


def save(user_id):
    id = RequestUtil.get_parameter(request, 'id', None)
    title = RequestUtil.get_parameter(request, 'title', None)
    completed = RequestUtil.get_parameter(request, 'completed', None)
    if completed == 'true':
        completed = True
    else:
        completed = False
    if id:
        todo = Todo.query.filter_by(id=id).first()
    else:
        todo = Todo(user_id=user_id, add_time=DateUtil.now_datetime()) # new todo
    
    if todo and todo.user_id == user_id:
        # update it.
        if title:
            todo.title = title
        if completed is not None:
            todo.completed = completed
#         print todo.dict()
        todo.save()
        return ResponseUtil.standard_response(1, todo.dict())
    else:
        return ResponseUtil.standard_response(0, 'save error.')


def remove(user_id):
    id = RequestUtil.get_parameter(request, 'id', None)
    
    if id:
        todo = Todo.query.filter_by(id=id).first()
        if todo:
            todo.delete()
            return ResponseUtil.standard_response(1, 'remove success.')
    return ResponseUtil.standard_response(0, 'remove error.')


def drop(user_id):
    Todo.query.filter_by(user_id=user_id).delete()
    return ResponseUtil.standard_response(1, 'drop success.')


def for_404(user_id):
    ResponseUtil.standard_response(0, '404')


# api request handler
hanlder = {
    'findAll': findAll,
    'save': save,
    'remove': remove,
    'drop': drop
}


@app.route('/api/<api>', methods=['POST', 'GET'])
@login_wrap.login_required('api')
def api(api):
    user_id = RequestUtil.get_login_user(session)
    rst = hanlder.get(api, for_404)(user_id)
    if rst:
        return rst
    return ResponseUtil.standard_response(1, 'test')
