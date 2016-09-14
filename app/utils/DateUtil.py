# -*- coding: utf-8 -*-
'''
Created on 2015年8月24日

@author: hustcc
'''
import datetime
import time


# now datatime string, can save into mysql
def now_datetime_string():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def now_datetime():
    return datetime.datetime.now()


def now_date_string():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def now_timestamp():
    return time.time()
