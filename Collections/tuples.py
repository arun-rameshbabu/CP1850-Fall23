# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:58:58 2023

@author: arun.rameshbabu
"""

# Creating Tuples
# Syntax tuple_name = (item1, item2, item3,....)

hits = (48.0, 30.0, 20.2, 100.0)
fruits = ('Apple', 'Orange', 'Banana', 'Kiwi', 'Grapes')
car = ('Volkswagen', 'Jetta', 2019, 45.65)

# Accessing elements
fruits[3]
car[1]
car[1] = 'Golf'

# Unpacking a tuple
mik, joe, ray, kla = hits

def tuple_example_fn():
    return 'Aru', ['Inst', 'Programmer'], 2023

name, pos, year = tuple_example_fn()
test1 = tuple_example_fn()
test1[1][0] = 'Racer'
test1[1] = 2005
test1[2] = 1023

# Looping a tuple
for fruit in fruits:
    print(fruit)