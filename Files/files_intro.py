# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:42:14 2023

@author: arun.rameshbabu
"""
import cards

output_example_handle = open("first_file.txt", 'w')
output_example_handle.write('This is my first file operation')
output_example_handle.close()


with open("first_file.txt", 'w') as outfile_handle:
    outfile_handle.write("This is the second file operation\n")
    
with open("first_file.txt", 'r') as outfile_handle:
    print(outfile_handle.readline())
    
with open("first_file.txt", 'a') as outfile_handle:
    print(outfile_handle.write('We are doing the files module.\n'))
    
# Reading files
with open("first_file.txt") as file_handle:
    for line in file_handle:
        print(line, end='')
    print()

with open("first_file.txt") as file_handle:
    content = file_handle.read()
    print(content)
    
with open("first_file.txt") as file_handle:
    content_lines = file_handle.readlines()
    print(content_lines[1])
    
deck = cards.get_deck()
with open('cards.txt', 'w') as card_file_handle:
    #card_file_handle.write(str(deck))
    for card in deck:
        card_file_handle.write(str(card[0]) + ' ' + str(card[1]) + ' ' + str(card[2] )+ '\n')
