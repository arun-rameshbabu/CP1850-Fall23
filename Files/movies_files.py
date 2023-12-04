# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:42:55 2023

@author: arun.rameshbabu
"""

FILENAME = 'movies.txt'

def write_movies(movies_list):
    with open(FILENAME, 'w') as file:
        for movie in movies_list:
            file.write(f'{movie}\n')

def read_movies():
    movies_list = []
    with open(FILENAME) as file:
        for name in file:
            name = name.replace('\n', "")
            movies_list.append(name)
    return movies_list

with open(FILENAME) as file:
    text = file.read()
    movies_list2 = text.split('\n')

movies_2d = [["Monty Python", 1975],
             ["Cat burning legs", 1958],
             ['Waterfront', 1954]]

import csv

with open("movies.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(movies_2d)    
    
import cards
deck = cards.get_deck()
with open("deck.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(deck)   


with open('movies.csv', newline='') as file_handler:
    reader = csv.reader(file_handler)
    for row in reader:
        print(f'{row[0]} :-) {row[1]}')

with open("movies_delim.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(movies_2d) 