# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:01:20 2023

@author: arun.rameshbabu
"""

import pickle

movie_list = [["Monty Python and the Holy Grail", 1975],
              ["On the Waterfront", 1954], 
              ["Cat on a Hot Tin Roof", 1958]]

# Writing a pickle to a file
with open('movies.bin', 'wb') as binary_file:
    pickle.dump(movie_list, binary_file)
    
# Reading from a binary(pickle) file
with open('movies.bin', 'rb') as binary_file:
    new_movie_collection = pickle.load(binary_file)