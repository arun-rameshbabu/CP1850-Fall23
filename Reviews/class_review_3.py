# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:40:43 2023

@author: arun.rameshbabu
"""

dict_fr_pickle = {'Wizard':{'Skills': ['Fireball', 'Ice Wall'],
                            'Equipment': ['Cloth Hat', 'Staff'],
                            'Inventory': ['HP Potion', 'MP Potion']},
                  'Rogue':{'Skills': ['Steal', 'Backstab'],
                           'Equipment': ['Leather Hat', 'Dagger'],
                           'Inventory': ['HP Potion', 'Poison']}}

import pickle

with open('Legends_of_CNA.pkl', 'wb') as bfh:
    pickle.dump(dict_fr_pickle, bfh)

with open('Legends_of_CNA.pkl', 'rb') as rbfh:
    checking_dict = pickle.load(rbfh)

# Reviewing Dictionaries
# Creating a dictionary
example_dictionary = {'date':'2020-12-22',
                      'quarter': 4,
                      'region': 'w',
                      'amount': 2500}
# Accessing the objects
example_dictionary['amount']                   

# Updating the objects
example_dictionary['amount'] = 3500

# Creating new keys
regions = {'w':'West', 'e':'East', 'n':'North', 's':'South'}

example_dictionary['region_full_name'] = regions[example_dictionary['region']]

# Nested Dictionaries
example_dictionary2 = {'date':{'year': 2020, 'month':12, 'date':22},
                      'quarter': 4,
                      'region': ['w', 'e'],
                      'amount': 2500}

# Accessing objects in nested dictionaries
example_dictionary2['date']
example_dictionary2['date']['year']

example_dictionary2['region']
example_dictionary2['region'][0]