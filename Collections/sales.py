# -*- coding: utf-8 -*-
"""
sales Created on Thu Oct  5 09:29:40 2023

This module contains functions for getting 
sales data from a user. @author: arun.rameshbabu
"""

def get_amount() -> float:
    """
    Gets a sales amount from the user, converts it to a float value, and returns the float value. 
    """
    while True:
        amount = float(input("Amount: "))
        if (amount>0):
            return amount
        else:
            print("Amount must be greater than zero \n")


def get_day(month) -> int:
    """
    Gets a day from the user, converts it to an int value, and returns the int value.

    """
    if month == 2:
        max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31
    while True:
        day = int(input(f"Day (1 - {max_days}): "))
        if day >= 1 and day <= max_days:
            return day
        else:
            print(f"Day must be between 1 and {max_days}. \n")

def get_month() -> int:
    """
    Gets a month from the user, converts it to an int value, and returns the int value.
    """
    while True:
        month = int(input("Month (1-12): "))
        if month >= 1 and month <=12:
            return month
        else:
            print("Month should be between 1 and 12. \n")

def get_year() -> int:
    """
    Gets a year from the user, converts it to an int value, and returns the int value.
    Expect the program to be used from 1900 to 3000 years
    """
    while True:
        year = int(input("Year (1900-3000): "))
        if year >= 1900 and year <= 3000:
            return year
        else:
            print("Year must be between 1900 to 3000. \n")

