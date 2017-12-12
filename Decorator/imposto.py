#!/usr/bin/env python
# -*- coding=utf-8 -*-

from abc import ABCMeta, abstractmethod

# Decorator utilizando o pattern OO
class Imposto(object):
    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_outro_imposto(self, orcamento):
        if self.__outro_imposto is not None:
            return self.__outro_imposto.calcula(orcamento)
        else:
            return 0

    @abstractmethod
    def calcula(self, orcamento): pass

# Bult-in Decorator
def IPVX(metodo_ou_funcao):
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50.0
    return wrapper

class Template_Imposto_Condicional(Imposto):
    __metaclass__ = ABCMeta
    
    def calcula(self, orcamento):
        if self.deve_utilizar_maxima(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_utilizar_maxima(self, orcamento): pass

    @abstractmethod
    def maxima_taxacao(self, orcamento): pass
    
    @abstractmethod
    def minima_taxacao(self, orcamento): pass


class ISS(Imposto):
    
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.10 + self.calculo_outro_imposto(orcamento)


class ICMS(Imposto):
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.20 + self.calculo_outro_imposto(orcamento)


class ICPP(Template_Imposto_Condicional):
    
    def deve_utilizar_maxima(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07 + self.calculo_outro_imposto(orcamento)

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05 + self.calculo_outro_imposto(orcamento)


class IKCV(Template_Imposto_Condicional):

    def deve_utilizar_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__item_maior_100(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.10 + self.calculo_outro_imposto(orcamento)

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_outro_imposto(orcamento)

    def __item_maior_100(self, orcamento):
        for item in orcamento.obter_items():
            if item.valor > 100:
                return True
        return False