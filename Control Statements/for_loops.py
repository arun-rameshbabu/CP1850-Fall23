# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:32:02 2023

@author: arun.rameshbabu
"""

# print(*range(10))
# print(*range(5,11))
# print(*range(10, -31, -2))

# for anything in range(1, 16):
#     print(anything)
# print("The for loop has ended")

variable_sum = 0
for number in range(1, 16):
    variable_sum = variable_sum + number

print(variable_sum)