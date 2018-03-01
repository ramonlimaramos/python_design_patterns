##!/usr/bin/env python
# coding=utf-8


import MSQLdb

class Connection_Factory(object):

    def get_connection(self):
        ''' Returns the connection '''
        return MSQLdb.connect(host='localhost',
            user='root',
            passwd='',
            db='company')