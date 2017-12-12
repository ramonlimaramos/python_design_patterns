# -*- coding=utf-8 -*-

from desconto import Desconto_Cinco_Items, Desconto_Quinhentos_Reais, Sem_Desconto
from orcamento import Orcamento, Item

class Calculador_Desconto(object):
    def execute(self, orcamento):
        cadeia_desconto = Desconto_Cinco_Items(
            Desconto_Quinhentos_Reais(
                Sem_Desconto()
            )
        )
        return cadeia_desconto.calcular(orcamento)

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - A', 100.0))
    orcamento.adiciona_item(Item('Item - B', 50.0))
    orcamento.adiciona_item(Item('Item - C', 400.0))

    print 'Desconto calculado %s' % (Calculador_Desconto().execute(orcamento))