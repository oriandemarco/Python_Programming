# File: OrianOrderReceiptList.py 
# Project: CSIS2101 Assignment 12
# Author: Orian Demarco 
# History: Version 1.1
# Date: November 26, 2023
# Program: Order Receipt List.
# Grade: 86
# Grade Comment: __init__ function ( constructor ), should take three input parameters 
# for the cost, weight_grams, and detail, but not num_quantity. Not as per specs. 
# For the OrderReceiptsList you are supposed to do only one for loop for print and 
# adding the weights and the amounts. (-14)
import product 

def main():
    invoice_cost = 0.0
    invoice_weight = 0
            # initialize the two variables that will get the total cost and sweight for 
            # all products on the invoice
    product_orian_list = [
        product.Product(1044.99, 2450, "Student Laptop"),
        product.Product(22.49, 25, "USB Keyboard"),
        product.Product(24.99, 35, "USB Mouse"),
        product.Product(49.99, 900, "External Speaker", 2)
    ]       
            # created a list with four instances of product.
            # Price, weight, and detail for each is given and 
            # the external speaker also has the quantity listed 

    print("Here are your shopping cart contents.")
    for products in product_orian_list:
        print(products)
            # iterates over each product in the list and the 
            # print statement uses the str method in Product which 
            # specifies the quantity, detail (product name), and cost
             
    for products in product_orian_list:
        invoice_cost += products.get_invoice_cost()
        invoice_weight += products.get_invoice_weight_in_grams()
            # the two variables in this for loop calculate the total 
            # invoice cost and weight by adding the cost and weight of each product
            # within the products list one at a time and saving it to respective variable.

    print(f"The cost of your invoice is ${invoice_cost:.2f}")
    print(f"The shipping weight is {invoice_weight // 1000} kilograms {invoice_weight % 1000} grams")
            # prints the total invoice cost and shipping weight.
            # the weight is formatted to convert grams to kg and grams 
            # using the integer division and modulo operations  

if __name__ == "__main__":
    main()