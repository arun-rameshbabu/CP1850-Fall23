# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:32:18 2023

@author: arun.rameshbabu
"""
try:
    number = int(input("Enter an integer: "))
    print(f"You entered {number}")
except ValueError as ve:
    print("Yon entered an invalid integer. Please try again")
    print(f"{ve}")
print("Bye!")

try:
    number = int(input("Enter an integer: "))
    print(f"You entered {number}")
except:
    print("Yon entered an invalid integer. Please try again")
print("Bye!")