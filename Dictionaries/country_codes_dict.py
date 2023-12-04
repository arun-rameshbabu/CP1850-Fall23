# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 08:35:53 2023

@author: arun.rameshbabu
"""

def menu():
    print("COMMAND MENU")
    print('view - View country name')
    print('add  - Add a country')
    print('del  - Delete a country')
    print('exit - Exit program')
    print()

def view(countries_dict):
    codes = list(countries_dict.keys())
    codes.sort()
    print_string = "Country codes: "
    for x in codes:
        print_string += x + " "
    print(print_string)

def view_name(countries_dict):
    view(countries_dict)
    code = input("Enter country code: ").upper()
    if code in countries_dict:
        country_name = countries_dict[code]
        print(f"Country Name: {country_name}. \n")
    else:
        print("No country with this code exists.\n")

def add_country(countries_dict):
    code = input("Enter country code: ").upper()
    if code in countries_dict:
        country_name = countries_dict[code]
        print(f'{country_name} is using this code.\n')
    else:
        country_name = input("Enter country_name: ").capitalize()
        countries_dict[code] = country_name
        print(f'{country_name} was added.\n')
        
def del_country(countries_dict):
    code = input("Enter country code: ").upper()
    if code in countries_dict:
        country_name = countries_dict.pop(code)
        print(f'{country_name} was deleted.\n')
    else:
        print("There is no country with this code.\n")
        
def main():
    countries = {'CA':'Canada', 'MX':'Mexico', 'US':'United States'}
    menu()
    while True:
        command = input('Command: ').lower()
        if command == 'view':
            view_name(countries)
        elif command == 'add':
            add_country(countries)
        elif command == 'del':
            del_country(countries_dict=countries)
        elif command == 'exit':
            print('Bye!')
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == '__main__':
    main()