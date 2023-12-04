# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:53:05 2023

@author: arun.rameshbabu
"""

file_name = input("Enter filename: ")
movies = []
try:
    with open(file_name) as file_handle:
        movies = file_handle.readlines()
except FileNotFoundError:
    print(f"Could not find the file named {file_name}")
except OSError as ose:
    print("File is found. Error reading the file")
    var = type(ose)
    print(f"Type of OS error is {var}")
except Exception:
    print("Unexpected Error Occured")