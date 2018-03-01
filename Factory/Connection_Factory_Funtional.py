##!/usr/bin/env python
# coding=utf-8

import MSQLdb

def get_connection():
    ''' Returns the connection '''
    return MSQLdb.connect(host='localhost',
                            user='root',
                            passwd='',
                            db='company')