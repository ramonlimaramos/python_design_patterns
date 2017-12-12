#!/usr/bin/env python
# -*- coding=utf-8 -*-

class ISS(object):
    def calcula(self, orcamento):
        return orcamento * 0.10

class ICMS(object):
    def calcula(self, orcamento):
        return orcamento * 0.20