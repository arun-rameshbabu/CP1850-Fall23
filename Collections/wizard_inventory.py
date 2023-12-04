# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:43:25 2023

@author: arun.rameshbabu
"""

def title():
    print("The Wizard Inventory program\n")
    

def menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


def show(items_list):
    for num, item in enumerate(items_list, start = 1):
        print(f"{num}. {item}")
    print()


def grab_item(items_list):
    if len(items_list) >= 4:
        print("You can't carry any more items. Drop something first.\n")
    else:
        item = input("Name: ")
        items_list.append(item)
        print(f"{item} was added.\n")
        

def edit_item(items_list):
    number = int(input("Number: "))
    if number < 1 or number > len(items_list):
        print("Invalid item number.\n")
    else:
        item = input("Updated name: ")
        items_list[number-1] = item
        print(f"Item number {number} was updated.\n")


def drop_item(items_list):
    number = int(input("Number: "))
    if number < 1 or number > len(items_list):
        print("Invalid item number.\n")
    else:
        item = items_list.pop(number - 1)
        print(f"{item} was dropped.\n")


def main():
    title()
    menu()
    
    my_wizard_inv = ['wooden staff', 'wizard hat', 'cloth shoes']
    
    while True:
        task = input("Command: ")
        if task == 'show':
            show(my_wizard_inv)
        elif task == 'grab':
            grab_item(my_wizard_inv)
        elif task == 'edit':
            edit_item(my_wizard_inv)
        elif task == 'drop':
            drop_item(my_wizard_inv)
        elif task == 'exit':
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == '__main__':
    main()