#!/usr/bin/env python
# coding=utf-8

''' OO Invokes '''
from Connection_Factory import Connection_Factory

connection = Connection_Factory().get_connection()
cursor = connection.get_cursor()
query = cursor.execute('SELECT * FROM employees')

for linha in query:
    print linha


''' Functional Invokes '''
from Connection_Factory_Funtional import get_connection

connection = get_connection()
cursor = connection.get_cursor()
query = cursor.execute('SELECT * FROM employees')

for linha in query:
    print linha