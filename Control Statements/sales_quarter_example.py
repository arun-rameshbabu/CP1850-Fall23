# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:13:16 2023

@author: arun.rameshbabu
"""
import sales as s
print("SALES DATA IMPORTER\n")
print("Enter sales data\n")
sales_loop = 'y'
index_print = 1
total_sales = 0
while sales_loop.lower() == 'y':
    #amount = float(input("Amount:\t\t\t"))
    amount = s.get_amount()
    #year = int(input("Year:\t\t\t"))
    year = s.get_year()
    #month = int(input("Month (1-12):\t\t"))
    month = s.get_month()
    #day = int(input("Day (1-31):\t\t"))
    day = s.get_day()
    if month in range(1,4):
        quarter = "Quarter 1"
    elif month in range(4,7):
        quarter = "Quarter 2"
    elif month in range(7, 10):
        quarter = "Quarter 3"
    else:
        quarter = "Quarter 4"
    print("\n{}. \t\t\t\t{}-{}-{}\t\t{}\t\t${:.1f}".format(index_print, year, month, day, quarter, amount))
    total_sales+=amount
    index_print+=1
    sales_loop = input("\nEnter more sales? (y/n): ")

print("\nTotal Sales")
print(20*'-')
print("${:.1f}".format(total_sales))
print("\nBye!")
