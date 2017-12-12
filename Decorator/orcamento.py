# -*- coding=utf-8 -*-

class Orcamento(object):
    def __init__(self):
        self.__items = []

    def obter_items(self):
        return tuple(self.__items)

    def adiciona_item(self, item):
        self.__items.append(item)

    @property
    def total_items(self):    
        return len(self.__items)

    @property
    def valor(self):
        total = 0.0
        for item in self.__items:
            total += item.valor
        return total

class Item(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor