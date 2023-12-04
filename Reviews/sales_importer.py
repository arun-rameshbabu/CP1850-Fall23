# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:01:28 2023

@author: arun.rameshbabu
"""

import sales
import sales_file_ops as si

def display_title():
    print("SALES DATA IMPORTER\n")


def display_menu():
    print("COMMAND MENU")
    print("view - View all sales")
    print("add  - Add sales")
    print("import - Import Sales from file")
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
        
        print("\tDate\t\tQuarter\t\tRegion\t\tAmount")
        print("-"*60)
        for num, data in enumerate(sales_collection, start=1):
            amount = data['amount']
            year = data['year']
            month = data['month']
            day = data['day']
            quarter = data['quarter']
            region = data['region']
            total_sales += amount
            
            print(f"{num}.\t{year}-{month}-{day}\t{quarter}\t\t\t{region}\t\t${amount}")
        print('-'*60)
        print(f"TOTAL: \t\t\t\t\t\t\t${total_sales}\n")


def add_sales(sales_collection, valid_regions):
    amount = sales.get_amount()
    year = sales.get_year()
    month = sales.get_month()
    day = sales.get_day(month)
    region = sales.get_region(valid_regions)
    print()
    
    quarter = get_quarter(month)
    
    sales_data = {'amount':amount, 'year':year, 'month':month, 
                  'day':day, 'quarter':quarter, 'region':region}
    sales_collection.append(sales_data)
    
    print(f"Sales for {year}-{month}-{day} added.\n")
    
def main():
    display_title()
    display_menu()
    sales_list = si.read_file('all_sales.csv')
    
    vaild_regions = {'w': 'West', 'm':'Mountain', 'c': 'Central', 'e':'East'}
    
    while True:
        command = input("Please enter a command: ").lower()
        if command == 'view':
            view_sales(sales_list)
        elif command == 'add':
            add_sales(sales_list, vaild_regions)
            si.write_file(sales_list)
            #si.write_file_basic(sales_list)
        elif command == 'import':
            filename = input("Enter the name of file to import: ")
            existing_sales_log = si.read_sales_log("sales_log.txt")
            if filename in existing_sales_log:
                print(f'File {filename} has already been imported. \n')
            else:
                new_sales_data = si.read_file(filename)
                for data in new_sales_data:
                    sales_list.append(data)
                si.sales_log("sales_log.txt", filename)
                print("Imported sales added to the list")
                si.write_file(sales_list)                
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