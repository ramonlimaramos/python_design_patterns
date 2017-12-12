#!/usr/bin/env python
# -*- coding=utf-8 -*-


from abc import ABCMeta, abstractmethod

class Estado_Orcamento(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.desconto_aplicado = False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento): pass
        
    @abstractmethod
    def aprova(self, orcamento): pass

    @abstractmethod
    def reprova(self, orcamento): pass

    @abstractmethod
    def finaliza(self, orcamento): pass

class Em_Aprovacao(Estado_Orcamento):
    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')
        
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Um orçamento em aprovação não pode ser finalizado')
    
class Aprovado(Estado_Orcamento):
    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')
        
    def aprova(self, orcamento):
        raise Exception('Um orçamento aprovado não pode ser aprovado novamente')

    def reprova(self, orcamento):
        raise Exception('Um orçamento aprovado não pode ser reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()
    
class Reprovado(Estado_Orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Um orçamento reprovado não pode receber desconto')
        
    def aprova(self, orcamento):
        raise Exception('Um orçamento reprovado não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Um orçamento reprovado não pode ser reprovado novamente')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()
    
class Finalizado(Estado_Orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Um orçamento finalizado não pode receber desconto')
        
    def aprova(self, orcamento):
        raise Exception('Um orçamento finalizado não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Um orçamento finalizado não pode ser reprovado')

    def finaliza(self, orcamento):
        raise Exception('Um orçamento finalizado não pode ser finalizado novamente')

class Orcamento(object):
    def __init__(self):
        self.__items = []
        self.estado_atual = Em_Aprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

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
        return total - self.__desconto_extra

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


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - A', 100.0))
    orcamento.adiciona_item(Item('Item - B', 50.0))
    orcamento.adiciona_item(Item('Item - C', 400.0))

    print 'Orçamento sem desconto %s' % (orcamento.valor)
    
    orcamento.aplica_desconto_extra()
    orcamento.aplica_desconto_extra()
    orcamento.aplica_desconto_extra()
    orcamento.aplica_desconto_extra()

    print 'Orçamento com desconto %s' % (orcamento.valor)
    