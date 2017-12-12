#!/usr/bin/env python
# -*- coding=utf-8 -*-
# coding=utf-8

from nota_fiscal import Nota_Fiscal

class Nota_Fiscal_Builder(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__itens = None
        self.__detalhes = None
        self.__data_emissao = None
    
    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_data_emissao(self, data_emissao):
        self.__data_emissao = data_emissao
        return self

    def com_detalhes(self, detalhes):
        if len(detalhes) <= 20:
            self.__detalhes = detalhes
            return self
        else:
            raise Exception('Detalhes não pode ter mais de 20 caracteres')

    def constroi(self):
        if self.__razao_social is None:
            raise Exception('Razao social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')
        if self.__itens is None:
            raise Exception('Itens deve ser preenchido')

        return Nota_Fiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            itens=self.__itens,
            detalhes=self.__detalhes,
            data_emissao=self.__data_emissao
        )
