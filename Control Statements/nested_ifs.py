# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:43:02 2023

@author: arun.rameshbabu
"""

# instructor = "Happy"
# instructor2 = "Unhappy"


# if (True):
#     if (instructor == "Happy"):
#         print("party in the class")
#         marks = 100
#         grades = 'A'
#     elif (instructor != "Happy"):
#         print ("Day off")
#         marks = None
#         grades = None
# else:
#     print("Dictatorship in class")
#     marks = 20
#     grades = 'F'

print("Program for customer discounts \n\n")
customer_type = input("Enter the customer type (R or W): \t\t")
invoice_total = float(input("Enter the invoice total: \t\t"))
if customer_type.lower() == 'r':
    if invoice_total < 250:
        discount_percent = 0
        invoice_amount = invoice_total - (invoice_total * discount_percent)
    else:
        discount_percent = 0.2
        invoice_amount = invoice_total - (invoice_total * discount_percent)
elif customer_type.lower() == 'w':
    discount_percent = 0.4
    invoice_amount = invoice_total - (invoice_total * discount_percent)
else:
    print("Customer type must be R or W")

print("Amount to be paid: {}".format(invoice_amount))
        