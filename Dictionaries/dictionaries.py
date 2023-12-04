# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:50:13 2023

@author: arun.rameshbabu
"""
# Creating Dictionaties
countries = {'CA':'Canada', 
             'US':'United States',
             'MX':'Mexico'}

movie = {'name': 'Robocop',
         'year': 1987,
         'price': 9.99}

# Retrieving values for a particular key
country = countries['CA']

country = countries.get('US')
country = countries.get('IN', 'Unknown')

# Updating values for an existing key
countries['CA'] = 'Cameroon'

# Adding to a dict
countries['IN'] = 'India'

# Properties
country_code = 'IN'
if country_code in countries:
    country = countries[country_code]
    print(country)
else:
    print(f"No country for this code {country_code}")
    
# Delete a key value pair
del countries['CA']
del country, country_code

country = countries.pop('US')
movie.clear()

# Accessing keys
countries.keys()

for code in countries.keys():
    print(f'{code}\t\t{countries[code]}')

for haha in countries:
    print(f'{haha}\t\t{countries[haha]}')

# Accessing values
countries.values()

for country in countries.values():
    print(country)
    
# Accessing both the keys and values
countries.items()

for country_code, country in countries.items():
    print(f'{country_code}\t\t{country}')

# Converting keys to a list
list(countries.keys())
list(countries.values())
list(countries.items())

# Converting from a list
countries_list = [['GB','Britain'],
                  ['NL','Netherlands'],
                  ['DE','Germany']]
dict(countries_list)
countries_list2 = [['GB','Britain', 'EU'],
                  ['NL','Netherlands', 'Americas'],
                  ['DE','Germany', 'EU']]
dict(countries_list2)