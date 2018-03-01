#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Estado(object):

    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato

class Historico(object):

    def __init__(self):
        self.__estados_salvos = []

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)