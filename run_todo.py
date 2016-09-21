# -*- coding: utf-8 -*-
'''
Created on 2016年9月14日

@author: hustcc
'''

from app import app


if __name__ == '__main__':
    port = 9966
    DEV_MODE = False
    app.run('0.0.0.0', port, debug=DEV_MODE)
