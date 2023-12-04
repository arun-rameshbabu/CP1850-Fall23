# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:09:40 2023

@author: arun.rameshbabu
"""

# def print_welcome():
#     print("Welcome to your first function!")
#     print('\n')
#     print("Done with the function")

# print_welcome()

# def print_welcome(message):
#     print(message)
#     print('\n')
#     print("Done with the function")

# some_var = 'I am so sleepy'
# print_welcome(some_var)

def calc_mpg(miles_driven, gallons_fuel):
    """
    

    Parameters
    ----------
    miles_driven : TYPE
        DESCRIPTION.
    gallons_fuel : TYPE
        DESCRIPTION.

    Returns
    -------
    mpg : TYPE
        DESCRIPTION.

    """
    mpg = miles_driven/gallons_fuel
    return mpg

miles_driven = 500
fuel = 14
calculated_mpg = calc_mpg(400, fuel)
print(calculated_mpg)
print(calc_mpg(100, 10))
