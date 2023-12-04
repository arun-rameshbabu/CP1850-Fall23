# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:07:48 2023

@author: arun.rameshbabu
"""

def command_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()


def list_movies(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print("{}. {} ({})".format(i, movie[0], movie[1]))
    print()
    

def add_movie(movie_list):
    movie = input("Name: ")
    year = input("Year: ")
    movie_list.append([movie, year])
    print("{} was added. \n".format(movie))


def delete_movie(movie_list):
    number = int(input("Number: "))
    if (number < 1) or (number > len(movie_list)):
        print("Invalid Selection \n")
    else:
        movie = movie_list.pop(number-1)
        print("{} was deleted. \n".format(movie[0]))


def main():
    movie_list = [["Monty Python and the Holy Grail", 1975],
                  ["On the Waterfront", 1954], 
                  ["Cat on a Hot Tin Roof", 1958]]
    command_menu()
    while True:
        command = input("Command: ")
        if command.lower() == 'list':
            list_movies(movie_list)
        elif command.lower() == 'add':
            add_movie(movie_list)
        elif command.lower() == 'del':
            delete_movie(movie_list)
        elif command.lower() == 'exit':
            break
        else:
            print("Invalid command. Please retry. \n")
    
    print("Bye!")


if __name__ == '__main__':
    main()
    