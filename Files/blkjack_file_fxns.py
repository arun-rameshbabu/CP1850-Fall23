# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:53:50 2023

@author: arun.rameshbabu
"""

def write_money(amount):
    with open('money.txt', 'w') as aruns_file:
        aruns_file.write(str(amount))


def read_money():
    with open('money.txt') as someones_wallet:
        money = someones_wallet.read()
        return int(money)