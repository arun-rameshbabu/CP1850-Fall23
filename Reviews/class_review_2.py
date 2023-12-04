# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:31:16 2023

@author: arun.rameshbabu
"""

d2_array = [['Arun Rameshbabu', 'jsdf7Tg2b'],
            ['Brad Jones', 'adafa7fVd32'],
            ['Casey Kim', 'afafTFdbh675']]

import csv

with open('passwords.csv', 'w', newline='') as rfh:
    csv_fh = csv.writer(rfh)
    csv_fh.writerows(d2_array)

with open('passwords2.csv', 'w') as rfh2:
    for row in d2_array:
        string_to_write = row[0]+ ','+ row[1]+ '\n'
        rfh2.write(string_to_write)
        
with open('passwords.csv', 'r', newline='') as rfh:
    csv_fh = csv.reader(rfh)
    structure = []
    for row in csv_fh:
        structure.append(row)

with open('passwords.csv') as rfh2:
    lines = rfh2.readlines()
    structure2 = []
    for line in lines:
        row = line.replace('\n', '').split(',')
        structure2.append(row)

     
