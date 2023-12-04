# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:05:18 2023

@author: arun.rameshbabu
"""

import random

def get_num():
    return random.randrange(1, 50)

def get_tuple(length):
    return tuple([get_num() for i in range(length)])

def get_list(length):
    return [get_num() for i in range(length)]

def get_median(collection):
    length = len(collection)
    if length % 2 == 0:
        indexes = [(length/2)-1, length/2]
    else:
        indexes = [len(collection)//2]
    sorted_collection = sorted(collection)
    median = 0
    for i in indexes:
        median += sorted_collection[int(i)]
    median = median / len(indexes)
    return median


def get_avg(collection):
    return (sum(collection) / len(collection))


def get_min(collection):
    return min(collection)


def get_max(collection):
    return max(collection)


def get_dups(collection):
    dups=[]
    for i in collection:
        count = collection.count(i)
        if (count > 1) and (i not in dups):
            dups.append(i)
    return dups

tuple_1 = get_tuple(11)
print("TUPLE DATA: ",tuple_1)
print("Average = {:.0f} Median = {:.0f} Min = {} Max = {} Dups = {}".format(get_avg(tuple_1), get_median(tuple_1), get_min(tuple_1), get_max(tuple_1), get_dups(tuple_1)))
print()
list_1 = get_list(11)
print("RANDOM DATA: ",list_1)
print("Average = {:.0f} Median = {:.0f} Min = {} Max = {} Dups = {}".format(get_avg(list_1), get_median(list_1), get_min(list_1), get_max(list_1), get_dups(list_1)))
print()
# print(sorted(tuple_1))
# print('Median is: {}'.format(get_median(tuple_1)))