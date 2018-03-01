#!/usr/bin/env python
# -*- coding=utf-8 -*-


from abc import ABCMeta, abstractmethod

class Expressao(object):
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def avalia(self, expressao_esquerda, expressao_direita):
        pass

class Soma(Expressao):
    
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_direita = expressao_direita
        self.__expressao_esquerda = expressao_esquerda

    def avalia(self):
        return (self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia())

class Subtracao(Expressao):
    
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_direita = expressao_direita
        self.__expressao_esquerda = expressao_esquerda

    def avalia(self):
        return (self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia())

class Numero(Expressao):
    
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

if __name__ == '__main__':
    
    expressao_direita = Subtracao(Numero(20), Numero(10))
    expressao_esquerda = Soma(Numero(5), Numero(5))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    resultado = expressao_conta.avalia()

    print resultado