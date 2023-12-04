# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:35:19 2023

@author: arun.rameshbabu
"""

# The reduce function
import functools

num_list = [1,2,3,4,5,6]

def squared(tot_val, current):
    return tot_val + (current * current)


# List comprehension advanced
import random

def get_num():
    return random.randrange(1, 10)

squares = [(num * num) for n in range(10) if (num := get_num()) <= 6]
