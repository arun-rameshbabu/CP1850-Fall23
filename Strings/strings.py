# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:35:59 2023

@author: arun.rameshbabu
"""

# Get Ascii Values
ord('A')
ord('a')

# String properties
len('Arun   ')

# String Access methods
string1 = 'This is the CP1850 class'
len(string1)
string1[0]
string1[5]
string1[12]
string1[-1]

string1[:3]
string1[12:18]
string1[12:]

# Multiline strings
query = '''SELECT name, value as CategoryValue 
FROM CategoryTable where name = ?'''

# Check for substring in a string
if('CP185o' in string1):
    print('Yes, substring exists\n')
else:
    print('Substring does not exist')
    
# Looping a string
for char in string1:
    print(char)

# Some basic string functions
# Check if is integer
user_entry = '2345.345'
if (user_entry.isdigit()):
    print("This is a numeric value")
else:
    print('This is not a numeric value')
    
# Check if it begins with a specific substring
string1.startswith('This')
string1.endswith('class')

# Transformations
string1.lower()
string1.upper()
string1.capitalize()
string1[12:18].capitalize()
string1.title()

string2 = '            This is string2'
string2.strip()
string1.replace('CP1850', 'CP4477')
user_entry.replace('.', '').isdigit()
user_entry.isnumeric()

email = 'arun.rameshbabu@cnl.na.ca'
email.removeprefix('arun.rameshbabu')
email.removesuffix('.na.ca')

# Find elements
at_index = email.find('@') 
email.removeprefix(email[:15])

# Splitting Strings
splitted_string = string1.split()
string1.split('is')
dates = '12/3/95'
dates.split('/')
name = 'BMW 330i Turbo'
name.split(' ',1)

# Joining Strings
'|'.join(splitted_string)
' '.join(splitted_string)
' waka waka '.join(splitted_string)

'a'.isupper()
