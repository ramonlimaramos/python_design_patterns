#!/usr/bin/env python
# -*- coding=utf-8 -*-

from imposto import ISS, ICMS
from orcamento import Orcamento

class Calculador_Imposto(object):
    def __init__(self, orcamento, imposto):
        self.__imposto_calculado = imposto.calcula(orcamento)

    @property
    def imposto_calculado(self):
        return self.__imposto_calculado

if __name__ == '__main__':
    orcamento = Orcamento(500)
    iss = Calculador_Imposto(orcamento.valor, ISS())
    icms = Calculador_Imposto(orcamento.valor, ICMS())

    print '%s\n%s' % (iss.imposto_calculado, icms.imposto_calculado)