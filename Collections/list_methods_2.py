# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:11:04 2023

@author: arun.rameshbabu
"""

num_list = [1,5,6,8,9,45,78,45,17,23,65,5,5,5,5,5]

num_list.count(5)

fruits = ['apples', 'apples', 'apples', 'apples', 'orange', 'grapes', 'Kiwi']
fruits.count('apple')

num_list.reverse()
print(num_list)

fruits.reverse()
fruits

num_list.sort()
num_list

fruits.sort()
fruits
fruits.sort(key=str.lower)
fruits
sorted(fruits)
sorted(fruits, key=str.lower)
max(num_list)
min(num_list)
sum(num_list, start=200)
