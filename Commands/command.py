#!/usr/bin/env python
# coding=utf-8

from datetime import date
from abc import ABCMeta, abstractmethod

class Order(object):

    def __init__(self, customer, value):
        self.__customer = customer
        self.__value = value
        self.__status = 'NEW'
        self.__date = None

    def checkout(self):
        self.__status = 'PAYED'

    def finish(self):
        self.__data = date.today()
        self.__status = 'DELIVERED'

    @property
    def customer(self):
        return self.__customer

    @property
    def value(self):
        return self.__value

    @property
    def status(self):
        return self.__status

    @property
    def date(self):
        return self.__date

class Command(object):
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

class Finish_Order(Command):
    
    def __init__(self, order):
        self.__order = order

    def execute(self):
        self.__order.finish()

class Checkout_Order(Command):
    
    def __init__(self, order):
        self.__order = order

    def execute(self):
        self.__order.checkout()

class Work_List(object):
    
    def __init__(self):
        self.__commands = []

    def append(self, command):
        self.__commands.append(command)

    def execute(self):
        for command in self.__commands:
            command.execute()


if __name__ == '__main__':

    order_one = Order('Me', 50.0)
    order_two = Order('You', 100.0)

    command_one = Checkout_Order(order_one)
    command_two = Checkout_Order(order_two)
    command_three = Finish_Order(order_one)

    work_list = Work_List()
    work_list.append(command_one)
    work_list.append(command_two)
    work_list.append(command_three)

    work_list.execute()