# -*- coding=utf-8 -*-

class Desconto_Cinco_Items(object):

    def __init__(self, proximo):
        self.__proximo = proximo
        
    def calcular(self, orcamento):
        if orcamento.total_items > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo.calcular(orcamento)

class Desconto_Quinhentos_Reais(object):

    def __init__(self, proximo):
        self.__proximo = proximo

    def calcular(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo.calcular(orcamento)

class Sem_Desconto(object):
    def calcular(self, orcamento):
        return 0