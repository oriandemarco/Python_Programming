# File: OrianOrderReceipt.py 
# Project: CSIS2101 Assignment 12
# Author: Orian Demarco 
# History: Version 1.1
# Date: November 26, 2023
# Program: Order Receipt.

#This program calculates the total invoice price in dollars for the product.
#And the total invoice weight in Kilograms for shipping.

import product

def main():
    invoice_cost = 0.0
    invoice_weight = 0

    # Put the 4 products being invoiceed in product1 through product 4
    product1 = product.Product(1044.99, 2450, "Student Laptop")
    product2 = product.Product(22.49, 25, "USB Keyboard")
    product3 = product.Product(24.99, 35, "USB Mouse")
    product4 = product.Product(49.99, 900, "External Speaker")
    product4.set_num_quantity(2)

    # Show the details of the invoice using __str__()
    print("Here are your shopping cart contents.")
    print(product1)
    print(product2)
    print(product3)
    print(product4)

    # Compute the invoice cost and invoice weight in this section
    invoice_cost += product1.get_invoice_cost()
    invoice_cost += product2.get_invoice_cost()
    invoice_cost += product3.get_invoice_cost()
    invoice_cost += product4.get_invoice_cost()
    invoice_weight += product1.get_invoice_weight_in_grams()
    invoice_weight += product2.get_invoice_weight_in_grams ()
    invoice_weight += product3.get_invoice_weight_in_grams ()
    invoice_weight += product4.get_invoice_weight_in_grams ()

    # Here we show the invoice details
    print(f"The cost of your invoice is ${invoice_cost:.2f}")
    print(f"The shipping weight is {invoice_weight // 1000} kilograms {invoice_weight % 1000} grams")

    #End of main
if __name__ == "__main__":
    main()