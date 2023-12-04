# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:34:38 2023

@author: arun.rameshbabu
"""

print('=' * 60)
print("\t\t\t\t\tBaseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit Program")
print('=' * 60)

choice = True
while(choice):
    choice = int(input("Menu option: "))
    if (choice == 1):
        print("Calculate batting average...")
        at_bats = input("Official number of at bats: ")
        hits = input("Number of hits:")
        batting_avg = int(hits)/int(at_bats)
        print("Batting average: {:.3f} \n".format(batting_avg))
    elif (choice == 2):
        #choice = False
        print("Bye!\n")
        break
    else:
        print("Not a valid option. Please try again.\n")