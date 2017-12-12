#!/usr/bin/env python
# -*- coding=utf-8 -*-

from imposto import ISS, ICMS, ICPP, IKCV
from orcamento import Orcamento, Item

class Calculador_Imposto(object):
    def __init__(self, orcamento, imposto):
        self.__calculado = imposto.calcula(orcamento)

    @property
    def imposto_calculado(self):
        return self.__calculado

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - A', 100.0))
    orcamento.adiciona_item(Item('Item - B', 50.0))
    orcamento.adiciona_item(Item('Item - C', 400.0))

    print 'ISS e ICMS'
    iss = Calculador_Imposto(orcamento, ISS())
    icms = Calculador_Imposto(orcamento, ICMS())
    print '%s\n%s' % (iss.imposto_calculado, icms.imposto_calculado)

    print 'ISS com ICMS'
    iss_com_icms = Calculador_Imposto(orcamento, ISS(ICMS()))
    print '%s' % (iss_com_icms.imposto_calculado)


    print 'ICPP e IKCV'
    icpp = Calculador_Imposto(orcamento, ICPP())
    ikcv = Calculador_Imposto(orcamento, IKCV())
    print '%s\n%s' % (icpp.imposto_calculado, ikcv.imposto_calculado)

    print 'ICPP com IKCV'
    icpp_com_ikcv = Calculador_Imposto(orcamento, ICPP(IKCV()))
    print '%s' % (icpp_com_ikcv.imposto_calculado)