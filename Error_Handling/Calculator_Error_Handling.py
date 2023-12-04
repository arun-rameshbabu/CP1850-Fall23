# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:28:28 2023

@author: arun.rameshbabu
"""

def title():
    print("The Total Calculator Program \n")

def get_price():
    while True:
        try:
            price = float(input("Enter Price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")
    
def get_quantity():
    while True:
        try:
            quan = int(input("Enter quantity: "))
            return quan
        except ValueError:
            print("Invalid integer. Please try again.") 
            
def main():
    title()
    p = get_price()
    q = get_quantity()
    total = p*q
    print(f"\nPRICE:\t\t\t{p}")
    print(f"QUANTITY:\t\t{q}")
    print(f"TOTAL:\t\t\t{total}")

if __name__ == '__main__':
    main()