#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Orcamento(object):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor