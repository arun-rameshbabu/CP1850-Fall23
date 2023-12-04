# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:01:28 2023

@author: arun.rameshbabu
"""

import sales

def display_title():
    print("SALES DATA IMPORTER\n")


def display_menu():
    print("COMMAND MENU")
    print("view - View all sales")
    print("add  - Add sales")
    print("menu - Show menu")
    print("exit - Exit program")
    print()
    

def get_quarter(month):
    if month >= 1 and month <= 3:
        quarter = 1
    elif month >= 4 and month <= 6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    elif month >= 10 and month <= 12:
        quarter = 4
    else:
        quarter = 0
    
    return quarter


def view_sales(sales_collection):
    if len(sales_collection) == 0:
        print("No sales to view. \n")
    else:
        total_sales = 0
        
        print("\tDate\t\tQuarter\t\tAmount")
        print("-"*40)
        for num, data in enumerate(sales_collection, start=1):
            amount = data[0]
            year = data[1]
            month = data[2]
            day = data[3]
            quarter = data[4]
            total_sales += amount
            
            print(f"{num}.\t{year}-{month}-{day}\t{quarter}\t\t\t${amount}")
        print('-'*40)
        print(f"TOTAL: \t\t\t\t\t\t${total_sales}\n")


def add_sales(sales_collection):
    amount = sales.get_amount()
    year = sales.get_year()
    month = sales.get_month()
    day = sales.get_day(month)
    print()
    
    quarter = get_quarter(month)
    
    sales_data = [amount, year, month, day, quarter]
    sales_collection.append(sales_data)
    
    print(f"Sales for {year}-{month}-{day} added.\n")
    
def main():
    display_title()
    display_menu()
    sales_list = []
    
    while True:
        command = input("Please enter a command: ").lower()
        if command == 'view':
            view_sales(sales_list)
        elif command == 'add':
            add_sales(sales_list)
        elif command == 'menu':
            print()
            display_menu()
        elif command == 'exit':
            print()
            break
        else:
            print("Invalid command. Please try again")
            print()
            display_menu()
    
    print('Bye!')

if __name__ == '__main__':
    main()