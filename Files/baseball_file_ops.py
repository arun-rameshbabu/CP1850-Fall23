# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:50:52 2023

@author: arun.rameshbabu
"""
import csv

def write_file(collection):
    with open("baseball_players.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(collection) 


def read_file():
    player_collection = []
    with open('baseball_players.csv', newline='') as file_handler:
        reader = csv.reader(file_handler)
        for row in reader:
            #print(f'{row[0]} :-) {row[1]}')
            player_collection.append([row[0], row[1], float(row[2]), float(row[3]), float(row[4])])
    return player_collection