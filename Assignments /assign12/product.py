# File: product.py 
# Project: CSIS2101 Assignment 12
# Author: Orian Demarco 
# History: Version 1.1
# Date: November 26, 2023
# Program: Product class.

class Product:
    def __init__(self, cost, weight_grams, detail, num_quantity=1):
        self.__cost = cost 
        self.__weight_grams = weight_grams
        self.__detail = detail
        self.__num_quantity = num_quantity 
            # initialized the 4 private variables and set quantity to 1 
    def get_cost(self):
        return self.__cost 
    def set_cost(self, cost):
        self.__cost = cost 
            
    def get_weight_grams(self):
        return self.__weight_grams 
    def set_weight_grams(self, weight_grams):
        self.__weight_grams = weight_grams

    def get_detail(self):
        return self.__detail
    def set_detail(self, detail):
        self.__detail = detail

    def get_num_quantity(self):
        return self.__num_quantity  
    def set_num_quantity(self, num_quantity ):
        self.__num_quantity = num_quantity 
            # methods to provide access (get) and modify (set) each variable 
    
    def get_invoice_cost(self):
        return self.__cost * self.__num_quantity 
            # method to calculate the total cost of a product based on the 
            # original price and the quantity of said item  
    def get_invoice_weight_in_grams(self):
        return self.__weight_grams * self.__num_quantity
            # method to calculate the total weight of a product based on the 
            # original weight and the quantity of said item 
    def __str__(self):
        return f"Cost of {self.__num_quantity} {self.__detail} is {self.__cost:.2f} each."
            # method that represents the print statement considering the values of 
            # quantity detail and cost