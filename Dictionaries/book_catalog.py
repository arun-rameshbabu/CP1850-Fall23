# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:43:29 2023

@author: arun.rameshbabu
"""

def menu():
    print("COMMAND MENU")
    print('show - Show book info')
    print('add  - Add book')
    print('edit  - Edit book')
    print('del  - Delete book')
    print('exit - Exit program')
    print()

def show(books_dict):
    title = input('Title: ').capitalize()
    if title in books_dict:
        print(f'Title: {title}')
        print(f"Author name: {books_dict[title]['author']}")
        print(f"Publication year: {books_dict[title]['year']}")
    else:
        print(f'Sorry, {title} doesn\'t exist in the catalog.\n')

def add_book(books_dict):
    title = input('Title: ').capitalize()
    author = input('Author name: ').capitalize()
    year = int(input('Publication year: '))
    print()
    books_dict[title] = {'author':author, 'year':year}

def delete_book(books_dict):
    title = input('Title: ').capitalize()
    if title in books_dict:
        books_dict.pop(title)
        print(f'{title} has been deleted.\n')
    else:
        print(f'Sorry, {title} doesn\'t exist in the catalog.\n')

def edit_book(books_dict):
    title = input('Title: ').capitalize()
    if title in books_dict:
        books_dict[title]['author'] = input('Author name: ').capitalize()
        books_dict[title]['year'] = int(input('Publication year: '))
        print(f'{title} has been modified.\n')
    else:
        print(f'Sorry, {title} doesn\'t exist in the catalog.\n')

def main():
    books = {'Python': {'author': 'Arun', 'year': 2023}, 
             'DSP': {'author':'Proakis', 'year': 2020}}
    menu()
    while True:
        command = input('Command: ').lower()
        if command == 'show':
            show(books)
        elif command == 'add':
            add_book(books)
        elif command == 'edit':
            edit_book(books)
        elif command == 'del':
            delete_book(books)
        elif command == 'exit':
            print('Bye!')
            break
        else:
            print("Not a valid command. Please try again.\n")

# if __name__ == '__main__':
#     main()

print(__name__)