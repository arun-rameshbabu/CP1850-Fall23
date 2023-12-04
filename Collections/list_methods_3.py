# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:17:28 2023

@author: arun.rameshbabu
"""

# Example of deep copy method
list1 = [1,2,3,4,5]
list2 = list1
list2[1] = 4

import copy
cp_list1 = [1,2,3,4,5]
cp_list2 = copy.deepcopy(cp_list1)
cp_list2[1] = 4

list_1 = [1,2,3,4,5]
list_2 = list_1.copy()
list_2[1] = 4

slice_example = [20,21,22,23,24,25,26,27]
slice_example[0:2]
slice_example[:2]
slice_example[4:]
slice_example[0:6:2]
slice_example[::-1]
slice_example[6:2:-1]

concat_example = slice_example + list1

# Map method
def square(n):
    return n*n
squares_list_1 = map(square, list_1)
list(squares_list_1)

# Filter method
def even_number(n):
    return n%2 == 0
evens = filter(even_number, slice_example)
b = list(evens)

a = [x*x for x in list1]
