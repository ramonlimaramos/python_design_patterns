#!/usr/bin/env python
# -*- coding=utf-8 -*-
# coding=utf-8

from datetime import date

class Item(object):
    
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_Fiscal(object):
    
    def __init__(self, razao_social, cnpj, itens, data_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        if len(detalhes) <= 20:
            self.__detalhes = detalhes 
        else:
            raise Exception('Detalhes não pode ter mais de 20 caracteres')
        self.__data_emissao = data_emissao

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def itens(self):
        return tuple(self.__itens)

    @property
    def data_emissao(self):
        return self.__data_emissao

    @property
    def detalhes(self):
        return self.__detalhes