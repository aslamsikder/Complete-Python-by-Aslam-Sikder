import random
import sys
import os
class Grocery:
    __name = None
    __quantity = 0
    __price = 0

    # Declaring constructor
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    # Initializing all the setter & getter method for all method
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, quantity):
        self.__quantity = quantity

    def get_name(self):
        return self.__quantity

    def set_name(self, price):
        self.__price = price

    def get_name(self):
        return self.__price

    def get_type(self):
        print("Grocery")

    def total(self, price, quantity):
        return price*quantity

    def toString(self):
        return "The price of {} kg {} is {}".format(self.__quantity, self.__name, self.__price)

total_price = Grocery("oil", 1, 110)
print(total_price.toString())

