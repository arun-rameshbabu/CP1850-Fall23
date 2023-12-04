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
    amount = input("Amount: ")
    return float(amount)


def get_day() -> int:
    """
    Gets a day from the user, converts it to an int value, and returns the int value.

    """
    day = input("Day: ")
    return int(day)


def get_month() -> int:
    """
    Gets a month from the user, converts it to an int value, and returns the int value.
    """
    month = input("Month: ")
    return int(month)


def get_year() -> int:
    """
    Gets a year from the user, converts it to an int value, and returns the int value.

    """
    year = input("Year: ")
    return int(year)
