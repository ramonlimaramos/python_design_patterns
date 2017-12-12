#!/usr/bin/env python
# -*- coding=utf-8 -*-

def imprime(nota_fiscal):
    print 'Realizando a operação imprime %s' % (nota_fiscal.cnpj)

def salva_no_banco(nota_fiscal):
    print 'Realizando a operação salva no banco %s' % (nota_fiscal.cnpj)

def envia_email(nota_fiscal):
    print 'Realizando a operação envia por email %s' % (nota_fiscal.cnpj)