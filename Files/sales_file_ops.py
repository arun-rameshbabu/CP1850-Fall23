# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:47:55 2023

@author: arun.rameshbabu
"""

import csv

def write_file(collection):
    with open("all_sales.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(collection) 


def read_file(file_name):
    sales_data = []
    with open(file_name, newline='') as file_handler:
        reader = csv.reader(file_handler)
        for row in reader:
            #print(f'{row[0]} :-) {row[1]}')
            sales_data.append([float(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])])
    return sales_data

def sales_log(file_name, object_name):
    with open(file_name, 'a') as file:
        file.write(f'{object_name}\n')

def read_sales_log(file_name):
    sales_log = []
    with open(file_name) as file:
        for name in file:
            name = name.replace('\n', "")
            sales_log.append(name)
    return sales_log

# def write_file_basic(collection):
#     with open('test_file.csv', 'w') as file:
#         for obj in collection:
#             file.write(f'{obj[0]},{obj[1]},{obj[2]},{obj[3]},{obj[4]}\n')