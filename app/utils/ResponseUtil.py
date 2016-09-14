#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年2月19日

@author: hzwangzhiwei
'''
from app.utils.JsonUtil import object_2_json


def standard_response(success, data):
    '''
    接口的标准json返回值，统一使用同一个方法，便于统一修改
    '''
    rst = {}
    rst['success'] = success
    rst['data'] = data
    return object_2_json(rst)
