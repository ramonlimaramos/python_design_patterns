#!/usr/bin/env python
# -*- coding=utf-8 -*-

from abc import ABCMeta, abstractproperty

class Template_Imposto_Condicional(object):
    
    __metaclass__ = ABCMeta
    
    def calcula(self, orcamento):
        if self.deve_utilizar_maxima(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractproperty
    def deve_utilizar_maxima(self, orcamento):
        pass

    @abstractproperty
    def maxima_taxacao(self, orcamento):
        pass
    
    @abstractproperty
    def minima_taxacao(self, orcamento):
        pass

class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.10

class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.20

class ICPP(Template_Imposto_Condicional):
    
    def deve_utilizar_maxima(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(Template_Imposto_Condicional):

    def deve_utilizar_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__item_maior_100(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.10

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __item_maior_100(self, orcamento):
        for item in orcamento.obter_items():
            if item.valor > 100:
                return True
        return False