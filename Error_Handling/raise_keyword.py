# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:56:36 2023

@author: arun.rameshbabu
"""
import csv
def get_movies(file_name):
    if len(file_name) == 0:
        raise FileNotFoundError ("The filename argument is required.")
    try:
        file_handle = open(file_name, newline="")
        try:
            raise ValueError ("The filename argument is required.")
            movies = []
            csv_read_handle = csv.reader(file_handle)
            for row in csv_read_handle:
                movies.append(row)
            return movies
        except Exception as e:
            print(type(e), e)
        finally:
            file_handle.close()
            print("Inner finally block is executed")
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Outer finally block is executed.")